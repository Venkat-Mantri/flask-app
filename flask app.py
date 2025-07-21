from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user store (dictionary)
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = str(len(users) + 1)  # Auto-increment ID
    users[user_id] = data
    return jsonify({"message": "User created", "user_id": user_id}), 201

# PUT update a user by ID
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id] = data
    return jsonify({"message": "User updated"})

# DELETE a user by ID
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)