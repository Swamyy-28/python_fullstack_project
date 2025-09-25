from src.db_manager import add_budget, get_all_budget, update_budget, delete_budget

class Budget_Buddy:
    """
    Acts as a bridge between frontend (Streamlit/FastAPI) and the database.
    """

    def __init__(self):
        pass

    # ---- Create --------
    def add(self, amount, category, expense_date, payment_method=None, description=None):
        if not amount or not description:
            return {"Success": False, "Message": "Amount & Description are required"}

        result = add_budget(amount, category, expense_date, payment_method, description)

        if result.data:
            return {"Success": True, "Message": "Budget added successfully", "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}

    # ---- Read --------
    def get_all(self):
        result = get_all_budget()
        if result.data:
            return {"Success": True, "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}

    # ---- Update --------
    def update(self, budget_id, amount=None, category=None, expense_date=None, payment_method=None, description=None):
        if not budget_id:
            return {"Success": False, "Message": "Budget ID is required for update"}

        result = update_budget(budget_id, amount, category, expense_date, payment_method, description)

        if result.data:
            return {"Success": True, "Message": "Budget updated successfully", "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}

    # ---- Delete --------
    def delete(self, budget_id):
        if not budget_id:
            return {"Success": False, "Message": "Budget ID is required for delete"}

        result = delete_budget(budget_id)

        if result.data:
            return {"Success": True, "Message": "Budget deleted successfully", "data": result.data}
        else:
            return {"Success": False, "Message": f"Error: {result.error}"}
        
