from flask import Blueprint, request, jsonify, current_app
from app.models.user import User
from app.extensions import db, bcrypt
import jwt as pyjwt
import datetime
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

# Register
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if not email or not password or not name:
        return jsonify({'message': 'Missing required fields'}), 400
    
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'User already exists'}), 400
    
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_pw, name=name)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401
    
    token = create_access_token(identity=str(user.id))
    return jsonify({'token': token}), 200


