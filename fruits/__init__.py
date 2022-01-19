from app import *

@app.get("/fruits")
def get_fruits():
    # code to return some fruits
    return {"message": "fruits"}

from fruits.function1 import *
from fruits.function2 import *