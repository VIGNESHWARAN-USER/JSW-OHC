import streamlit as st
from datetime import date

# Function to render the form
def fitness_form():
    st.title("Fitness after Medical Leave")

    # Split the form into 2 rows with 5 columns each
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        leave_reason = st.selectbox("Leave Reason", ["Treated", "Personal Leave"])
        if leave_reason == "Treated":
            dis = st.text_input("Enter Disease/Condition")
    
    with col2:
        leave_from = st.date_input("Leave From", min_value=date.today())
    
    with col3:
        leave_up_to = st.date_input("Leave Up To", min_value=leave_from)
    
    with col4:
        number_of_days = st.number_input("No. of Days Leave", min_value=1, step=1)
    
    with col5:
        rejoining_date = st.date_input("Re-joining Duty on")

    col6, col7, col8 = st.columns(3)

    with col6:
        shift = st.selectbox("Shift", ["G", "A", "B", "C"])
    
    with col7:
        issued_by = st.text_input("Certificate Issued By")
    
    with col8:
        treated_at = st.selectbox("Treated At", ["Govt Hospital", "ESI Hospital", "Private Hospital"])

    col9, col10 = st.columns(2)

    with col9:
        note = st.text_area("Note")

    # Submit button
    if st.button("Submit"):
        # Handle form submission logic here
        st.success("Form submitted successfully!")

# Run the form
fitness_form()
