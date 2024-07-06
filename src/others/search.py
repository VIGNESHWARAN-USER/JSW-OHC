import streamlit as st
import os
import pandas as pd
from streamlit_modal import Modal


def show_data(emp):
    # show name and id and other details with one view button
    for i in range(len(emp)):
        with st.container(border=1):
            st.write(emp[i]["emp_no"], emp[i]["name"])
            if st.button("View",key=i):
                st.session_state.open_modal = True
                st.session_state.usr_prof = emp[i]
                st.rerun()

def set_data(emp):
    st.session_state.data = emp.to_dict('records')

def Search(cursor):
    modal = Modal(
        "Employee Profile",
        key="modal",
    )
    if "usr_prof" not in st.session_state:
        st.session_state.usr_prof = {}
    if "search" not in st.session_state:
        st.session_state.search = False
    if "searchinp" not in st.session_state:
        st.session_state.searchinp = ""

    if "data" not in st.session_state:
        st.session_state.data = {}
    if "open_modal" not in st.session_state:
        st.session_state.open_modal = False

    if st.session_state.open_modal == False:
        st.title("Search")
        search1, search2 = st.columns([8,2])
        with search1:
            st.session_state.searchinp = st.text_input("search",placeholder="Search by Patient ID")
        with search2:
            st.write("<div><br></div>", unsafe_allow_html=True)
            st.session_state.search = st.button("Search")

        if st.session_state.search:
            cursor.execute(f"SELECT * FROM Employee_det WHERE emp_no like '%{st.session_state.searchinp}%' ")

            emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
            if emp.empty:
                st.error("No records found")
            else:
                set_data(emp)

        st.write(pd.DataFrame(st.session_state.data))
        show_data(st.session_state.data)


    else:
        st.title("Employee Profile")
        st.write(st.session_state.usr_prof)
        if st.button("close"):
            st.session_state.open_modal = False
            st.rerun()
