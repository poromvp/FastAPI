import uuid
from datetime import datetime

from typing import Annotated, List
from fastapi import (
    Body,
    Cookie,
    FastAPI,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    status,
    File,
    UploadFile,
)
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI(title="Mini E-Library", description="Project tổng hợp FastAPI Part 2-19")

fake_books_db = {
    1: {"id": 1, "title": "FastAPI Masterclass", "price": 19.99}
}
fake_users_db: dict[str,str] = {}

def fake_password_hasher(raw_password: str):
    return f"supersecret_{raw_password}"

#a) Nested & Extra Data Types: Tạo model Author (có UUID là id, tên, ngày sinh datetime).
class Author(BaseModel):
    id: Annotated[str, Field(uuid.uuid4())]
    name: Annotated[str, Field()]
    date: Annotated[datetime | None, Field()] = None

@app.post("/authors/")
async def create_author(author: Author):
    return {"author": author}


#b) Fields & Example: Tạo model Book chứa Author (Nested model). Dùng Field để ràng buộc giá sách > 0. Cấu hình Config để hiển thị dữ liệu mẫu (Example Data) trên Swagger UI.
class Book (BaseModel):
    id: Annotated[int, Field()]
    title: Annotated[str, Field(min_length=2, max_length=100)]
    price: Annotated[float, Field(gt=0.0)]
    author: Annotated[Author, Field()]
    model_config = {
            "json_schema_extra": {
                "examples" : [
                    {
                        "author" : {
                            "id" : "e4c2f507-f1dd-4b2c-b9dc-14af7f73eea8",
                            "name": "Trinh Tan Dat",
                            "date": "3" 
                        },
                        "price" : 12.5
                    }
                ]
            }
        }

@app.post("/books/")
async def create_book(book: Book):
    return {"book": book}

#c) Extra Models: Tạo 3 model cho người dùng: UserIn (có password), UserOut (không password), và UserInDB (có hashed_password).
class UserBase(BaseModel):
    username: str
    email:str

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    haspassword: Annotated[str, Field()]


#d) Form Fields: Tạo endpoint POST /login. Nhận username và password bằng Form (không phải JSON).

#e) Response Model: Tạo endpoint POST /users/register. Nhận vào UserIn, nhưng bắt buộc dùng response_model=UserOut để tự động lọc bỏ password khi trả về.

#f) Header & Cookie: Tạo endpoint GET /users/me. Yêu cầu một session_id từ Cookie và user_agent từ Header để giả lập việc kiểm tra phiên đăng nhập.

#g) String Validation (Query): GET /books. Nhận query q để tìm sách, yêu cầu độ dài tối thiểu 3 ký tự.