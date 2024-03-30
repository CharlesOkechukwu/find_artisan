#!/usr/bin/python
"""api entry point for find-artisans"""
import os
from flask import Flask, Blueprint
from . import fa_app


app = Flask(__name__)
app.secret_key = "findartisan"
app.register_blueprint(fa_app)

@app.teardown_appcontext
def close_con(statcode=None):
    """close connection to database"""
    from models import storage
    storage.close()

if __name__ == "__main__":
    app.run(debug=True)