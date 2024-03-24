#!/usr/bin/python
"""api entry point for find-artisans"""
from flask import Flask

app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)