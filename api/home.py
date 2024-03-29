#!/usr/bin/python3
"""module to handle home page views for fa_app"""
from flask import app, render_template, request
from models import storage
from . import fa_app


@fa_app.route("/", strict_slashes=False, methods=['GET', 'POST'])
def home():
    """render home page"""
    return render_template('index.html')