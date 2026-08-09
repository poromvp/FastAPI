from typing import Annotated

from fastapi import FastAPI, Query
#from pydantic import BaseModel

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item_by_id(item_id: int, q:str | None = None):
    result = {"item_id" : item_id}
    if q:
        result.update({"q": q})
    return result