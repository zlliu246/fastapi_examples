from app import app

@app.get("/books")
def get_books():
    # code to return some books
    return {"message": "books"}

from books.function1 import *
from books.function2 import *