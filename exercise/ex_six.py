from typing import Annotated

from fastapi import FastAPI, Query

from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello World"}