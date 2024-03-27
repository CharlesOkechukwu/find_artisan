#!/usr/bin/python
"""api entry point for find-artisans"""
from flask import Flask, Blueprint
from .views import fa_app


app = Flask(__name__)
app.register_blueprint(fa_app)



if __name__ == "__main__":
    app.run(debug=True)