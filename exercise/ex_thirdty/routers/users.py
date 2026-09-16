from fastapi import APIRouter

# Khởi tạo APIRouter cho Userss
router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def read_users():
    return [{"username": "alice"}, {"username": "bob"}]
