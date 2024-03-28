#!/usr/bin/python3
"""module to handle account api views for fa_app"""
from flask import render_template, request
from models import storage
from . import fa_app
from models.user import User, Base

@fa_app.route("/signup", strict_slashes=False, methods=['GET', 'POST'])
def register():
    """render register template and process input"""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        pass1 = request.form['password']
        pass2 = request.form['cpass']
        if pass1 == pass2:
            password = pass1.encode('utf-8')
        else:
            msg = "Passwords don't match!"
        user_dict = {
            "name": name, "email": email, "address": address,
            "city": city, "state": state, "country": country,
            "password": password
        }
        user = User(**user_dict)
        user.set_pass()
        storage.add_new(user)
        storage.save()
    return render_template('signup.html')

@fa_app.route("/login", strict_slashes=False, methods=['POST', 'GET'])
def login():
    """login a user"""
    return render_template("login.html")