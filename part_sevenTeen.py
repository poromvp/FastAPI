import uuid
from datetime import datetime

from fastapi import (
    Body,
    Cookie,
    FastAPI,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    status,
    File,
    UploadFile,
)
from pydantic import BaseModel, Field

app = FastAPI()


# Part 17 Request File
@app.post("/files/")
async def create_file(f: bytes = File(...)):
    return {"file": len(f)}


@app.post("/upload-files/")
async def create_upload_files(files: UploadFile):
    return {"file-name": files.filename}
