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


# ==========================================
# NHÓM 2: MIDDLEWARE DẠNG CLASS (Bài e, f, g)
# ==========================================
# Đây là cách làm hướng dẫn trong video part 28
class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # f) Bắt đầu bấm giờ
        start_time = time.time()

        # Chuyển request đi tiếp đến các middleware khác hoặc hàm xử lý (route)
        response = await call_next(request)

        # Tính toán thời gian xử lý
        process_time = time.time() - start_time

        # g) Thêm thông tin vào Header của Response trả về cho Client
        response.headers["X-Process-Time"] = f"{process_time:.4f} giây"

        return response


# Gắn class middleware vào ứng dụng
app.add_middleware(ProcessTimeMiddleware)


# ==========================================
# NHÓM 3: MIDDLEWARE DẠNG HÀM (Bài h, i)
# ==========================================
@app.middleware("http")
async def log_and_filter_requests(request: Request, call_next):
    # h) Ghi log request tới
    print(f"[LOG] Đang xử lý: {request.method} {request.url}")

    # i) Đánh chặn Request nếu có dấu hiệu xấu (Ví dụ: header X-Banned-IP)
    if "x-banned-ip" in request.headers:
        print("[CẢNH BÁO] Phát hiện IP bị cấm. Đã chặn request!")
        # Trả về lỗi trực tiếp mà KHÔNG gọi call_next (route bên dưới sẽ không được chạy)
        return JSONResponse(
            status_code=403,
            content={"detail": "Bạn không có quyền truy cập hệ thống này."},
        )

    # Nếu bình thường, cho phép request đi tiếp
    response = await call_next(request)

    return response


# ==========================================
# NHÓM 4: ENDPOINTS ĐỂ TEST (Bài j)
# ==========================================


@app.get("/api/data", tags=["Dashboard"])
async def get_chart_data():
    """Endpoint mô phỏng lấy dữ liệu dashboard"""
    # Dừng 0.1 giây để test X-Process-Time hiển thị rõ hơn
    time.sleep(0.1)
    return {"sales": 1500, "visitors": 3200, "status": "Good"}


@app.post("/api/reports", tags=["Dashboard"])
async def create_report(payload: dict):
    """Endpoint tạo báo cáo"""
    return {"message": "Báo cáo đã được tạo", "received_data": payload}
