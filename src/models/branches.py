from src.db import db

class Branches(db.Model):

    __tablename__='branches'

    ifsc = db.Column(db.String(11), primary_key=True, nullable=False)
    bank_id = db.Column(db.Integer)
    branch = db.Column(db.String(500))
    address = db.Column(db.String(500))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    state = db.Column(db.String(50))