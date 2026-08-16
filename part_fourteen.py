from fastapi import FastAPI

from pydantic import BaseModel

from typing import Literal, Union

app = FastAPI()


# Part 14: Extra Model
class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: Literal["car"] = "car"


class PlaneItem(BaseItem):
    type: Literal["plane"] = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]
