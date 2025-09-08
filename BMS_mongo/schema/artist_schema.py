from pydantic import BaseModel, Field
from typing import Optional, List
from constants.artist_venueEnum import OccupationEnum

class CastCrew(BaseModel):
    name: str
    role: str

class Artist(BaseModel):
    id : Optional[str] = Field(None,alias="_id")
    name : str
    occupation : OccupationEnum
    also_known : Optional[str] = None
    birthplace : str
    children: Optional[int] = None #count of children
    about : str
    spouse : Optional[str] = None
    family : Optional[List[CastCrew]] = None  #list of family and peer
    peer : Optional[List[CastCrew]] = None
    is_available: bool = True

class UpdateArtist(Artist):
    name : Optional[str] = None
    occupation : Optional[OccupationEnum] = None
    also_known : Optional[str] = None
    birthplace : Optional[str] = None
    children: Optional[int] = None #count of children
    about : Optional[str] = None
    spouse : Optional[str] = None
    family : Optional[List[CastCrew]] = None  #list of family and peer
    peer : Optional[List[CastCrew]] = None  
    is_available: bool = True
 

class DeleteArtist(BaseModel):
    message: str