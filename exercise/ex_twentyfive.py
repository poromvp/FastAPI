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
    Response,
)
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

fake_db: Dict[str, list] = {
    "rooms": [],
    "devices": [
        {"id": 1, "name": "Living Room Light", "type": "light"},
        {"id": 2, "name": "Front Camera", "type": "camera"},
    ],
}


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


@app.post("/login", tags=["Authentication"])
async def authenticate_login(
    response: Response,
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    if username == "admin" and password == "123456":
        response.set_cookie(key="session_token", value="super-iot-token")
        return {"message": "Dang nhap thanh cong, Cookie da duoc thiet lap"}
    raise HTTPException(status_code=400, detail="Sai username va password")


@app.get("/devices", tags=["IoT Devices"])
async def list_devices(
    filters: Annotated[DeviceFilter, Depends()],
    current_user: Annotated[dict, Depends(verify_user)],
):
    devices = fake_db["devices"]
    if filters.type_filter:
        devices = [d for d in devices if d.get("type") == filters.type_filter]
    return {
        "user": current_user,
        "filters_applied": {"skip": filters.skip, "limit": filters.limit},
        "data": devices[filters.skip : filters.skip + filters.limit],
    }


@app.post("/rooms", status_code=status.HTTP_201_CREATED, tags=["Rooms"])
async def create_room(
    room_data: Annotated[
        RoomCreate, Body(..., description="Du lieu JSON phuc tap da tang")
    ],
    current_user: Annotated[dict, Depends(verify_user)],
):
    new_room = room_data.model_dump()
    fake_db["rooms"].append(new_room)
    return {
        "message": f"Phong {room_data.room_name} da duoc tao boi {current_user['username']}",
        "room_info": new_room,
    }


@app.post("/devices/{device_id}/firmware")
async def update_firmware(
    device_id: Annotated[int, Path(..., ge=1, description="ID thiet bi can update")],
    version_name: Annotated[str, Form(description="Phien ban firmware, VD: v2.1.0")],
    file_firmware: Annotated[
        UploadFile, File(description="File nhi phan firmware(.bin)")
    ],
    current_user: Annotated[dict, Depends(verify_user)],
):
    if not any(d["id"] == device_id for d in fake_db["devices"]):
        raise HTTPException(status_code=404, detail="Khong tim thay thiet bi")

    return {
        "device_id": device_id,
        "action": "Firmware Uploaded",
        "version": version_name,
        "filename": file_firmware.filename,
        "uploaded_by": current_user["username"],
    }
