from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item (BaseModel):
    student_id : str
    name: str
    grade: int | None = None

@app.post("/items")
async def create_item(item : Item):
    item_dict = item.dict()
    if item.grade:
        item_dict.update({"descripton": f"{item.name} học lớp {item.grade} có mã số là {item.student_id}"})
    return item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id:int, item: Item):
    return {"item_id": item_id, **item.dict()}