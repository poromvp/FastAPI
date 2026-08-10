from typing import Annotated

from fastapi import FastAPI, Query

from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Chào mừng đến với Pet Store!"}