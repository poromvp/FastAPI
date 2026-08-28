import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from fastapi import (
    FastAPI,
    Path,
    Query,
    Body,
    Header,
    Form,
    File,
    UploadFile,
    Depends,
    HTTPException,
    Request,
    status,
)
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="E-Learning Platform API",
    description="Bai tap tong hop tu Part 2 den Part 25",
    version="1.0.0",
)
