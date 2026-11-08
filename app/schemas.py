from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# ==================== AUTH SCHEMAS ====================
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    phone: Optional[str] = None
    id_card: Optional[str] = None # Số CCCD (12 chữ số)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ForgotPasswordRequest(BaseModel):
    email: str

class ForgotPasswordReset(BaseModel):
    email: str
    otp_code: str
    new_password: str

class UserOut(BaseModel):
    id: int
    email: str
    full_name: str
    phone: Optional[str]
    id_card: Optional[str] = None
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


# ==================== SUBJECT & MAJOR SCHEMAS ====================
class SubjectOut(BaseModel):
    id: int
    code: str
    name: str
    credits: int
    semester: int
    subject_type: str
    description: Optional[str]

    class Config:
        from_attributes = True

class MajorOut(BaseModel):
    id: int
    code: str
    name: str
    category: Optional[str] = "Chung"
    description: Optional[str]
    quota: int
    benchmark_score: float
    predicted_score: Optional[float] = 0.0

    class Config:
        from_attributes = True

class MajorUpdateQuota(BaseModel):
    quota: int
    benchmark_score: Optional[float] = None
    predicted_score: Optional[float] = None

class MajorDetailOut(MajorOut):
    subjects: List[SubjectOut] = []

    class Config:
        from_attributes = True


# ==================== M02 ADMISSIONS SCHEMAS ====================
class ApplicationCreate(BaseModel):
    full_name: str
    id_card: str
    email: EmailStr
    phone: str
    method: Optional[str] = "THPT"
    method_code: Optional[str] = "THPT"
    method_name: Optional[str] = "Xét tuyển kết quả thi tốt nghiệp THPT"
    subject_combination: Optional[str] = None
    priority_area: Optional[str] = "KV3"
    priority_score: Optional[float] = 0.0
    score_details: Optional[str] = None
    score: float
    major_id: int # Nguyện vọng 1
    major_nv2_id: Optional[int] = None # Nguyện vọng 2
    proof_url: Optional[str] = None
    user_id: Optional[int] = None

class ApplicationStatusUpdate(BaseModel):
    status: str # HOP_LE, TU_CHOI, etc.
    officer_note: Optional[str] = None

class PublicVerifyLookupRequest(BaseModel):
    app_code: str
    id_card_last4: str # 4 số cuối CCCD để xác minh danh tính

class PublicVerifyLookupOut(BaseModel):
    app_code: str
    full_name: str
    id_card_masked: str
    phone_masked: str
    major_name: str
    major_code: str
    major_nv2_name: Optional[str] = None
    method_code: Optional[str] = None
    method_name: Optional[str] = None
    subject_combination: Optional[str] = None
    priority_area: Optional[str] = None
    priority_score: Optional[float] = None
    score: float
    status: str
    admitted_major_name: Optional[str] = None
    payment_status: str
    created_at: datetime

class ApplicationOut(BaseModel):
    id: int
    app_code: str
    full_name: str
    id_card: str
    email: str
    phone: str
    method: str
    method_code: Optional[str] = "THPT"
    method_name: Optional[str] = None
    subject_combination: Optional[str] = None
    priority_area: Optional[str] = "KV3"
    priority_score: Optional[float] = 0.0
    score_details: Optional[str] = None
    score: float
    status: str
    officer_note: Optional[str] = None
    major_id: int
    major_nv2_id: Optional[int] = None
    admitted_major_name: Optional[str] = None
    user_id: Optional[int] = None
    proof_url: Optional[str] = None
    student_code: Optional[str] = None
    student_email: Optional[str] = None
    enrolled_at: Optional[datetime] = None
    appeal_note: Optional[str] = None
    appeal_proof_url: Optional[str] = None
    appeal_status: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

class ApplicationUpdate(BaseModel):
    major_id: Optional[int] = None
    major_nv2_id: Optional[int] = None
    method: Optional[str] = None
    method_code: Optional[str] = None
    method_name: Optional[str] = None
    subject_combination: Optional[str] = None
    priority_area: Optional[str] = None
    priority_score: Optional[float] = None
    score_details: Optional[str] = None
    score: Optional[float] = None
    proof_url: Optional[str] = None

class ApplicationAppealRequest(BaseModel):
    appeal_note: str
    appeal_proof_url: Optional[str] = None

class ApplicationAppealReview(BaseModel):
    appeal_status: str # APPROVED, REJECTED
    officer_note: Optional[str] = None
    new_score: Optional[float] = None
    new_status: Optional[str] = None


# ==================== M07 FINANCE SCHEMAS ====================
class PaymentCreate(BaseModel):
    application_id: int
    method: Optional[str] = "QR_CHUYEN_KHOAN"

class FeeConfigUpdate(BaseModel):
    amount: float
    fee_name: Optional[str] = None
    description: Optional[str] = None

class PaymentSimulate(BaseModel):
    tx_code: str

class WebhookIPNPayload(BaseModel):
    content: Optional[str] = None
    description: Optional[str] = None
    memo: Optional[str] = None
    amount: Optional[float] = None
    account_number: Optional[str] = None
    bank_code: Optional[str] = None
    transaction_id: Optional[str] = None

class PaymentOut(BaseModel):
    id: int
    tx_code: str
    application_id: int
    amount: float
    method: str
    status: str
    qr_payload: Optional[str]
    paid_at: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True


# ==================== M12 SUPPORT SCHEMAS ====================
class FAQOut(BaseModel):
    id: int
    category: str
    question: str
    answer: str

    class Config:
        from_attributes = True

class TicketCreate(BaseModel):
    sender_name: str
    sender_email: EmailStr
    sender_phone: Optional[str] = None
    category: str
    subject: str
    message: str
    application_id: Optional[int] = None
    user_id: Optional[int] = None

class TicketReply(BaseModel):
    reply: str

class TicketOut(BaseModel):
    id: int
    ticket_code: str
    sender_name: str
    sender_email: str
    category: str
    subject: str
    message: str
    reply: Optional[str]
    status: str
    created_at: datetime
    resolved_at: Optional[datetime]

    class Config:
        from_attributes = True

class AIChatQuery(BaseModel):
    query: str
    score: Optional[float] = None
    combination: Optional[str] = None # Tổ hợp môn (A00, A01, D01, B00...)
    history: Optional[List[dict]] = None # Lịch sử chat [{role: 'user'|'model', text: '...'}]

class ScoreCalculateRequest(BaseModel):
    method: str = "THPT" # THPT, IELTS_COMBINED, DGNL_HSA, DGNL_TSA, DGNL_APT
    m1_score: Optional[float] = 0.0 # Toán
    m2_score: Optional[float] = 0.0 # Môn 2 (Lý / Hóa / Văn)
    m3_score: Optional[float] = 0.0 # Môn 3 (Anh / Hóa / Lý)
    ielts_band: Optional[float] = None # 5.5, 6.0, 6.5, 7.0, 7.5+
    dgnl_score: Optional[float] = None # HSA (150), TSA (100), APT (1200)
    priority_area: Optional[str] = "KV3" # KV1 (0.75), KV2_NT (0.5), KV2 (0.25), KV3 (0.0)
    priority_target: Optional[str] = "NONE" # UT1 (2.0), UT2 (1.0), NONE (0.0)

class RecommendedMajorItem(BaseModel):
    id: int
    code: str
    name: str
    category: str
    quota: int
    benchmark_score: float
    predicted_score: float
    tier: str # target, safe, reach
    chance_percent: int

class ScoreCalculateOut(BaseModel):
    method: str
    raw_base_score: float
    ielts_converted_score: Optional[float] = None
    priority_score: float
    final_score: float
    priority_note: str
    safe_majors: List[RecommendedMajorItem]
    target_majors: List[RecommendedMajorItem]
    reach_majors: List[RecommendedMajorItem]
