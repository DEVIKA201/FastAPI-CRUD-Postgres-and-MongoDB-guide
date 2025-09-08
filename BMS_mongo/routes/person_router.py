from fastapi import APIRouter
from service.person_service import get_people, get_person_by_id, update_person, soft_delete_person, create_person
from schema.person_schema import Person, DeletePerson, UpdatePerson

people_router = APIRouter(tags=["people"])

#Create new artist
@people_router.post("/person/",response_model=Person)
async def create_new_artist(artist: Person):
    return await create_person(artist)

#Fetch all artists
@people_router.get("/artists/",response_model=list[Person])
async def read_all_artist():
    return await get_people()

#Fetch an artist
@people_router.get("/artists/{artist_id}", response_model=Person)
async def read_artist(artist_id: str):
    return await get_person_by_id(artist_id)

#Update artist details
@people_router.put("/artists/{artist_id}",response_model=UpdatePerson)
async def update_artist_by_id(artist_id:str, artist: UpdatePerson):
    return await update_person(artist_id,artist)

#Soft delete artist
@people_router.delete("/artists/{artist_id}", response_model=DeletePerson)
async def delete_artist(artist_id:str):
    return await soft_delete_person(artist_id)
    