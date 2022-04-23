from fastapi import FastAPI
from routes.customer import customerrouter
from routes.books import bookrouter
from routes.favouritebooks import favoritebookrouter

app = FastAPI(title="Bookstore API's", version="1.0.0")


app.include_router(customerrouter, prefix="/customer")
app.include_router(bookrouter, prefix="/books")
app.include_router(favoritebookrouter, prefix="/favbooks")
