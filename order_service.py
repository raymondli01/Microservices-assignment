from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# In-memory order store
orders = {
    1: {"user_id": 1, "product": "Laptop"},
    2: {"user_id": 2, "product": "Smartphone"},
}

USER_SERVICE_URL = "http://localhost:5001"

@app.get("/orders/<int:order_id>")
def get_order(order_id: int):
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    # Fetch user details from the User Service
    try:
        resp = requests.get(f"{USER_SERVICE_URL}/users/{order['user_id']}", timeout=3)
        if resp.status_code == 200:
            result = dict(order)
            result["user"] = resp.json()
            return jsonify(result)
        else:
            return jsonify({"error": "Failed to fetch user details", "order": order}), 502
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "User Service unavailable", "details": str(e)}), 502

@app.post("/orders")
def create_order():
    new_order = request.get_json(force=True) or {}
    # Basic validation
    if "user_id" not in new_order or "product" not in new_order:
        return jsonify({"error": "Both 'user_id' and 'product' are required"}), 400

    next_id = max(orders.keys(), default=0) + 1
    orders[next_id] = {"user_id": int(new_order["user_id"]), "product": new_order["product"]}
    return jsonify({"order_id": next_id}), 201

if __name__ == "__main__":
    # Listen on localhost:5002
    app.run(port=5002)
