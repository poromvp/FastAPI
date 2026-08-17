from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#a
@app.get("/")
async def root():
    return {"message" : "Chào mừng bạn đã đến với trang web"}

#b
@app.get