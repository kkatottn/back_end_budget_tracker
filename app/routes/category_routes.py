from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.user import User
from app.models.category import Category

category_bp = Blueprint('category_bp', __name__, url_prefix='')


@category_bp.route("/<user_id>/category", methods=['GET'])
def get_all_user_categories(user_id):
    params = request.args
    month = params['month']
    year = params['year']    
    categories = Category.query.filter(Category.user_id == user_id and Category.month == month and Category.year == year).all()


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

