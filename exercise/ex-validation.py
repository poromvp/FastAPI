from fastapi import FastAPI, Query
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

# f)
@app.put("/books/{book_id}")
async def update_book(book_id:int, book:Book, is_discount:bool = False):
    final_price = book.price * 0.9 if is_discount else book.price
    return {
        "book_id": book_id,
        "is_discount_applied": is_discount,
        "final_price": final_price,
        "updated_data": book
    }

# g)
@app.get("/search/")
async def search_book(q:str = Query(..., min_length=3, max_length=50)):
    return {"search query": q, "message" : "Đang tìm kiếm..."}

# h)
@app.get("/users/verify")
async def verify_book(phone:str = Query(..., pattern=r"^0\d{9}$", description="Số điện thoại phải 10 số và bắt đầu bằng 0")):
    return {"phone": phone, "status": "Hợp lệ"}