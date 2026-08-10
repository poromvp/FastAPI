from typing import Annotated

from fastapi import FastAPI, Query

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