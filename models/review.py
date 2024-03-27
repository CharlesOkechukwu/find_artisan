#!/usr/bin/python3
"""review class module"""
from models import storage
from .user import Base
from sqlalchemy import Column, String, Integer, Foreignkey


class Review(Base):
    """Review class to record reviews on an artisan"""
    __tablename__ = "reviews"
    rid = Column(Integer, primary_key=True, autoincement=True)
    a_id = Column(Integer, Foreignkey("artisan.a_id"), nullable=False)
    comment = Column(String(300), nullable=False)
    rating = Column(Integer, nullable=False)
    uid = Column(Integer, Foreignkey("users.id"), nullable=False)
    rname = Column(String(200), Foreignkey("users.name"), nullable=False)

    def __init__(self, a_id, comment, rating, uid, rname):
        """Initiate class attributes and properties"""
        self.a_id = a_id
        self.comment = comment
        self.rating = rating
        self.uid = uid
        self.rname = rname

    def get_review(self, a_id):
        """get all reviews associated with a service or artisan"""
        reviews = storage.get_all(Review, a_id)
        return reviews