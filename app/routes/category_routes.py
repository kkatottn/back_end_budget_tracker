from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.user import User
from app.models.category import Category
from sqlalchemy import and_
from app.models.expense import Expense
category_bp = Blueprint('category_bp', __name__, url_prefix='')


@category_bp.route("/<user_id>/category", methods=['GET'])
def get_all_user_categories(user_id):
    params = request.args
    month = params['month']
    year = params['year']    
    categories = Category.query.filter(and_(Category.user_id == user_id, Category.month == month, Category.year == year)).all()


    user_categories = []
    for category in categories:
        user_categories.append({"category_id": category.category_id, "title": category.title})

    return jsonify({"user categories": user_categories})

@category_bp.route("/category", methods=['GET'])
def get_all_default_categories():
    categories = Category.query.filter(Category.user_id.is_(None)).all()

    default_categories = []
    for category in categories:
        default_categories.append({"category_id": category.category_id, "title": category.title})

    return {"default categories": default_categories}

@category_bp.route("/<user_id>/category", methods=['POST'])
def new_user_category(user_id):
    request_body = request.get_json()
    
    new_category = Category(title=request_body['title'], user_id=user_id, month=request_body['month'], year=request_body['year'])

    db.session.add(new_category)
    db.session.commit()
    return jsonify({
        'id': new_category.category_id,
        'msg': f"Category {new_category.title} has been created."
    }), 201

@category_bp.route("/category", methods=['POST'])
def new_default_category():
    request_body = request.get_json()
    
    new_category = Category(title=request_body['title'])

    db.session.add(new_category)
    db.session.commit()
    return jsonify({
        'id': new_category.category_id,
        'user_id': new_category.user_id,
        'msg': f"Category {new_category.title} has been created."
    }), 201

@category_bp.route("/category/<category_id>", methods=["PATCH"])
def edit_one_category(category_id):
    request_body = request.get_json()

    current_category = Category.query.get(category_id)
    
    current_category.title = request_body["title"]
    db.session.commit()

    return jsonify({"msg": f'Category set to new title: {current_category.title}'})