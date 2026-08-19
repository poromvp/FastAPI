import uuid
from datetime import datetime

from typing import Annotated
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
async def create_file(
    files: Annotated[list[bytes], File(..., description="list of file")],
):
    return {"file": [len(file) for file in files]}


@app.post("/upload-files/")
async def create_upload_files(
    files: Annotated[list[UploadFile], File(..., description="list of file")],
):
    return {"file-name": [file.filename for file in files]}
