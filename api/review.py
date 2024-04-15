#!/usr/bin/python3
"""module for review views"""
import os
from flask import render_template, request, redirect, url_for, session, current_app
from models import storage
from . import fa_app
from models.review import Review


@fa_app.route("/review/add/<int:a_id>", strict_slashes=False, methods=['POST', 'GET'])
def add_review(a_id):
    """add a review to database"""
    if request.method == 'POST':
        rating = request.form['rating']
        comment = request.form['comment']
        rname = session['username']
        uid = session['id']
        review = Review(a_id=a_id, comment=comment, rating=rating, uid=uid, rname=rname)
        storage.add_new(review)
        storage.save()
        reviewed = True
        msg = "Your Review Was Added Sucessfully!"
        return redirect(url_for('fa_app.view_artisan', a_id=a_id, reviewed=reviewed,))

@fa_app.route("/review/<a_id>/<int:rid>", strict_slashes=False, methods=['POST'])
def update_review(a_id, rid):
    """update a review"""
    if request.method == 'POST':
        review = storage.get_review(rid)
        rating = request.form['rating']
        comment = request.form['comment']
        if review != "":
            review.rating = rating
        if comment != "":
            review.comment = comment
        storage.save()
    return redirect(url_for('fa_app.view_artisan', a_id=a_id))