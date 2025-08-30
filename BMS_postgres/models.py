from sqlalchemy import Column, Integer, String, Date,Enum as SEnum, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship
from enum import Enum as PyEnum

Base = declarative_base()

class Location(Base):
    __tablename__= 'locations'

    location_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    users = relationship('User',back_populates='location')

class IdentityEnum(PyEnum):
    Male = "Male"
    Female = "Female"

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    phone_no = Column(String, index=True, unique=True,nullable=True)
    email = Column(String, index=True, unique=True, nullable=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    bday = Column(Date, nullable=True)
    identity = Column(SEnum(IdentityEnum) , nullable=True)
    is_married = Column(Boolean, nullable=True)
    pincode = Column(Integer, nullable=True)
    address_line1 = Column(String, nullable=True)
    address_line2 = Column(String, nullable=True)
    landmark = Column(String, nullable=True)
    state = Column(String, nullable=True)
    city = Column(Integer,ForeignKey('locations.location_id'))

    location = relationship('Location',back_populates='users')

    __table_args__ = (
        CheckConstraint(
            'email IS NOT NULL OR phone_no IS NOT NULL',
            name="check_email_phone_not_null"
        ),
    )
