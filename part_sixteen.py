from fastapi import FastAPI, Form

from pydantic import BaseModel, Field

app = FastAPI()

# Part 16: Form Fields


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    print("password", password)
    return {"username": username}
