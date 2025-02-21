from flask import request, Flask, jsonify, Blueprint
from app.models import User
from flask import current_app as app
from flask_httpauth import HTTPBasicAuth
from app import db

main_routes = Blueprint('main_routes', __name__)

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    users = User.query.filter_by(username=username).first()
    if users and users.password == password:
        return username
    elif username == "admin" and password == "admin":
        return "admin"
    return None

@main_routes.route("/", methods=["GET"])
@auth.login_required
def home():
    return "Welcome to the User API"

@main_routes.route("/users", methods=["GET"])
@auth.login_required
def get_users():
    users = User.query.all()
    return jsonify([{"id":user.id,"username":user.username} for user in users])

@main_routes.route("/users/<int:id>", methods=["GET"])
@auth.login_required
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"id":user.id,"username":user.username})

@main_routes.route("/users", methods=["POST"])
@auth.login_required
def add_user():
    data = request.get_json()

    # Ensure required fields are present
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Missing username and password"}), 400

    # name = data['name']
    # email = data['email']
    username = data['username']
    password = data['password']

    # Default values for required fields
    default_name = "Default Name"
    default_email = f"{username}@example.com"

    # Check if username or email already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 400
    # if User.query.filter_by(email=email).first():
    #     return jsonify({"message": "Email already exists"}), 400

    # Create new user
    user = User(name=default_name, email=default_email, username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created", "id": user.id}), 201


@main_routes.route("/users/<int:id>", methods=["PUT"])
@auth.login_required
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    data = request.get_json()
    user.username = data['username']
    user.password = data['password']
    db.session.commit()
    return jsonify({"message": "User updated"}), 200

@main_routes.route("/users/<int:id>", methods=["DELETE"])
@auth.login_required
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200