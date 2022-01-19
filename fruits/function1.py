from app import app

@app.get("/fruits/function1")
def fruits_f1():
    return {"message": "fruits function 1"}