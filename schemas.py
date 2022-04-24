from typing import List
from pydantic import BaseModel,EmailStr

class CreateCustomer(BaseModel):
    id : int
    name : str
    password : str
    email :EmailStr
    class Config:
        orm_mode = True

class CreateBook(BaseModel):
    id : int
    book_name : str
    description : str
    image_link :str
    class Config:
        orm_mode = True
        
class CreateFavouriteBook(BaseModel):
    customer_id : int
    count: int
    class Config:
        orm = True

class BookSchema(CreateCustomer):
    books: List[CreateBook]
    
class CustomerSchema(CreateBook):
    customer: List[CreateCustomer]