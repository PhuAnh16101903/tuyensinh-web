import os
import shutil
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Hỗ trợ cấu hình CSDL Cloud vĩnh viễn (Supabase / Neon / PostgreSQL) qua biến môi trường DATABASE_URL
env_db_url = os.environ.get('DATABASE_URL') or os.environ.get('POSTGRES_URL')

if env_db_url:
    # Chuẩn hóa tiền tố postgres:// thành postgresql:// cho SQLAlchemy
    if env_db_url.startswith('postgres://'):
        env_db_url = env_db_url.replace('postgres://', 'postgresql://', 1)
    DATABASE_URL = env_db_url
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
else:
    # Tương thích với môi trường Serverless của Vercel (chỉ thư mục /tmp được phép ghi)
    is_serverless = (
        not os.access(BASE_DIR, os.W_OK)
        or any(k in os.environ for k in ['VERCEL', 'VERCEL_ENV', 'AWS_LAMBDA_FUNCTION_NAME', 'LAMBDA_TASK_ROOT'])
    )

    if is_serverless:
        DB_PATH = '/tmp/admission_system.db'
        orig_db = os.path.join(BASE_DIR, 'admission_system.db')
        if not os.path.exists(DB_PATH) and os.path.exists(orig_db):
            try:
                shutil.copy2(orig_db, DB_PATH)
            except Exception as e:
                print(f'[Vercel SQLite Notice] Error copying DB to /tmp: {e}')
    else:
        DB_PATH = os.path.join(BASE_DIR, 'admission_system.db').replace('\\', '/')

    DATABASE_URL = f'sqlite:///{DB_PATH}'
    engine = create_engine(
        DATABASE_URL, connect_args={'check_same_thread': False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
