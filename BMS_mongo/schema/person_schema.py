from pydantic import BaseModel, Field
from typing import Optional, List
from constants.person_venueEnum import OccupationEnum

class CastCrew(BaseModel):
    id : Optional[str] = Field(None,alias="_id")
    role: Optional[str]=None

class Person(BaseModel):
    id : Optional[str] = Field(None,alias="_id")
    name : str
    occupation : List[OccupationEnum]
    also_known : Optional[str] = None
    birthplace : str
    children: Optional[int] = None #count of children
    about : str
    spouse : Optional[str] = None
    family : Optional[List[CastCrew]] = None  #list of family and peer
    peer_and_more : Optional[List[CastCrew]] = None
    is_available: bool = True

class UpdatePerson(Person):
    name : Optional[str] = None
    occupation : Optional[List[OccupationEnum]] = None
    also_known : Optional[str] = None
    birthplace : Optional[str] = None
    children: Optional[int] = None #count of children
    about : Optional[str] = None
    spouse : Optional[str] = None
    family : Optional[List[CastCrew]] = None  #list of family and peer
    peer_and_more : Optional[List[CastCrew]] = None  
    is_available: bool = True
 

class DeletePerson(BaseModel):
    message: str