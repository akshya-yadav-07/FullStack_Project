from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore
import pymongo # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore

app = Flask(__name__)
CORS(app)

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['user_database']

# Collections for users and details
users_collection = db['users']
details_collection = db['details']  # Define this collection for storing user details

# Sign up route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Check if the user already exists
    if users_collection.find_one({'email': email}):
        return jsonify({"error": "User already exists"}), 400

    # Hash the password and insert user into the database
    hashed_password = generate_password_hash(password)
    users_collection.insert_one({
        "email": email,
        "password": hashed_password
    })

    return jsonify({"message": "User signed up successfully"}), 201

# Login route (optional)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = users_collection.find_one({'email': email})

    # Check if user exists and password is correct
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({"message": "Logged in successfully", "email": user['email']}), 200

# Details form route
@app.route('/details', methods=['POST'])
def store_details():
    data = request.get_json()

    # Insert the details into MongoDB
    detail_id = details_collection.insert_one({
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone'],
        'address': data['address'],
        'city': data['city'],
        'state': data['state'],
        'zip': data['zip']
    }).inserted_id

    return jsonify({'message': 'Details stored successfully', 'id': str(detail_id)}), 200

if __name__ == '__main__':
    app.run(debug=True)
