"""
Part 7 Body - Multiple Parameters
"""

from fastapi import FastAPI, Query, Path

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None
    

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150),
    q: str = Query(None),
    item: Item | None = None,
    user: User
):
    results = {"item_id": item_id}
    if q:
        results.update({"q" : q})
    if item:
        results.update({"item" :item})
    if user:
        results.update({"user" : user})
    return results