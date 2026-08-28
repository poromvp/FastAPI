import datetime
from typing import Annotated
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
    title="Smart Home IoT Hub",
    version="1.0",
)


class DeviceConfig(BaseModel):
    ip_address: Annotated[str, Field()]
    mac_address: Annotated[str, Field(..., pattern="MAC")]
    is_online: Annotated[bool, Field()] = False


class DeviceCreate(BaseModel):
    name: Annotated[str, Field(..., min_length=3)]
    device_type: Annotated[str, Field()]
    config: Annotated[DeviceConfig, Field()]


class RoomCreate(BaseModel):
    room_name: Annotated[str, Field()]
    floor: Annotated[int, Field(..., ge=0)]
    devices: Annotated[list[DeviceCreate], Field()]
