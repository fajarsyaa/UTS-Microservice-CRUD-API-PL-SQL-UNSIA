from functools import wraps
from flask import request, jsonify, make_response
import os
import jwt
from datetime import datetime, timedelta

# Assuming users is defined here in decorates.py
users = {}

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the token from the Authorization header
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return make_response(
                jsonify({
                    'message': 'Unauthorized, missing or invalid token'
                }), 401
            )

        # Extract the token from the Authorization header
        user_token = auth_header.split(' ')[1]

        try:
            secret_key = 'secret999'  # Replace with your actual secret key
            payload = jwt.decode(user_token, secret_key, algorithms=['HS256'])
            is_admin = payload.get('is_admin', False)

             # Check the route permission based on user role
            if is_admin == False:
                return make_response(
                    jsonify({
                        'message': 'Unauthorized, only admins can access this menu'
                    }), 403
                )

            # You can access the decoded payload using payload['username']
        except jwt.ExpiredSignatureError:
            return make_response(
                jsonify({
                    'message': 'Token has expired'
                }), 401
            )
        except jwt.InvalidTokenError:
            return make_response(
                jsonify({
                    'message': 'Invalid token'
                }), 401
            )

        # Continue with the original functionality if the token is valid
        return f(*args, **kwargs)
    
    return decorated_function

def header_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the token from the Authorization header
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return make_response(
                jsonify({
                    'message': 'Unauthorized, missing or invalid token'
                }), 401
            )

        # Extract the token from the Authorization header
        user_token = auth_header.split(' ')[1]

        try:
            secret_key = 'secret999'  # Replace with your actual secret key
            payload = jwt.decode(user_token, secret_key, algorithms=['HS256'])

            # You can access the decoded payload using payload['username']
        except jwt.ExpiredSignatureError:
            return make_response(
                jsonify({
                    'message': 'Token has expired'
                }), 401
            )
        except jwt.InvalidTokenError:
            return make_response(
                jsonify({
                    'message': 'Invalid token'
                }), 401
            )

        # Continue with the original functionality if the token is valid
        
        return f(*args, **kwargs)
    
    return decorated_function