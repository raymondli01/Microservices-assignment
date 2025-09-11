from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user store
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}

@app.get("/users/<int:user_id>")
def get_user(user_id: int):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.post("/users")
def create_user():
    new_user = request.get_json(force=True) or {}
    # Basic validation
    if not new_user.get("name") or not new_user.get("email"):
        return jsonify({"error": "Both 'name' and 'email' are required"}), 400
    next_id = max(users.keys(), default=0) + 1
    users[next_id] = {"name": new_user["name"], "email": new_user["email"]}
    return jsonify({"user_id": next_id}), 201

if __name__ == "__main__":
    # Listen on localhost:5001
    app.run(port=5001)
