from fastapi import APIRouter

# Khởi tạo APIRouter cho Admin (Sub-app nội bộ)
router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/stats")
async def get_admin_stats():
    return {"total_users": 2, "total_entries": 15}
