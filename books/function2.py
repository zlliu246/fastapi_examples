from app import app

@app.get("/books/function2")
def books_f2():
    return {"message": "books function 2"}