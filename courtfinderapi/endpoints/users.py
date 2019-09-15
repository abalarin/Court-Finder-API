from flask import Blueprint, jsonify, request
from flask_cors import CORS

from passlib.hash import sha256_crypt


from courtfinderapi.app import session, client
from courtfinderapi.models.users import User

users = Blueprint("users", __name__)

CORS(users) # enable CORS on the courts blue print

@users.route('/login', methods=['POST'])
def login():
    username = request.json['user']['username']
    password_candidate = request.json['user']['password']

    if username is None or password_candidate is None:
        return {"error": "Plz info"}

    result = session.query(User).filter_by(username=username).first()
    print(result)

    # If a user exsists and passwords match - login
    if result is not None and sha256_crypt.verify(password_candidate, result.password):
        return {"msg" : "success"}
    else:
        return {"msg" : "failure"}, 401
