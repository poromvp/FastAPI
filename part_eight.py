"""
Part 7 Body - Multiple Parameters
"""

from fastapi import FastAPI, Query, Path, Body

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(...)
    ):
    results = {"item_id": item_id, "item" : item}
    return results