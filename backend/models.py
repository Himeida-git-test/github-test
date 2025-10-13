from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from database import Base

# Book ORM 모델
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key = True)

    title = Column(String(300), nullable = False)
    author = Column(String(150), nullable = False)
    price = Column(Integer, nullable = False)
    stock = Column(Integer, default = 0)
    description = Column(Text, nullable = True)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())