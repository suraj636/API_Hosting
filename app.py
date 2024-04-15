from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Creating an instance of FastAPI app
app = FastAPI()

# Creating a Pydantic model for request body validation
class Numbers(BaseModel):
    num1: float
    num2: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the calculator API!"}


# Defining the route for addition
@app.post("/add")
def add(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

# Defining the route for multiplication
@app.post("/multiply")
def multiply(numbers: Numbers):
    result = numbers.num1 * numbers.num2
    return {"result": result}

# Defining the route for subtraction
@app.post("/subtract")
def subtract(numbers: Numbers):
    result = numbers.num1 - numbers.num2
    return {"result": result}
