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
)
from pydantic import BaseModel, Field

app = FastAPI()