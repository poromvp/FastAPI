from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    item_name: str
    price: float

@app.post("/users/{user_id}/orders")
async def create_orders_for_user(user_id: int, order: Order, discount_code: str | None = None):
    order_dict = order.model_dump(); 
    if discount_code:
        order_dict.update({"discount_code": discount_code})
    return order_dict

class ProductInfo(BaseModel):
    name: str
    price: float

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: ProductInfo, force_update:bool = False):
    product_dict = product.model_dump()
    if force_update:
        product_dict.update({"name" : "Đã cập nhật"})
    return product_dict
