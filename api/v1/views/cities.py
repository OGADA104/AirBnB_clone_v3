#!/usr/bin/python3
"""states view module"""
from models.city import City
from models import storage
from flask import jsonify, abort
from api.v1.views import app_views
from flask import request


@app_views.route('/cities/', methods=['GET'])
def get_cities():
    """return a json on city"""
    cities = storage.all(City).values()
    return jsonify([city.to_dict() for city in cities])

@app_views.route('/cities/<id>', methods=['GET'])
def get_city_id(id):
    """gets a city identified by id"""
    cities = storage.all(City).values()
    city = [obj.to_dict() for obj in cities if obj.id == id]
    if city:
        return jsonify([city])
    else:
        return jsonify({"error": "Not found"}), 404

@app_views.route('/cities/<id>', methods=['DELETE'])
def delete_city(id):
    """deletes a city identified by id"""
    cities = storage.all("City").values()
    city = [obj.to_dict() for obj in cities if obj.id == id]
    if state == []:
        abort(404)
    state.remove(city[0])
    for obj in cities:
        if obj.id == id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200

@app_views.route('/cities/', methods=['POST'])
def create_city():
    """Create a new city."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400

    new_city = City(**data)
    storage.new(new_city)
    storage.save()

    return jsonify(new_city.to_dict()), 201

@app_views.route('/cities/<id>', methods=['PUT'])
def update_city(id):
    """Update a city."""
    cities = storage.all("City").values()
    city = [obj.to_dict() for obj in cities if obj.id == id]
    if city == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    city[0]['name'] = request.json['name']
    for obj in cities:
        if obj.id == id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(state[0]), 200
