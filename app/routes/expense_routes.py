from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from datetime import datetime
from app.models.user import User
from app.models.expense import Expense

# expense_bp = Blueprint('expense_bp', __name__, url_prefix='/expense')

# @expense_bp.route("/<user_id>/", methods=['GET'])
# def get_all_expenses():
    

#     selected_user = User.query.filter(User.email == user_email)

#     if not selected_user:
#         abort(make_response({'msg': 'user not found'}, 404))
    
#     return selected_user
    

# @user_bp.route("", methods=['POST'])
# def new_user():
#     request_body = request.get_json()
    
#     new_user = User(id_token=request_body['id_token'], email=request_body['email'], name=request_body['name'])

#     db.session.add(new_user)
#     db.session.commit()
#     return {
#         'id': new_user.user_id,
#         'email': new_user.email,
#         'msg': f'{new_user.name} has successfully created an account'
#     }, 201
