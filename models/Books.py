from database_config import Base
from sqlalchemy import String,Integer,Column,Text
from sqlalchemy_utils import URLType

class Books(Base):
    __tablename__= 'Books'
    id = Column(Integer,primary_key=True)
    book_name = Column(String(255),nullable=False)
    description = Column(Text())
    image_link = Column(URLType)
    
    def __repr__(self):
        return self.book_name
