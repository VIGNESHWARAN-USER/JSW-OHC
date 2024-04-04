import streamlit as st
import os
import pandas as pd


def Search(cursor):
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
        else:
            st.write("No data found")
