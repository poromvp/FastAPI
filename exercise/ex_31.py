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
