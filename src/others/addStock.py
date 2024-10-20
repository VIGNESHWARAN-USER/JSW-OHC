import streamlit as st
import pandas as pd
def addStock(connection):
    st.title("Pharmacy Inventory Management")

    # Fetch existing inventory from database
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pharmacy_inventory")
    inventory = cursor.fetchall()

    # Display inventory in a table
    if inventory:
        df = pd.DataFrame(inventory, columns=['ID', 'Medicine Name', 'Quantity', 'Expiry Date','category'])
        st.table(df)

    # Add new medicine to the inventory
    with st.form("add_medicine_form"):
        st.subheader("Add New Medicine")
        medicine_name = st.text_input("Medicine Name")
        quantity = st.number_input("Quantity", min_value=0)
        expiry_date = st.date_input("Expiry Date")
        submit_button = st.form_submit_button("Add Medicine")

        if submit_button:
            if medicine_name and quantity > 0:
                cursor.execute(f"INSERT INTO pharmacy_inventory (medicine_name, quantity, expiry_date) VALUES ('{medicine_name}', {quantity}, '{expiry_date}')")
                connection.commit()
                st.success(f"{medicine_name} has been added to the inventory")
            else:
                st.error("Please enter valid details")