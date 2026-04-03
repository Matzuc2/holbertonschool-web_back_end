#!/usr/bin/env python3
"""Hello world"""

from flask import Flask, jsonify, request, abort, redirect, make_response

from auth import Auth
from sqlalchemy.exc import NoResultFound

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def hello_world():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['GET', 'POST'])
def register():
    email = request.form.get('email')
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email=email, password=password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get("password")
    boolean = AUTH.valid_login(email=email, password=password)
    if boolean is False:
        abort(401)
    else:
        session_id = AUTH.create_session(email=email)
        data = {"email": email, "message": "logged in"}
        response = jsonify(data)
        response.set_cookie(key="session_id", value=session_id)
        return response


@app.route("/sessions", methods=['DELETE'])
def logout():
    session_id = request.cookies.get('session_id')
    try:
        user = AUTH._db.find_user_by(session_id=session_id)
        if user is None:
            return 403
        AUTH.destroy_session(user_id=user.id)
        return redirect('/')
    except NoResultFound:
        return make_response("", 403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
