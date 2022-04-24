from db_object import db
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


async def execute(query, is_many, values=None):

    if is_many:
        await db.execute_many(query=query, values=values)
    else:
        await db.execute(query=query, values=values)


async def fetch(query, is_one, values=None):
    """
    Param 1: Query string
    Param 2: True for getting One row , False for many rows
    Param 3: values for the query
    Return data in dict format"""

    if is_one:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            out = None
        else:
            out = dict(result)
    else:
        result = await db.fetch_all(query=query, values=values)
        if result is None:
            out = None
        else:
            out = []
            for row in result:
                out.append(dict(row))
    return out


async def update_favourite_books(customer_id, book_list):
    query = 'update "FavouriteBooks" set favourite_books_list=:favourite_books_list where customer_id=:customer_id'
    values = {"favourite_books_list": book_list, "customer_id": customer_id}
    await execute(query, False, values)


async def db_get_favouritebook_from_id(customer_id):
    query = "select * from LikedBooks where customer_id=:customer_id"
    values = {"customer_id": customer_id}
    author = await fetch(query, True, values)
    return author


async def create_favourite_books(customer_id, book_list):
    query = 'Insert into "FavouriteBooks"(customer_id,favourite_books_list) values(customer_id=:customer_id,favourite_books_list=:"favourite_books_list")'
    values = {"favourite_books_list": book_list, "customer_id": customer_id}
    await execute(query, True, values)
