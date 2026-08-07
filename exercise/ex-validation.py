from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="BookStore API")

# e)
class Book(BaseModel):
    title:str
    author:str
    price:float
    description:str | None = None

    

# a)
@app.get("/")
async def root():
    return {"message": "Chào mừng đến với cửa hàng sách"}


# c)
@app.get("/books/bestseller")
async def getBestSellerBook():
    return {"message": "Đây là sách bán chạy nhất"}


# b)
@app.get("/books/{book_id}")
async def getBookById(book_id: int):
    return {"book_id": book_id, "status": "available"}


# d)
@app.get("/books/")
async def findBooks(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit, "message": f"Trả về {limit} sách, bỏ qua {skip} sách đầu."}


# e)
@app.post("/books/")
async def create_book(book:Book):
    return {"message":"Sách đã được tạo thành công", "book_info" : book.model_dump()}


