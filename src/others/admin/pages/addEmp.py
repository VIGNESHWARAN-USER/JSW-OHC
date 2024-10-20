import streamlit as st
import pandas as pd
from mysql.connector import IntegrityError
from datetime import datetime, date
from streamlit_option_menu import option_menu

def addEmp(connection, cursor):
    st.title("Add Employees")

    # Layout for file uploading
    r0c1, r0c2, r0c3 = st.columns([3, 2, 2])

    with r0c1:
        form_name = option_menu(
            None,
            ["Basic details", "Others"],
            orientation="vertical",
            icons=['info', 'gear']
        )

    with r0c2:
        uploaded_file_contractor = st.file_uploader("Upload Contractor Basic details", type=["csv", "xlsx"])
        if uploaded_file_contractor is not None:
            df_contractor = pd.read_excel(uploaded_file_contractor,header=[0])
            #st.write(df_contractor.head())
            df_contractor.fillna("null", inplace=True)

            data_dict = df_contractor.to_dict(orient='records')
            def convert_to_nested_dict(d_list):
                result = []
                for d in d_list:
                    temp_dict = {}
                    for keys, value in d.items():
                        if isinstance(keys, str):
                            temp_dict[keys] = value  
                        else:
                            temp = temp_dict
                            for key in keys[:-1]:
                                temp = temp.setdefault(key, {})
                            temp[keys[-1]] = value
                    result.append(temp_dict)
                return result



            dataitem = convert_to_nested_dict(data_dict)
            st.write(dataitem[0])

            # Convert the DataFrame to a dictionary
            #data = df_employee.to_dict(orient='records')
            #st.write(data[0])  # Displaying the first row for preview
            #$st.write(data[1])  # Displaying the second row for preview

            if st.button("Submit"):
                st.write("Data Submitted")

                for i in dataitem:
                    try:
                        # Print the keys to check if 'Department ' has extra spaces
                        #st.write(i.keys())  # This will help debug the issue

                        # Strip spaces from all keys in the dictionary
                        i = {k.strip(): v for k, v in i.items()}

                        doj = datetime.strptime(i['Date of Joining'], '%d/%m/%Y').strftime('%Y-%m-%d')
                        #dob = datetime.strptime(i['Date of Birth'], '%d/%m/%Y').strftime('%Y-%m-%d')

                        dob = datetime.strptime(i['Date of Birth'], '%d/%m/%Y')  
    
                        # Calculate the age
                        age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
                        age = int(age)

                        department = i.get('Department', 'Unknown')
                        nature_of_job = i.get('Nature of job', 'Unknown')
                        emg_con_person = i.get('Emergency Contact person ', 'Unknown')
                        emg_con_number = i.get('Emergency Contact phone ', 'Unknown')

                        insert_Emp = ("INSERT INTO contractor_det (emp_no, name, dob, age, gender, aadhar_no, identification_mark, "
                                    "blood_group, name_of_contractor ,tem_emp_no, date_of_join, designation, department, nature_of_job, "
                                    "personal_phone_no, personal_mail, emg_con_person, "
                                    "emg_con_relation, emg_con_number,address) "
                                    "VALUES (%s ,%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s ,%s)")

                        emp_data = (i['Employee No'], i['Name'],  dob.strftime('%Y-%m-%d'), 
                                    age, i['Sex'], 
                                    i['Aadhar No.'], i['Identification Marks'], 
                                    i['Blood Group'], i['Name of Contractor'], i['Temp Emp No.'], doj, i['Designation'],
                                    department, nature_of_job, 
                                    i['Phone (Personal)'],
                                    i['Mail Id (Personal)'],
                                    emg_con_person, 
                                    i['Emergency Contact Relation'], 
                                    emg_con_number,i['Address'])

                        # Execute the query and commit the transaction
                        cursor.execute(insert_Emp, emp_data)
                        connection.commit()

                    except IntegrityError:
                        st.write(f"Employee {i['Employee No']} already exists. Fetching existing data...")
                        select_query = "SELECT * FROM Employee_det WHERE emp_no = %s"
                        cursor.execute(select_query, (i['Employee No'],))
                        existing_data = cursor.fetchone()
                        st.write(existing_data)

                    except Exception as e:
                        st.write(f"Error while inserting employee {i['Employee No']}: {e}")


    with r0c3:
        #upload button
        uploaded_file = st.file_uploader("Upload Employee Basic details", type=["csv","xlsx"])
        if uploaded_file is not None:
            dfE = pd.read_excel(uploaded_file,header=[0], dtype={'Phone (Personal)': str, 'Phone (Office)': str,'Emergency Contact  phone':str})
            dfE.fillna("null", inplace=True)
            # convert the df to json
            data = dfE.to_dict(orient='records')
            st.write(data[0])
            st.write(data[1])
            if st.button("Submit", key = 'a'):
                st.write("Data Submitted")
            
                for i in data:
                    st.write(i.keys())

                    doj = datetime.strptime(i['Date of Joining'], '%d-%b-%Y').strftime('%Y-%m-%d')
                    dob = datetime.strptime(i['Date of Birth'], '%d-%b-%Y').strftime('%Y-%m-%d')
                    try:
                        insert_Emp = ("INSERT INTO Employee_det (emp_no, name, dob, age, gender,  blood_group, date_of_join, designation, department, personal_phone_no, office_phone_no, personal_mail, office_mail, emg_con_person, emg_con_relation, emg_con_number) VALUES (%s , %s, %s, %s ,%s, %s, %s, %s ,%s, %s, %s, %s, %s, %s ,%s, %s)")
                        emp_data = (i['Employee No'], i['Name'], dob, i['Age '], i['Gender'],i['Blood Group'],doj,i['Designation'],i['Department'],i['Personal mobile no'],i['office mobile no'],i['Personal Email ID'],i['Company Email ID'],i['Emergency Contact Person'],i['Emergency Contact Relation'],i['Emergency Contact Number'])
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
        r1c1, r1c2, r1c3 = st.columns([3, 2, 4])

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
            address = st.text_area("Address")

        # Age is calculated from DOB
        age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
        

        # Add Save button to manually save the employee data
        if st.button("Save"):
            try:
                insert_Emp_manual = ("INSERT INTO Employee_det (emp_no, name, dob, age, gender, aadhar_no, identification_mark, "
                                     "blood_group, height, weight, date_of_join, designation, department, nature_of_job, "
                                     "personal_phone_no, office_phone_no, personal_mail, office_mail, emg_con_person, "
                                     "emg_con_relation, emg_con_number, address) "
                                     "VALUES (%s ,%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s ,%s, %s, %s)")

                emp_data_manual = (employee_no, name, dob, age, sex, aadhar_no, identification_marks, blood_group, height,
                                   weight, date_of_joining, designation, department, nature_of_job, phone_personal, phone_office,
                                   mail_id_personal, mail_id_office, emergency_contact_person, emergency_contact_relation,
                                   emergency_contact_phone, address)

                cursor.execute(insert_Emp_manual, emp_data_manual)
                connection.commit()
                st.write("Employee data saved successfully!")

            except Exception as e:
                st.write(f"Error while saving employee data: {e}")