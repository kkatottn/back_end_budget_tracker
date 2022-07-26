from sqlalchemy import PrimaryKeyConstraint
from app import db

class Budget(db.Model):
    budget_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.Column("User", backpopulate='budget')