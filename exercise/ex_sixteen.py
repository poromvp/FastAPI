from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field

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

#d
class BookCreate(BaseModel):
    title: str = Field(..., min_length=3)
    author: str = Field(..., pattern="^AUTHOR-[A-z]+$")
    #j
    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "title" : "Lập trình Python",
                    "author" : "Trịnh Tấn Đạt"
                }
            ]
        }
    }

@app.post("/books/")
async def create_book(book: BookCreate):
    return book

#e 
@app.get("/books/search/")
async def search_book(keyword: str = Query(..., min_length=3, max_length=50)):
    return {"keyword" : keyword}

#f
@app.get("/authors/{author_id}")
async def get_author_by_id(author_id: int = Path(..., ge=1, le=1000)):
    return {"author_id" : author_id}

#g
class PublisherInfo(BaseModel):
    name:str

@app.put("/books/{book_id}")
async def update_book(*,book_id: int = Path(..., gt=0), publisher_info: PublisherInfo, importance: int = Body(...), book: BookCreate):
    return {
        "book_id" : book_id,
        "publisher_info" : publisher_info,
        "book": book,
        "importance" : importance
    }

#h
class MagazineCreate(BaseModel):
    price: int = Field(..., gt=0)
    code: str = Field(..., pattern="^MAG-\\d{4}$")

@app.post("/magazines/")
async def create_magazine(magazine: MagazineCreate):
    return {"magazine" : magazine}

#i
class Location(BaseModel):
    city: str
    zip_code: str

class LibaryCreate(BaseModel):
    books: list[BookCreate]
    location: Location

@app.post("/libraries/")
async def create_library(library: LibaryCreate):
    return {"library" : library}
