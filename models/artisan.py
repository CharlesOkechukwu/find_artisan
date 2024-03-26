#!/usr/bin/python3
"""artisan class module"""
from user import User, Base
from storage import Storage
import sqlalchemy
from sqlalchemy import Column, String, Integer, Foreignkey, Float
from sqlalchemy.orm import relationship

class Artisan(Base):
    """Artisan class containing services rendered by Artisans"""
    __tablename__ = "artisans"
    a_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, Foreignkey('users.id'), nullable=False)
    address = Column(String(300), nullable=False)
    phone_number = Column(String(300), nullable=False)
    email = Column(String(300), nullable=False)
    name = Column(String(200), Foreignkey('users.name'), nullable=False)
    business_name = Column(String(200), nullable=True)
    service = Column(String(100), nullable=False)
    bio = Column(String(300), nullable=False)
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)
    reviews = relationship("Reviews", backref="artisans")

    def __init__(self, **kwargs):
        """Initialize all values to be entered
        into the artisan table"""
        self.user_id = kwargs["user_id"]
        self.address = kwargs["address"]
        self.phone_number = kwargs["phone_number"]
        self.email = kwargs["email"]
        self.name = kwargs["name"]
        self.business_name = kwargs["business_name"]
        self.service = kwargs["service"]
        self.bio = kwargs["bio"]
        self.lat = kwargs["lat"]
        self.long = kwargs["long"]
    
    def get_service(self, id):
        """get artisan service where id is equal to a_id"""
        obj = storage.get_obj(id=id)
        return obj
    
    def all_services(self, user_id):
        """get all services of a user by id"""
        services = storage.get_all(user_id)
        return services