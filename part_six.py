from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item_by_id(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=10, le=100),
    q: str
    ):
    result: dict[str, int | str] = {"item_id": item_id}
    if q:
        result.update({"q": q})
    return result