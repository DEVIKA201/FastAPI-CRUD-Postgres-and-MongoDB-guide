from sqlalchemy.orm import Session
import models, route, schema

def create_user(db:Session, data: schema.UserCreate):
    user = models.User(**data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def read_user(db:Session, user_id: int | None = None):
    query = db.query(models.User)
    if user_id :
        return query.filter(models.User.user_id == user_id).first()
    return query.all()

def update_user(db:Session,user: schema.UserUpdate, user_id: int):
    update_query = db.query(models.User).filter(models.User.user_id == user_id).first()
    if update_query:
        for key,value in user.model_dump(exclude_unset=True).items():
            setattr(update_query,key,value)
    if not update_query:
        return None
    db.commit()
    db.refresh(update_query)
    return update_query

def delete_user(db:Session, user_id:int):
    delete_query = db.query(models.User).filter(models.User.user_id == user_id).first()
    if delete_query:
        db.delete(delete_query)
        db.commit()
    return delete_query

def create_location(db:Session, data:schema.LocationCreate):
    location = models.Location(**data.model_dump())
    db.add(location)
    db.commit()
    db.refresh(location)
    return location

def read_location(db:Session, location_id :int | None = None):
    query = db.query(models.Location)
    if location_id:
        return query.filter(models.Location.location_id == location_id).first()
    return query.all()
