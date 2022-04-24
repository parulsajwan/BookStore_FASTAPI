from database_config import Base
from sqlalchemy import String, Integer, Column, ForeignKey


class FavouriteBooks(Base):
    __tablename__ = 'FavouriteBooks'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('Customer.id'))
    favourite_books_list = Column(String(128))
