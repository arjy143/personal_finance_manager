from flask import Blueprint, jsonify, request
from datetime import datetime
from Financials import Transaction
from sqlalchemy import exc

transactions_bp = Blueprint('transactions', __name__)

# curl -v http://localhost:5000/api/transactions
@transactions_bp.route('/transactions')
def get_transactions():
    transactions = [transaction.json for transaction in Transaction.find_all()]
    return jsonify(transactions)

# curl -v http://localhost:5000/api/transaction/1
@transactions_bp.route('/transaction/<int:id>')
def get_transaction(id):
    transaction = Transaction.find_by_id(id)
    return jsonify(transaction.json)

#curl --header "Content-Type: application/json" --request POST --data "{\"description\": \"kebabs\", \"amount\": 10.96, \"category\": \"Takeaway\", \"date\": \"2024-06-05\"}" http://localhost:5000/api/transaction
@transactions_bp.route('/transaction', methods=['POST'])
def post_transaction():
    request_transaction = request.json
    transaction = Transaction(
        request_transaction["description"], 
        request_transaction["amount"], 
        request_transaction["category"],
        datetime.strptime(request_transaction["date"], '%Y-%m-%d').date()
    )
    try:
        transaction.save_to_db()
        return jsonify(transaction.json), 201
    except Exception as e:
        return f'An exception {e} occurred while creating transaction with description: {transaction.description}', 500


#curl --header "Content-Type: application/json" --request PUT --data "{\"description\": \"Chinese\", \"amount\": 10.49, \"category\": \"Takeaway\", \"date\": \"2024-06-05\"}" http://localhost:5000/api/transaction/2
@transactions_bp.route('/transaction/<int:id>', methods=['PUT'])
def put_transaction(id):
    try:
        existing_transaction = Transaction.find_by_id(id)

        if existing_transaction:
            updated_transaction = request.json
            existing_transaction.description = updated_transaction['description']
            existing_transaction.amount = updated_transaction['amount']
            existing_transaction.category = updated_transaction['category']
            existing_transaction.date = datetime.strptime(updated_transaction['date'], '%Y-%m-%d').date()
            existing_transaction.save_to_db()

            return jsonify(existing_transaction.json), 200

        return f'transaction with id {id} not found', 404

    except exc.SQLAlchemyError:
        return f'An exception occurred while updating transaction with name: {updated_transaction.name}', 500

# curl --request DELETE -v http://localhost:5000/api/transaction/2
@transactions_bp.route('/transaction/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    existing_transaction = Transaction.find_by_id(id)
    if existing_transaction:
        existing_transaction.delete_from_db()
        return jsonify({
            'message': f'Deleted transaction with id {id}'
        }), 200
    return f'transaction with id {id} not found', 404
