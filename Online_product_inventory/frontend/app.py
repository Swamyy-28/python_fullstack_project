# app.py
import streamlit as st
import requests
import pandas as pd

# -------------------- API URLs --------------------
API_BASE_PRODUCTS = "http://127.0.0.1:8000/products"
API_BASE_SUPPLIERS = "http://127.0.0.1:8000/suppliers"

# -------------------- Streamlit Setup --------------------
st.set_page_config(page_title="🛍️ Product Inventory", layout="wide")
st.title("🛍️ Online Product Inventory")

# -------------------- Sidebar ------------------------
st.sidebar.header("📌 Menu")
menu = st.sidebar.radio("Navigate", ["Products", "Suppliers"])

# -------------------- Products Section --------------------
if menu == "Products":
    action = st.radio("Choose Action", ["Add Product", "View Products", "Update Product", "Delete Product"])

    # Add Product
    if action == "Add Product":
        st.subheader("➕ Add New Product")
        with st.form("add_product_form"):
            name = st.text_input("Product Name")
            category = st.text_input("Category")
            supplier_id = st.number_input("Supplier ID (Optional)", min_value=0, step=1)
            price = st.number_input("Price", min_value=0.0, format="%.2f")
            quantity = st.number_input("Quantity", min_value=0, step=1)
            submit = st.form_submit_button("Add Product")

            if submit:
                payload = {
                    "name": name,
                    "category": category,
                    "supplier_id": supplier_id if supplier_id > 0 else None,
                    "price": price,
                    "quantity": quantity
                }
                try:
                    res = requests.post(API_BASE_PRODUCTS, json=payload)
                    if res.status_code == 200:
                        st.success("✅ Product Added Successfully!")
                    else:
                        st.error(f"❌ Failed: {res.json().get('detail','Unknown Error')}")
                except Exception as e:
                    st.error(f"⚠️ Error connecting to API: {e}")

    # View Products
    elif action == "View Products":
        st.subheader("📊 All Products")
        try:
            res = requests.get(API_BASE_PRODUCTS)
            if res.status_code == 200:
                data = res.json().get("data", [])
                df = pd.DataFrame(data)
                if not df.empty:
                    st.dataframe(df, use_container_width=True)
                else:
                    st.info("No products found.")
            else:
                st.error("❌ Failed to fetch products.")
        except Exception as e:
            st.error(f"⚠️ Error connecting to API: {e}")

    # Update Product
    elif action == "Update Product":
        st.subheader("✏️ Update a Product")
        product_id = st.number_input("Enter Product ID to Update", min_value=1, step=1)
        with st.form("update_product_form"):
            new_name = st.text_input("New Name")
            new_category = st.text_input("New Category")
            new_supplier_id = st.number_input("New Supplier ID (Optional)", min_value=0, step=1)
            new_price = st.number_input("New Price", min_value=0.0, format="%.2f")
            new_quantity = st.number_input("New Quantity", min_value=0, step=1)
            submit_update = st.form_submit_button("Update Product")

            if submit_update:
                payload = {
                    "name": new_name,
                    "category": new_category,
                    "supplier_id": new_supplier_id if new_supplier_id > 0 else None,
                    "price": new_price,
                    "quantity": new_quantity
                }
                try:
                    res = requests.put(f"{API_BASE_PRODUCTS}/{product_id}", json=payload)
                    if res.status_code == 200:
                        st.success("✅ Product Updated Successfully!")
                    else:
                        st.error(f"❌ Failed: {res.json().get('detail','Unknown Error')}")
                except Exception as e:
                    st.error(f"⚠️ Error connecting to API: {e}")

    # Delete Product
    elif action == "Delete Product":
        st.subheader("🗑️ Delete a Product")
        product_id = st.number_input("Enter Product ID to Delete", min_value=1, step=1)
        if st.button("Delete Product"):
            try:
                res = requests.delete(f"{API_BASE_PRODUCTS}/{product_id}")
                if res.status_code == 200:
                    st.success("✅ Product Deleted Successfully!")
                else:
                    st.error(f"❌ Failed: {res.json().get('detail','Unknown Error')}")
            except Exception as e:
                st.error(f"⚠️ Error connecting to API: {e}")

# -------------------- Suppliers Section --------------------
elif menu == "Suppliers":
    action = st.radio("Choose Action", ["Add Supplier", "View Suppliers", "Update Supplier", "Delete Supplier"])

    # Add Supplier
    if action == "Add Supplier":
        st.subheader("➕ Add New Supplier")
        with st.form("add_supplier_form"):
            name = st.text_input("Supplier Name")
            contact = st.text_input("Contact Info")
            submit = st.form_submit_button("Add Supplier")

            if submit:
                payload = {"name": name, "contact": contact}
                try:
                    res = requests.post(API_BASE_SUPPLIERS, json=payload)
                    if res.status_code == 200:
                        st.success("✅ Supplier Added Successfully!")
                    else:
                        st.error(f"❌ Failed: {res.json().get('detail','Unknown Error')}")
                except Exception as e:
                    st.error(f"⚠️ Error connecting to API: {e}")

    # View Suppliers
    elif action == "View Suppliers":
        st.subheader("📊 All Suppliers")
        try:
            res = requests.get(API_BASE_SUPPLIERS)
            if res.status_code == 200:
                data = res.json().get("data", [])
                df = pd.DataFrame(data)
                if not df.empty:
                    st.dataframe(df, use_container_width=True)
                else:
                    st.info("No suppliers found.")
            else:
                st.error("❌ Failed to fetch suppliers.")
        except Exception as e:
            st.error(f"⚠️ Error connecting to API: {e}")

    # Update Supplier
    elif action == "Update Supplier":
        st.subheader("✏️ Update a Supplier")
        supplier_id = st.number_input("Enter Supplier ID to Update", min_value=1, step=1)
        with st.form("update_supplier_form"):
            new_name = st.text_input("New Name")
            new_contact = st.text_input("New Contact")
            submit_update = st.form_submit_button("Update Supplier")

            if submit_update:
                payload = {"name": new_name, "contact": new_contact}
                try:
                    res = requests.put(f"{API_BASE_SUPPLIERS}/{supplier_id}", json=payload)
                    if res.status_code == 200:
                        st.success("✅ Supplier Updated Successfully!")
                    else:
                        st.error(f"❌ Failed: {res.json().get('detail','Unknown Error')}")
                except Exception as e:
                    st.error(f"⚠️ Error connecting to API: {e}")

    # Delete Supplier
    elif action == "Delete Supplier":
        st.subheader("🗑️ Delete a Supplier")
        supplier_id = st.number_input("Enter Supplier ID to Delete", min_value=1, step=1)
        if st.button("Delete Supplier"):
            try:
                res = requests.delete(f"{API_BASE_SUPPLIERS}/{supplier_id}")
                if res.status_code == 200:
                    st.success("✅ Supplier Deleted Successfully!")
                else:
                    st.error(f"❌ Failed: {res.json().get('detail','Unknown Error')}")
            except Exception as e:
                st.error(f"⚠️ Error connecting to API: {e}")
