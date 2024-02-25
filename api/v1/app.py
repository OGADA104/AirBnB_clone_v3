#!/usr/bin/python3
import os
from models import storage
from api.v1.views import app_views
from flask import Flask


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_app_context(exception):
    """Close the database connection after each request."""
    storage.close()


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    threaded = True

    # Run the Flask server
    app.run(host=host, port=port, threaded=threaded, debug=True)
