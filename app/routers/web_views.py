
from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import os
from ..database import get_db
from ..models import Major, AdmissionApplication, PaymentTransaction, SupportTicket, FAQItem, FeeConfig, User, Subject
from .auth import decode_access_token
templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates")
if not os.path.exists(templates_dir):
    for candidate in [
        os.path.join(os.getcwd(), "app", "templates"),
        os.path.join(os.getcwd(), "templates"),
        "/var/task/app/templates",
        "/var/task/templates"
    ]:
        if os.path.exists(candidate):
            templates_dir = candidate
            break
templates = Jinja2Templates(directory=templates_dir)
def render_template(request: Request, name: str, context: dict):
    """
    Hàm render template tương thích 100% với mọi phiên bản Starlette/FastAPI:
    - Starlette >= 0.28: TemplateResponse(request=request, name=name, context=context)
    - Starlette < 0.28: TemplateResponse(name, context)
    Tránh lỗi TypeError: unhashable type: 'dict' trên môi trường Vercel.
    """
    ctx = dict(context)
    ctx["request"] = request
    try:
        return templates.TemplateResponse(request=request, name=name, context=ctx)
    except TypeError:
        return templates.TemplateResponse(name, ctx)
router = APIRouter(include_in_schema=False)
def get_current_user(request: Request, db: Session):
    token = request.cookies.get("auth_token")
    if token:
        payload = decode_access_token(token)
        if payload and "sub" in payload:
            try:
                user = db.query(User).filter(User.id == int(payload["sub"])).first()
                if user:
                    return user
            except Exception:
                pass
    user_id = request.cookies.get("user_id")
    if not user_id:
        return None
    try:
        return db.query(User).filter(User.id == int(user_id)).first()
    except Exception:
        return None
# --- TRANG CHỦ & CHI TIẾT NGÀNH ---
@router.get("/")
def home_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    majors = db.query(Major).all()
    faqs = db.query(FAQItem).all()
    total_subjects = db.query(Subject).count()

    return render_template(request, "index.html", {
        "user": user,
        "majors": majors,
        "faqs": faqs,
        "total_subjects": total_subjects
    })

# --- CHUYÊN TRANG TÍNH ĐIỂM, ĐỀ ÁN, NGÀNH ĐÀO TẠO & TRA CỨU KẾT QUẢ ---
@router.get("/calculator")
def calculator_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    majors = db.query(Major).all()
    return render_template(request, "calculator.html", {
        "user": user,
        "majors": majors
    })

@router.get("/tinh-diem")
def tinh_diem_alias(request: Request, db: Session = Depends(get_db)):
    return calculator_page(request, db)

@router.get("/quy-che")
def regulations_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    fees = db.query(FeeConfig).all()
    return render_template(request, "regulations.html", {
        "user": user,
        "fees": fees
    })

@router.get("/de-an")
def de_an_alias(request: Request, db: Session = Depends(get_db)):
    return regulations_page(request, db)

@router.get("/majors")
def majors_catalog_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    majors = db.query(Major).all()
    total_subjects = db.query(Subject).count()
    return render_template(request, "majors_catalog.html", {
        "user": user,
        "majors": majors,
        "total_subjects": total_subjects
    })

@router.get("/nganh-dao-tao")
def nganh_dao_tao_alias(request: Request, db: Session = Depends(get_db)):
    return majors_catalog_page(request, db)

@router.get("/lookup")
def lookup_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    return render_template(request, "lookup.html", {
        "user": user
    })

@router.get("/tra-cuu")
def tra_cuu_alias(request: Request, db: Session = Depends(get_db)):
    return lookup_page(request, db)
@router.get("/majors/{major_id}")
def major_detail_page(major_id: int, request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    major = db.query(Major).filter(Major.id == major_id).first()
    if not major:
        raise HTTPException(status_code=404, detail="Không tìm thấy ngành học!")

    subjects = db.query(Subject).filter(Subject.major_id == major_id).order_by(Subject.semester, Subject.code).all()
    total_credits = sum(s.credits for s in subjects)

    return render_template(request, "major_detail.html", {
        "user": user,
        "major": major,
        "subjects": subjects,
        "total_credits": total_credits
    })
@router.get("/login")
def login_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if user:
        if user.role in ["ADMIN", "OFFICER"]:
            return RedirectResponse(url="/admin")
        return RedirectResponse(url="/student")
    return render_template(request, "login.html", {"user": None})

@router.get("/register")
def register_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if user:
        if user.role in ["ADMIN", "OFFICER"]:
            return RedirectResponse(url="/admin")
        return RedirectResponse(url="/student")
    return render_template(request, "register.html", {"user": None})

@router.get("/logout")
def logout_view():
    resp = RedirectResponse(url="/")
    resp.delete_cookie("auth_token")
    resp.delete_cookie("user_id")
    resp.delete_cookie("user_role")
    return resp
# --- ĐĂNG NHẬP ADMIN & CÁN BỘ ---
@router.get("/admin/login")
def admin_login_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if user:
        if user.role in ["ADMIN", "OFFICER"]:
            return RedirectResponse(url="/admin")
        return RedirectResponse(url="/student")
    return render_template(request, "admin_login.html", {"user": None})

# --- CỔNG HỌC SINH (YÊU CẦU ĐĂNG NHẬP) ---
@router.get("/student")
def student_portal(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user:
        return RedirectResponse(url="/login?msg=please_login")
    if user.role in ["ADMIN", "OFFICER"]:
        return RedirectResponse(url="/admin")

    majors = db.query(Major).all()
    fees = db.query(FeeConfig).all()
    # Lấy toàn bộ danh sách hồ sơ xét tuyển / nguyện vọng của thí sinh này
    my_applications = db.query(AdmissionApplication).filter(
        (AdmissionApplication.user_id == user.id) | (AdmissionApplication.email == user.email)
    ).order_by(AdmissionApplication.created_at.desc()).all()

    my_tickets = db.query(SupportTicket).filter(
        (SupportTicket.user_id == user.id) | (SupportTicket.sender_email == user.email)
    ).order_by(SupportTicket.created_at.desc()).all()

    return render_template(request, "student_portal.html", {
        "user": user,
        "majors": majors,
        "fees": fees,
        "my_applications": my_applications,
        "my_tickets": my_tickets
    })

# --- CỔNG QUẢN TRỊ & TÁC NGHIỆP CÁN BỘ (YÊU CẦU QUYỀN OFFICER HOẶC ADMIN) ---
@router.get("/admin")
def admin_portal(request: Request, db: Session = Depends(get_db)):
    user = get_current_user(request, db)
    if not user or user.role not in ["ADMIN", "OFFICER"]:
        return RedirectResponse(url="/admin/login?msg=staff_required")

    majors = db.query(Major).all()
    applications = db.query(AdmissionApplication).order_by(AdmissionApplication.score.desc()).all()
    transactions = db.query(PaymentTransaction).order_by(PaymentTransaction.created_at.desc()).all()
    tickets = db.query(SupportTicket).order_by(SupportTicket.created_at.desc()).all()
    
    fees = db.query(FeeConfig).all()
    paid_tx = [t for t in transactions if t.status == 'PAID']
    revenue = sum(t.amount for t in paid_tx)

    return render_template(request, "admin_portal.html", {
        "user": user,
        "majors": majors,
        "fees": fees,
        "applications": applications,
        "transactions": transactions,
        "tickets": tickets,
        "revenue": revenue,
        "paid_count": len(paid_tx),
        "total_count": len(transactions),
        "is_admin": user.role == "ADMIN"
    })

# --- BIÊN LAI ĐIỆN TỬ (IN / XUẤT PHIẾU THU LỆ PHÍ) ---
@router.get("/receipt/{tx_code}")
def receipt_page(tx_code: str, request: Request, db: Session = Depends(get_db)):
    tx = db.query(PaymentTransaction).filter(PaymentTransaction.tx_code == tx_code).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Không tìm thấy hóa đơn thanh toán!")
    app = db.query(AdmissionApplication).filter(AdmissionApplication.id == tx.application_id).first()
    if not app:
        raise HTTPException(status_code=404, detail="Không tìm thấy hồ sơ tương ứng!")

    user = get_current_user(request, db)
    if not user:
        return RedirectResponse(url=f"/login?msg=please_login&redirect=/receipt/{tx_code}")

    # Bảo mật quyền sở hữu: Thí sinh chỉ được xem biên lai của chính mình!
    if user.role == "STUDENT" and (app.user_id != user.id and app.email != user.email):
        raise HTTPException(status_code=403, detail="Bảo mật: Bạn không có quyền truy cập biên lai của thí sinh khác!")

    major = db.query(Major).filter(Major.id == app.major_id).first()
    return render_template(request, "receipt.html", {
        "tx": tx,
        "app": app,
        "major": major
    })

# --- IN PHIẾU ĐĂNG KÝ XÉT TUYỂN CHUẨN A4 (PDF) ---
@router.get("/application/print/{app_code}")
def application_print_page(app_code: str, request: Request, db: Session = Depends(get_db)):
    app = db.query(AdmissionApplication).filter(AdmissionApplication.app_code == app_code).first()
    if not app:
        raise HTTPException(status_code=404, detail="Không tìm thấy hồ sơ tuyển sinh!")

    user = get_current_user(request, db)
    if not user:
        return RedirectResponse(url=f"/login?msg=please_login&redirect=/application/print/{app_code}")

    if user.role == "STUDENT" and (app.user_id != user.id and app.email != user.email):
        raise HTTPException(status_code=403, detail="Bảo mật: Bạn không có quyền truy cập hồ sơ của thí sinh khác!")

    return render_template(request, "application_print.html", {
        "app": app,
        "user": user
    })

# --- IN GIẤY BÁO TRÚNG TUYỂN & NHẬP HỌC CHUẨN A4 (PDF) ---
@router.get("/certificate/print/{app_code}")
def certificate_print_page(app_code: str, request: Request, db: Session = Depends(get_db)):
    app = db.query(AdmissionApplication).filter(AdmissionApplication.app_code == app_code).first()
    if not app:
        raise HTTPException(status_code=404, detail="Không tìm thấy hồ sơ tuyển sinh!")

    user = get_current_user(request, db)
    if not user:
        return RedirectResponse(url=f"/login?msg=please_login&redirect=/certificate/print/{app_code}")

    if user.role == "STUDENT" and (app.user_id != user.id and app.email != user.email):
        raise HTTPException(status_code=403, detail="Bảo mật: Bạn không có quyền truy cập hồ sơ của thí sinh khác!")

    admitted_major = app.major
    if app.status == "TRUNG_TUYEN_NV2" and app.major_nv2:
        admitted_major = app.major_nv2

    return render_template(request, "certificate_print.html", {
        "app": app,
        "admitted_major": admitted_major,
        "user": user
    })
# --- FILE SWAGGER UI RIÊNG & TÀI LIỆU OPENAPI ---
@router.get("/swagger-ui")
def custom_swagger_ui():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "swagger_ui.html"))
    return FileResponse(file_path, media_type="text/html")

@router.get("/swagger_spec.json")
def custom_swagger_spec():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "swagger_spec.json"))
    return FileResponse(file_path, media_type="application/json")
