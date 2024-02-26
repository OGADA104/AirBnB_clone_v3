#!/usr/bin/python3
"""states view module"""
from models.state import State
from models import storage
from flask import jsonify
from api.v1.views import app_views
from flask import request, abort


@app_views.route('/states/', methods=['GET'])
def get_states():
    """return a json on states"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<id>', methods=['GET'])
def get_state_id(id):
    """gets a state identified by id"""
    states = storage.all(State).values()
    state = [obj.to_dict() for obj in states if obj.id == id]
    if state:
        return jsonify([state])
    else:
        return jsonify({"error": "Not found"}), 404


@app_views.route('/state/<id>', methods=['GET', 'DELETE'])
def delete_state(id):
    """deletes a state identified by id"""
    state = storage.get(State, id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'])
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
def update_state(id):
    """Update a state."""
    states = storage.all("State").values()
    state = [obj.to_dict() for obj in states if obj.id == id]
    if state == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    state[0]['name'] = request.json['name']
    for obj in states:
        if obj.id == id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(state[0]), 200
