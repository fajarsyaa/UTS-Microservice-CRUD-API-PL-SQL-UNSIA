import os
from ..models import User
from flask import request, jsonify, make_response, session
from flask_session import Session
from .. import db
from . import user_api_blueprint
from flask_login import login_user
from ..helper import AESCipher
from application.userservice.decorates import header_required, admin_required
import secrets
import jwt
from jwt import encode
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError


key = "rahasia"
cipher = AESCipher(key)

# users = {}

# Helper function to generate JWT token
def generate_jwt_token(username, is_admin=False):
    expiration_time = datetime.utcnow() + timedelta(days=1)  # Set token expiration time as needed
    payload = {
        'username': username,
        'exp': expiration_time,
        'is_admin': is_admin
    }
    secret_key = 'secret999'  # Change this to a strong secret key
    token = encode(payload, secret_key, algorithm='HS256')
    return token


# register
@user_api_blueprint.route('/api/admin/create', methods=['POST'])
def admin_register():
    

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    username = request.json['username']

    password  = cipher.encrypt((str(request.json['password'])))

    user = User()
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.password = password
    user.username = username
    user.is_admin = True
    user.authenticated = True

    try:
        # Tambahkan user ke sesi (session) basis data
        db.session.add(user)

        # Commit perubahan ke basis data
        db.session.commit()

        return jsonify({
            'message': 'ok',
            'result': user.to_json()
        })

    except IntegrityError as e:
        # Tangkap kesalahan jika terjadi IntegrityError (misalnya, duplikasi username atau email)
        db.session.rollback()  # Batalkan perubahan karena ada kesalahan

        return jsonify({
            'message': 'Username atau Email telah terdaftar',
        })

    except Exception as e:
        # Tangkap kesalahan umum lainnya
        db.session.rollback()  # Batalkan perubahan karena ada kesalahan

        return jsonify({
            'message': 'Terjadi kesalahan saat menambahkan pengguna ke basis data',
        })


# register
@user_api_blueprint.route('/api/user/create', methods=['POST'])
def user_register():
    

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    username = request.json['username']

    password  = cipher.encrypt((str(request.json['password'])))

    user = User()
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.password = password
    user.username = username
    user.is_admin = False
    user.authenticated = True

    try:
        # Tambahkan user ke sesi (session) basis data
        db.session.add(user)

        # Commit perubahan ke basis data
        db.session.commit()

        return jsonify({
            'message': 'ok',
            'result': user.to_json()
        })

    except IntegrityError as e:
        # Tangkap kesalahan jika terjadi IntegrityError (misalnya, duplikasi username atau email)
        db.session.rollback()  # Batalkan perubahan karena ada kesalahan

        return jsonify({
            'message': 'Username atau Email telah terdaftar',
        })

    except Exception as e:
        # Tangkap kesalahan umum lainnya
        db.session.rollback()  # Batalkan perubahan karena ada kesalahan

        return jsonify({
            'message': 'Terjadi kesalahan saat menambahkan pengguna ke basis data',
        })



# login
@user_api_blueprint.route('/api/user/login', methods=['POST'])
def post_login():
    username = request.json['username']
    user =  User.query.filter_by(username=username).first()
    if user:                
        if cipher.decrypt(user.password) == (str(request.json['password'])):
            is_admin = user.is_admin
            token = generate_jwt_token(username, is_admin=is_admin)
            session['token'] = token
            user.token = token

            # user.encode_api_key()
            db.session.commit()
            login_user(user)
            
            return make_response(
                jsonify({
                    'message':'log in success',
                    'token': token
                })
            )
    return make_response(
        jsonify({
            'message': 'logg in failed'
        }), 401
    )

# edit user
@user_api_blueprint.route('/api/user/edit/<int:user_id>', methods=['PUT'])
@admin_required
def edit_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return make_response(
            jsonify({
                'message': 'User not found'
            }), 404
        )

    # Dapatkan data yang dikirim dalam request JSON
    data = request.json

    # Cek apakah email atau username sudah terdaftar
    if 'email' in data and data['email'] != user.email:
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return make_response(
                jsonify({
                    'message': 'Email is already registered by another user'
                }), 400
            )

    if 'username' in data and data['username'] != user.username:
        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user:
            return make_response(
                jsonify({
                    'message': 'Username is already registered by another user'
                }), 400
            )

    # Update data pengguna sesuai kebutuhan
    if 'first_name' in data:
        user.first_name = data['first_name']
    if 'last_name' in data:
        user.last_name = data['last_name']
    if 'email' in data:
        user.email = data['email']
    if 'username' in data:
        user.username = data['username']
    if 'is_admin' in data:
        user.is_admin = data['is_admin']

    try:
        # Simpan perubahan ke database
        db.session.commit()
    except IntegrityError:
        # Tangani kesalahan integritas (duplikat email atau username)
        db.session.rollback()
        return make_response(
            jsonify({
                'message': 'Email or username is already registered by another user'
            }), 400
        )

    return make_response(
        jsonify({
            'message': 'User updated successfully',
            'data': user.to_json()
        }), 200
    )

@user_api_blueprint.route('/api/users', methods=['GET'])
@header_required    
def get_all_user():
    users = User.query.all()
    data = []
    for x in users:
        xusers = {}
        xusers['user_id'] = x.id
        xusers['username'] = x.username
        xusers['first_name'] = x.first_name
        xusers['last_name'] = x.last_name
        xusers['email'] = x.email
        data.append(xusers)
        
    return make_response(
        jsonify({
            'message':'success',
            'data': data
        }), 200
    )

# delete user
@user_api_blueprint.route('/api/user/delete/<int:user_id>', methods=['DELETE'])
@admin_required
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return make_response(
            jsonify({
                'message': 'User not found'
            }), 404
        )

    try:
        # Hapus user dari database
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        # Tangani kesalahan lain yang mungkin terjadi saat menghapus
        db.session.rollback()
        return make_response(
            jsonify({
                'message': f'Failed to delete user. Error: {str(e)}'
            }), 500
        )

    return make_response(
        jsonify({
            'message': 'User deleted successfully'
        }), 200
    )