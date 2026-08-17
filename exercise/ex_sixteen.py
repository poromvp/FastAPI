from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

#a
@app.get("/")
async def root():
    return {"message" : "Chào mừng bạn đã đến với trang web"}

#b
@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int = Path(..., gt=0)):
    return {"book_id" : book_id}