#!/usr/bin/python
"""api entry point for find-artisans"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "Hello im running"

if __name__ == "__main__":
    app.run(debug=True)