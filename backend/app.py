from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import smtplib
import os

app = Flask(__name__)
CORS(app)

otp_store = {}

# Send OTP
@app.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.get_json()
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    otp = str(random.randint(100000, 999999))
    otp_store[email] = otp

    # Simulate sending OTP (in real-world use SMTP or an email API)
    print(f"Sending OTP {otp} to {email}")

    return jsonify({"message": "OTP sent successfully"}), 200

# Register
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    otp = data.get("otp")
    password = data.get("password")
    confirm_password = data.get("confirm_password")

    if not all([name, email, otp, password, confirm_password]):
        return jsonify({"error": "All fields are required"}), 400

    if otp_store.get(email) != otp:
        return jsonify({"error": "Invalid or expired OTP"}), 400

    if password != confirm_password:
        return jsonify({"error": "Passwords do not match"}), 400

    del otp_store[email]
    return jsonify({"message": "Registration successful!"}), 200

@app.route("/", methods=["GET"])
def home():
    return "Backend Running"

if __name__ == "__main__":
    app.run(debug=True)
