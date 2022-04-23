from fastapi import Depends, APIRouter
from database_config import SessionLocal,engine
from starlette.status import HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_201_CREATED
from typing import List
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
import models.customer as custom
from sqlalchemy.orm import Session

customerrouter = APIRouter()
custom.Base.metadata.create_all(engine)

class CreateCustomer(BaseModel):
    id : int
    name : str
    password : str
    email :EmailStr
    class Config:
        orm_mode = True

bcrypt_context = CryptContext(schemes=["bcrypt"])

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_password_hash(password):
    return bcrypt_context.hash(password)

@customerrouter.post("/create",status_code=HTTP_201_CREATED)
async def create_customers(id:int, name:str, email:EmailStr, password:str,\
                               db: Session = Depends(get_db)):
    try:
        create_customer = custom.Customer()
        create_customer.id = id
        create_customer.name = name
        create_customer.email = email
        hash_password = get_password_hash(password)
        create_customer.password = hash_password
        data = db.query(custom.Customer).filter(custom.Customer.email == email).first()
        if data:
            return("Data already exists")
        else:
            db.add(create_customer)
            db.commit()
            return ('Customer has been created')
    except Exception as e:
        return ("ERROR: ",e)

@customerrouter.get("/", status_code=HTTP_200_OK)
async def get_all_customer(db: Session = Depends(get_db)):
    data = db.query(custom.Customer).all()
    return data

@customerrouter.get("/{id}",status_code=HTTP_200_OK)
async def get_customer_by_id(id:int,db: Session = Depends(get_db)):
    data = db.query(custom.Customer).filter(custom.Customer.id == id).first()
    if data:
        return data
    return ('status', HTTP_404_NOT_FOUND)
