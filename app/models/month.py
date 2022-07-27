from sqlalchemy import PrimaryKeyConstraint
from app import db

class Month(db.Model):
    month_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    