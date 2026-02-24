#!/usr/bin/env python3
"""
Route module for the API.

This module initializes the Flask application, sets up CORS,
registers blueprints, configures authentication, and defines
error handlers for common HTTP errors.
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth = os.getenv("AUTH_TYPE")

if auth:
    print(auth)
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handle 404 Not Found errors.

    Args:
        error: The error object passed by Flask.

    Returns:
        str: A JSON response with an error message and 404 status code.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    Handle 401 Unauthorized errors.

    Args:
        error: The error object passed by Flask.

    Returns:
        str: A JSON response with an error message and 401 status code.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    Handle 403 Forbidden errors.

    Args:
        error: The error object passed by Flask.

    Returns:
        str: A JSON response with an error message and 403 status code.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """
    Execute before each request to validate authentication.

    This function runs before processing any request. It checks if
    authentication is required for the requested path and validates
    the authorization header and current user. If authentication fails,
    it aborts the request with appropriate HTTP error codes.

    Excluded paths that don't require authentication:
        - /api/v1/status/
        - /api/v1/unauthorized/
        - /api/v1/forbidden/

    Aborts with:
        - 401: If authorization header is missing or invalid.
        - 403: If the current user cannot be authenticated.

    Returns:
        None: Returns early if no authentication is needed.
    """
    if auth is None:
        return
    paths_without_auth = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/'
        ]
    if not auth.require_auth(request.path, paths_without_auth):
        return
    if not auth.authorization_header(request):
        abort(401)
    if not auth.current_user(request):
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
