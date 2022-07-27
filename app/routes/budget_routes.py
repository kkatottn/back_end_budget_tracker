from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from datetime import datetime
from app.models.user import User
from app.models.budget import Budget

budget_bp = Blueprint('budget_bp', __name__, url_prefix='')

@budget_bp.route("/<user_id>/budget", methods=['GET'])
def get_budget(user_id):
    params = request.args
    month = params['month']
    year = params['year']
    current_budget = Budget.query.filter(Budget.month == month and Budget.year == year)
    
    return current_budget

@budget_bp.route("/<user_id>/budget", methods=['POST'])
def new_budget(user_id):
    request_body = request.get_json()
    
    new_budget = Budget(amount=request_body['amount'], user_id = user_id, month=request_body['month'], year=request_body['year'])

    db.session.add(new_budget)
    db.session.commit()
    return jsonify({
        'id': new_budget.budget_id,
        'amount': new_budget.amount,
        'msg': f"A budget of ${new_budget.amount} has been set."
    }), 201

@budget_bp.route("/<budget_id>", methods=['PATCH'])
def edit_budget(budget_id):
    request_body = request.get_json()
    current_budget = Budget.query.get(budget_id)
    current_budget.amount = request_body['amount']

    db.session.commit()

    return jsonify({
        "msg": f"Budget has been updated to ${current_budget.amount}"
    })
    
