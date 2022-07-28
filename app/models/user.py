from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_token = db.Column(db.String)
    email = db.Column(db.String)
    name = db.Column(db.String)
    expenses = db.relationship("Expense", back_populates="user", lazy=True)
    budget = db.relationship("Budget", back_populates="user", lazy=True)
    category = db.relationship("Category", back_populates="user", lazy=True)


