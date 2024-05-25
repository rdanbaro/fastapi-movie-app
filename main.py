from fastapi import FastAPI, Body, Path, Query, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional


from Config.database import engine, Base, Session
from models.movie import Movie as Model_Movie
from fastapi.encoders import jsonable_encoder
from middlewars.error_handler import ErrorHandler
from middlewars.jwt_bearer import JWTBearer
from routers.movie import movie_router
from routers.auth import auth_router
from routers.user import user_router

app = FastAPI()
app.title = 'hola'
app.version = '500'
app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(user_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)





@app.get('/', tags=['hello', 'q boleiro'])
def message():
    return HTMLResponse('<h1>Hola</h1>')





