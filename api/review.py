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
        return redirect(url_for('fa_app.view_artisan', a_id=a_id, reviewd=reviewed,))