from app import db

class Expense(db.Model):
    expense_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Numeric(15,2))
    category = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship("User", backpopulate='expenses')

    