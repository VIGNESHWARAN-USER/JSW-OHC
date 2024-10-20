import streamlit as st
import pandas as pd

def expiry(connection):
    st.title("Medicines Approaching Expiry")
    cursor = connection.cursor()

    # Fetch medicines that will expire in the next 25 days
    cursor.execute("SELECT * FROM pharmacy_inventory WHERE expiry_date BETWEEN CURDATE() AND CURDATE() + INTERVAL 25 DAY")
    expiring_medicines = cursor.fetchall()

    if expiring_medicines:
        df = pd.DataFrame(expiring_medicines, columns=['ID', 'Medicine Name', 'Quantity', 'Expiry Date','category'])
        st.table(df)
    else:
        st.info("No medicines are approaching expiry.")
