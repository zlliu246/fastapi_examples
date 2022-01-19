from app import app

@app.get("/fruits/function2")
def fruits_f2():
    return {"nessage": "fruits function 2"}