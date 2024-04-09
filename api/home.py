#!/usr/bin/python3
"""module to handle home page views for fa_app"""
from flask import app, render_template, request, session
from models import storage
from . import fa_app


@fa_app.route("/", strict_slashes=False, methods=['GET', 'POST'])
def home():
    """render home page"""
    user = None
    if session.get('loggedin')  == True:
        user = storage.get_user(session['id'])
    return render_template('index.html', user=user)