from fastapi import FastAPI, Query
app = FastAPI()


@app.get("/items/{item_id}")
async def read_item_by_id(item_id: int, q: str | None = Query(None, alias="item_query")):
    result: dict[str, int | str] = {"item_id": item_id}
    if q:
        result.update({"q": q})
    return result