# 🛍️ Online Product Inventory

**Online Product Inventory** is a Python application designed to help small businesses manage their products, stock levels, and suppliers efficiently. It provides an intuitive dashboard using **Streamlit** and persistent storage via **Supabase**, making inventory management simple and accessible.

## Features of Online Product Inventory

### Add Products
Add new products with details like name, category, supplier, price, and quantity.

### Update / Delete Products
Modify product details or remove discontinued items to maintain accurate inventory.

### Track Stock Levels
Monitor the number of units in stock and get low-stock alerts.

### Manage Suppliers
Add and view supplier information, including name and contact details.

### Filter and Search
Search products by category or supplier for easy access and management.

### Low-Stock Alerts
Automatically notify when a product's stock falls below a defined threshold.

### Dashboard Interface
Interactive and user-friendly Streamlit dashboard for managing products and suppliers.


## project Structure

ONLINE_PRODUCT_INVENTORY/
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
- Python 3.8 or higher  
- Supabase account  
- Git (for cloning the repository)  

### 1. Clone or Download the Project
**Option 1: Clone with Git**  
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
 
CREATE TABLE suppliers (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  contact TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE products (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name TEXT NOT NULL,
  category TEXT NOT NULL,
  supplier_id BIGINT REFERENCES suppliers(id) ON DELETE SET NULL,
  price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
  quantity INT NOT NULL CHECK (quantity >= 0),
  created_at TIMESTAMP DEFAULT NOW()
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

