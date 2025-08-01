from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import jwt
import datetime

app = Flask(__name__)
CORS(app)  # Enable global CORS
app.config['SECRET_KEY'] = 'y23@8f$kS!p2Lz7#MhD9G@qWeTz*XvB0'

users = []
otp_store = {}

# ✅ Send OTP (with OPTIONS handling)
@app.route('/send-otp', methods=['POST', 'OPTIONS'])
@cross_origin()
def send_otp():
    if request.method == 'OPTIONS':
        return '', 200  # Preflight response

    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    # Simulate OTP generation and store
    otp = "123456"  # Replace with real OTP logic later
    otp_store[email] = otp
    print(f"[INFO] OTP for {email}: {otp}")

    return jsonify({'message': f'OTP sent to {email}'}), 200

# ✅ Register
@app.route('/register', methods=['POST', 'OPTIONS'])
@cross_origin()
def register():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    otp = data.get('otp')

    # Validate fields
    if not all([name, email, password, confirm_password, otp]):
        return jsonify({'error': 'All fields are required'}), 400
    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match'}), 400
    if otp_store.get(email) != otp:
        return jsonify({'error': 'Invalid OTP'}), 400

    for user in users:
        if user['email'] == email:
            return jsonify({'error': 'User already exists'}), 400

    users.append({'name': name, 'email': email, 'password': password})
    del otp_store[email]
    return jsonify({'message': 'User registered successfully'}), 201

# ✅ Login
@app.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin()
def login():
    if request.method == 'OPTIONS':
        return '', 200

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = next((u for u in users if u['email'] == email and u['password'] == password), None)
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401

    token = jwt.encode(
        {'email': user['email'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )
    return jsonify({'token': token})

# ✅ Sample tool route (protected)
@app.route('/tools/pdf', methods=['POST', 'OPTIONS'])
@cross_origin()
def summarize_pdf():
    if request.method == 'OPTIONS':
        return '', 200
    return jsonify({'summary': 'This is a placeholder summary for PDF'}), 200

# ✅ OCR tool route
@app.route('/tools/ocr', methods=['POST', 'OPTIONS'])
@cross_origin()
def ocr_tool():
    if request.method == 'OPTIONS':
        return '', 200
    return jsonify({'text': 'This is a placeholder extracted text from image'}), 200

# ✅ Health check
@app.route('/')
def home():
    return 'Backend is running.'

# ✅ Start app
if __name__ == '__main__':
    app.run(debug=True)

