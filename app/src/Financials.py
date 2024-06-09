from db import db

class Budget(db.Model):
    __tablename__ = 'budgets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Numeric(14, 2), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)

    def __init__(self, name, amount, start_date, end_date=None):
        self.name = name
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "amount" : float(self.amount),
            "start_date" : str(self.start_date),
            "end_date" : str(self.end_date) if self.end_date else None
        }

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(14, 2), nullable=False)
    category = db.Column(db.String(50))
    date = db.Column(db.Date, nullable=False)

    def __init__(self, description, amount, category, date):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def json(self):
        return {
            "id" : self.id,
            "description" : self.description,
            "amount" : float(self.amount),
            "category" : self.category,
            "date" : str(self.date)
        }
