#!/usr/bin/python3
"""states view module"""
from models.user import User
from models import storage
from flask import jsonify
from api.v1.views import app_views
from flask import request, abort


@app_views.route('/users/', methods=['GET'])
def get_users():
    """return a json on users"""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<id>', methods=['GET'])
def get_user_id(id):
    """gets a users identified by id"""
    users = storage.all(User).values()
    user = [obj.to_dict() for obj in users if obj.id == id]
    if state:
        return jsonify([user])
    else:
        return jsonify({"error": "Not found"}), 404


@app_views.route('/users/<id>', methods=['GET', 'DELETE'])
def delete_user(id):
    """deletes a user identified by id"""
    user = storage.get(User, id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users/', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    if 'email' not in data:
        return jsonify({"error": "Missing email"}), 400

    if 'password' not in data:
        return jsonify({"error": "Missing password"}), 400

    new_user = User(**data)
    storage.new(new_user)
    storage.save()

    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<id>', methods=['PUT'])
def update_user(id):
    """Update a user."""
    users = storage.all("User").values()
    user = [obj.to_dict() for obj in users if obj.id == id]
    if user == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    user[0]['name'] = request.json['name']
    for obj in users:
        if obj.id == id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(user[0]), 200
