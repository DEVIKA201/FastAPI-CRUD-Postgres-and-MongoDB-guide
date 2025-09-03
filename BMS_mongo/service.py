from fastapi import HTTPException
from schema import Movies, MovieDelete, MovieUpdate
from bson import ObjectId
from db import db

#create a movie
async def create_movie_service(movie:Movies):
    movie_dict = movie.model_dump(by_alias=True, exclude_none=True)
    result = await db["movie_details"].insert_one(movie_dict)
    movie_dict["_id"] = str(result.inserted_id)
    return movie_dict

#Fetch all movies
async def get_movies_services():
    movies = await db["movie_details"].find().to_list()
    #convert movie id to string
    convert_id_to_string = []
    for movie in movies:
        movie["_id"] = str(movie["_id"])
        convert_id_to_string.append(movie)
    return convert_id_to_string

#Fetch movies by id
async def fetch_movie_by_id(movie_id:str):
    movie = await db["movie_details"].find_one({"_id":ObjectId(movie_id)})
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found!")
    movie["_id"]=str(movie["_id"])
    return movie
    
#Update movie by id
async def update_movie_by_id(movie_id:str, movie:MovieUpdate):
    update_data = movie.model_dump(by_alias=True, exclude_none=True)
    result = await db["movie_details"].update_one(
        {"_id":ObjectId(movie_id)},
        {"$set":update_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Movie not found!")
    updated_movie = await db["movie_details"].find_one({"_id":ObjectId(movie_id)})
    updated_movie["_id"] = str(updated_movie["_id"])
    return updated_movie

#Delete movie by id
async def delete_movie_by_id(movie_id:str):
    result = await db["movie_details"].update_one(
        {"_id":ObjectId(movie_id), "is_available":True},
        {"$set":{"is_available":False}}
    )
    if result.matched_count==0:
        raise HTTPException(status_code=404,detail="Movie doesn't exist")
    return {"message":"Movie deleted successfully"}
