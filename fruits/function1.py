from app import app

@app.get("/fruits/function1")
def fruits_f1():
    return {"nessage": "fruits function 1"}