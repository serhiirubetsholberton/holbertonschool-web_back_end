#!/usr/bin/env python3
""" Basic Flask app, Register user, Log in, Log out, User profile,
    Get reset passwords token, Update password end-point """


from flask import Flask, jsonify, request, abort, redirect, make_response
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def get():
    """
        for now it only returns the
        jsonify message,
        only allow get request
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """get user credentials"""
    email = request.form["email"]
    password = request.form["password"]
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"})


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """log in function"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        sess = AUTH.create_session(email)
        resp = make_response({"email": email, "message": "logged in"})
        resp.set_cookie("session_id", sess)
        return resp

    abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout() -> None:
    """logout view"""
    session = request.cookies.get("session_id")
    try:
        user = AUTH.get_user_from_session_id(session_id=session)
    except NoResultFound:
        abort(403)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """return user's email"""
    session = request.cookies.get("session_id")
    try:
        user = AUTH.get_user_from_session_id(session_id=session)
    except NoResultFound:
        abort(403)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ Get reset passwords token, takes an email string argument and returns
        a JSON payload """
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """ Update password end-point, takes an email and reset_token string
        arguments and returns a JSON payload """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_pwd = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_pwd)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)

""" Start flask application """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
