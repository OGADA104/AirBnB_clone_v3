#!/usr/bin/python3
"""create app """
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_app_context(exception):
    """Close the database connection after each request."""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """run if main"""
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    threaded = True

    # Run the Flask server
    app.run(host=host, port=port, threaded=threaded, debug=True)
