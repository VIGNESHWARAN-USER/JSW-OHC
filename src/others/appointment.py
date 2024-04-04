import streamlit as st
import os
import pandas as p


def Appointment(cursor, accessLevel):
    st.header("Appointments")

    if accessLevel == "doctor":
        st.subheader("Doctor Appointments")
    elif accessLevel == "nurse":

        file_upload  = st.file_uploader("Appointments Upload", type=['xlsx'])

        if file_upload is not None:
            df = p.read_excel(file_upload, dtype={'Phone (Personal)': str, 'Emergency Contact  phone':str})
            st.write(df)

            if st.button("Submit"):
                st.write("Data Submitted")
                # convert the df to json
                data = df.to_dict(orient='records')
                for i in data:
                    st.write(i)
