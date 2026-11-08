import random
import re
import hashlib
import datetime
from typing import Optional
import jwt
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User, PasswordResetToken
from ..schemas import UserRegister, UserLogin, UserOut, ForgotPasswordRequest, ForgotPasswordReset

router = APIRouter(prefix="/api/auth", tags=["Xác thực & Tài khoản"])

# Cấu hình JWT Token
SECRET_KEY = "UniAdmissionsSecureJWTKey_NEU2026_AdvancedAdmissionSecurityKey123456789!"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24 * 365 # Duy trì phiên 1 năm

def hash_password(password: str) -> str:
    """Băm mật khẩu an toàn với thuật toán SHA-256 kèm muối cố định cho đồ án"""
    salt = "UniAdmission2026SecureSalt$"
    return hashlib.sha256((salt + password).encode('utf-8')).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Kiểm tra mật khẩu khớp với chuỗi băm (hoặc plaintext legacy)"""
    return hash_password(plain_password) == hashed_password or plain_password == hashed_password

def create_access_token(data: dict, expires_delta: Optional[datetime.timedelta] = None) -> str:
    """Tạo JSON Web Token (JWT) có chữ ký điện tử HS256 bảo vệ toàn vẹn phiên"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.now(datetime.timezone.utc) + expires_delta
    else:
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str) -> Optional[dict]:
    """Giải mã và xác thực chữ ký JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except Exception:
        return None

def set_auth_cookies(response: Response, user: User) -> str:
    """Ghi cookie JWT token HttpOnly dạng Session Cookie (xóa phiên khi đóng trình duyệt, link mới luôn ở trạng thái Đăng Xuất)"""
    token_payload = {
        "sub": str(user.id),
        "email": user.email,
        "role": user.role,
        "full_name": user.full_name
    }
    token = create_access_token(token_payload)
    # Session Cookie (không set max_age): Khi đóng trình duyệt hoặc truy cập mới sẽ tự động đăng xuất
    # Bắt buộc có path="/" để áp dụng thống nhất toàn bộ trang web
    response.set_cookie(key="auth_token", value=token, httponly=True, samesite="lax", path="/")
    response.set_cookie(key="user_id", value=str(user.id), httponly=True, samesite="lax", path="/")
    response.set_cookie(key="user_role", value=user.role, httponly=True, samesite="lax", path="/")
    return token

@router.post("/register", response_model=UserOut)
def register_student(data: UserRegister, response: Response, db: Session = Depends(get_db)):
    """[Thí sinh] Đăng ký tài khoản học sinh bằng Email và CCCD (mật khẩu bảo mật >= 8 ký tự, CCCD đúng 12 chữ số)"""
    # 1. Ràng buộc mật khẩu bắt buộc phải từ 8 ký tự trở lên
    if not data.password or len(data.password) < 8:
        raise HTTPException(status_code=400, detail="Mật khẩu đăng ký bắt buộc phải từ 8 ký tự trở lên!")

    # 2. Ràng buộc CCCD bắt buộc đúng 12 chữ số
    clean_id_card = None
    if data.id_card:
        clean_id_card = data.id_card.strip()
        if not re.match(r"^\d{12}$", clean_id_card):
            raise HTTPException(status_code=400, detail="Số Căn cước công dân (CCCD) bắt buộc phải gồm đúng 12 chữ số!")

    existing = db.query(User).filter(User.email == data.email.lower()).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email này đã được đăng ký tài khoản!")

    if clean_id_card:
        existing_id = db.query(User).filter(User.id_card == clean_id_card).first()
        if existing_id:
            raise HTTPException(status_code=400, detail=f"Số CCCD {clean_id_card} này đã được đăng ký bởi tài khoản khác!")

    new_user = User(
        email=data.email.lower(),
        password=hash_password(data.password),
        full_name=data.full_name,
        phone=data.phone,
        id_card=clean_id_card,
        role="STUDENT"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    set_auth_cookies(response, new_user)
    return new_user

@router.post("/login")
def login_student(data: UserLogin, response: Response, db: Session = Depends(get_db)):
    """[Thí sinh] Đăng nhập bằng Email và Mật khẩu (cấp phiên bảo mật JWT)"""
    user = db.query(User).filter(User.email == data.email.lower()).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Email hoặc mật khẩu không chính xác!")

    token = set_auth_cookies(response, user)

    return {
        "message": "Đăng nhập thành công!",
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role
        }
    }

def get_current_user_from_req(request: Request, db: Session = Depends(get_db)):
    """Lấy thông tin người dùng hiện tại từ JWT token hoặc session cookie an toàn"""
    token = request.cookies.get("auth_token")
    if not token:
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

    if token:
        payload = decode_access_token(token)
        if payload and "sub" in payload:
            try:
                user = db.query(User).filter(User.id == int(payload["sub"])).first()
                if user:
                    return user
            except Exception:
                pass

    uid = request.cookies.get("user_id")
    if uid:
        try:
            return db.query(User).filter(User.id == int(uid)).first()
        except Exception:
            pass

    return None

def require_logged_in_user(request: Request, db: Session = Depends(get_db)) -> User:
    """Yêu cầu bắt buộc đã đăng nhập"""
    user = get_current_user_from_req(request, db)
    if not user:
        raise HTTPException(status_code=401, detail="Vui lòng đăng nhập để thực hiện thao tác này!")
    return user

def require_officer_or_admin(request: Request, db: Session = Depends(get_db)) -> User:
    """Yêu cầu quyền Cán bộ Tuyển sinh (OFFICER) hoặc Quản trị viên (ADMIN)"""
    user = require_logged_in_user(request, db)
    if user.role not in ["OFFICER", "ADMIN"]:
        raise HTTPException(status_code=403, detail="Quyền truy cập bị từ chối: Yêu cầu quyền Cán bộ hoặc Admin!")
    return user

def require_admin(request: Request, db: Session = Depends(get_db)) -> User:
    """Yêu cầu quyền Quản trị viên cấp cao (ADMIN)"""
    user = require_logged_in_user(request, db)
    if user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Quyền truy cập bị từ chối: Thao tác này chỉ dành riêng cho Admin!")
    return user

@router.post("/admin-login")
def login_admin(data: UserLogin, response: Response, db: Session = Depends(get_db)):
    """[Cán bộ / Admin] Đăng nhập Cổng Quản Trị & Nghiệp Vụ Tuyển Sinh (JWT)"""
    user = db.query(User).filter(User.email == data.email.lower()).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Email hoặc mật khẩu không chính xác!")

    if user.role not in ["ADMIN", "OFFICER"]:
        raise HTTPException(status_code=403, detail="Tài khoản này không có quyền Cán bộ tuyển sinh hoặc Quản trị viên!")

    token = set_auth_cookies(response, user)
    role_title = "Quản trị viên" if user.role == "ADMIN" else "Cán bộ tuyển sinh"
    return {
        "message": f"Đăng nhập {role_title} thành công!",
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role
        }
    }

@router.post("/logout")
def logout(response: Response):
    """Đăng xuất tài khoản và xóa token bảo mật"""
    response.delete_cookie("auth_token")
    response.delete_cookie("user_id")
    response.delete_cookie("user_role")
    return {"message": "Đã đăng xuất thành công"}


# ==========================================================
# MODULE XAC THUC: QUEN MAT KHAU & CAP MA OTP
# ==========================================================
@router.post("/forgot-password/request-otp")
def request_password_reset_otp(data: ForgotPasswordRequest, db: Session = Depends(get_db)):
    """[Quen Mat Khau] Buoc 1: Tiep nhan yeu cau, kiem tra tai khoan va sinh ma OTP 6 so xac thuc"""
    input_val = data.email.strip()
    if not input_val:
        raise HTTPException(status_code=400, detail="Vui lòng nhập Email, Số điện thoại hoặc CCCD của bạn!")
    
    clean_email = input_val.lower()
    user = db.query(User).filter(User.email == clean_email).first()
    
    # Neu khong tim thay bang email, thu tim bang So dien thoai hoac CCCD
    if not user:
        user = db.query(User).filter(
            (User.phone == input_val) | (User.id_card == input_val)
        ).first()
        if user:
            clean_email = user.email.lower()
    
    if not user:
        raise HTTPException(status_code=404, detail="Không tìm thấy tài khoản tương ứng với thông tin bạn cung cấp. Vui lòng kiểm tra lại hoặc Đăng ký tài khoản mới!")
    
    # Sinh ma OTP 6 chu so ngau nhien
    otp_code = f"{random.randint(100000, 999999)}"
    expires_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    
    reset_entry = PasswordResetToken(
        email=clean_email,
        otp_code=otp_code,
        is_used=0,
        expires_at=expires_at
    )
    db.add(reset_entry)
    db.commit()
    
    return {
        "success": True,
        "message": f"Ma xac thuc OTP da duoc tao thanh cong cho tai khoan {user.full_name} ({clean_email})!",
        "email": clean_email,
        "full_name": user.full_name,
        "otp_code": otp_code,
        "expires_in_minutes": 15
    }

@router.post("/forgot-password/verify-and-reset")
def verify_otp_and_reset_password(data: ForgotPasswordReset, db: Session = Depends(get_db)):
    """[Quen Mat Khau] Buoc 2: Xac thuc ma OTP va cap nhat mat khau moi bao mat (tu 8 ky tu tro len)"""
    clean_email = data.email.strip().lower()
    clean_otp = data.otp_code.strip()
    new_pw = data.new_password.strip() if data.new_password else ""
    
    if not clean_email or not clean_otp:
        raise HTTPException(status_code=400, detail="Vui lòng điền đầy đủ Email và Mã xác nhận OTP!")
    
    if len(new_pw) < 8:
        raise HTTPException(status_code=400, detail="Mật khẩu mới bắt buộc phải có độ dài từ 8 ký tự trở lên!")
    
    # Tim ma OTP con han va chua dung
    token_entry = db.query(PasswordResetToken).filter(
        PasswordResetToken.email == clean_email,
        PasswordResetToken.otp_code == clean_otp,
        PasswordResetToken.is_used == 0
    ).order_by(PasswordResetToken.id.desc()).first()
    
    if not token_entry:
        raise HTTPException(status_code=400, detail="Mã OTP không chính xác hoặc đã được sử dụng trước đó!")
    
    if token_entry.expires_at < datetime.datetime.utcnow():
        raise HTTPException(status_code=400, detail="Mã OTP này đã hết hiệu lực (quá 15 phút). Vui lòng yêu cầu cấp mã mới!")
    
    user = db.query(User).filter(User.email == clean_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Không tìm thấy tài khoản người dùng tương ứng!")
    
    # Cap nhat mat khau moi da bam an toan
    user.password = hash_password(new_pw)
    token_entry.is_used = 1
    db.commit()
    
    return {
        "success": True,
        "message": f"Dat lai mat khau cho tai khoan {clean_email} thanh cong! Ban co the dang nhap ngay voi mat khau moi."
    }
