from app import db

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    month = db.Column(db.Integer, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
    user = db.relationship("User", back_populates='category')
    expenses = db.relationship("Expense", back_populates="category", lazy=True)
    
    def to_dict(self):

        return {
            "id": self.user_id,
            "id_token": self.id_token,
            "email": self.email,
            "name": self.name,
            }