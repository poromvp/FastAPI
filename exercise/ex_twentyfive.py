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
    Cookie,
)
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


class DeviceConfig(BaseModel):
    ip_address: Annotated[str, Field(..., pattern=r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")]
    mac_address: Annotated[str, Field(..., min_length=7, max_length=17)]
    is_online: Annotated[bool, Field()] = False


class DeviceCreate(BaseModel):
    name: Annotated[str, Field(..., min_length=3, max_length=50)]
    device_type: Annotated[str, Field(..., pattern=r"^(light|thermostat|camera)$")]
    config: Annotated[DeviceConfig, Field()]


class RoomCreate(BaseModel):
    room_name: Annotated[str, Field(..., min_length=3)]
    floor: Annotated[int, Field(..., ge=0)]
    devices: Annotated[list[DeviceCreate], Field()]


class DeviceFilter:
    def __init__(
        self,
        skip: Annotated[int, Query(ge=0)] = 0,
        limit: Annotated[int, Query(ge=1, le=50)] = 10,
        type_filter: Annotated[
            str | None, Query(description="Loc theo loai: light, camera,...")
        ] = None,
    ):
        self.skip = skip
        self.limit = limit
        self.type_filter = type_filter


def get_token(session_token: Annotated[str | None, Cookie()] = None):
    if not session_token:
        raise HTTPException(status_code=401, detail="Vui long dang nhap (Thieu cookie)")
    return session_token


def verify_user(token: Annotated[str | None, Depends(get_token)]):
    if token != "super-iot-token":
        raise HTTPException(
            status_code=403, detail="token khong phai la super-iot-token"
        )
    return {"username": "home_owner"}


def verify_admin_key(
    x_admin_key: Annotated[str, Header(description="Header bat buoc cho quyen admin")],
):
    if x_admin_key != "admin-secret":
        raise HTTPException(status_code=403, detail="Tai khoan khong co quyen Admin")


app = FastAPI(
    title="Smart Home IoT Hub", version="1.0", dependencies=[Depends(verify_admin_key)]
)


@app.post("/test/")
async def testing_model(device: RoomCreate):
    return device
