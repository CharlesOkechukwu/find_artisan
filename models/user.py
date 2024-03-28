#!/usr/bin/python3
"""Module for User class"""
import bcrypt
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
class User(Base):
    """User class conatins all the details of the user"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(300), nullable=False)
    email = Column(String(300), nullable=False, unique=True)
    address = Column(String(300), nullable=True)
    city = Column(String(250), nullable=False)
    state = Column(String(250), nullable=False)
    country = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    """artisan = relationship("Artisan", backref="User")"""
    def __init__(self, **kwargs):
        """initiate variables"""
        self.name = kwargs['name']
        self.email = kwargs['email']
        self.address = kwargs['address']
        self.city = kwargs['city']
        self.state = kwargs['state']
        self.country = kwargs['country']
        self.__password = kwargs['password']
    
    def set_pass(self):
        """hash password and upload password"""
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(password=self.__password, salt=salt)
    
    def check_pass(self, password):
        """check password entered"""
        return bcrypt.checkpw(password, self.password.encode('utf-8'))
        