import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

# ==========================================
# KHỞI TẠO ỨNG DỤNG
# ==========================================
app = FastAPI(title="Analytics Dashboard API", version="1.0.0")
