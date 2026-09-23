from fastapi import (
    FastAPI, BackgroundTasks, Depends, Path, status
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
