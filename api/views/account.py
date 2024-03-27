#!/usr/bin/python3
"""module to handle account api views for fa_app"""
from flask import render_template
from models import storage
from . import fa_app
from models.user import User, Base

@fa_app.route("/signup", strict_slashes=False)
def register():
    """render register template and process input"""
    render_template('signup.html')