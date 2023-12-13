from ..models import User
from flask import request, jsonify
# from passlib.hash import sha256_crypt
from .. import db
from . import user_api_blueprint
from cryptography.fernet import Fernet


@user_api_blueprint.route('/api/user/create', methods=['POST'])
def user_register():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    username = request.json['username']

    encryption_key = generate_key()
    password = encrypt_password((str(request.json['password'])), encryption_key)

    user = User()
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.password = password
    user.username = username
    user.authenticated = True

    db.session.add(user)
    db.session.commit()
    
    return jsonify(
        {
            'message':'user added',
            'result': user.to_json()
        }
    )

# Fungsi untuk menghasilkan kunci
def generate_key():
    return Fernet.generate_key()

# Fungsi untuk enkripsi password
def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(password.encode())
    return cipher_text

# Fungsi untuk dekripsi password
def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_text

