import os
from flask import Flask, jsonify, request

app = Flask(__name__)
APP_ENV = os.environ.get("APP_ENVIRONMENT", "development")

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

@app.route("/environment")
def environment():
    return jsonify({"environment": APP_ENV}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)