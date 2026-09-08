import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

# ==========================================
# KHỞI TẠO ỨNG DỤNG
# ==========================================
app = FastAPI(title="Analytics Dashboard API", version="1.0.0")

# ==========================================
# NHÓM 1: CẤU HÌNH CORS (Bài a, b, c, d)
# ==========================================
# Danh sách các domain Frontend được phép truy cập
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # a) Chỉ cho phép các domain trong list
    allow_credentials=True,  # d) Cho phép gửi cookie/token
    allow_methods=["GET", "POST"],  # b) Chỉ cho phép GET và POST
    allow_headers=[
        "X-Dashboard-Token",
        "Content-Type",
        "Authorization",
    ],  # c) Giới hạn header
)
