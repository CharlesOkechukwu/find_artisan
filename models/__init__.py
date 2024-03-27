#!/usr/bin/python3
"""initiate storage class instance"""
from .storage_db import Storage

storage = Storage()
storage.load_db()