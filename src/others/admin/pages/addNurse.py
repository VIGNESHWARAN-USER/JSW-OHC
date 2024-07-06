import streamlit as st
from  streamlit_option_menu import option_menu

def addNurse():
    st.title("Add Nurse")
    r0c1,r0c2,r0c3= st.columns([3,2,4])
    with r0c1:
        
        form_name = option_menu(
            None,
            ["Basic details","Register Mail Id"],
            orientation="horizontal",
            icons=['a','a','a','a','a']
        )
        
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