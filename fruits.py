from app import *

@app.get("/fruits")
def get_fruits():
    # code to return some fruits
    return {"message": "fruits"}