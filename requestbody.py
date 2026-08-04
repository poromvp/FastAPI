from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item (BaseModel):
    student_id : str
    name: str
    grade: int | None = None

@app.post("/items")
async def create_item(item : Item):
    return item