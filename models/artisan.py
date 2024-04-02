#!/usr/bin/python3
"""artisan class module"""
from .user import Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Artisan(Base):
    """Artisan class containing services rendered by Artisans"""
    __tablename__ = "artisans"
    a_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    address = Column(String(300), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(250), nullable=False)
    country = Column(String(250), nullable=False)
    phone_number = Column(String(300), nullable=False)
    email = Column(String(300), nullable=False)
    name = Column(String(300), nullable=False)
    business_name = Column(String(200), nullable=True)
    service = Column(String(100), nullable=False)
    bio = Column(String(300), nullable=False)
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)
    image1 = Column(String(300), nullable=False)
    image2 = Column(String(300), nullable=True)
    image3 = Column(String(300), nullable=True)
    image4 = Column(String(300), nullable=True)
    def __init__(self, **kwargs):
        """Initialize all values to be entered
        into the artisan table"""
        self.user_id = kwargs["user_id"]
        self.address = kwargs["address"]
        self.city = kwargs["city"]
        self.state = kwargs["state"]
        self.country = kwargs["country"]
        self.phone_number = kwargs["phone_number"]
        self.email = kwargs["email"]
        self.name = kwargs["name"]
        self.business_name = kwargs["business_name"]
        self.service = kwargs["service"]
        self.bio = kwargs["bio"]
        self.image1 = kwargs["image1"]
        self.image2 = kwargs["image2"]
        self.image3 = kwargs["image3"]
        self.image4 = kwargs["image4"]
    
    def coordinates(self):
        """set coordinates of an address"""
        from geopy.geocoders import Nominatim
        full_address = self.address + ", " + self.city + ", " + self.state + ", " + self.country
        geolocator = Nominatim(user_agent = "fa_app")
        location = geolocator.geocode(full_address)
        if location is None:
            location = geolocator.geocode(self.city)
        self.lat = location.latitude
        self.long = location.longitude
    
    def get_distance(self, lat, long):
        """get distance between two addresses or location in kilometer"""
        from geopy import distance
        obj_loc = (self.lat, self.long)
        user_loc = (lat, long)
        dist = distance.distance(obj_loc, user_loc).km
        return dist