from sqlalchemy import PrimaryKeyConstraint
from app import db

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
    user = db.Column("User", backpopulate='category')
    expenses = db.relationship("Expense", back_populates="category", lazy=True)
    