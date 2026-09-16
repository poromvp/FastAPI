from fastapi import APIRouter

# Khởi tạo APIRouter cho Entries[cite: 1]
router = APIRouter(prefix="/entries", tags=["Entries"])


@router.post("/")
async def create_entry():
    return {"message": "Đã tạo nhật ký mới thành công!"}
