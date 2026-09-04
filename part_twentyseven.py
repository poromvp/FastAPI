from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Decoded Header
# {
#  "alg": "HS256",
#  "typ": "JWT"
# }

# Decoded Payload
# {
#  "sub": "1234567890",
#  "name": "John Doe",
#  "admin": true,
#  "iat": 1516239022
# }

# JWT Signature Vetification
# a-string-secret-at-least-256-bits-long

# JSON Web Token
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30
