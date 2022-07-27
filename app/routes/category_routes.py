from turtle import title
from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from datetime import datetime
from app.models.user import User
from app.models.category import Category

category_bp = Blueprint('category_bp', __name__, url_prefix='')


# @category_bp.route("/<user_id>/category", methods=['GET'])
# def new_category(user_id):
#     request_body = request.get_json()
    
#     new_category = Category(amount=request_body['amount'], user_id = user_id, month=request_body['month'], year=request_body['year'])

#     db.session.add(new_budget)
#     db.session.commit()
#     return jsonify({
#         'id': new_budget.budget_id,
#         'amount': new_budget.amount,
#         'msg': f"A budget of ${new_budget.amount} has been set."
#     }), 201

@category_bp.route("/<user_id>/category", methods=['POST'])
def new_category(user_id):
    request_body = request.get_json()
    
    new_category = Category(title=request_body['title'], user_id = user_id)

    db.session.add(new_category)
    db.session.commit()
    return jsonify({
        'id': new_category.category_id
        'msg': f"Category {new_category.title} has been created."
    }), 201

