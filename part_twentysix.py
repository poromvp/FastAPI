from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_user = {
    "kiet": dict(
        username="a",
        full_name="aa",
        email="quangkietle382@gmail.com",
        hashed_password="fakeashedsecret",
        disable=False,
    ),
    "poro": dict(
        username="a",
        full_name="aa",
        email="quangkietle382@gmail.com",
        hashed_password="fakeashedsecret",
        disable=True,
    ),
}


def fake_hashed_password(password):
    return f"fakehashed{password}"


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disable: bool | None = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    return User(
        username=f"{token}fakedecoded",
        email="quangkietle382@gmail.com",
        fullname="PoroMVP",
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
