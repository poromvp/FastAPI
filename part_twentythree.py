from fastapi import FastAPI, Query, Depends
from typing import Annotated

app = FastAPI()


# Part 23:Classes as Dependencies
class Cat:
    def __init__(self, name: str):
        self.name = name


fake_items_db = [{"item_name": "pyrus", "item_name": "aquos", "item_name": "ventus"}]


class CommonQueryParams:
    def __init__(
        self,
        q: Annotated[str | None, Query()] = None,
        skip: Annotated[int, Query()] = 0,
        limit: Annotated[int, Query()] = 100,
    ):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"item": items})
    return response
