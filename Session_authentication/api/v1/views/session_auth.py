#!/usr/bin/env python3
""" Module of session view
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def view():
    email=request.form.get('email',None)
    password=request.form.get('password', None)
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({'error': 'password missing'}), 400
    users = User.search({'email': email})
    if not users and len(users) == 0:
        return jsonify({ "error": "no user found for this email" }), 404
    if not users[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}),404 
    from api.v1.app import auth
    import os
    session_id = auth.create_session(users[0].id)
    response = users[0].to_json()
    out = jsonify(state=0, msg='success')
    out.set_cookie(os.environ['SESSION_NAME'], session_id)
    return response
    
