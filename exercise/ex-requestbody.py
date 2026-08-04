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

