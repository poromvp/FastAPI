from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="BookStore API")

@app.get("/")
async def root():
    return {"message" : "Chào mừng đến với cửa hàng sách"}