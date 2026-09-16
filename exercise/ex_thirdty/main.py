from fastapi import FastAPI

# Import các router từ các sub-module
from routers import users, entries
from internal import admin

app = FastAPI(
    title="E-Diary App", description="Ứng dụng chia nhỏ thành nhiều file (Part 30)"
)

# Nhúng (include) các router vào app chính
app.include_router(users.router)
app.include_router(entries.router)
app.include_router(admin.router)


@app.get("/")
async def root():
    return {"message": "Chào mừng đến với E-Diary System!"}
