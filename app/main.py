from typing import Union
from app.models import *
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome to Tenkara"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {
                "item_id": item_id, 
                "q": q
            }
      
@app.post("/movement/")
async def add_movement(movement: Movement):
    return movement

