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
