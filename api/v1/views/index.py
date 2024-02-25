#!/usr/bin/python3
"""create app view"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """Returns a JSON response with status OK."""
    return jsonify({"status": "OK"})
