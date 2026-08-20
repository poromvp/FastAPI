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

#d) 