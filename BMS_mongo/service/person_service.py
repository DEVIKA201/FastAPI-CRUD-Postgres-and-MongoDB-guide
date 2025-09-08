from schema.person_schema import Person, UpdatePerson, DeletePerson
from db import db
from bson import ObjectId
from fastapi import HTTPException

#Create new artist
async def create_person(artist: Person):
    artist_dict = artist.model_dump(by_alias=True, exclude_none=True)
    result = await db["artist_details"].insert_one(artist_dict)
    artist_dict["_id"] = str(result.inserted_id)
    return artist_dict 

#Fetch artist 
async def get_people():
    people = await db["artist_details"].find().to_list()
    convert_id_to_string = []
    for artist in people:
        artist["_id"] = str(artist["_id"])
        convert_id_to_string.append(artist)
    return convert_id_to_string 

#Fetch artist by id
async def get_person_by_id(artist_id:str):
    person = await db["artist_details"].find_one({"_id":ObjectId(artist_id)})
    if not person:
        raise HTTPException(status_code=404, detail="Artist not found!")
    person["_id"]=str(person["_id"])
    return person

#Update an artist
async def update_person(artist_id: str, artist: UpdatePerson):
    update_data = artist.model_dump(by_alias=True, exclude_none=True)
    result = await db["artist_details"].update_one(
        {"_id":ObjectId(artist_id)},
        {"$set":update_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Artist not found!")
    updated_artist = await db["artist_details"].find_one({"_id":ObjectId(artist_id)})
    updated_artist["_id"] = str(updated_artist["_id"])
    return updated_artist    

#Delete artist
async def soft_delete_person(artist_id: str):
    result = await db["artist_details"].update_one(
        {"_id":ObjectId(artist_id),"is_available":True},
        {"$set":{"is_available":False}}
    )
    if result.matched_count ==0:
        raise HTTPException(status_code=404, detail="Artist doesn't exits")
    return {"message":"Artist deleted successfully"}