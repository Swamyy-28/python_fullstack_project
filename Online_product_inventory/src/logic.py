# logic.py
from src.db import (
    add_supplier, get_all_suppliers, update_supplier, delete_supplier,
    add_product, get_all_products, update_product, delete_product
)

class InventoryManager:
    """
    Acts as a bridge between frontend (Streamlit/FastAPI) and Supabase database
    for managing products and suppliers.
    """

    def __init__(self):
        pass

    # -------------------- Supplier Methods --------------------
    def add_supplier(self, name, contact=None):
        if not name:
            return {"Success": False, "Message": "Supplier name is required"}

        result = add_supplier(name, contact)
        if result.data:
            return {"Success": True, "Message": "Supplier added successfully", "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}

    def get_all_suppliers(self):
        result = get_all_suppliers()
        if result.data:
            return {"Success": True, "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}

    def update_supplier(self, supplier_id, name=None, contact=None):
        if not supplier_id:
            return {"Success": False, "Message": "Supplier ID is required for update"}

        result = update_supplier(supplier_id, name, contact)
        if result.data:
            return {"Success": True, "Message": "Supplier updated successfully", "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}

    def delete_supplier(self, supplier_id):
        if not supplier_id:
            return {"Success": False, "Message": "Supplier ID is required for delete"}

        result = delete_supplier(supplier_id)
        if result.data:
            return {"Success": True, "Message": "Supplier deleted successfully", "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}

    # -------------------- Product Methods --------------------
    def add_product(self, name, category, supplier_id=None, price=0.0, quantity=0):
        if not name or not category:
            return {"Success": False, "Message": "Product name and category are required"}

        result = add_product(name, category, supplier_id, price, quantity)
        if result.data:
            return {"Success": True, "Message": "Product added successfully", "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}

    def get_all_products(self):
        result = get_all_products()
        if result.data:
            return {"Success": True, "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}

    def update_product(self, product_id, name=None, category=None, supplier_id=None, price=None, quantity=None):
        if not product_id:
            return {"Success": False, "Message": "Product ID is required for update"}

        result = update_product(product_id, name, category, supplier_id, price, quantity)
        if result.data:
            return {"Success": True, "Message": "Product updated successfully", "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}

    def delete_product(self, product_id):
        if not product_id:
            return {"Success": False, "Message": "Product ID is required for delete"}

        result = delete_product(product_id)
        if result.data:
            return {"Success": True, "Message": "Product deleted successfully", "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}
