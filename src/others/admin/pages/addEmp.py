import streamlit as st
import pandas as pd
from mysql.connector import IntegrityError
from datetime import datetime
from  streamlit_option_menu import option_menu

def addEmp(connection,cursor):
    st.title("Add Employees")

    r0c1,r0c2,r0c3= st.columns([3,2,2])
    with r0c1:
        
        form_name = option_menu(
            None,
            ["Basic details","others"],
            orientation="vertical",
            icons=['a','a','a','a','a']
        )
    with r0c2:
        uploaded_file = st.file_uploader("Upload Contractor Basic details", type=["csv","xlsx"])
        if uploaded_file is not None:
            dfC = pd.read_excel(uploaded_file)
    with r0c3:
        #upload button
        uploaded_file = st.file_uploader("Upload Employee Basic details", type=["csv","xlsx"])
        if uploaded_file is not None:
            dfE = pd.read_excel(uploaded_file, dtype={'Phone (Personal)': str, 'Phone (Office)': str,'Emergency Contact  phone':str})
            dfE.fillna("null", inplace=True)
            # convert the df to json
            data = dfE.to_dict(orient='records')
            st.write(data[0])
            st.write(data[1])
            if st.button("Submit"):
                st.write("Data Submitted")
            
                for i in data:
                    doj = datetime.strptime(i['Date of Joining'], '%d-%b-%Y').strftime('%Y-%m-%d')
                    dob = datetime.strptime(i['Date of Birth'], '%d-%b-%Y').strftime('%Y-%m-%d')
                    try:
                        insert_Emp = ("INSERT INTO Employee_det (emp_no, name, dob, age, gender, aadhar_no, identification_mark, blood_group, height, weight, date_of_join, designation, department, nature_of_job, personal_phone_no, office_phone_no, personal_mail, office_mail, emg_con_person, emg_con_relation, emg_con_number) VALUES (%s ,%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s ,%s, %s)")
                        emp_data = (i['Employee No'], i['Name'], dob, i['Age - calculate from DOB'], i['Sex'], i['Aadhar No.'],i['Identification Marks'],i['Blood Group'],i['Height in cm'],i['weight in Kg'],doj,i['Designation'],i['Department '],i['Nature of Job '],i['Phone (Personal)'],i['Phone (Office)'],i['Mail Id (Personal)'],i['Mail Id (Office)'],i['Emergency Contact  person '],i['Emergency Contact Relation'],i['Emergency Contact  phone'])
                        cursor.execute(insert_Emp, emp_data)
                        connection.commit()
                    except IntegrityError as e:
                        st.write("Data already exists. Fetching existing data...")
                        select_query = "SELECT * FROM Employee_det WHERE emp_no = %s"
                        cursor.execute(select_query, (i['Employee No'],))
                        existing_data = cursor.fetchone()
                        st.write(existing_data)
                    except Exception as e:
                        st.write("Error: ", e)
                        
                st.write("Data Inserted")

            
    if form_name == "Basic details":
            r1c1,r1c2,r1c3 = st.columns([3,2,4])

            with r1c1:
                name = st.text_input("Name")
                dob = st.date_input("Date of Birth")
                sex = st.selectbox("Sex", options=["Male", "Female", "Other"])
                aadhar_no = st.text_input("Aadhar No.")
                identification_marks = st.text_input("Identification Marks")
                blood_group = st.text_input("Blood Group")
                height = st.number_input("Height in cm", format="%f")
                weight = st.number_input("Weight in Kg", format="%f")
                
            with r1c2:
                employee_no = st.text_input("Employee No.")
                date_of_joining = st.date_input("Date of Joining")
                designation = st.text_input("Designation")
                department = st.text_input("Department")
                nature_of_job = st.text_input("Nature of Job")
                phone_personal = st.text_input("Phone (Personal)")
                phone_office = st.text_input("Phone (Office)")
                mail_id_personal = st.text_input("Mail Id (Personal)")
                
                
            with r1c3:
                mail_id_office = st.text_input("Mail Id (Office)")
                emergency_contact_person = st.text_input("Emergency Contact Person")
                emergency_contact_relation = st.text_input("Emergency Contact Relation")
                emergency_contact_phone = st.text_input("Emergency Contact Phone")
                mail_id_emergency_contact_person = st.text_input("Mail Id (Emergency Contact Person)")
                address = st.text_area("Address")

            # Age is calculated from DOB
            from datetime import date
            age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
            st.text(f"Age: {age}")

            # Save button        