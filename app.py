from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the greeting API"}

@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}"}
