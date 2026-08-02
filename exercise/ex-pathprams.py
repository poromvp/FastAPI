from fastapi import FastAPI

app = FastAPI()

@app.get("/books/{book_id}")
async def get_book_by_id(book_id : int):
    return {"book_id" : book_id, "title": "Sách bí ẩn"}
