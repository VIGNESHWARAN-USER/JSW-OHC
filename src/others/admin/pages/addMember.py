import streamlit as st
def addMember(connection,cursor):
    st.header("Add Member")
    with st.container(border=1):
        rc1, rc2 = st.columns(2)
        with rc1:
            st.write("Enter employee number")
            st.text_input("Employee Number", label_visibility='collapsed')
            st.write("Enter Name")
            st.text_input("Employee Name", label_visibility='collapsed')
            st.write("Enter designation")
            st.selectbox("designation", options=["Admin","Registration","Nurse","Doctor","Pharmacy"],label_visibility='collapsed')
            st.write("Enter Mail ID")
            st.text_input("mail_id", label_visibility='collapsed')
            st.write("Enter Role")
            st.multiselect("Role", options=["Doctor", "Nurse"],label_visibility='collapsed')
            st.write("Enter the Date Joined")
            st.date_input("join", label_visibility='collapsed')
            st.write("Enter the Date Exited")
            st.date_input("exit", label_visibility='collapsed')
            