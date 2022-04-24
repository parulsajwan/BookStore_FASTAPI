from database_config import Base
from sqlalchemy import String,Integer,Column
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = 'Customer'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255),nullable=False)
    password = Column(String(128))
    email = Column(String, unique=True)
    books = relationship("Books", secondary="LikedBooks", back_populates='customers')
