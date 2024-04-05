import streamlit as st
import os
import pandas as pd
from datetime import datetime

def Appointment(connection, accessLevel):
    st.header("Appointments")

    if accessLevel == "doctor":
        st.subheader("Doctor Appointments")

        data = pd.read_sql("SELECT * FROM appointments", connection)


        if len(data) > 0:
            st.write(data)
    elif accessLevel == "nurse":

        file_upload  = st.file_uploader("Appointments Upload", type=['xlsx'])

        if file_upload is not None:
            df = pd.read_excel(file_upload, dtype={'Phone (Personal)': str, 'Emergency Contact  phone':str})

            st.write(df['Emergency Contact  person '])
            if st.button("Submit"):
                st.write("Data Submitted")
                st.write(df.columns)
                df.fillna("null", inplace=True)
                # convert the df to json
                data = df.to_dict(orient='records')
                for i in data:
                    st.write(i)
                    appoint_date = datetime.strptime(i['Date for Appointment'][:10], '%d-%m-%Y').strftime('%Y-%m-%d')
                    dob = datetime.strptime(i['Date of Birth'][:10], '%d-%m-%Y').strftime('%Y-%m-%d')
                    doj = datetime.strptime(i['Date of Joining'][:10], '%d-%m-%Y').strftime('%Y-%m-%d')

                    # Insert the data into the database
                    add_patient = ("INSERT INTO appointments (appoint_date, visit_reason, emp_name, dob, age, gender, aadharno, identify_marks, blood_group, height, weight, contractor_name, temp_emp_no, date_of_joining, emp_no, designation, department, nature_of_job, phone_no, mail_id, emer_con_per, emer_con_rel, emer_con_phone, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                    patient_data = (appoint_date, i['Visit Reason'], i['Name'], dob, i['Age - calculate from DOB'], i['Sex'], i['Aadhar No.'], i['Identification Marks'], i['Blood Group'], i['Height in cm'], i['weight in Kg'], i['Name of Contractor'], i['Temp Emp No.'], doj, i['Employee No'], i['Designation'], i['Department (Latest & previous)'], i['Nature of Job (Latest & previous)'], i['Phone (Personal)'], i['Mail Id (Personal)'], i['Emergency Contact  person '], i['Emergency Contact Relation'], i['Emergency Contact  phone'], i['Address'])

                    cursor = connection.cursor()
                    cursor.execute(add_patient, patient_data)
                    connection.commit()
                    cursor.close()

                    st.write("Data Inserted")


