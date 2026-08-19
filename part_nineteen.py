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
    Request,
)
from fastapi.responses import HTMLResponse, JSONResponse
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


class ItemErrorHandler(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(ItemErrorHandler)
async def item_error_handler(request: Request, exc: ItemErrorHandler):
    return JSONResponse(
        status_code=418, content={"message": "Opps, something went wrong"}
    )


@app.get("/items-error/{name}")
async def get_item(name: Annotated[str, Path()]):
    if name == "aaa":
        raise ItemErrorHandler(name=name)
    return {"name": name}
