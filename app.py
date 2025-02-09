from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import pymysql
import json
import os
import datetime

app = Flask(__name__)
CORS(app)

# JWT Configuration
app.config["JWT_SECRET_KEY"] = "super_secret_key"
jwt = JWTManager(app)

# Rate Limiting (100 requests per 15 minutes per IP)
limiter = Limiter(key_func=get_remote_address)
limiter.init_app(app)


# MySQL Configuration
db = pymysql.connect(host="localhost", user="root", password="Amos12!@", database="sss_db")

# File for logging metadata
LOG_FILE = "logs.json"

# Helper function: Log metadata
def log_metadata(action, item_id=None):
    log_data = {"timestamp": str(datetime.datetime.now()), "action": action, "item_id": item_id}
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            logs = json.load(file)
    logs.append(log_data)
    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

# Authentication: User login & JWT token generation
users = {"admin": "admin123"}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        access_token = create_access_token(identity=username)
        return jsonify(token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401

# CRUD Operations

@app.route("/api/items", methods=["POST"])
@jwt_required()
def create_item():
    data = request.json
    cursor = db.cursor()
    sql = "INSERT INTO items (name, description) VALUES (%s, %s)"
    cursor.execute(sql, (data["name"], data["description"]))
    db.commit()
    item_id = cursor.lastrowid
    log_metadata("CREATE", item_id)
    return jsonify({"message": "Item created successfully", "id": item_id})

@app.route("/api/items", methods=["GET"])
@jwt_required()
def get_items():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    return jsonify(items)

@app.route("/api/items/<int:item_id>", methods=["GET"])
@jwt_required()
def get_item(item_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    return jsonify(item)

@app.route("/api/items/<int:item_id>", methods=["PUT"])
@jwt_required()
def update_item(item_id):
    data = request.json
    cursor = db.cursor()
    sql = "UPDATE items SET name=%s, description=%s WHERE id=%s"
    cursor.execute(sql, (data["name"], data["description"], item_id))
    db.commit()
    log_metadata("UPDATE", item_id)
    return jsonify({"message": "Item updated successfully"})

@app.route("/api/items/<int:item_id>", methods=["DELETE"])
@jwt_required()
def delete_item(item_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM items WHERE id=%s", (item_id,))
    db.commit()
    log_metadata("DELETE", item_id)
    return jsonify({"message": "Item deleted successfully"})

# Rate Limiting Middleware
@app.errorhandler(429)
def ratelimit_error(e):
    return jsonify(error="Rate limit exceeded. Try again later."), 429

# Error Handling
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error="Internal server error. Please try again later."), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
