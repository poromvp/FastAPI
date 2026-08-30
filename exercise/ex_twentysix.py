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
