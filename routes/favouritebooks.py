from fastapi import Depends, APIRouter
from database_config import SessionLocal,engine
from starlette.status import HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_201_CREATED
import models.favouritebooks as favouritebook
from sqlalchemy.orm import Session
from schemas import CreateFavouriteBook

favoritebookrouter = APIRouter()
favouritebook.Base.metadata.create_all(engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@favoritebookrouter.get("/", status_code=HTTP_200_OK)
async def get_all_customer(db: Session = Depends(get_db)):
    data = db.query(favouritebook.FavouriteBooks).all()
    return data

@favoritebookrouter.get("/{id}", status_code=HTTP_200_OK)
async def get_customer_by_id(id:int,db: Session = Depends(get_db)):
    data = db.query(favouritebook.FavouriteBooks).filter(favouritebook.FavouriteBooks.customer_id == id).first()
    if data:
        return data
    return {'status', HTTP_404_NOT_FOUND}

data = []
single_data = {}
@favoritebookrouter.get("/count/", status_code=HTTP_200_OK)
async def get_all_favourite_books_count(db: Session = Depends(get_db)):
    query = db.query(favouritebook.FavouriteBooks).all()
    # for i in data:
    #     # count = len(i.favourite_books_list.split(','))
    #     # customer = i.customer_id
    #     # single_data['favourite_books_list'] = count
    #     # single_data['customer_id'] = customer
    #     # data.append(single_data)
    #     data.append(i)
    return query