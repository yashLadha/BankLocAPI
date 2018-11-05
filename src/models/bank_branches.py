from src.db import db

class BankBranches(db.Model):

    __tablename__='bank_branches'

    ifsc = db.Column(db.String(11), nullable=False, primary_key=True)
    bank_id = db.Column(db.Integer, nullable=False)
    branch = db.Column(db.String(100))
    address = db.Column(db.String(100))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    state = db.Column(db.String(50))
    bank_name = db.Column(db.String(49))

    def serialize(self):
        return {
            'ifsc': self.ifsc,
            'bank_id': self.bank_id,
            'branch': self.branch,
            'address': self.address,
            'city': self.city,
            'district': self.district,
            'state': self.state,
            'bank_name': self.bank_name
        }
