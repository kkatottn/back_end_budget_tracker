from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.user import User
from app.models.budget import Budget
from sqlalchemy import and_
budget_bp = Blueprint('budget_bp', __name__)

@budget_bp.route("/<user_id>/budget", methods=['GET'])
def get_budget(user_id):
    params = request.args
    month = params['month']
    year = params['year']
    current_budget = Budget.query.filter(and_(Budget.month == month, Budget.year == year, user_id == user_id)).first()
    
    if not current_budget:
        return {"msg":f"User with user ID {user_id} didn't set budget yet"}

    return {"budget_id": current_budget.budget_id, "amount": current_budget.amount, "month": current_budget.month, "year":current_budget.year}

@budget_bp.route("/<user_id>/budget", methods=['POST'])
def new_budget(user_id):
    request_body = request.get_json()
    
    new_budget = Budget(amount=request_body['amount'], user_id=user_id, month=request_body['month'], year=request_body['year'])

    db.session.add(new_budget)
    db.session.commit()
    return jsonify({
        'id': new_budget.budget_id,
        'amount': new_budget.amount,
        'msg': f"A budget of ${new_budget.amount} has been set."
    }), 201

@budget_bp.route("/<user_id>/budget", methods=['PATCH'])
def edit_budget(user_id):
    # params = request.args
    # month = params['month']
    # year = params['year']

    request_body = request.get_json()
    # do we not need this line?
    current_budget = Budget.query.filter(and_(Budget.month == request_body["month"], Budget.year == request_body["year"], user_id == user_id)).first()
    current_budget.amount = request_body['amount']

    db.session.commit()

    return jsonify({
        "msg": f"Budget has been updated to ${current_budget.amount}"
    })
    
