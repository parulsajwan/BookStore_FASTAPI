from fastapi import Depends, APIRouter,File,UploadFile
from database_config import SessionLocal,engine
from starlette.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_404_NOT_FOUND
from typing import List
from pydantic import BaseModel
import models.books as book
from sqlalchemy.orm import Session
import shutil


bookrouter = APIRouter()
book.Base.metadata.create_all(engine)
class CreateBook(BaseModel):
    id : int
    book_name : str
    description : str
    image_link :str
    class Config:
        orm_mode = True

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@bookrouter.post("/create", status_code=HTTP_201_CREATED)
async def add_book(id:int, book_name:str, description:str,image_link:UploadFile = File(...),
                   db: Session = Depends(get_db)):
    try:
        add_book = book.Books()
        add_book.id = id
        add_book.book_name = book_name
        add_book.description = description
        with open("media/"+image_link.filename, "wb") as image:
            shutil.copyfileobj(image_link.file,image)

        add_book.image_link = str("media/"+image_link.filename)
        db.add(add_book)
        db.commit()
        return ("Book has been Created")
    except Exception as e:
        return("Error:",e)

@bookrouter.get("/", status_code=HTTP_200_OK)
async def get_all_books(db: Session = Depends(get_db)):
    try:
        data = db.query(book.Books).all()
        return data
    except Exception as e:
        return("Error:",e)

@bookrouter.get("/{id}",status_code=HTTP_200_OK)
async def get_book_by_id(id:int,db: Session = Depends(get_db)):
    try:
        data = db.query(book.Books).filter(book.Books.id == id).first()
        if data:
            return data
        else:
            return {'status', HTTP_404_NOT_FOUND}
    except Exception as e:
        return("Error:", e)
