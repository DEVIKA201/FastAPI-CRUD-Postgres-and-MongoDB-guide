from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime
from constants.movieEnum import LanguageEnum, FormatEnum, GenreEnums
from bson import ObjectId

class Movies(BaseModel):
    id: Optional[str] = Field(None,alias="_id")
    title: str
    date_of_release: datetime
    duration: str
    language: LanguageEnum
    rating : str
    format: FormatEnum
    genre: GenreEnums
    about : str
    is_active : bool
    is_available: bool
    is_stream : bool = False
    price_rent: Optional[float] = None
    price_buy: Optional[float] = None
    
class Config:
    populate_by_name = True

class MovieUpdate(Movies):
    title: Optional[str] =None
    date_of_release: Optional[datetime] = None
    duration: Optional[str] = None
    language: Optional[LanguageEnum] =None
    rating : Optional[str] =None
    format: Optional[FormatEnum]=None
    genre: Optional[GenreEnums] =None
    about : Optional[str] = None
    is_active : Optional[bool]=None
    is_available: Optional[bool]=None
    is_stream : Optional[bool]=None
    price_rent: Optional[float] = None
    price_buy: Optional[float] = None

class MovieDelete(BaseModel):
    message: str