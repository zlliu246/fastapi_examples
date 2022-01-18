from app import app

@app.get("/books")
def get_books():
    # code to return some books
    return {"message": "books"}