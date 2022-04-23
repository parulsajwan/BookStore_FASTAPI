from database_config import Base
from sqlalchemy import String,Integer,Column,ForeignKey
from sqlalchemy_utils import EmailType


class FavouriteBooks(Base):
    __tablename__ = "FavouriteBooks"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("Customer.id"))
    favourite_books_list = Column(String(128),unique=True)

    def __repr__(self):
        return self.books.name
