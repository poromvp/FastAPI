from fastapi import FastAPI, Query, Depends, Body
from typing import Annotated

app = FastAPI()


# Part 24: Sub-Dependencies
def query_extractor(q: str | None = None):
    return q


def query_or_body_extractor(
    q: str = Depends(query_extractor), last_query: str | None = Body(None)
):
    if not q:
        return last_query
    return q


@app.post("/item")
async def try_query(query_or_body: str = Depends(query_or_body_extractor)):
    return {"q_or_body": query_or_body}
