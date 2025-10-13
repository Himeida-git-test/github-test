from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_PATH = 'sqlite:///database.db'

# 엔진
engine = create_engine(
    DB_PATH, 
    connect_args={'check_same_thread': False}
)

# 세션
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

# Base 모델
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base 모델에 등록된 모델 클래스를 생성해주는 create_table 함수
def create_table():
    Base.metadata.create_all(bind = engine)