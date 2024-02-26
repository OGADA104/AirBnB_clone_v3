#!/usr/bin/python3
"""states view module"""
from models.state import State
from models import storage
from flask import jsonify
from api.v1.views import app_views
from flask import request


@app_views.route('/states', methods=['GET'])
def get_states():
    """return a json on states"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])

@app_views.route('/states/<id>', methods=['GET'])
def get_state_id(id):
    """gets a state identified by id"""
    state = storage.get(State, id)
    if state:
        return jsonify([state.to_dict()])
    else:
        return jsonify({"error": "Not found"}), 404

@app_views.route('/state/<id>', methods=['DELETE'])
def delete_state(id):
    """deletes a state identified by id"""
    state = storage.get(State, id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        return jsonify({"error": "Not found"}), 404

@app_views.route('/states', methods=['POST'])
def create_state():
    """Create a new state."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400

    new_state = State(**data)
    storage.new(new_state)
    storage.save()

    return jsonify(new_state.to_dict()), 201

@app_views.route('/states/<id>', methods=['PUT'])
def udate_state(id):
    """Update a state."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    state = storage.get(State, id)
    if not state:
        return jsonify({"error": "Not found"}), 404

    for key, value in data.items():
        if key != 'id' and key != 'created_at' and key != 'updated_at':
            setattr(state, key, value)

    storage.save()

    return jsonify(state.to_dict()), 200
