# 💰 Personal Expense Tracker

A Python-based Personal Expense Tracker built using MVC architecture.

## 🚀 Features

- Income tracking
- Expense tracking
- Transaction management
- Expense categories
- Monthly budgets
- Budget alerts
- Spending analytics
- Monthly spending trends
- Dashboard
- SQLite database
- MVC architecture

## 🛠️ Technologies

- Python
- Streamlit
- SQLite
- Pandas
- Plotly

## 🏗️ Architecture

The project follows the MVC architecture.

### Model

Responsible for:

- Database
- Data structures
- Database operations

### View

Responsible for:

- Streamlit interface
- Forms
- Tables
- Charts
- User interaction

### Controller

Responsible for:

- Business logic
- Validation
- CRUD operations
- Analytics

## 📁 Project Structure

```text
personal_expense_tracker/
│
├── app.py
│
├── models/
│   ├── database.py
│   ├── transaction_model.py
│   └── budget_model.py
│
├── controllers/
│   ├── transaction_controller.py
│   ├── budget_controller.py
│   └── dashboard_controller.py
│
├── views/
│   ├── transaction_view.py
│   ├── budget_view.py
│   └── dashboard_view.py
│
├── data/
│
├── requirements.txt
├── README.md 
└── .gitignore

to run this project uv run streamlit run app.py
