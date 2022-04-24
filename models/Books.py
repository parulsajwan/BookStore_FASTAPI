from database_config import Base
from sqlalchemy import String, Integer, Column, Text
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship


class Books(Base):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True)
    book_name = Column(String(255), nullable=False)
    description = Column(Text())
    image_link = Column(URLType)
    customers = relationship("Customer", secondary="LikedBooks", back_populates='books')
