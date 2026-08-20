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

app = FastAPI()

#a) Nested & Extra Data Types: Tạo model Author (có UUID là id, tên, ngày sinh datetime).

#b) Fields & Example: Tạo model Book chứa Author (Nested model). Dùng Field để ràng buộc giá sách > 0. Cấu hình Config để hiển thị dữ liệu mẫu (Example Data) trên Swagger UI.

#c) Extra Models: Tạo 3 model cho người dùng: UserIn (có password), UserOut (không password), và UserInDB (có hashed_password).

#d) Form Fields: Tạo endpoint POST /login. Nhận username và password bằng Form (không phải JSON).

#e) Response Model: Tạo endpoint POST /users/register. Nhận vào UserIn, nhưng bắt buộc dùng response_model=UserOut để tự động lọc bỏ password khi trả về.

#f) Header & Cookie: Tạo endpoint GET /users/me. Yêu cầu một session_id từ Cookie và user_agent từ Header để giả lập việc kiểm tra phiên đăng nhập.

#g) String Validation (Query): GET /books. Nhận query q để tìm sách, yêu cầu độ dài tối thiểu 3 ký tự.