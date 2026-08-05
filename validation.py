from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item (BaseModel):
    student_id : str
    name: str
    grade: int | None = None

@app.get("/items")
async def read_items(q: str | None = Query(None, min_length=3, max_length=10)):
    results = {"items" : "baa"}
    if q:
        results.update({"q" : q})
    return results