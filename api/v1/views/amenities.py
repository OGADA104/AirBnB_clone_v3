#!/usr/bin/python3
"""states view module"""
from models.amenity import Amenity
from models import storage
from flask import jsonify
from api.v1.views import app_views
from flask import request, abort


@app_views.route('/amenities/', methods=['GET'])
def get_amenity():
    """return a json on states"""
    amenities = storage.all(Amenity).values()
    return jsonify([Amenity.to_dict() for amenity in amenities])


@app_views.route('/amenities/<id>', methods=['GET'])
def get_amenities_id(id):
    """gets a state identified by id"""
    amenities = storage.all(Amenity).values()
    amenity = [obj.to_dict() for obj in amenities if obj.id == id]
    if amenity:
        return jsonify([amenity])
    else:
        return jsonify({"error": "Not found"}), 404


@app_views.route('/amenities/<id>', methods=['GET', 'DELETE'])
def delete_amenity(id):
    """deletes a state identified by id"""
    amenity = storage.get(Amenity, id)
    if amenity is None:
        abort(404)
    
    storage.delete(amenity)
    storage.save()
    
    return jsonify({}), 200


@app_views.route('/amenities/', methods=['POST'])
def create_amenity():
    """Create a new state."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400

    new_amenity = Amenity(**data)
    storage.new(new_amenity)
    storage.save()

    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<id>', methods=['PUT'])
def update_amenity(id):
    """Update a state."""
    amenities = storage.all("Amenity").values()
    amenity = [obj.to_dict() for obj in amenities if obj.id == id]
    if state == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    state[0]['name'] = request.json['name']
    for obj in amenities:
        if obj.id == id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(state[0]), 200
