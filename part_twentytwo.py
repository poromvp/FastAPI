from fastapi import FastAPI, Query, Depends
from typing import Annotated

app = FastAPI()


# Part 22: Dependencies Intro
@app.get("/items/")
async def common_parameters(
    q: Annotated[str | None, Query()] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(common: dict = Depends(common_parameters)):
    return common


@app.get("/users/")
async def read_users(common: dict = Depends(common_parameters)):
    return common
