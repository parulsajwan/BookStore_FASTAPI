from fastapi import FastAPI
from routes.customer import customerrouter
from routes.books import bookrouter
from routes.favouritebooks import favoritebookrouter
from routes.likedbooks import likedrouter
from db_object import db
app = FastAPI(title="Bookstore API's", version="1.0.0")


app.include_router(customerrouter, prefix="/customer")
app.include_router(bookrouter, prefix="/books")
app.include_router(likedrouter, prefix="/likedbooks")
app.include_router(favoritebookrouter, prefix="/favbooks")

@app.on_event("startup")
async def connect_db():
    await db.connect()

@app.on_event("shutdown")
async def disconnect_db():
    await db.disconnect()