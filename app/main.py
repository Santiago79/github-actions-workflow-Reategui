from fastapi import FastAPI
from pydantic import BaseModel
from .calculator import sum, resta, mult

app = FastAPI()

class CalcRequest(BaseModel):
    a: int
    b: int

@app.post("/sum")
def sum_endpoint(request: CalcRequest):
    return {"result": sum(request.a, request.b)}

@app.post("/resta")
def resta_endpoint(request: CalcRequest):
    return {"result": resta(request.a, request.b)}

@app.post("/mult")
def mult_endpoint(request: CalcRequest):
    return {"result": mult(request.a, request.b)}