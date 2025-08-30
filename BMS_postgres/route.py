from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import service, models,schema
from db import engine, get_db
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

app = FastAPI()
models.Base.metadata.create_all(bind = engine)

####location####

#create location
@app.post("/locations/",response_model=schema.LocationCreate)
async def create_new_location(location:schema.LocationCreate, db:Session=Depends(get_db)):
    return service.create_location(db,location)

#get location
@app.get("/locations/",response_model=list[schema.LocationRead])
@app.get("/locations/{location_id}", response_model=schema.LocationRead) #get location by location id
async def get_locations(
    location_id : Optional[int] =None,
    db:Session=Depends(get_db)
):
    location = service.read_location(db, location_id)
    if location_id is not None and not location:
        raise HTTPException(status_code=404, detail="Location not found!")
    return location

####User###

#create user
@app.post("/users/",response_model=schema.UserCreate)
async def create_new_user(user:schema.UserCreate, db:Session= Depends(get_db)):
    return service.create_user(db,user)

#get user
@app.get("/users/", response_model=list[schema.UserRead])
@app.get("/users/{user_id}", response_model= schema.UserRead) # get user by user id
async def get_users(
    user_id : Optional[int] = None,
    db: Session = Depends(get_db)
):
    user = service.read_user(db, user_id)
    if user_id is not None and not user:
        raise HTTPException(status_code=404, detail="User not found!")
    return user
    
#update user
@app.put("/users/{user_id}",response_model=schema.UserRead)
async def update_existing_user(user:schema.UserUpdate, user_id:int, db: Session=Depends(get_db)):
    update_existing_user = service.update_user(db, user, user_id)
    if not update_existing_user:
        raise HTTPException(status_code=404, detail="User not found!")
    return update_existing_user

#delete user
@app.delete("/users/{user_id}",response_model= schema.UserRead)
async def delete_existing_user(user_id:int, db:Session = Depends(get_db)):
    delete_existing_user = service.delete_user(db,user_id)
    if delete_existing_user:
        return delete_existing_user
    raise HTTPException(status_code=404, detail="User not found")