from flask import Blueprint, request, jsonify
from auth import create_jwt, verify_jwt
from datetime import datetime
from config import UTC, WIB

routes = Blueprint('routes', __name__)

@routes.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "adminpass":
        token = create_jwt(username)
        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401

@routes.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"message": "Token is missing"}), 403

    token = token.replace("Bearer ", "")
    decoded = verify_jwt(token)

    if isinstance(decoded, str):
        return jsonify({"message": decoded}), 403

    exp_wib = datetime.fromtimestamp(decoded["exp"], tz=UTC).astimezone(WIB).strftime('%Y-%m-%d %H:%M:%S %Z')

    return jsonify(
        {
            "message": "Access granted",
            "token expired at": exp_wib,
            "detail": decoded
        }
    )
