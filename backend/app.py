
from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt, datetime

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'super_secret_key'

users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    for user in users:
        if user['email'] == data['email']:
            return jsonify({'error': 'User already exists'}), 400
    users.append(data)
    return jsonify({'message': 'User registered'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = next((u for u in users if u['email'] == data['email'] and u['password'] == data['password']), None)
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401
    token = jwt.encode({'email': user['email'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})

@app.route('/tools/pdf', methods=['POST'])
def summarize_pdf():
    return jsonify({'summary': 'This is a placeholder summary for PDF'}), 200

@app.route('/tools/ocr', methods=['POST'])
def ocr_tool():
    return jsonify({'text': 'This is a placeholder extracted text from image'}), 200
