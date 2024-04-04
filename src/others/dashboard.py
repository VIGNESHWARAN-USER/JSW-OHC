import streamlit as st
import os
import pandas as pd

def Dashboard(cursor,accessLevel):
    st.header("Dashboard")
    
    # Initialize the variables
    if "total_census" not in st.session_state:
        st.session_state.total_census = 0 
    if "total_healthy" not in st.session_state:
        st.session_state.total_healthy = 0
    if "total_unhealthy" not in st.session_state:
        st.session_state.total_unhealthy = 0
    if "appointments" not in st.session_state:
        st.session_state.appointments = 0

    r1c1,r1c2 = st.columns([2,7])
    with r1c1:
        st.write("<div style='width:100px;height:25px'></div>",unsafe_allow_html=True)
        date = st.date_input("Select a Date")
    with r1c2:
        uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx'])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        
        # Update the counts from the dataframe
        st.session_state.total_census = df['census'].sum()
        st.session_state.total_healthy = df['healthy'].sum()
        st.session_state.total_unhealthy = df['unhealthy'].sum()
        st.session_state.appointments = df['appointments'].sum()

    def get_data(val, name):
            with st.container(border=1):
                st.write(f"<p style='text-align:center;font-weight:bold;font-size:50px;margin-bottom:-30px'>{val}</p>", unsafe_allow_html=True)
                st.write(f"<p style='text-align:center'>{name}</p>", unsafe_allow_html=True)

    with st.container(border=1):
        r1c1,r1c2,r1c3,r1c4 = st.columns(4)
        with r1c1:
            get_data(st.session_state.total_census, "Total Census")
        with r1c2:
            get_data(st.session_state.total_healthy, "Healthy")
        with r1c3:
            get_data(st.session_state.total_unhealthy, "Unhealthy")
        with r1c4:
            get_data(st.session_state.total_appointment, "Appointments")