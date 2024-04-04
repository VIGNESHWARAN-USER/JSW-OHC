import streamlit as st
import os
import pandas as p


def Appointment(cursor, accessLevel):
    st.header("Appointments")

    if accessLevel == "doctor":
        st.subheader("Doctor Appointments")
    elif accessLevel == "nurse":
        st.subheader("Nurse Appointments")