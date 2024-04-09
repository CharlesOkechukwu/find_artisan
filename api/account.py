#!/usr/bin/python3
"""module to handle account api views for fa_app"""
from flask import render_template, request, redirect, session, url_for, flash
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
    msgs = {}
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password = password.encode('utf-8')
        obj = storage.get_obj(User, email)
        if obj is not None:
            verify = obj.check_pass(password)
            if verify == True:
                session['loggedin'] = True
                session['username'] = obj.name
                session['id'] = obj.id
                return redirect(url_for('fa_app.home'))
            else:
                msgs.update(login = "Invalid email or password!")
    return render_template("login.html", msgs=msgs)

@fa_app.route('/account', strict_slashes=False, methods=['POST', 'GET'])
def account():
    """display account details"""
    if session['loggedin'] == True:
        user = storage.get_user(session['id'])
        if request.method == 'GET':
            services = storage.get_myservices(session['id'])
            return render_template('account.html', user=user, services=services)
        else:
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']

            if address != "":
                user.address = address
            if city != "":
                user.city = city
            if state != "":
                user.state = state
            if country != "":
                user.country = country
            storage.save()
            flash("Account updated sucessfully")
            return redirect(url_for('fa_app.account'))
    else:
        return redirect(url_for('fa_app.login'))

@fa_app.route("/logout", strict_slashes=False)
def logout():
    """logout a user"""
    session.clear()
    return redirect(url_for('fa_app.home'))