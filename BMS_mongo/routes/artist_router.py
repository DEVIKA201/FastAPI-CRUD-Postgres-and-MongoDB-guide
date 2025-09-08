from fastapi import APIRouter
from service.artist_service import create_artist, get_artist_by_id, get_artists, update_artist, soft_delete_artist
from schema.artist_schema import Artist, UpdateArtist, DeleteArtist

artist_router = APIRouter(tags=["artists"])

#Create new artist
@artist_router.post("/artists/",response_model=Artist)
async def create_new_artist(artist: Artist):
    return await create_artist(artist)

#Fetch all artists
@artist_router.get("/artists/",response_model=list[Artist])
async def read_all_artist():
    return await get_artists()

#Fetch an artist
@artist_router.get("/artists/{artist_id}", response_model=Artist)
async def read_artist(artist_id: str):
    return await get_artist_by_id(artist_id)

#Update artist details
@artist_router.put("/artists/{artist_id}",response_model=UpdateArtist)
async def update_artist_by_id(artist_id:str, artist: UpdateArtist):
    return await update_artist(artist_id,artist)

#Soft delete artist
@artist_router.delete("/artists/{artist_id}", response_model=DeleteArtist)
async def delete_artist(artist_id:str):
    return await soft_delete_artist(artist_id)
    