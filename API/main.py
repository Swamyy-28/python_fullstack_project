from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Import Budget_Buddy from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import Budget_Buddy

app = FastAPI(title="Budget Buddy", version="1.0")

# ---------- Allow frontend (Streamlit/React) to call the API ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Pydantic Models ----------------
class BudgetAdd(BaseModel):
    amount: float
    category: str
    expense_date: str
    payment_method: str | None = None
    description: str | None = None

class BudgetUpdate(BaseModel):
    amount: float | None = None
    category: str | None = None
    expense_date: str | None = None
    payment_method: str | None = None
    description: str | None = None

# ---------------- Logic Instance ----------------
logic = Budget_Buddy()

# ---------------- API Endpoints ----------------

@app.post("/budget/")
def add_budget(budget: BudgetAdd):
    result = logic.add(
        amount=budget.amount,
        category=budget.category,
        expense_date=budget.expense_date,
        payment_method=budget.payment_method,
        description=budget.description,
    )
    if result["Success"]:
        return result
    raise HTTPException(status_code=400, detail=result["Message"])

@app.get("/budget/")
def get_all_budgets():
    result = logic.get_all()
    if result["Success"]:
        return result
    raise HTTPException(status_code=404, detail=result["Message"])

@app.put("/budget/{budget_id}")
def update_budget(budget_id: int, budget: BudgetUpdate):
    result = logic.update(
        budget_id,
        amount=budget.amount,
        category=budget.category,
        expense_date=budget.expense_date,
        payment_method=budget.payment_method,
        description=budget.description,
    )
    if result["Success"]:
        return result
    raise HTTPException(status_code=400, detail=result["Message"])

@app.delete("/budget/{budget_id}")
def delete_budget(budget_id: int):
    result = logic.delete(budget_id)
    if result["Success"]:
        return result
    raise HTTPException(status_code=400, detail=result["Message"])
