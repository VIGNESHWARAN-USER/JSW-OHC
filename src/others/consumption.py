import streamlit as st
import pandas as pd
def consumption(connection):
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