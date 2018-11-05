from src.db import db

class Banks(db.Model):

    __tablename__ = 'banks'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(49))