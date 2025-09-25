# db_manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

# load environment variables 
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")

supabase=create_client(url,key)

# create Budget
def add_budget(amount, category, expense_date, payment_method=None, description=None):
    return supabase.table("budget").insert({
        "amount": amount,
        "category": category,
        "expense_date": str(expense_date),
        "payment_method": payment_method,
        "description": description
    }).execute()

def get_all_budget():
    return supabase.table("budget").select("*").order("expense_date", desc=True).execute()

def update_budget(budget_id, amount=None, category=None, expense_date=None, payment_method=None, description=None):
    update_data = {}
    if amount is not None:
        update_data["amount"] = amount
    if category is not None:
        update_data["category"] = category
    if expense_date is not None:
        update_data["expense_date"] = str(expense_date)
    if payment_method is not None:
        update_data["payment_method"] = payment_method
    if description is not None:
        update_data["description"] = description
    return supabase.table("budget").update(update_data).eq("id", budget_id).execute()

def delete_budget(budget_id):
    return supabase.table("budget").delete().eq("id", budget_id).execute()