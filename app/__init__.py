from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")


    from .models.user import User
    from .models.expense import Expense
    from .models.budget import Budget
    from .models.category import Category

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    from .routes.expense_routes import expense_bp
    app.register_blueprint(expense_bp)

    from .routes.budget_routes import budget_bp
    app.register_blueprint(budget_bp)

    from .routes.category_routes import category_bp
    app.register_blueprint(category_bp)

    return app




    