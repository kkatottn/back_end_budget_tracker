from sqlalchemy import PrimaryKeyConstraint
from app import db

class Year(db.Model):
    year_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    # user = db.Column("User", backpopulate='budget')