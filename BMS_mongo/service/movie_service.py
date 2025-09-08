from fastapi import HTTPException
from schema.movie_schema import AllMovies, Movies, MovieDelete, MovieUpdate
from schema.person_schema import CastCrew
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
    movies = await db["movie_details"].find(
        {},
        {"title":1,"language":1,"rating":1}
    ).to_list()
    for movie in movies:
        movie["_id"] = str(movie["_id"])
    return movies

#Fetch movies by id
async def fetch_movie_by_id(movie_id:str):
    pipeline = [
        {"$match":{"_id":ObjectId(movie_id)}},
        {
            "$lookup":{
                "from":"artist_details",
                "localField":"cast._id",
                "foreignField":"_id",
                "as": "cast_info"
            }
        },
        {
            "$lookup":{
                "from":"artist_details",
                "localField":"crew._id",
                "foreignField":"_id",
                "as":"crew_info"
            }
        },
        {
            "$project":{
                "_id": {"$toString": "$_id"},
                "title":1,
                "date_of_release":1,
                "duration":1,
                "language":1,
                "rating":1,
                "format":1,
                "genre":1,
                "about":1,
                "is_active":1,
                "is_available":1,
                "is_stream":1,
                "price_rent":1,
                "price_buy":1,
                "cast":1,
                "crew":1,

                "cast_info":{
                    "$map":{
                        "input":"$cast_info",
                        "as":"person",
                        "in":{
                            "_id":{"$toString":"$$person.id"},
                            "name":"$$person.name",
                            "occupation":"$$person.occupation",
                            "also_known":"$$person.also_known",
                            "birthplace":"$$person.birthplace",
                            "children":"$$person.children",
                            "about":"$$person.about",
                            "spouse":"$$person.spouse",
                            "family":"$$person.family",
                            "peer_and_more":"$$person.peer_and_more"
                        }
                    }
                },
                "crew_info":{
                    "$map":{
                        "input":"$crew_info",
                        "as":"person",
                        "in":{
                            "_id":{"$toString":"$$person.id"},
                            "name":"$$person.name",
                            "occupation":"$$person.occupation",
                            "also_known":"$$person.also_known",
                            "birthplace":"$$person.birthplace",
                            "children":"$$person.children",
                            "about":"$$person.about",
                            "spouse":"$$person.spouse",
                            "family":"$$person.family",
                            "peer_and_more":"$$person.peer_and_more"
                        }
                    }                    
                }
            }
        }
        
    ]

    movie = await db["movie_details"].aggregate(pipeline).to_list(length=1)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie[0]
    
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
