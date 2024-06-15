from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
from Financials import Transaction

reports_bp = Blueprint('reports', __name__)

#curl -v http://localhost:5000/api/reports/monthly
@reports_bp.route('/reports/monthly')
def get_monthly_report():
    today = datetime.today()
    start_date = today.replace(day=1)
    end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    transactions = Transaction.query.filter(Transaction.date >= start_date, Transaction.date <= end_date).all()

    report_data = {
        "labels": [transaction.date.strftime('%Y-%m-%d') for transaction in transactions],
        "values": [transaction.amount for transaction in transactions]
    }

    return jsonify(report_data)

#curl -v http://localhost:5000/api/reports/annual
@reports_bp.route('/reports/annual')
def get_annual_report():
    today = datetime.today()
    start_date = today.replace(month=1, day=1)
    end_date = today.replace(month=12, day=31)
    transactions = Transaction.query.filter(Transaction.date >= start_date, Transaction.date <= end_date).all()

    report_data = {
        "labels": [transaction.date.strftime('%Y-%m-%d') for transaction in transactions],
        "values": [transaction.amount for transaction in transactions]
    }

    return jsonify(report_data)

@reports_bp.route('/reports/custom')
def get_custom_report():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({"error": "Please provide start_date and end_date parameters."}), 400

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    transactions = Transaction.query.filter(Transaction.date >= start_date, Transaction.date <= end_date).all()

    report_data = {
        "labels": [transaction.date.strftime('%Y-%m-%d') for transaction in transactions],
        "values": [transaction.amount for transaction in transactions]
    }

    return jsonify(report_data)

