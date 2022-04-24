from database_config import Base
from sqlalchemy import Column,ForeignKey,Integer


class LikedBooks(Base):
    __tablename__ = "LikedBooks"
    
    customer_id = Column(Integer, ForeignKey("Customer.id"), primary_key=True)
    liked = Column(Integer, ForeignKey("Books.id"), primary_key=True)
