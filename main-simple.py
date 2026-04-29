from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "App running inside Docker"}

@app.get("/test")
def test():
    return {"status": "working"}