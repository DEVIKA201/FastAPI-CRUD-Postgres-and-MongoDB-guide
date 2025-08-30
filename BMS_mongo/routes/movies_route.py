from fastapi import APIRouter, HTTPException
from schema import Movies, MovieUpdate, MovieDelete
from db import db
from bson import ObjectId

router = APIRouter(prefix="/movies",tags=["Movies"])

def id_to_string(movie:dict) -> dict:
    movie["_id"] = str(movie["_id"])
    return movie

#Create movie
@router.post("/",response_model=Movies)
async def create_movie(movie:Movies):
    movie_dict = movie.model_dump(by_alias=True, exclude_none=True)
    #movie_dict = movie.dict(by_alias=True)
    result = await db["movie_details"].insert_one(movie_dict)
    movie_dict["_id"] = str(result.inserted_id)
    return movie_dict

#Fetch movies
@router.get("/",response_model=list[Movies])
async def get_movies():
    movies = await db["movie_details"].find().to_list()
    return [id_to_string(m) for m in movies]

#Fetch movies by id
@router.get("/{movie_id}",response_model=MovieUpdate)
async def get_movie_by_id(movie_id:str):
    movie = await db["movie_details"].find_one({"_id":ObjectId(movie_id)})
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found!")
    
    return id_to_string(movie)
    
#Update movie by id
@router.put("/{movie_id}",response_model=MovieUpdate)
async def update_movie(movie_id:str, movie:MovieUpdate):
    update_data = movie.model_dump(by_alias=True, exclude_none=True)
    result = await db["movie_details"].update_one(
        {"_id":ObjectId(movie_id)},
        {"$set":update_data}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Movie not found!")
    updated = await db["movie_details"].find_one({"_id":ObjectId(movie_id)})
    return id_to_string(updated)

#Delete movie by id
@router.delete("/{movie_id}")
async def delete_movie(movie:MovieDelete, movie_id:str):
    result = await db["movie_details"].update_one(
        {"_id":ObjectId(movie_id)},
        {"$set":{"is_available":False}}
    )
    if result.modified_count==0:
        raise HTTPException(status_code=404,detail="Movie doesn't exist")
    return {"message":"movie deleted successfully"}
