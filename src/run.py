from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.db import db
from src.models.bank_branches import BankBranches
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5432/bankdb'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

@app.route('/')
def index():
    return jsonify({'Hello': 'There'})

@app.route('/fetchdetail', methods=['GET'])
def get_branches():
    bank_name = request.args.get('name')
    bank_city = request.args.get('city')
    branches = BankBranches.query.filter_by(bank_name=bank_name, city=bank_city).all()
    if branches:
        payload = {}
        for idx, branch in enumerate(branches):
            payload[idx] = branch.serialize()
        return jsonify(payload)
    return jsonify({'response': -1, 'status': 'Record not found'})

@app.route('/details', methods=['GET'])
def get_details():
    branch_code = request.args.get('ifsc')
    bank_data = BankBranches.query.filter_by(ifsc=branch_code).first()
    if bank_data:
        return jsonify(bank_data.serialize())
    return jsonify({'response': -1, 'status': 'Record not found'})



if __name__ == '__main__':
    app.run(port=8000, debug=True)