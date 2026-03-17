from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    amount = Column(Float)
    currency = Column(String)
    status = Column(String, default="pending") # pending, completed, failed
    timestamp = Column(DateTime(timezone=True), server_default=func.now())