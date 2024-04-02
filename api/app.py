#!/usr/bin/python
"""api entry point for find-artisans"""
import os
from flask import Flask, Blueprint
from . import fa_app
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = "findartisan"
app.register_blueprint(fa_app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.teardown_appcontext
def close_con(statcode=None):
    """close connection to database"""
    from models import storage
    storage.close()

if __name__ == "__main__":
    app.run(debug=True)