from fastapi import Depends, APIRouter
from database_config import SessionLocal,engine
from starlette.status import HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_201_CREATED
from typing import List
from pydantic import BaseModel
import models.likedbooks as likedbook
from models.favouritebooks import FavouriteBooks
from sqlalchemy.orm import Session
from sql_function import update_favourite_books

likedrouter = APIRouter()
likedbook.Base.metadata.create_all(engine)

class CreateCLikedBooks(BaseModel):
    id : int
    customer_id : int
    liked : int
    class Config:
        orm_mode = True

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@likedrouter.post("/create",status_code=HTTP_201_CREATED)
async def create_customers(customer_id:int, liked:int, db: Session = Depends(get_db)):
    try:
        create_likedbook = likedbook.LikedBooks()
        create_likedbook.customer_id = customer_id
        create_likedbook.liked = liked
        data = db.query(likedbook.LikedBooks).\
            filter(likedbook.LikedBooks.customer_id == customer_id,\
                likedbook.LikedBooks.liked == liked).first()
        if data:
            return("Data already exists")
        else:
            db.add(create_likedbook)
            db.commit()
            create_favourite = FavouriteBooks()
            fav_books = db.query(FavouriteBooks).filter(FavouriteBooks.customer_id==customer_id).first()
            if fav_books:
                book_list = fav_books.favourite_books_list
                if str(liked) in book_list:
                    return( "This book is already liked by the same Customer")
                book_list = book_list + ',' + str(liked)
                await update_favourite_books(customer_id, book_list)
                return ('Book liked or Added to Favourite Book list')
            else:
                create_favourite.customer_id = customer_id
                create_favourite.favourite_books_list = str(liked)
                db.add(create_favourite)
                db.commit()
                return("Book liked")
    except Exception as e:
        return ("ERROR: ",str(e))

@likedrouter.get("/", status_code=HTTP_200_OK)
async def get_all_customer(db: Session = Depends(get_db)):
    data = db.query(likedbook.LikedBooks).all()
    return data

@likedrouter.get("/{id}",status_code=HTTP_200_OK)
async def get_customer_by_id(id:int,db: Session = Depends(get_db)):
    data = db.query(likedbook.LikedBooks).filter(likedbook.LikedBooks.customer_id==id).first()
    if data:
        return data
    return ('status', HTTP_404_NOT_FOUND)
