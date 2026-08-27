from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

fake_db = {}


class Item(BaseModel):
    title: str
    timestap: datetime
    description: str | None = None


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    print(fake_db)
    return "Success"
