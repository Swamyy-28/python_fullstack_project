# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

# ---------------------- App Setup --------------------
app = FastAPI(title="Online Product Inventory", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------- Data Models --------------------
class Supplier(BaseModel):
    name: str
    contact: Optional[str] = None

class Product(BaseModel):
    name: str
    category: str
    supplier_id: Optional[int] = None
    price: float
    quantity: int

# ---------------------- In-memory storage --------------------
suppliers: List[dict] = []
products: List[dict] = []

next_supplier_id = 1
next_product_id = 1

# ---------------------- Supplier Endpoints ----------------------
@app.get("/suppliers")
def get_suppliers():
    return {"data": suppliers}

@app.post("/suppliers")
def add_supplier(supplier: Supplier):
    global next_supplier_id
    supplier_dict = supplier.dict()
    supplier_dict["id"] = next_supplier_id
    next_supplier_id += 1
    suppliers.append(supplier_dict)
    return {"message": "Supplier added", "supplier": supplier_dict}

@app.put("/suppliers/{supplier_id}")
def update_supplier(supplier_id: int, supplier: Supplier):
    for s in suppliers:
        if s["id"] == supplier_id:
            s.update(supplier.dict())
            return {"message": "Supplier updated", "supplier": s}
    return {"detail": "Supplier not found"}

@app.delete("/suppliers/{supplier_id}")
def delete_supplier(supplier_id: int):
    for s in suppliers:
        if s["id"] == supplier_id:
            suppliers.remove(s)
            # Also remove supplier reference from products
            for p in products:
                if p["supplier_id"] == supplier_id:
                    p["supplier_id"] = None
            return {"message": "Supplier deleted"}
    return {"detail": "Supplier not found"}

# ---------------------- Product Endpoints ----------------------
@app.get("/products")
def get_products():
    return {"data": products}

@app.post("/products")
def add_product(product: Product):
    global next_product_id
    product_dict = product.dict()
    product_dict["id"] = next_product_id
    next_product_id += 1
    products.append(product_dict)
    return {"message": "Product added", "product": product_dict}

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    for p in products:
        if p["id"] == product_id:
            p.update(product.dict())
            return {"message": "Product updated", "product": p}
    return {"detail": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            return {"message": "Product deleted"}
    return {"detail": "Product not found"}
