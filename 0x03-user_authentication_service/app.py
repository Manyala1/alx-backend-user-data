#!/usr/bin/env python3
""" Route module for the API """
from flask import Flask, jsonify
from sqlalchemy.orm.exc import NoResultFound

from auth import Auth

app = Flask(__name__)
AUTH =AUTH()

@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return:
    -JSON payload
    """
    return jsonify({"message": "Bienvenue"})
