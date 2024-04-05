import streamlit as st
import os
import pandas as pd
from streamlit_modal import Modal


def Search(cursor):
    if "view" not in st.session_state:
        st.session_state.view = False

    if "data" not in st.session_state:
        st.session_state.data = {}
    if "open_modal" not in st.session_state:
        st.session_state.open_modal = False

    if st.session_state.open_modal:
        modal.open()

    st.title("Search")
    search1, search2 = st.columns([8,2])
    with search1:
        search = st.text_input("",placeholder="Search by Patient ID")
    with search2:
        st.write("<div><br></div>", unsafe_allow_html=True)
        searchbtn = st.button("Search")
    if searchbtn:
        cursor.execute(f"SELECT * FROM empprof WHERE PatientID LIKE '%{search}%'")
        result = cursor.fetchall()
        if result:
            data = pd.DataFrame(result,columns=["Aadhar Number","PatientID", "Name","Department","Blood Group","Phone Number","Age","Gender","Desigination","Vaccinated","Address","Date of Birth", "Personal Mail ID", "Identification mark", "Official Email ID", "Nature of Job","Employee","Contractor"])                                          
            # remove the last two columns
            data.drop(data.columns[-2:], axis=1, inplace=True)
            for i in data.index:
                with st.container(border=1):
                    st.header(f"Patient ID: {data['PatientID'][i]}")
                    st.subheader(f"Name: {data['Name'][i]}")
                    st.write(f"Age: {data['Age'][i]}")
                    if st.button("View"):
                        st.session_state.view = True
                        st.session_state.data = data.loc[i].to_dict()
                        st.session_state.open_modal = True

    st.write(st.session_state.data)
    modal = Modal(
        "Profile", 
        key="profile-modal",
        padding=20,
        max_width=744
    )
    

    if modal.is_open():
        with modal.container():
            st.write("Profile Information:")
            for key, value in st.session_state.data.items():
                st.write(f"{key}: {value}")