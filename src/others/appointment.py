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

                # insert the data into the database

                # +-----------------+-----------------------+------+-----+---------+-------+
                # | Field           | Type                  | Null | Key | Default | Extra |
                # +-----------------+-----------------------+------+-----+---------+-------+
                # | appoint_date    | date                  | NO   | PRI | NULL    |       |
                # | visit_reason    | varchar(50)           | YES  |     | NULL    |       |
                # | emp_name        | varchar(50)           | YES  |     | NULL    |       |
                # | dob             | date                  | YES  |     | NULL    |       |
                # | age             | int                   | YES  |     | NULL    |       |
                # | gender          | enum('Male','Female') | YES  |     | NULL    |       |
                # | aadharno        | varchar(15)           | YES  |     | NULL    |       |
                # | identify_marks  | varchar(200)          | YES  |     | NULL    |       |
                # | blood_group     | varchar(10)           | YES  |     | NULL    |       |
                # | height          | varchar(10)           | YES  |     | NULL    |       |
                # | weight          | varchar(10)           | YES  |     | NULL    |       |
                # | contractor_name | varchar(255)          | YES  |     | NULL    |       |
                # | temp_emp_no     | varchar(50)           | YES  |     | NULL    |       |
                # | date_of_joining | date                  | YES  |     | NULL    |       |
                # | emp_no          | varchar(30)           | YES  | MUL | NULL    |       |
                # | designation     | varchar(255)          | YES  |     | NULL    |       |
                # | department      | varchar(255)          | YES  |     | NULL    |       |
                # | nature_of_job   | varchar(255)          | YES  |     | NULL    |       |
                # | phone_no        | varchar(15)           | YES  |     | NULL    |       |
                # | mail_id         | varchar(50)           | YES  |     | NULL    |       |
                # | emer_con_per    | varchar(255)          | YES  |     | NULL    |       |
                # | emer_con_rel    | varchar(255)          | YES  |     | NULL    |       |
                # | emer_con_phone  | varchar(20)           | YES  |     | NULL    |       |
                # | address         | varchar(255)          | YES  |     | NULL    |       |
                # +-----------------+-----------------------+------+-----+---------+-------+

                # 0	Date for Appointment
                # 1	Visit Reason
                # 2	Name
                # 3	Date of Birth
                # 4	Age - calculate from DOB
                # 5	Sex
                # 6	Aadhar No.
                # 7	Identification Marks
                # 8	Blood Group
                # 9	Height in cm
                # 10	weight in Kg
                # 11	Name of Contractor
                # 12	Temp Emp No.
                # 13	Date of Joining
                # 14	Employee No
                # 15	Designation
                # 16	Department (Latest & previous)
                # 17	Nature of Job (Latest & previous)
                # 18	Phone (Personal)
                # 19	Mail Id (Personal)
                # 20	Emergency Contact  person 
                # 21	Emergency Contact Relation
                # 22	Emergency Contact  phone
                # 23	Address

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


