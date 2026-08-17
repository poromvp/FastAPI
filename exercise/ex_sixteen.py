from fastapi import FastAPI, Path, Query
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

#c
@app.get("/books/")
async def get_books(skip:int = Query(0, gt=0), limit:int = Query(10, gt=0)):
    limit = limit + skip
    return {f"danh sach book tu {skip} den {limit}"}