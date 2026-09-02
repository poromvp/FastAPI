from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt

app = FastAPI()


class Token(BaseModel):
    access_token: str
    token_type: str


class UserInDB(BaseModel):
    username: str
    email: str
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


SECRET_KEY = "day_la_mot_chuoi_bi_mat_cuc_ky_kho_doan"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "hashed_password": get_password_hash("secret123"),
    }
}


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)

    # Xác thực Username và Password
    if not user_dict or not verify_password(
        form_data.password, user_dict["hashed_password"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sai tên đăng nhập hoặc mật khẩu",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Tạo Token
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Không thể xác thực thông tin đăng nhập",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user_dict = fake_users_db.get(username)
    if user_dict is None:
        raise credentials_exception

    return UserInDB(**user_dict)


@app.get("/users/me")
async def read_users_me(current_user: UserInDB = Depends(get_current_user)):
    # Ẩn password trước khi trả về
    return {"username": current_user.username, "email": current_user.email}


class UserCreate(BaseModel):
    username: str
    password: str


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    role: str = "user"


# Cấu hình JWT & Hashing
SECRET_KEY = "super-secret-key-rag"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")  # n) Cấu hình OAuth2

# Fake DB (Mô phỏng bảng SQLite)
fake_users_db = {
    "admin": UserInDB(
        username="admin", hashed_password=pwd_context.hash("123456"), role="admin"
    )
}


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Sai username hoặc password")

    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token không hợp lệ")
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token đã hết hạn")
    except JWTError:
        raise HTTPException(status_code=401, detail="Không thể xác thực token")


@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"user_profile": current_user}


@app.post("/chat/queries")
async def chat_with_llm(prompt: str, current_user: dict = Depends(get_current_user)):
    return {
        "user": current_user.get("sub"),
        "response": f"Đã truy xuất FAISS và trả lời cho: {prompt}",
    }


def require_admin(current_user: dict = Depends(get_current_user)):
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Cần quyền Admin để thao tác")
    return current_user
