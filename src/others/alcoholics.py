import streamlit as st
import mysql.connector
from datetime import datetime

def alcoholics(connection, cursor):
    st.title("Alcoholic Status")

    # Initialize session state variables to store form data
    if "alcohol_form_data" not in st.session_state:
        st.session_state.alcohol_form_data = {}

    # Employee Number field (stored in form data state)
    emp_no = st.text_input("Employee Number", value=st.session_state.alcohol_form_data.get("emp_no", ""))
    st.session_state.alcohol_form_data["emp_no"] = emp_no

    # Select Type (Employee/Contractor)
    type_selection = st.selectbox("Select Type", ["Employee", "Contractor"])
    st.session_state.alcohol_form_data["type"] = type_selection

    # Select Health Status (Match the enum values in your database: 'Health', 'Unhealth')
    health_status = st.selectbox("Health Status", ["Health", "Unhealth"])  # Corrected options
    st.session_state.alcohol_form_data["health_status"] = health_status

    # Enter Alcoholic Level (decimal value)
    alcoholic_level = st.text_input("Enter Alcoholic Level (e.g., 0.00)", value=st.session_state.alcohol_form_data.get("alcoholic_level", "0.00"))
    st.session_state.alcohol_form_data["alcoholic_level"] = alcoholic_level

    # Button to add data
    if st.button("Add Data", type="primary"):
        # Prepare data for insertion into Alcohol table
        sql = """
            INSERT INTO Alcohol (
                emp_no, type, health_status, alcoholic_level
            ) VALUES (
                %s, %s, %s, %s
            )
        """

        # Extract values from session state and convert alcoholic_level to float
        try:
            alcoholic_level_float = float(st.session_state.alcohol_form_data["alcoholic_level"])
        except ValueError:
            st.error("Invalid input for Alcoholic Level. Please enter a valid decimal number.")
            return
        
        # Prepare data tuple for insertion
        data = (
            emp_no,  # Employee Number
            st.session_state.alcohol_form_data["type"],  # Type (Employee/Contractor)
            st.session_state.alcohol_form_data["health_status"],  # Health Status (Corrected)
            alcoholic_level_float  # Alcoholic Level
        )

        try:
            # Execute the insert statement
            cursor.execute(sql, data)
            connection.commit()
            st.success("Data Saved Successfully")

            # Optional: Reset form data after successful submission
            st.session_state.alcohol_form_data = {}

        except mysql.connector.Error as e:
            st.error(f"Error saving data: {e}")

    # Optional: Display the form data state for verification
    st.write(st.session_state.alcohol_form_data)
