from app import db

class Expense(db.Model):
    expense_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Numeric(15,2))
    description = db.Column(db.String)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship("User", backpopulate='expenses')
    category_id = db.Column(db.Intger, db.ForeignKey('category.category_id'), nullable=False)
    category = db.relationship('Category', backpopulate='expenses')

    