from flask import Blueprint, jsonify, request, make_response, abort
from requests import session
from app import db
from datetime import datetime
from app.models.user import User

user_bp = Blueprint('user_bp', __name__, url_prefix='/user')

@user_bp.route("/<user_email>", methods=['GET'])
def get_user(user_email):
    #valide if this email exists in our DB

    current_user = User.query.filter(User.email == user_email).first()

    if not current_user:
        abort(make_response({'msg': 'user not found'}, 404))
    
    return jsonify({"user_id": current_user.user_id, "id_token": current_user.id_token, "email": current_user.email, "name": current_user.name})    

@user_bp.route("", methods=['POST'])
def new_user():
    request_body = request.get_json()
    
    new_user = User(id_token=request_body['id_token'], email=request_body['email'], name=request_body['name'])

    db.session.add(new_user)
    db.session.commit()
    return {
        'id': new_user.user_id,
        'email': new_user.email,
        'msg': f'{new_user.name} has successfully created an account'
    }, 201

