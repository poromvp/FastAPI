from fastapi import FastAPI, Query, Path, Body

from pydantic import BaseModel, Field

app = FastAPI()

#Part 10 - Declare Request Example Data

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., examples={
    "normal" : {
        "summary" : "test case 1",
        "name" : "bakugan",
        "description" : "cap nhat item thanh cong",
        "price" : 1.2,
        "tax" : 1.6
    }
})):
    result = {"item_id": item_id, "item":item}
    return result