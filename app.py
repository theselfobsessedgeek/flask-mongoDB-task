from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from mongoengine import connect
from models import Item
import os

# Boilerplate setup of the credentials
load_dotenv()
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
SECRET_KEY = os.getenv('SECRET_KEY')
app = Flask(__name__)
app.config['MONGO_URI'] = f"mongodb+srv://shubhamahlawatg:{MONGO_PASSWORD}@testingproject.m1y8rc8.mongodb.net/?retryWrites=true&w=majority&appName=testingProject"
app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['MONGODB_SETTINGS'] = {
    'db': 'testingProject',
    'host': f"mongodb+srv://shubhamahlawatg:{MONGO_PASSWORD}@testingproject.m1y8rc8.mongodb.net/?retryWrites=true&w=majority&appName=testingProject"
}

mongo = PyMongo(app)
jwt = JWTManager(app)

connect(db=app.config['MONGODB_SETTINGS']['db'], host=app.config['MONGODB_SETTINGS']['host'])

@app.route('/login', methods=['POST'])
def login():
    # Dummy login only for demonstration purposes
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username == 'user' and password == 'password':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/items', methods=['POST'])
@jwt_required()
def create_item():
    data = request.get_json()
    item = Item(**data)
    item.save()
    return jsonify({"message": "Item created successfully"}), 201

@app.route('/items', methods=['GET'])
def get_all_items():
    items = Item.objects.all()

    # Convert QuerySet to a list of dictionaries
    items_list = [{"name": item.name, "description": item.description, "created_at": item.created_at} for item in items]

    # Serialize the list of dictionaries
    return jsonify(items_list), 200

@app.route('/items/<item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = Item.objects.get_or_404(id=item_id)
    return jsonify(item), 200

@app.route('/items/<item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    data = request.get_json()
    Item.objects(id=item_id).update(**data)
    return jsonify({"message": "Item updated successfully"}), 200

@app.route('/items/<item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    Item.objects(id=item_id).delete()
    return jsonify({"message": "Item deleted successfully"}), 200

# Middleware - JWT Token Validation
@app.before_request
def jwt_token_validation():
    if request.endpoint and 'jwt' in app.extensions:
        jwt_required()(lambda: None)()

if __name__ == '__main__':
    app.run(debug=True)