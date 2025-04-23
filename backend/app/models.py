from . import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    description = db.Column(db.String)
    amount = db.Column(db.Float)
    type = db.Column(db.String)  # debit or credit
    category = db.Column(db.String)  # populated by ML

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'description': self.description,
            'amount': self.amount,
            'type': self.type,
            'category': self.category
        }
