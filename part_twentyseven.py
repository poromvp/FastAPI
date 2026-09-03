from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

SECRET_KEY = "helloxinchaomoinguoidadenvoichannelcuaminh"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = dict(
    poro=dict(
        username="poromvp",
        full_name="poro mvp",
        email="quangkietle382@gmail.com",
        hashed_password="",
        disable=False,
    )
)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disable: bool = False
