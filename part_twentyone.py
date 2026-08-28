from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

fake_db = {}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: set[str] = set()


items = {
    "Pyrus": {"name": "drago", "price": 100},
    "Aquos": {
        "name": "elfin",
        "description": "day la mot guardiant bakugan",
        "price": 180,
        "tax": 20.2,
    },
    "Subterra": {
        "name": "wilda",
        "description": None,
        "price": 150.2,
        "tax": 10.2,
        "tags": [],
    },
}

# @app.put("/items/{id}")
# def update_item(id: str, item: Item):
#    json_compatible_item_data = jsonable_encoder(item)
#    fake_db[id] = json_compatible_item_data
#    print(fake_db)
#   return "Success"


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items.get(item_id)


@app.put("/items/{item_id}")
def update_bakugan(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


# stored_item_data = items.get("Pyrus")
# print(stored_item_data)


@app.patch("/items/{item_id}", response_model=Item)
async def patch_item(item_id: str, item: Item):
    stored_item_data = items.get(item_id)
    if stored_item_data is not None:
        stored_item_model = Item(**stored_item_data)

        update_data = item.model_dump(exclude_unset=True)
        print(update_data)
