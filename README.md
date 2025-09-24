# Budget Buddy

Budget Buddy is a simple and user-friendly Python application designed to help users manage their personal finances effectively. It allows users to record, organize, and analyze their daily or monthly expenses through an intuitive command-line interface.


## Features of Budget Buddy

# Add Expenses
Record daily or monthly expenses with details like amount, category, date, payment method, and description.

# Organize by Categories
Categorize expenses such as Food, Transport, Utilities, Entertainment, etc., for better tracking.

# View Expense Summary
Get a quick overview of total spending for a day, week, or month.

# Filter and Search
Filter expenses by category, date range, or payment method to analyze specific spending patterns.

# Generate Reports
View category-wise and monthly summaries to understand where your money is going.

# Simple Command-Line Interface
Easy-to-use text-based interface that is lightweight and beginner-friendly.

# Data Storage
Save and retrieve all expense records using CSV files or SQLite database for persistent storage.

# Track Payment Methods
Record whether an expense was made via cash, card, or digital wallet.

# Edit or Delete Records
Update or remove expense entries to maintain accurate records.

# Analyze Spending Trends
Identify patterns in your spending habits to improve budgeting and saving.


## project Structure

Budget Buddy/
|
|---src/
|    |___logic.py
operations
|    |___db.py
|
|---API/
|    |___main.py
|
|---frontend/
|    |___ap.py
|
|___requirements.txt
|
|___README.md
|
|___.env


## Quick Start
 
### Prerequisites

-Python 3.8 or higher
-A Supabase account
-Git(Push,cloning)


### 1.clone or Download the project

# option 1: clone with Git
git clone <repository-url>

# option 2:Download and extract the Zip file

### 2.Install Dependencies

# Install all required python packages
pip install -r requirements.txt

### 3.Set up Supabase Databases 
 
1.Create a supabase Project:

2.Create the tasks table:
 
 -Go to sql editor in your supabase dashboard
 -Run this sql command:

 --sql 
 
CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    amount NUMERIC(10, 2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    expense_date DATE NOT NULL,
    payment_method VARCHAR(50),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


3. **Get your credentials:

## 4. Configure Environment Variables

1. Create a `.env` file in the project root

2. Add your Supabase credentials to `.env`:
SUPABASE_URL=https://aulzrmndpekemovocmrx.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF1bHpybW5kcGVrZW1vdm9jbXJ4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI0NjgsImV4cCI6MjA3MzY1ODQ2OH0.vsn7gqWrjnOMDTy8evCa9KWUbIsvooVo1fUxD_H--TM

## 5. Run the Application 

## Streamlit Frontend
streamlit run forward/app.py

The app will open in your browser at `http://localhost:8000`

## How to use

## Technical Details

## Technologies Used

-**Frontend**: Streamlit (python web framework)
-**Backend**:FastAPI (Python Rest API framework)
-**Database**:Supabase(PostgreSQL-based backend-as-a-service)
-**Language**: Python 3.8+

### Key Components

1. **`src/db.py`**:Database operations 
    - Handles all crud operations with Supabase

2. **`src/logic.py`**:Business logic task validation and processing

## Trouble shooting

## Common Issues

## Future enhancements

