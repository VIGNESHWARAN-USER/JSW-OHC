from re import A
import streamlit as st
import mysql.connector
from streamlit_option_menu import option_menu
import bcrypt

def addDoctor():
    # Initialize the session state for saved_emp_no
    if 'saved_emp_no' not in st.session_state:
        st.session_state.saved_emp_no = None  # Initialize with None or an empty value

    st.title("Add Doctor")
    r0c1, r0c2, r0c3 = st.columns([3, 2, 4])
    with r0c1:
        form_name = option_menu(
            None,
            ["Basic details", "Register Mail Id"],      
            orientation="horizontal",
            icons=['a', 'a']
        )

    if form_name == "Basic details":
        # Using form to ensure explicit submission
        with st.form(key="basic_details_form"):
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
                mail_id_emergency_contact_person = st.text_input("Mail Id (Emergency Contact Person)")
                address = st.text_area("Address")

            # Age Calculation
            from datetime import date
            age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
            st.text(f"Age: {age}")

            # Submit button inside form
            if st.form_submit_button("Save Basic Details"):
                # Check if employee_no is not empty
                if not employee_no:
                    st.error("Employee No. cannot be empty.")
                    return

                # Check if employee_no is already in use
                if check_employee_no_exists(employee_no):
                    st.error(f"Employee No. {employee_no} already exists. Please use a different Employee No.")
                    return

                # Save basic details if no issues
                save_doctor_to_db(employee_no, name, dob, age, sex, aadhar_no, identification_marks,
                                  blood_group, height, weight, date_of_joining, designation, department,
                                  nature_of_job, phone_personal, phone_office, mail_id_personal, mail_id_office,
                                  emergency_contact_person, emergency_contact_relation, emergency_contact_phone,
                                  mail_id_emergency_contact_person, address)
                
                # Save the employee_no in session_state to persist between page reloads
                st.session_state.saved_emp_no = employee_no
                st.success("Basic details have been saved successfully!")

    else:
        # OHC Mail and Password Registration Section
        if st.session_state.saved_emp_no:  # Check if the emp_no is already saved
            with st.form(key="ohc_mail_form"):
                r1c1, r1c2, r1c3 = st.columns([2, 3, 2])
                with r1c2:
                    st.subheader("Register OHC Mail and Password")
                    ohc_mail = st.text_input("OHC Mail ID", value="@jsw.in")
                    if st.form_submit_button("Check Email Availability"):
                        if check_email_availability(ohc_mail):
                            st.success("Email is available")
                        else:
                            st.error("Email is already registered")
                    password = st.text_input("Password", type="password")

                    # Save OHC mail and password after checking availability
                    if st.form_submit_button("Save OHC Mail",type="primary"):
                        if check_email_availability(ohc_mail):
                            save_ohc_mail_and_password(st.session_state.saved_emp_no, ohc_mail, password)
                            st.success("OHC Mail and password have been saved successfully!")  
                            st.session_state.saved_emp_no = None 
                        else:
                            st.error("Email is already registered. Please use a different email.")
                        
        else:
            st.warning("Please save the basic details first.")


def check_employee_no_exists(employee_no):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host="mysql-5893c62-jsw-test.a.aivencloud.com",
            user="avnadmin",
            password="AVNS_uVkEh0awpxi9I4bEOCq",
            database="defaultdb",
            port=19129
        )

        # Create a cursor object
        cursor = connection.cursor()

        # SQL query to check if employee_no already exists
        check_query = "SELECT COUNT(*) FROM doctor WHERE emp_no = %s"
        cursor.execute(check_query, (employee_no,))
        result = cursor.fetchone()

        # If result[0] > 0, employee_no is already taken
        return result[0] > 0

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def check_email_availability(email):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host="mysql-5893c62-jsw-test.a.aivencloud.com",
            user="avnadmin",
            password="AVNS_uVkEh0awpxi9I4bEOCq",
            database="defaultdb",
            port=19129
        )

        # Create a cursor object
        cursor = connection.cursor()

        # SQL query to check if email already exists
        check_query = "SELECT COUNT(*) FROM doctor WHERE ohc_mail = %s"
        cursor.execute(check_query, (email,))
        result = cursor.fetchone()

        # If result[0] > 0, email is already taken
        return result[0] == 0

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def save_doctor_to_db(emp_no, name, dob, age, gender, aadhar_no, identification_mark, blood_group,
                      height, weight, date_of_join, designation, department, nature_of_job,
                      personal_phone_no, office_phone_no, personal_mail, office_mail,
                      emg_con_person, emg_con_relation, emg_con_number, emg_con_mail, address):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host="mysql-5893c62-jsw-test.a.aivencloud.com",
            user="avnadmin",
            password="AVNS_uVkEh0awpxi9I4bEOCq",
            database="defaultdb",
            port=19129
        )

        # Create a cursor object
        cursor = connection.cursor()

        # SQL query to insert doctor data into the 'doctor' table
        insert_query = """
        INSERT INTO doctor (emp_no, name, dob, age, gender, aadhar_no, identification_mark, blood_group, height, 
        weight, date_of_join, designation, department, nature_of_job, personal_phone_no, office_phone_no, 
        personal_mail, office_mail, emg_con_person, emg_con_relation, emg_con_number, emg_con_mail, address) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Execute the query with the form data
        cursor.execute(insert_query, (emp_no, name, dob, age, gender, aadhar_no, identification_mark, blood_group,
                                      height, weight, date_of_join, designation, department, nature_of_job,
                                      personal_phone_no, office_phone_no, personal_mail, office_mail, emg_con_person,
                                      emg_con_relation, emg_con_number, emg_con_mail, address))

        # Commit the transaction
        connection.commit()

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def save_ohc_mail_and_password(emp_no, ohc_mail, password):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host="mysql-5893c62-jsw-test.a.aivencloud.com",
            user="avnadmin",
            password="AVNS_uVkEh0awpxi9I4bEOCq",
            database="defaultdb",
            port=19129
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # SQL query to update OHC Mail and password for the doctor
        update_query = """
        UPDATE doctor SET ohc_mail = %s, password = %s WHERE emp_no = %s
        """

        # Execute the query with the form data
        cursor.execute(update_query, (ohc_mail, hashed_password, emp_no))

        # Commit the transaction
        connection.commit()

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()