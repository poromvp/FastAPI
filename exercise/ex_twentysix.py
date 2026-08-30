from fastapi import FastAPI
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

fake_users_db = {"admin": {"username": "admin", "password": "secret123"}}


class User(BaseModel):
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str


def fake_decode_token(token: str):
    if token == "fake-super-secret-token":
        return {"username": "admin"}
    return None


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token không hợp lệ",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"message": "Bảo mật thành công!", "user_info": current_user}


@app.get("/public-data")
async def read_public_data():
    return {"message": "Ai cũng xem được dữ liệu này"}


@app.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)

    # Kiểm tra user có tồn tại và password có đúng không
    if not user_dict or form_data.password != user_dict["password"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Sai tên đăng nhập hoặc mật khẩu",
        )

    # Trả về token định dạng chuẩn
    return {"access_token": "fake-super-secret-token", "token_type": "bearer"}
