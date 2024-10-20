import streamlit as st
import pandas as pd
def currStock(connection):
    st.title("Current Stock")

    # Fetch and display current stock
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pharmacy_inventory")
    inventory = cursor.fetchall()

    # Display inventory in a table
    if inventory:
        df = pd.DataFrame(inventory, columns=['ID', 'Medicine Name', 'Quantity', 'Expiry Date','category'])
        st.table(df)
    else:
        st.info("No medicines in stock.")