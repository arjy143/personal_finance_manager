from flask import Flask
from db import db
from routes.transactions_routes import transactions_bp
from routes.budgets_routes import budgets_bp
from routes.reports_routes import reports_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://root:password@db:5432/finances'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(transactions_bp, url_prefix='/api')
app.register_blueprint(budgets_bp, url_prefix='/api')
app.register_blueprint(reports_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
