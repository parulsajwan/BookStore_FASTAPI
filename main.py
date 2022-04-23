from fastapi import FastAPI
from routes.Customer import customer
from routes.Books import book
from routes.FavouriteBook import favoritebook

app = FastAPI(title="Bookstore API's", version="1.0.0")


app.include_router(customer, prefix="/customer")
app.include_router(book, prefix="/books")
app.include_router(favoritebook, prefix="/favbooks")
