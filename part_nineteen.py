import uuid
from datetime import datetime

from typing import Annotated, List
from fastapi import (
    Body,
    Cookie,
    FastAPI,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    status,
    File,
    UploadFile,
)
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI()

# Part 19: Handling Error
items = {"a": "item a"}


@app.get("/items/{item_id}")
async def get_item_by_id(item_id: Annotated[str, Path()]):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="item-id khong hop le",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}
