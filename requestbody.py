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