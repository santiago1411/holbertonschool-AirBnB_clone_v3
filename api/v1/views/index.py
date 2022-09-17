#!/usr/bin/python3
""" Index """

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def Api_Status():
    """ Status of API Returned in Json"""
    return jsonify({"status": "OK"})

