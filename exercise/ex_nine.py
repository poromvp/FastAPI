# Exercise 7 8 9

from fastapi import FastAPI

app = FastAPI()

#a)
@app.get("/")
async def read_root():
    return {"message" : "TechMart API"}

