import uuid
from datetime import datetime

from typing import Annotated, List
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
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI()

# Part 18: Request Forms and Files


@app.post("/upload-file/")
async def upload(
    *,
    file: Annotated[bytes, File()],
    file_optional: Annotated[UploadFile | None, File()] = None,
    file_uploader: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file": len(file),
        "file_uploader": file_uploader.content_type,
        "token": token,
    }
