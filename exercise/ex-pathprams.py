from fastapi import FastAPI

app = FastAPI()

@app.get("/books/{book_id}")
async def get_book_by_id(book_id : int):
    return {"book_id" : book_id, "title": "Sách bí ẩn"}

@app.get("/employees/{emp_id}")
async def get_employees_by_id(emp_id: int):
    return {"employee_id": emp_id, "status": "Active"}

@app.get("/categories/{category_name}/posts")
async def get_category_by_posts(category_name:str):
    return {"category": category_name, "message": "Danh sách bài viết của chuyên mục"}
