import uvicorn

from typing import Union
from fastapi import FastAPI
from db.base import database
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def root():
	return {"Hello": "World"}

@app.on_event("startup")
async def startup():
	await database.connect()

@app.on_event("shutdown")
async def shutdown():
	await database.disconnect()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


if __name__ == "__main__":
	uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)