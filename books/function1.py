from app import app

@app.get("/books/function1")
def books_f1():
    return {"message": "books function 1"}