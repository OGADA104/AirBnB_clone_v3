#!/usr/bin/python3
"""create app view"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models import amenity, city, place, review, state, user


@app_views.route('/status')
def status():
    """Returns a JSON response with status OK."""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """Returns statistics."""

    # Get the counts from your data storage
    amenity_count = len(storage.all(amenity))
    city_count = len(storage.all(city))
    place_count = len(storage.all(place))
    review_count = len(storage.all(review))
    state_count = len(storage.all(state))
    user_count = len(storage.all(user))

    # Construct the statistics data
    stat_data = {
        "amenities": amenity_count,
        "cities": city_count,
        "places": place_count,
        "reviews": review_count,
        "states": state_count,
        "users": user_count
    }

    return jsonify(stat_data)
