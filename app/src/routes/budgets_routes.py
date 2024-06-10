from flask import Blueprint, jsonify, request
from datetime import datetime
from Financials import Budget
from sqlalchemy import exc

budgets_bp = Blueprint('budgets', __name__)

#curl http://localhost:5000/api/budgets 
@budgets_bp.route('/budgets')
def get_budgets():
    budgets = [budget.json for budget in Budget.find_all()]
    return jsonify(budgets)

@budgets_bp.route('/budget/<int:id>')
def get_budget(id):
    budget = Budget.find_by_id(id)
    return jsonify(budget.json)

#curl --header "Content-Type: application/json" --request POST --data "{\"name\": \"TestBudget\", \"amount\": 50, \"start_date\": \"2024-06-03\", \"end_date\": \"2024-06-10\"}" http://localhost:5000/api/budget
@budgets_bp.route('/budget', methods=['POST'])
def post_budget():
    request_budget = request.json
    budget = Budget(
        request_budget["name"], 
        request_budget["amount"], 
        datetime.strptime(request_budget["start_date"], '%Y-%m-%d').date(),
        datetime.strptime(request_budget["end_date"], '%Y-%m-%d').date() if request_budget.get("end_date") else None
    )
    try:
        budget.save_to_db()
        return jsonify(budget.json), 201
    except Exception as e:
        return f'An exception {e} occurred while creating budget with name: {budget.name}', 500

@budgets_bp.route('/budget/<int:id>', methods=['PUT'])
def put_budget(id):
    try:
        existing_budget = Budget.find_by_id(id)

        if existing_budget:
            updated_budget = request.json
            existing_budget.name = updated_budget['name']
            existing_budget.amount = updated_budget['amount']
            existing_budget.start_date = datetime.strptime(updated_budget['start_date'], '%Y-%m-%d').date()
            existing_budget.end_date = datetime.strptime(updated_budget['end_date'], '%Y-%m-%d').date() if updated_budget.get('end_date') else None
            existing_budget.save_to_db()

            return jsonify(existing_budget.json), 200

        return f'budget with id {id} not found', 404

    except exc.SQLAlchemyError:
        return f'An exception occurred while updating budget with name: {updated_budget.name}', 500

@budgets_bp.route('/budget/<int:id>', methods=['DELETE'])
def delete_budget(id):
    existing_budget = Budget.find_by_id(id)
    if existing_budget:
        existing_budget.delete_from_db()
        return jsonify({
            'message': f'Deleted budget with id {id}'
        }), 200
    return f'budget with id {id} not found', 404
