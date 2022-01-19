from app import app

@app.get("/books/function2")
def books_f2():
    return {"nessage": "books function 2"}