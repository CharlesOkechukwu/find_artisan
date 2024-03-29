#!/usr/bin/python3
"""set up blueprint for findartisan"""
from flask import Blueprint

fa_app = Blueprint("fa_app", __name__, url_prefix="/api")

from .account import *
from .home import *
from .artisan import *