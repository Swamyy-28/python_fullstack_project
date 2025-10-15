# db.py
import os
from supabase import create_client
from dotenv import load_dotenv

# -------------------- Load environment variables --------------------
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# -------------------- Supplier Functions --------------------
def add_supplier(name, contact=None):
    return supabase.table("inv_suppliers").insert({
        "name": name,
        "contact": contact
    }).execute()

def get_all_suppliers():
    return supabase.table("inv_suppliers").select("*").order("id", desc=True).execute()

def update_supplier(supplier_id, name=None, contact=None):
    update_data = {}
    if name is not None:
        update_data["name"] = name
    if contact is not None:
        update_data["contact"] = contact
    return supabase.table("inv_suppliers").update(update_data).eq("id", supplier_id).execute()

def delete_supplier(supplier_id):
    # Also remove supplier reference from products
    supabase.table("inv_products").update({"supplier_id": None}).eq("supplier_id", supplier_id).execute()
    return supabase.table("inv_suppliers").delete().eq("id", supplier_id).execute()

# -------------------- Product Functions --------------------
def add_product(name, category, supplier_id=None, price=0.0, quantity=0):
    return supabase.table("inv_products").insert({
        "name": name,
        "category": category,
        "supplier_id": supplier_id,
        "price": price,
        "quantity": quantity
    }).execute()

def get_all_products():
    return supabase.table("inv_products").select("*").order("id", desc=True).execute()

def update_product(product_id, name=None, category=None, supplier_id=None, price=None, quantity=None):
    update_data = {}
    if name is not None:
        update_data["name"] = name
    if category is not None:
        update_data["category"] = category
    if supplier_id is not None:
        update_data["supplier_id"] = supplier_id
    if price is not None:
        update_data["price"] = price
    if quantity is not None:
        update_data["quantity"] = quantity
    return supabase.table("inv_products").update(update_data).eq("id", product_id).execute()

def delete_product(product_id):
    return supabase.table("inv_products").delete().eq("id", product_id).execute()
