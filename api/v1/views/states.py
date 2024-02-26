#!/usr/bin/python3
"""states view module"""
from models.state import State
from models import storage
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'])
def get_states():
    """return a json on states"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])
