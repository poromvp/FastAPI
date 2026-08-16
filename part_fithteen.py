from fastapi import FastAPI, status

from pydantic import BaseModel

app = FastAPI()

# Part 15: Response status codes


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}


@app.delete("/items/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(pk: str):
    print("pk", pk)
    return pk
