#!/usr/bin/python3
""" Index """

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def Api_Status():
    """ Status of API Returned in Json"""
    return jsonify({"status": "OK"})

@app_views.route('/stats')
def count():
    """Returns the number of each objects by type"""
    objects = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }
    objects = {k: storage.count(v) for k, v in objects.items()}
    return jsonify(objects)
