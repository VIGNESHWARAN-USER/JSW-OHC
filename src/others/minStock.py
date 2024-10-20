import streamlit as st
import pandas as pd
def minStock(connection):
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