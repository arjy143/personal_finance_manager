from flask import Flask, jsonify, request

transactions = [
    {'id': 1, 'description': 'apples', 'amount': 2.50, 'category': 'Groceries', 'date': '8/6/2024'},
    {'id': 2, 'description': 'toothpaste', 'amount': 0.99, 'category': 'Health', 'date': '9/6/2024'}
]
budgets = [
    {'id': 1, 'name': 'budget for week', 'amount': 10, 'start-date': '4/6/202410', 'end-date': '11/6/2024'}
]
app = Flask(__name__)

# curl -v http://localhost:5000/transactions
@app.route('/transactions')
def get_transactions():
    return jsonify(transactions)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')