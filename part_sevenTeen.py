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
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI()


# Part 17 Request File
@app.post("/files/")
async def create_file(
    files: Annotated[List[bytes], File(..., description="list of file")],
):
    return {"file": [len(file) for file in files]}


@app.post("/upload-files/")
async def create_upload_files(
    files: Annotated[List[UploadFile], File(..., description="list of file")],
):
    return {"file-name": [file.filename for file in files]}


@app.post("/load-file/")
async def load_files(files: List[UploadFile]):
    return {"file-name": [file.filename for file in files]}


# Thêm một giao diện HTML nhỏ để test thay cho Swagger UI
@app.get("/")
async def main():
    content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Upload Nhiều File</title>
    </head>
    <body>
        <h2>Giao diện Test Upload File Thực Tế</h2>
        <!-- Form này sẽ tự động gọi API /load-file/ của bạn -->
        <form action="/load-file/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit" value="Tải lên">
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=content)
