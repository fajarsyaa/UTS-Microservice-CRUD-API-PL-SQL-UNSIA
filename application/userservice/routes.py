import os
from ..models import User
from flask import request, jsonify, make_response
from .. import db
from . import user_api_blueprint
from flask_login import login_user
from ..helper import AESCipher
from application.userservice.decorates import header_required


key = "rahasia"
cipher = AESCipher(key)


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
    user.authenticated = True

    db.session.add(user)
    db.session.commit()
    
    return jsonify(
        {
            'message':'user added',
            'result': user.to_json()
        }
    )


# login
@user_api_blueprint.route('/api/user/login', methods=['POST'])
def post_login():
    username = request.json['username']
    user =  User.query.filter_by(username=username).first()
    if user:                
        if cipher.decrypt(user.password) == (str(request.json['password'])):
            user.encode_api_key()
            db.session.commit()
            login_user(user)
            
            return make_response(
                jsonify({
                    'message':'logged in',
                    'token': user.api_key
                })
            )
    return make_response(
        jsonify({
            'message': 'not logged in'
        }), 401
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