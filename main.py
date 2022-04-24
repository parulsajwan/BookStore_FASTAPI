import os
from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache
from routes.customer import customerrouter
from routes.books import bookrouter
from routes.favouritebooks import favoritebookrouter
from routes.likedbooks import likedrouter
from db_object import db
from sqlalchemy.orm import Session

LOCAL_REDIS_URL = "redis://127.0.0.1:6379"

app = FastAPI(title="Bookstore API's", version="1.0.0")


app.include_router(customerrouter, prefix="/customer")
app.include_router(bookrouter, prefix="/books")
app.include_router(likedrouter, prefix="/likedbooks")
app.include_router(favoritebookrouter, prefix="/favbooks")


@app.on_event("startup")
async def startup():
    await db.connect()
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session])


@app.on_event("shutdown")
async def disconnect_db():
    await db.disconnect()
