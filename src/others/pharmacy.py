import streamlit as st
import pandas as pd
import mysql.connector

# Function to handle all pharmacy-related operations
def pharmacy_operations():

    def manage_inventory():
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
                    cursor.execute(f"INSERT INTO pharmacy_inventory (medicine_name, quantity, expiry_date,'category') VALUES ('{medicine_name}', {quantity}, '{expiry_date}','{category}')")
                    connection.commit()
                    st.success(f"{medicine_name} has been added to the inventory")
                else:
                    st.error("Please enter valid details")

    def record_consumption():
        st.title("Record Medicine Consumption")

        # Select medicine and enter quantity to record consumption
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pharmacy_inventory")
        inventory = cursor.fetchall()
        if inventory:
            df = pd.DataFrame(inventory, columns=['ID', 'Medicine Name', 'Quantity', 'Expiry Date','category'])
            selected_medicine = st.selectbox("Select Medicine", df['Medicine Name'])
            quantity = st.number_input("Quantity Consumed", min_value=0)
            submit_button = st.button("Record Consumption")

            if submit_button and quantity > 0:
                cursor.execute(f"UPDATE pharmacy_inventory SET quantity = quantity - {quantity} WHERE medicine_name = '{selected_medicine}'")
                connection.commit()
                st.success(f"Recorded consumption of {quantity} units of {selected_medicine}")

    def view_current_stock():
        st.title("Current Stock")

        # Fetch and display current stock
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pharmacy_inventory WHERE quantity > 0")
        stock = cursor.fetchall()

        if stock:
            df = pd.DataFrame(stock, columns=['ID', 'Medicine Name', 'Quantity', 'Expiry Date','category'])
            st.table(df)
        else:
            st.info("No medicines in stock.")

    def view_expiring_medicines():
        st.title("Medicines Approaching Expiry")

        # Fetch and display medicines that are near expiry
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pharmacy_inventory WHERE expiry_date <= CURDATE() + INTERVAL 30 DAY")
        expiring_medicines = cursor.fetchall()

        if expiring_medicines:
            df = pd.DataFrame(expiring_medicines, columns=['ID', 'Medicine Name', 'Quantity', 'Expiry Date','category'])
            st.table(df)
        else:
            st.info("No medicines are approaching expiry.")

    def view_minimum_stock():
        st.title("Medicines Below Minimum Stock")

        # Fetch and display medicines with quantity below a certain threshold
        minimum_stock_threshold = st.number_input("Set Minimum Stock Threshold", min_value=0, value=10)
        submit_button = st.button("Check Stock")

        if submit_button:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM pharmacy_inventory WHERE quantity <= {minimum_stock_threshold}")
            low_stock_medicines = cursor.fetchall()

            if low_stock_medicines:
                df = pd.DataFrame(low_stock_medicines, columns=['ID', 'Medicine Name', 'Quantity', 'Expiry Date','category'])
                st.table(df)
            else:
                st.info(f"No medicines below {minimum_stock_threshold} units.")



