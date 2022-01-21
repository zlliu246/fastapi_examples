import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return {"message": "hello world"}

import os

@app.get("/images")
def images():
    out = []
    for filename in os.listdir("static/images"):
        out.append({
            "name": filename.split(".")[0],
            "path": "/static/images/" + filename
        })
    return out

@app.get("/music")
def music():
    out = []
    for filename in os.listdir("static/mp3"):
        out.append({
            "name": filename.split(".")[0],
            "path": "/static/mp3/" + filename
        })
    return out

@app.get("/pdfs")
def pdfs():
    out = []
    for filename in os.listdir("static/pdfs"):
        out.append({
            "name": filename.split(".")[0],
            "path": "/static/pdfs/" + filename
        })
    return out


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000)

