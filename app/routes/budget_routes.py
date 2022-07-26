from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from datetime import datetime
from app.models.user import User
from app.models.budget import Budget

budget_bp = Blueprint('budget_bp', __name__, url_prefix='')

@budget_bp.route("/<user_id>", methods=['GET'])
def get_budget(user_id):
    current_user = User.query.get(user_id)
    current_budget = current_user.budget
    
    return current_budget

@budget_bp.route("/<user_id>", methods=['POST'])
def new_budget(user_id):
    request_body = request.get_json()
    
    current_user = User.query.get(user_id)
    new_budget = Budget(amount=request_body['amount'], user = current_user)

    db.session.add(new_budget)
    db.session.commit()
    return {
        'id': new_budget.budget_id,
        'amount': new_budget.amount,
        'msg': f"A budget of ${new_budget.amount} has been set."
    }, 201

@budget_bp.route("/<budget_id>", methods=['PATCH'])
def edit_budget(budget_id):
    request_body = request.get_json()
    
    current_budget = User.query.get(user_id)
    new_budget = Budget(amount=request_body['amount'], user = current_user)
