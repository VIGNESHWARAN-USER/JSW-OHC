import streamlit as st
import pandas as pd
from datetime import date, timedelta
from streamlit_option_menu import option_menu

def Review_People(connection, accessLevel):
    st.header("Review People")

    # Option menu to select review type: Today, Tomorrow, or Not Attempted
    form_name = option_menu(
        None,
        ["Today Review", "Tomorrow Review", "Not Attempted"],
        orientation="horizontal",
        icons=['a', 'a', 'a']
    )

    # Set the current date and tomorrow's date for comparison
    today = date.today()
    tomorrow = today + timedelta(days=1)

    # SQL Queries based on the selected condition (Today, Tomorrow, or Not Attempted)
    if form_name == "Today Review":
        query = f"SELECT * FROM appointments WHERE appoint_date = '{today}' AND status = 'Not Attempted'"
    elif form_name == "Tomorrow Review":
        query = f"SELECT * FROM appointments WHERE appoint_date = '{tomorrow}' AND status = 'Not Attempted'"
    elif form_name == "Not Attempted":
        query = "SELECT * FROM appointments WHERE status = 'Not Attempted'"

    # Fetch the data from the database
    cursor = connection.cursor()
    cursor.execute(query)
    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

   
    # Set up columns for layout
    n1c1, n1c2, n1c3 = st.columns([2, 0.5, 7])

    with n1c1:
            # Set up the appointment category option menu
        visit_reason = option_menu(
            None,
            ["Pre Employment", "Pre Placement", "Annual / Periodical", "Camps", 
            "Fitness After Medical Leave", "Illness", "Injury", "Followup Visit", 
            "Special Work Fitness"],
            menu_icon='building-fill-add',
            icons=['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
            default_index=0
        )

        # Filter data based on the selected visit reason
        if visit_reason != "All":
            emp = emp[emp['visit_reason'] == visit_reason]

        with st.container():
            st.markdown(
                """
                <style>
                .vertical-line {
                    border-left: 1px solid #D3D3D3;
                    height: 750px;
                    margin-left: 10px;
                    margin-right: 10px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            
                # Display the selected appointment category
                #st.markdown("### Appointment Category: " + visit_reason)

    with n1c2:
        # Add a vertical line for visual separation
        st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)

    with n1c3:
        # Create columns for displaying data
        c1, c2, c3, c4, c5, c6 = st.columns([1, 1, 1, 1, 1, 2])

        with c1:
            st.markdown("##### Profile")

        with c2:
            st.markdown("##### PID")

        with c3:
            st.markdown("##### Name")

        with c4:
            st.markdown("##### Gender")

        with c5:
            st.markdown("##### Appointments")

        with c6:
            st.markdown(
                """
                <style>
                .center-text {
                    text-align: center;
                }
                </style>
                <div class="center-text">
                    <h5>Details</h5>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Display the data in a structured way
        if not emp.empty:
            for index, row in emp.iterrows():
                # Create columns for each field
                c1, c2, c3, c4, c5, c6 = st.columns([1, 1, 1, 1, 1, 2])

                with c1:
                    st.write(row['appoint_ID'])  # Appointment ID or Profile

                with c2:
                    st.write(row['emp_no'])  # Employee PID or No.

                with c3:
                    st.write(row['emp_name'])  # Employee Name

                with c4:
                    st.write(row['gender'])  # Gender

                with c5:
                    st.write(row['appoint_date'])  # Appointment Date

                with c6:
                    # Display a "View" button for more details (or replace with another field if needed)
                    st.button("View", key=f"view_{row['emp_no']}")
        else:
            st.error("No records found")

    # Close the cursor after execution
    cursor.close()
