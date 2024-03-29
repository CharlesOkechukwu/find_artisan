#!/usr/bin/python3
"""module for artisan views"""
from flask import render_template, request, redirect, url_for, session
from models import storage
from . import fa_app
from werkzeug.utils import secure_filename
from models.artisan import Artisan


@fa_app.route("/artisan/add", strict_slashes=False, methods=['POST', 'GET'])
def add_artisan():
    """add an artisan to database"""
    if session.get('loggedin') is False:
        return redirect(url_for('fa_app.login'))
    return render_template('add_artisan.html')