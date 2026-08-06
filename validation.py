from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    student_id: str
    name: str
    grade: int | None = None


@app.get("/items")
async def read_items(
    q: str | None = Query(
        None, 
        min_length=3, 
        max_length=10, 
        title="Sample query string",
        description="This is a sample query string",
        alias= "item-query"),
    ):
    #         dict[key, value có thể là str hoặc list[str]]
    results: dict[str, str | list[str]] = {"items": "baa"}
    if q is not None:
        results.update({"q": q})
    return results

@app.get("/items_hidden")
async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_querry": "Not found"}