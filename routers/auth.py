from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewars.jwt_bearer import JWTBearer
from models.user import User as Model_User
from pydantic import BaseModel, Field
from routers.user import User
from Config.database import Session
from utils.jwt_manager import create_token, validate_token

auth_router = APIRouter()
DB = Session()

@auth_router.post('/register', tags=['auth'], response_model=dict, status_code=201)
def register(user: User):
    new_user = Model_User(**user.model_dump())
    DB.add(new_user)
    DB.commit()
    return JSONResponse(content={'message': 'Usuario creado'}, status_code=201)

@auth_router.post('/login', tags=['auth'], response_model=dict)
def login(user: User):
    login_user = DB.query(Model_User).filter(Model_User.email == user.email and Model_User.password == user.password).first()
        
    if login_user:
        token =create_token(user.model_dump())
        return JSONResponse(content={'token': token, 'message': 'Credenciales correctas'}, status_code=200)
            
    return JSONResponse(content={'message': 'Credenciales incorrectas'}, status_code=401)
