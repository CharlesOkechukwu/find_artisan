#!/usr/bin/python3
"""review class module"""
from .user import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from .artisan import Artisan

class Review(Base):
    """Review class to record reviews on an artisan"""
    __tablename__ = "reviews"
    rid = Column(Integer, primary_key=True, autoincrement=True)
    a_id = Column(Integer, ForeignKey("artisans.a_id"), nullable=False)
    comment = Column(String(300), nullable=False)
    rating = Column(Integer, nullable=False)
    uid = Column(Integer, ForeignKey("users.id"), nullable=False)
    rname = Column(String(200), nullable=False)

    def __init__(self, a_id, comment, rating, uid, rname):
        """Initiate class attributes and properties"""
        self.a_id = a_id
        self.comment = comment
        self.rating = rating
        self.uid = uid
        self.rname = rname