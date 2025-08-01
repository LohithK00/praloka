from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import smtplib
import os

app = Flask(__name__)
CORS(app)

otp_store = {}

# Set your Gmail + App Password here
SMTP_EMAIL = 'lohithdarling55@gmail.com'  # Replace with your Gmail
SMTP_PASSWORD = 'foktiyygwngkuwle'  # Replace with your Gmail App Password
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

@app.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.get_json()
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    otp = str(random.randint(100000, 999999))
    otp_store[email] = otp

    subject = "Your Praloka OTP Code"
    body = f"Your OTP for Praloka registration is: {otp}"
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(SMTP_EMAIL, email, message)
        print(f"OTP {otp} sent to {email}")
        return jsonify({"message": "OTP sent successfully"}), 200
    except Exception as e:
        print("Email sending failed:", str(e))
        return jsonify({"error": "Failed to send OTP"}), 500

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
