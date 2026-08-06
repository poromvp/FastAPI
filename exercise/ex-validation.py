from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="BookStore API")

#a)
@app.get("/")
async def root():
    return {"message" : "Chào mừng đến với cửa hàng sách"}

#b)
@app.get("/books/{book_id}")
async def get_book_by_id(book_id:int):
    return {"book_id" : book_id, "status": "available"}
