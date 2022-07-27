from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.user import User
from app.models.expense import Expense

expense_bp = Blueprint('expense_bp', __name__, url_prefix='')

@expense_bp.route("/<user_id>/expense", methods=['GET'])
def get_month_expenses(user_id):
    params = request.args

    if len(params) == 2:
        month = params['month']
        year = params['year']
        expenses = Expense.query.filter(Expense.user_id == user_id and Expense.month == month and Expense.year == year)
    elif len(params) == 3:
        month = params['month']
        year = params['year']
        category = params['category']

        expenses = Expense.query.filter(Expense.user_id == user_id and Expense.month == month and Expense.year == year and Expense.category == category)
    
    return expenses


@expense_bp.route("/<user_id>/expense", methods=['POST'])
def add_new_expense(user_id):
    request_body = request.get_json()
    
    new_expense = Expense(amount=request_body['amount'],description=request_body['description'],user_id=user_id,category_id=request_body['category_id'],month=request_body['month'],year=request_body['year'])

    db.session.add(new_expense)
    db.session.commit()
    return jsonify({
        'id': new_expense.expense_id,
        'description': new_expense.description,
        'msg': f'Expense with id: {new_expense.expense_id} has successfully created an account'
    }), 201


@expense_bp.route("/expense/<expense_id>", methods=['PATCH'])
def edit_expense(expense_id):
    request_body = request.get_json()

    current_expense = Expense.query.get(expense_id)
    
    if "description" and "amount" in request_body:
        current_expense.amount = request_body['amount']
        current_expense.description = request_body['description']

    db.session.commit()
    return jsonify ({"msg":"Expense has been edited"})
