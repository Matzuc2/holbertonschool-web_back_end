#!/usr/bin/env python3
""" Module of session view
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """POST, it is to log into your account"""

    from api.v1.app import auth
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({'error': 'password missing'}), 400
    users = User.search({'email': email})
    if not users and len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    if not users[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    session_id = auth.create_session(users[0].id)
    response = jsonify(users[0].to_json())
    response.set_cookie(os.environ['SESSION_NAME'], session_id)
    return response


@app_views.route(
        '/auth_session/logout', methods=['DELETE'], strict_slashes=False
        )
def delete():
    """DELETE, it is the route to logout from your account"""

    from api.v1.app import auth
    success = auth.destroy_session(request)
    if success is False:
        abort(404)
    if success is True:
        return jsonify({}), 200
