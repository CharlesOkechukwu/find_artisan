#!/usr/bin/python3
"""Module for User class"""
import bcrypt
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class User(Base):
    """User class conatins all the details of the user"""
    def __init__(self, **kwargs):
        """initiate variables"""
        self.name = kwargs['name']
        self.email = kwargs['email']
        self.address = kwargs['address']
        self.city = kwargs['city']
        self.state = kwargs['state']
        self.country = kwargs['country']
        self.password = kwargs['password']
    
    def set_pass(self):
        """hash password and upload password"""
        password = self.password
        salt = bcrypt.gensalt()
        self.passowrd = bcrypt.hashpw(password=password, salt=salt)
    
    def check_pass(self, db_pass, u_pass):
        """check password entered"""
        return bcrypt.checkpw(passowrd=u_pass, hash_password=db_pass)
        