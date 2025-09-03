from fastapi import APIRouter
from service import create_movie_service, get_movies_services, fetch_movie_by_id, update_movie_by_id, delete_movie_by_id
from schema import Movies, MovieDelete, MovieUpdate
from typing import List

movie_router = APIRouter(tags=["movies"])

#Create movie
@movie_router.post("/movies/",response_model=Movies)
async def create_movie(movie:Movies):
    return await create_movie_service(movie)

#Fetch movies
@movie_router.get("/movies/",response_model=list[Movies])
async def get_movies():
    return await get_movies_services()

#Fetch movies by id
@movie_router.get("/movies/{movie_id}",response_model=MovieUpdate)
async def get_movie_by_id(movie_id:str):
    return await fetch_movie_by_id(movie_id)

#Update movie by id
@movie_router.put("/movies/{movie_id}",response_model=MovieUpdate)
async def update_movie(movie_id:str, movie:MovieUpdate):
    return await update_movie_by_id(movie_id, movie)

#Delete movie by id
@movie_router.delete("/movies/{movie_id}",response_model=MovieDelete)
async def delete_movie(movie_id: str):
    return await delete_movie_by_id(movie_id)