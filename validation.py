from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item (BaseModel):
    student_id : str
    name: str
    grade: int | None = None

@app.get("/items")
async def read_items(q: list[str] | None = None):
    results : dict[str, str| list[str]] = {"items" : "baa"}
    if q is not None:
        results.update({"q" : q})
    return results