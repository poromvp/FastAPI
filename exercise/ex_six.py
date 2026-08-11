from typing import Annotated

from fastapi import FastAPI, Query, Path

from pydantic import BaseModel

app = FastAPI()

#d)
class Pet(BaseModel):
    name: str
    age: int

#a)
@app.get("/")
async def read_root():
    return {"message": "Chào mừng đến với Pet Store!"}

#b)
@app.get("/pets/{pet_id}")
async def read_pet(pet_id: int):
    return {"pet_id": pet_id}

#c)
@app.get("/pets/")
async def search_pets(type:str = "", limit:int = 10):
    return {"type": type, "limit": limit}

#d)
@app.post("/pets/")
async def create_pet(pet: Pet):
    return {"message": f"Pet {pet.name} created successfully!", "pet": pet}

#e)
@app.put("/pets/{pet_id}")
async def update_pet(pet_id: int, pet: Pet, is_adopted: bool = False):
    return {
        "message": f"Pet {pet_id} updated successfully!", 
        "pet": pet, 
        "is_adopted": is_adopted
        }

#f)
@app.get("/search/")
async def search_items(q: str = Query(..., min_length=3, max_length=15)):
    return {"search_keyword": q}

#g)
@app.get("/employees/")
async def read_employees(emp_code: str = Query(..., regex=r"^EMP\d{3}$",title="Employee Code")):
    return {"employee_code": emp_code}

#h)
@app.get("/items/{item_id}")
async def read_products(item_id: int = Path(..., ge=10, le=100)):
    return {"item_id": item_id}

#i)
@app.get("/tags/")
async def list_query_parameter(tags: list[str] = Query([])):
    return {"tags" : tags}

#j)
class Order (BaseModel):
    item_name: str
    quantity: int

@app.post("/orders/{order_id}")
async def create_order(*,order_id:int = Path(..., gt=0), discount_code: str = Query(None, max_length=8), order:Order):
    result = dict({"order id" : order_id, "order" : order})
    if discount_code:
        result.update({"discount_code" : discount_code})
    return result