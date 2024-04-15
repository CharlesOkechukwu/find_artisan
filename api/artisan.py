#!/usr/bin/python3
"""module for artisan views"""
import os
from flask import render_template, request, redirect, url_for, session, current_app
from models import storage
from . import fa_app
from flask import jsonify, flash
from werkzeug.utils import secure_filename
from models.artisan import Artisan


@fa_app.route("/artisan/add", strict_slashes=False, methods=['POST', 'GET'])
def add_artisan():
    """add an artisan to database"""
    if session.get('loggedin') is None:
        return redirect(url_for('fa_app.login'))
    else:
        msgs = {}
        if request.method == 'POST':
            name = session['username']
            business_name = request.form['business_name']
            service = request.form.get('service', False)
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            phone_number = request.form['phone_number']
            email = request.form['email']
            bio = request.form['bio']
            file1 = request.files['image1']
            image1 = upload_file(file1)
            file2 = request.files['image2']
            image2 = upload_file(file2)
            file3 = request.files['image3']
            image3 = upload_file(file3)
            file4 = request.files['image4']
            image4 = upload_file(file4)
            artisan_dict = {
                "user_id": session['id'], "name": name, "business_name": business_name,
                "service": service, "address": address, "city": city, "state": state,
                "country": country, "phone_number": phone_number, "email": email,
                "bio": bio, "image1": image1, "image2": image2, "image3": image3,
                "image4": image4
            }
            artisan = Artisan(**artisan_dict)
            artisan.coordinates()
            storage.add_new(artisan)
            storage.save()
            msgs.update(success = "Service added sucessfully!")
            msgs.update(more = "Have more services you render? Add them below!")
        return render_template('add_artisan.html', msgs=msgs)

def allowed_file(filename):
    """check if file is allowed"""
    allowed = ['png', 'jpg', 'jpeg']
    return '.' in filename and filename.split('.')[-1] in allowed

def upload_file(file):
    """Upload a file and return url to path"""
    upload_folder = 'api/static/uploads'
    current_app.config['UPLOAD'] = upload_folder
    current_app.config['UPLOAD_FOLDER'] = '/static/uploads/'
    filename = secure_filename(file.filename)
    if filename == '':
        return None
    if file and allowed_file(filename):
        file.save(os.path.join(current_app.config['UPLOAD'], filename))
        image = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        return image
    else:
        flash("Invalid file format, only png, jpg and jpeg allowed!")
        return None

@fa_app.route("/artisan/<a_id>", strict_slashes=False)
def view_artisan(a_id):
    """view an artisan details on a single page"""
    artisan = storage.get_artisan(a_id)
    reviews = storage.get_reviews(a_id)
    if artisan is None:
        return "no artisan found"
    return render_template('view_artisan.html', artisan=artisan, reviews=reviews)

@fa_app.route("/services/<input>", strict_slashes=False, methods=['POST', 'GET'])
def services(input):
    """view all services"""
    services = None
    get_services = storage.get_services(input)
    services = [service.service for service in get_services]
    services = list(set(services))
    if services == []:
        return ["Sorry can't find the service you're looking for"]
    return jsonify(services)

@fa_app.route("/artisan/find", strict_slashes=False, methods=['POST'])
def find_artisan():
    """find artisans that render a service around you"""
    from geopy.geocoders import Nominatim
    if request.method == 'POST':
        service = request.form['search']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        filter = request.form.get('filters')

        full_address = address + ", " + city + ", " + country

        geolocator = Nominatim(user_agent = "fa_app")
        location = geolocator.geocode(full_address)
        if location is None:
            location = geolocator.geocode(city)
        lat = location.latitude
        long = location.longitude

        artisans = None
        if filter == "nearby":
            objs = storage.get_by_city(city, service)
            artisans = []
            for obj in objs:
                distance = obj.get_distance(lat, long)
                if distance < 30:
                    artisans.append(obj)
        elif filter == "in-city":
            artisans = storage.get_by_city(city, service)
        elif filter == "in-state":
            artisans = storage.get_by_state(state, service)
        else:
            artisans = storage.get_by_country(country, service)
        return render_template('display.html', artisans=artisans)

@fa_app.route("/artisan/delete/<a_id>", strict_slashes=False)
def delete_artisan(a_id):
    """delete an artisan from database"""
    artisan = storage.get_artisan(a_id)
    storage.delete(artisan)
    storage.save()
    flash("Service deleted sucessfully!")
    return redirect(url_for('fa_app.account'))
    
@fa_app.route("/artisan/edit/<a_id>", strict_slashes=False, methods=['POST', 'GET'])
def edit_artisan(a_id):
    """edit an artisan details"""
    if session['loggedin'] == True:
        artisan = storage.get_artisan(a_id)
        if request.method == 'GET':
            return render_template('edit_artisan.html', artisan=artisan)
        else:
            business_name = request.form['business_name']
            service = request.form.get('service', False)
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            phone_number = request.form['phone_number']
            email = request.form['email']
            bio = request.form['bio']
            if business_name != "":
                artisan.business_name = business_name
            if service != "":
                artisan.service = service
            if address != "":
                artisan.address = address
            if city != "":
                artisan.city = city
            if state != "":
                artisan.state = state
            if country != "":
                artisan.country = country
            if phone_number != "":
                artisan.phone_number = phone_number
            if email != "":
                artisan.email = email
            if bio != "":
                artisan.bio = bio
            storage.save()
            flash("Service updated sucessfully!")
            return redirect(url_for('fa_app.account'))

    else:
        return redirect(url_for('fa_app.login'))