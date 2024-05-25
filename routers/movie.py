from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewars.jwt_bearer import JWTBearer
from models.movie import Movie as Model_Movie
from Config.database import Session
from pydantic import BaseModel, Field
from typing import Optional
from services.movie import MovieService


movie_router = APIRouter()

DB = Session()


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str
    year: int
    rating: float = Field(le=10)
    category: str

    class Config:
        json_schema_extra = {
            "example": {
               "title": "Titulo de ejemplo",
                "overview": "Descripcion de ejemplo",
                "year": 2009,
                "rating": 7.8,
                "category": "Acción"
            }
        }
 




@movie_router.get('/movies', tags=['movies'], response_model=list[Movie], dependencies=[Depends(JWTBearer())])
def get_movies() -> list[Movie]:
    
   
    pelis = MovieService(DB).get_movies()
    
    return JSONResponse(content=jsonable_encoder(pelis), status_code=200)


@movie_router.get('/movies/{movie_id}', tags=['movies'], response_model=Movie, status_code=200)
def get_movie(movie_id: int) -> Movie:
    
    
    peli = MovieService(DB).get_movie(movie_id)
    
    
    if not peli:
        return JSONResponse(content={'message': 'Pelicula no encontrada'}, status_code=404)
    else:
        return JSONResponse(content=jsonable_encoder(peli), status_code=200)


@movie_router.get('/movies/', tags=['movies'], response_model=list[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15) , year: int = Query(ge=1900, le=2022)) -> list[Movie]:
    
    mv = MovieService(DB).get_movies_by_category(category, year)
    
    
    return JSONResponse(content=jsonable_encoder(mv), status_code=200)


@movie_router.post('/movies/', tags=['movies'], response_model=dict)
def create_movie(movie: Movie) -> dict:
   
    new_movie = MovieService(DB).create_movie(movie)
    
    
    return JSONResponse(content={'message': 'Pelicula creada'}, status_code=200) #'Pelicula creada'

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict)
def update_movie(id: int, movie: Movie) -> dict:
    
    
    movi = MovieService(DB).get_movie(id)
    if not movi:
        return JSONResponse(content={'message': 'Pelicula no encontrada'}, status_code=404)
    
    return JSONResponse(content={'message': 'Pelicula actualizada'}, status_code=200) #'Pelicula actualizada'
    
        
    
        
@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict)
def delete_movie(id: int = Path(ge=1)) -> dict:
    
    mv = MovieService(DB).delete_movie(id)
    if not mv:
        return JSONResponse(content={'message': 'Pelicula no encontrada'}, status_code=404)
    return JSONResponse(content={'message': 'Pelicula eliminada'}, status_code=200) #'Pelicula eliminada'