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

INSERT INTO Budgets (name, amount, start_date, end_date) VALUES 
('Monthly Groceries', 500.00, '2024-06-01', '2024-06-30'),
('Rent', 1500.00, '2024-06-01', '2024-06-30'),
('Entertainment', 300.00, '2024-06-01', '2024-06-30');

INSERT INTO Transactions (description, amount, category, date) VALUES 
('Grocery shopping at Walmart', 120.50, 'Groceries', '2024-06-05'),
('Movie night', 45.00, 'Entertainment', '2024-06-06'),
('Dinner at a restaurant', 85.75, 'Food & Dining', '2024-06-07'),
('Monthly Rent Payment', 1500.00, 'Rent', '2024-06-01'),
('Gym Membership', 50.00, 'Fitness', '2024-06-02');
