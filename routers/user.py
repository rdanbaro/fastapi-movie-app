from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewars.jwt_bearer import JWTBearer
from models.user import User as Model_User
from Config.database import Session
from pydantic import BaseModel, Field
from typing import Optional

user_router = APIRouter()

class User(BaseModel):
    email: str
    password: str

@user_router.get('/users', tags=['users'], response_model=list[User])
def get_users() -> list[User]:
    return JSONResponse(content=usuarios)
