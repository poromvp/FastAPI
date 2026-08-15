from fastapi import FastAPI, Query, Path, Body

from pydantic import BaseModel, Field

app = FastAPI()