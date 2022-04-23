from database_config import Base
from sqlalchemy import String,Integer,Column
from sqlalchemy_utils import EmailType


class Customer(Base):
    __tablename__ = "Customer"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255),nullable=False)
    password = Column(String(128))
    email = Column(String, unique=True)

    def __repr__(self):
        return self.name
