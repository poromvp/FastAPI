from fastapi import FastAPI, status
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


class Tags(Enum):
    items = "items"
    users = "users"


@app.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.items],
    summary="Tao san pham",
    # description="Create an item with all the information",
    response_description="The created item",
)
async def create_item(item: Item):
    """
    Tao mot san pham voi tat ca thong tin:
    - name: moi item phai deu co ten
    - _description_: mo ta dai thon lon
    - **price**: required
    - __tax__: neu item khong co tinh thue thi bo
    - *tags*: item thuoc loai nao
    """
    return item


@app.get("/items/", tags=[Tags.items])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Kim Sang Sik"}]


# @app.get("/cates/{category}") Test Enum
# async def get_cate(category: Tags):
#    if category == Tags.items:
#        return {"message": Tags.items}
#    return {"message": Tags.users}


@app.get("/elements/", tags=[Tags.items], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
