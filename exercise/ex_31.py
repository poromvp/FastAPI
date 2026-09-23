from fastapi import FastAPI, BackgroundTasks, Depends, Path, status
import time
import datetime

app = FastAPI(
    title="Notification & Audit System",
    description="Thực hành Background Tasks và Dependency Injection (Part 31)",
)
