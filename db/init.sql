CREATE TABLE IF NOT EXISTS budgets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    amount NUMERIC(14, 2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE
);

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    amount NUMERIC(14, 2) NOT NULL,
    category VARCHAR(50),
    date DATE NOT NULL
);

-- Insert transactions
INSERT INTO transactions (id, description, amount, category, date)
VALUES (1, 'apples', 2.50, 'Groceries', '2024-06-08'),
       (2, 'toothpaste', 0.99, 'Health', '2024-06-09');

-- Insert budgets
INSERT INTO budgets (id, name, amount, start_date, end_date)
VALUES (1, 'budget for week', 10.00, '2024-06-04', '2024-06-11');
