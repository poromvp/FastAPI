from fastapi import FastAPI, BackgroundTasks, Depends, Path, status
import time
import datetime

app = FastAPI(
    title="Notification & Audit System",
    description="Thực hành Background Tasks và Dependency Injection (Part 31)",
)


def write_audit_log(action: str, user_id: int):
    # time.sleep(3) giả lập việc xử lý nặng như gọi API bên thứ 3 hoặc gửi Email
    time.sleep(3)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] User {user_id}: {action}\n"

    with open("audit_log.txt", mode="a", encoding="utf-8") as log_file:
        log_file.write(log_message)


def write_ip_log(ip: str):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] SYSTEM: Request received from IP {ip}\n"

    with open("audit_log.txt", mode="a", encoding="utf-8") as log_file:
        log_file.write(log_message)


def track_request_ip(
    background_tasks: BackgroundTasks, ip_address: str = "192.168.1.100"
):
    """
    Dependency này nhận BackgroundTasks trực tiếp từ FastAPI.
    Nó sẽ chèn thêm một tác vụ ghi log IP vào hàng đợi chạy ngầm.
    """
    background_tasks.add_task(write_ip_log, ip_address)
    return ip_address


@app.post(
    "/users/{user_id}/notify",
    status_code=status.HTTP_202_ACCEPTED,  # Câu a: Trả về mã 202
    tags=["Notifications"],
)
async def send_user_notification(
    background_tasks: BackgroundTasks,  # Yêu cầu FastAPI cấp phát BackgroundTasks
    user_id: int = Path(..., ge=1),
    ip: str = Depends(track_request_ip),  # Câu e: Gọi Dependency
):
    """
    Gửi thông báo cho người dùng.
    API này trả về kết quả ngay lập tức nhờ ủy thác công việc cho Background Tasks.
    """
    action_desc = f"Sent push notification to device. (Requested from {ip})"
    background_tasks.add_task(write_audit_log, action_desc, user_id)

    # Người dùng nhận được JSON này tức thì, không cần đợi 3 giây
    return {
        "message": "Notification is being sent in the background",
        "user_id": user_id,
        "status": "Accepted",
    }


LOG_FILE = "tasks_log.txt"


def write_log(message: str):
    """Hàm phụ trợ ghi thông tin tác vụ vào file."""
    with open(LOG_FILE, mode="a", encoding="utf-8") as f:
        f.write(f"{message}\n")


def send_welcome_email(email: str):
    time.sleep(3)  # Giả lập độ trễ kết nối SMTP server
    write_log(f"[EMAIL] Đã gửi thư chào mừng đến địa chỉ: {email}")


def log_client_audit(tag: str):
    time.sleep(1)
    write_log(f"[AUDIT] Ghi nhận request từ Client-Tag: {tag}")


def optimize_image(image_id: int, quality: str):
    time.sleep(4)  # Giả lập thời gian nén ảnh
    write_log(f"[MEDIA] Ảnh #{image_id} đã được nén về chất lượng '{quality}'")


def send_invoice_email(order_id: int):
    time.sleep(2)
    write_log(f"[INVOICE] Hóa đơn cho đơn hàng #{order_id} đã được gửi thành công")


def update_inventory_analytics(order_id: int):
    time.sleep(1)
    write_log(f"[ANALYTICS] Kho hàng đã cập nhật dữ liệu thống kê cho đơn #{order_id}")


def audit_tracker(
    background_tasks: BackgroundTasks, client_tag: str | None = Header(default=None)
):
    """Dependency trích xuất Header và đẩy tác vụ audit vào hàng đợi nền."""
    if client_tag:
        background_tasks.add_task(log_client_audit, client_tag)
    return client_tag


class RegisterRequest(BaseModel):
    email: EmailStr
    username: str


@app.post("/register", status_code=status.HTTP_202_ACCEPTED, tags=["Auth"])
async def register_user(
    user: RegisterRequest,
    background_tasks: BackgroundTasks,
    client_tag: str | None = Depends(audit_tracker),
):
    # Đưa tác vụ gửi email vào nền
    background_tasks.add_task(send_welcome_email, user.email)

    return {
        "status": "success",
        "message": f"Tài khoản {user.username} đã được tạo. Các tác vụ thông báo đang chạy ngầm.",
        "client_tag": client_tag,
    }


@app.post("/images/optimize", status_code=status.HTTP_202_ACCEPTED, tags=["Media"])
async def process_image_optimization(
    image_id: int, target_quality: str, background_tasks: BackgroundTasks
):
    background_tasks.add_task(optimize_image, image_id, target_quality)
    return {
        "message": f"Yêu cầu nén ảnh #{image_id} đã được tiếp nhận.",
        "status": "Processing in background",
    }


@app.post("/orders/checkout", status_code=status.HTTP_202_ACCEPTED, tags=["Orders"])
async def checkout_order(order_id: int, background_tasks: BackgroundTasks):
    # Hệ thống chạy lần lượt các tác vụ được gắn vào
    background_tasks.add_task(send_invoice_email, order_id)
    background_tasks.add_task(update_inventory_analytics, order_id)

    return {
        "order_id": order_id,
        "message": "Đơn hàng đã thanh toán thành công, hệ thống đang đồng bộ hóa đơn và kho.",
    }
