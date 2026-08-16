from fastapi import FastAPI, Query, Path, Body

from pydantic import BaseModel, Field

app = FastAPI()


# Part 13: Response Model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


# class ItemOut(BaseModel):
#    name: str
#    price: float


@app.post("/items/", response_model=Item, response_model_include={"name", "price"})
async def create_item(item: Item):
    return item
