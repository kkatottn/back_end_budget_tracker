from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from datetime import datetime
from app.models.user import User

user_bp = Blueprint('user_bp', __name__, url_prefix='/user')

@user_bp.route("/<user_email>", methods=['GET'])
def get_user(user_email):
    #valide if this email exists in our DB

    selected_user = User.query.filter(User.email == user_email)

    if not selected_user:
        abort(make_response({'msg': 'user not found'}, 404))
    
    return selected_user
    

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

@user_bp.route("/<user_id>", methods=['GET'])
def get_budget(user_id):
    current_user = User.query.get(user_id)
    current_budget = current_user.budget

    if current_budget is None:
        abort(make_response({'msg': 'budget is not set yet!'}, 404))
    
    return current_budget

# @user_bp.route("/<user_id>", methods=['POST'])
# def new_budget(user_id):
#     request_body = request.get_json()
    
#     current_user = User.query.get(user_id)
#     new_budget = Budget(amount=request_body['amount'], user = current_user)

#     db.session.add(new_budget)
#     db.session.commit()
#     return {
#         'id': new_budget.budget_id,
#         'amount': new_budget.amount,
#         'msg': f"A budget of ${new_budget.amount} has been set."
#     }, 201

@user_bp.route("/<user_id>", methods=['PATCH'])
def edit_budget(user_id):
    request_body = request.get_json()
    
    current_user = User.query.get(user_id)
    current_user.budget = request_body['budget']

    return {'msg': f'Budget ${current_user.budget} is added!'}, 200
