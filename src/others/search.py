import streamlit as st
import os
import pandas as pd
from streamlit_modal import Modal

def set_data(emp):
    st.session_state.data = emp.to_dict('records')[0]

def Search(cursor):
    if "search" not in st.session_state:
        st.session_state.search = False
    if "searchinp" not in st.session_state:
        st.session_state.searchinp = ""
    if "view" not in st.session_state:
        st.session_state.view = False

    if "data" not in st.session_state:
        st.session_state.data = {}
    if "open_modal" not in st.session_state:
        st.session_state.open_modal = False

    st.title("Search")
    search1, search2 = st.columns([8,2])
    with search1:
        st.session_state.searchinp = st.text_input("search",placeholder="Search by Patient ID")
    with search2:
        st.write("<div><br></div>", unsafe_allow_html=True)
        st.session_state.search = st.button("Search")

    if st.session_state.search:
        cursor.execute(f"SELECT * FROM Employee_det WHERE emp_no = '{st.session_state.searchinp}'")

        emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
        if emp.empty:
            st.error("No records found")
        else:
            set_data(emp)
    
    st.write(st.session_state.data)