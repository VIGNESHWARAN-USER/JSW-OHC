import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_option_menu import option_menu
def Appointment(connection, accessLevel):
    cursor = connection.cursor()
    if "open_modal" not in st.session_state:
        st.session_state.open_modal = False
    if "emp_no" not in st.session_state:
        st.session_state.emp_no
    if "vs" not in st.session_state:
        st.session_state.vs = None
    if st.session_state.open_modal == True:
        st.header("Appointments")
        st.markdown("""
    <style>
        .stButton>button {
            background-color: #22384F; 
            color: white;
            border-radius: 5px;
            font-size: 15px;
            height: 10px;
        }
        .stButton>button:hover {
            background-color: #1B2D3A; 
        }
    </style>""", unsafe_allow_html=True)
        if accessLevel == "doctor":
            with st.container(height=600, border=1):
                r1c1, r1c2 = st.columns([3,10])
                with r1c1:
                    opt = option_menu(menu_title=None, menu_icon='./src/assets/Folder.png', icons=['folder','folder','folder','folder','folder','folder','folder','folder','folder'], options=['Pre Employment', 'Pre Placement', 'Annual/Periodical', 'Camps', 'Fitness After Medical Leave','Illness', 'Injury', 'Followup Visit', 'Special Work Fitness'])
                if opt == 'Pre Employment':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Pre Employment'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=500):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c1, r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,1,2,1,2,1])
                                with r2c1:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Profile</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.image('./src/assets/profile.png', width = 28)
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        st.write(val)
                                with r2c3:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.write(val)
                                with r2c4:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                    for val in emp['gender']:
                                        st.write(val)
                                with r2c5:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                    for val in emp['appoint_date']:
                                        st.write(val)
                                with r2c6:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        if st.button('View', key= val, type='primary'):
                                            st.session_state.emp_no = val
                                            st.session_state.open_modal = False
                                            st.session_state.vs = opt
                                            st.rerun()
                elif opt == 'Pre Placement':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Pre Placement'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=500):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c1, r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,1,2,1,2,1])
                                with r2c1:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Profile</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.image('./src/assets/profile.png', width = 28)
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        st.write(val)
                                with r2c3:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.write(val)
                                with r2c4:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                    for val in emp['gender']:
                                        st.write(val)
                                with r2c5:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                    for val in emp['appoint_date']:
                                        st.write(val)
                                with r2c6:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        if st.button('View', key= val, type='primary'):
                                            st.session_state.emp_no = val
                                            st.session_state.open_modal = False
                                            st.session_state.vs = opt
                                            st.rerun()
                elif opt == 'Annual/Periodical':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Annual/Periodical'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=500):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c1, r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,1,2,1,2,1])
                                with r2c1:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Profile</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.image('./src/assets/profile.png', width = 28)
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        st.write(val)
                                with r2c3:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.write(val)
                                with r2c4:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                    for val in emp['gender']:
                                        st.write(val)
                                with r2c5:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                    for val in emp['appoint_date']:
                                        st.write(val)
                                with r2c6:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        if st.button('View', key= val, type='primary'):
                                            st.session_state.emp_no = val
                                            st.session_state.open_modal = False
                                            st.session_state.vs = opt
                                            st.rerun()
                elif opt == 'Camps':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Camps'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=500):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c1, r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,1,2,1,2,1])
                                with r2c1:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Profile</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.image('./src/assets/profile.png', width = 28)
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        st.write(val)
                                with r2c3:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.write(val)
                                with r2c4:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                    for val in emp['gender']:
                                        st.write(val)
                                with r2c5:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                    for val in emp['appoint_date']:
                                        st.write(val)
                                with r2c6:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        if st.button('View', key= val, type='primary'):
                                            st.session_state.emp_no = val
                                            st.session_state.open_modal = False
                                            st.session_state.vs = opt
                                            st.rerun()
                elif opt == 'Fitness After Medical Leave':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Fitness After Medical Leave'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=500):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c1, r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,1,2,1,2,1])
                                with r2c1:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Profile</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.image('./src/assets/profile.png', width = 28)
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        st.write(val)
                                with r2c3:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.write(val)
                                with r2c4:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                    for val in emp['gender']:
                                        st.write(val)
                                with r2c5:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                    for val in emp['appoint_date']:
                                        st.write(val)
                                with r2c6:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        if st.button('View', key= val, type='primary'):
                                            st.session_state.emp_no = val
                                            st.session_state.open_modal = False
                                            st.session_state.vs = opt
                                            st.rerun()
                elif opt == 'Illness':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Illness'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=500):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c1, r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,1,2,1,2,1])
                                with r2c1:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Profile</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.image('./src/assets/profile.png', width = 28)
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        st.write(val)
                                with r2c3:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.write(val)
                                with r2c4:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                    for val in emp['gender']:
                                        st.write(val)
                                with r2c5:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                    for val in emp['appoint_date']:
                                        st.write(val)
                                with r2c6:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        if st.button('View', key= val, type='primary'):
                                            st.session_state.emp_no = val
                                            st.session_state.open_modal = False
                                            st.session_state.vs = opt
                                            st.rerun()
                elif opt == 'Injury':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Injury'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=500):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c1, r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,1,2,1,2,1])
                                with r2c1:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Profile</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.image('./src/assets/profile.png', width = 28)
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        st.write(val)
                                with r2c3:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.write(val)
                                with r2c4:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                    for val in emp['gender']:
                                        st.write(val)
                                with r2c5:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                    for val in emp['appoint_date']:
                                        st.write(val)
                                with r2c6:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        if st.button('View', key= val, type='primary'):
                                            st.session_state.emp_no = val
                                            st.session_state.open_modal = False
                                            st.session_state.vs = opt
                                            st.rerun()
                elif opt == 'Followup Visit':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Followup Visit'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=500):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c1, r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,1,2,1,2,1])
                                with r2c1:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Profile</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.image('./src/assets/profile.png', width = 28)
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        st.write(val)
                                with r2c3:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.write(val)
                                with r2c4:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                    for val in emp['gender']:
                                        st.write(val)
                                with r2c5:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                    for val in emp['appoint_date']:
                                        st.write(val)
                                with r2c6:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        if st.button('View', key= val, type='primary'):
                                            st.session_state.emp_no = val
                                            st.session_state.open_modal = False
                                            st.session_state.vs = opt
                                            st.rerun()  
                elif opt == 'Special Work Fitness':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Special Work Fitness'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=500):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c1, r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,1,2,1,2,1])
                                with r2c1:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Profile</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.image('./src/assets/profile.png', width = 28)
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        st.write(val)
                                with r2c3:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_name']:
                                        st.write(val)
                                with r2c4:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                    for val in emp['gender']:
                                        st.write(val)
                                with r2c5:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                    for val in emp['appoint_date']:
                                        st.write(val)
                                with r2c6:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                    for val in emp['emp_no']:
                                        if st.button('View', key= val, type='primary'):
                                            st.session_state.emp_no = val
                                            st.session_state.open_modal = False
                                            st.session_state.vs = opt
                                            st.rerun()   
        elif accessLevel == "nurse":
            file_upload  = st.file_uploader("Appointments Upload", type=['xlsx'])

            if file_upload is not None:
                df = pd.read_excel(file_upload, dtype={'Phone (Personal)': str, 'Emergency Contact  phone': str})
                if 'Emergency Contact person ' in df.columns:
                    st.write(df['Emergency Contact person '])
                else:
                    st.write("The 'Emergency Contact person' column is missing.")

                if st.button("Submit"):
                    st.write("Data Submitted")
                    st.write(df.columns)
                    df.fillna("null", inplace=True)
                    
                    # Convert the df to json
                    data = df.to_dict(orient='records')
                    for i in data:
                        st.write(i)
                        
                        # Convert date fields using strftime without slicing
                        appoint_date = pd.to_datetime(i['Date for Appointment']).strftime('%Y-%m-%d')
                        dob = pd.to_datetime(i['Date of Birth']).strftime('%Y-%m-%d')
                        doj = pd.to_datetime(i['Date of Joining']).strftime('%Y-%m-%d')

                        # Insert the data into the database
                        add_patient = ("INSERT INTO appointments (appoint_date, visit_reason, emp_name, dob, age, gender, aadharno, identify_marks, blood_group, height, weight, contractor_name, temp_emp_no, emp_no, date_of_joining,  designation, department, nature_of_job, phone_no, mail_id, emer_con_per, emer_con_rel, emer_con_phone, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                        patient_data = (appoint_date, i['Visit Reason'], i['Name'], dob, i['Age - calculate from DOB'], i['Sex'], i['Aadhar No.'], i['Identification Marks'], i['Blood Group'], i['Height in cm'], i['weight in Kg'], i['Name of Contractor'], i['Temp Emp No.'], i['Employee No'], doj, i['Designation'], i['Department (Latest & previous)'], i['Nature of Job (Latest & previous)'], i['Phone (Personal)'], i['Mail Id (Personal)'], i['Emergency Contact person '], i['Emergency Contact Relation'], i['Emergency Contact phone'], i['Address'])

                        cursor = connection.cursor()
                        cursor.execute(add_patient, patient_data)
                        connection.commit()
                        cursor.close()
                        st.success('Data Imported Successfully')

                        st.write("Data Inserted")
    elif st.session_state.open_modal == False:
        st.subheader('Doctor > Appointments')
        r0c1, r0c2,r0c3 = st.columns([5,4,1])
        with r0c1:
            opt = option_menu(
                        None,
                        ["Appointments","Employee Profile"],
                        orientation="horizontal",
                        icons=['a','a']
                    )
        with r0c3:
            if st.button('close'):
                st.session_state.open_modal = True
                st.rerun()
        if(opt == "Appointments"):
            cursor.execute(f"SELECT * FROM Employee_det where emp_no = {st.session_state.emp_no}")
            emp_row = cursor.fetchone()
            if emp_row:
                emp = pd.DataFrame([emp_row], columns=[desc[0] for desc in cursor.description])
            with st.container(height=600, border=1):   
                st.markdown(f"**Visit reason :** {st.session_state.vs}")
                st.subheader('Basic Details')
                r1c1, r1c2, r1c3 = st.columns(3)
                with r1c1:
                    st.text_input(label='Patient_ID', value=emp['emp_no'][0])
                    st.text_input(label = 'Gender',value=emp['gender'][0])
                    st.text_input(label = 'Nature of Job',value=emp['nature_of_job'][0])
                    st.text_input(label = 'Mobile No.',value=emp['personal_phone_no'][0])
                with r1c2:
                    st.text_input(label = 'Patient Name',value=emp['name'][0])
                    st.text_input(label = 'Department',value=emp['department'][0])
                    st.text_input(label = 'Aadhaar Number',value=emp['aadhar_no'][0])
                    st.text_input(label = 'Blood Group',value=emp['blood_group'][0])
                with r1c3:
                    st.text_input(label = 'Hospital',value=emp['name'][0])
                    st.text_input(label = 'Designation',value=emp['designation'][0])
                    st.text_input(label = 'Address',value=emp['address'][0])
                cursor.execute(f"SELECT * FROM vitals where emp_no = {st.session_state.emp_no}")
                emp_row = cursor.fetchone()
                if emp_row:
                    emp = pd.DataFrame([emp_row], columns=[desc[0] for desc in cursor.description])
                st.subheader('Vitals')
                st.markdown('**Blood Preasure**')
                r2c1, r2c2 = st.columns([4,6])
                with r2c1:
                    st.text_input(label = 'Systolic', value = emp['Systolic'][0])
                    st.text_input(label = 'Diolic', value = emp['Diastolic'][0])
                r3c1, r3c2, r3c3 = st.columns(3)
                with r3c1:
                    st.text_input(label = 'Pulse Rate', value = emp['PulseRate'][0])
                    st.text_input(label = 'Respiratory Rate', value = emp['RespiratoryRate'][0])
                with r3c2:
                    st.text_input(label = 'sp O2', value = emp['SpO2'][0])
                    st.text_input(label = 'Height', value = emp['Height'][0])
                with r3c3:
                    st.text_input(label = 'Temperature', value = emp['Temperature'][0])
                    st.text_input(label = 'Weight', value = emp['Weight'][0])
                r4c1, r4c2 = st.columns([4,6])
                with r4c1:
                    st.text_input(label = 'BMI ( in value )', value = emp['BMI'][0])
                st.subheader('Renel Function Test')
                r5c1, r5c2, r5c3 = st.columns(3)
                with r5c1:
                    st.markdown('**Name**')
                    st.write('Blood urea nitrogen (BUN) (mg/dL)')
                    st.write('Sr.Creatinine (mg/dL)')
                    st.write('Sodium (meg/dL)')
                    st.write('Calcium (mg/dL)')
                    st.write('Potassium (meg/dL)')
                    st.write('Uric acid (mg/dL)')
                    st.write('sr.urea (mg/dL)')
                    st.write('Phosphorus (mg/dL)')
                with r5c2:
                    cursor.execute(f"SELECT * FROM rft_result where emp_no = {st.session_state.emp_no}")
                    emp_row = cursor.fetchone()
                    if emp_row:
                        emp = pd.DataFrame([emp_row], columns=[desc[0] for desc in cursor.description])
                    st.markdown('**Result**')
                    st.text_input(label = '1' ,label_visibility='collapsed', value= emp['bun'][0])
                    st.text_input(label = '2' ,label_visibility='collapsed', value= emp['sr_creatinine'][0])
                    st.text_input(label = '3' ,label_visibility='collapsed', value= emp['sodium'][0])
                    st.text_input(label = '4' ,label_visibility='collapsed', value= emp['calcium'][0])
                    st.text_input(label = '5' ,label_visibility='collapsed', value= emp['potassium'][0])
                    st.text_input(label = '6' ,label_visibility='collapsed', value= emp['uric_acid'][0])
                    st.text_input(label = '7' ,label_visibility='collapsed', value= emp['urea'][0])
                    st.text_input(label = '8' ,label_visibility='collapsed', value= emp['phosphorus'][0])
                
                with r5c3:
                    st.markdown('**Reference Range**')
                    st.write('1-2 (mg/dL )')
                    st.write('50 -60  (F) (mg/dL )')
                    st.write('1-2 (mg/dL )')
                    st.write('50 -60  (F) (mg/dL )')
                    st.write('1-2 (mg/dL )')
                    st.write('50 -60  (F) (mg/dL )')
                    st.write('1-2 (mg/dL )')
                    st.write('50 -60  (F) (mg/dL )')
                st.subheader('Fitness')
                r6c1, r6c2 = st.columns([4,6])
                st.markdown("""
                    <style>
                        .stRadio > div{
                            gap: 14px;
                        }   
                    </style>
        """, unsafe_allow_html=True)
                # cursor.execute(f"SELECT * FROM rft_result where emp_no = {st.session_state.emp_no}")
                # emp_row = cursor.fetchone()
                # if emp_row:
                #     emp1 = pd.DataFrame([emp_row], columns=[desc[0] for desc in cursor.description])
                with r6c1:
                    # val = emp1['status']
                    # Setting the default value using the `value` parameter
                    val = st.radio(
                        'a',  # Label for the radio button (hidden in this case)
                        options=['Fit to Join', 'Unfit', 'Conditional Fit'],  # Options for the radio button
                        index=['Fit to Join', 'Unfit', 'Conditional Fit'].index("Unfit"),  # Set the default index based on `val`
                        label_visibility='collapsed'  # Hides the label
                    )
                with r6c2:
                    st.text_area('Comments')
                st.subheader('Consultant')
                st.markdown('**Remarks**')
                # cursor.execute(f"SELECT * FROM consultation where emp_no = {st.session_state.emp_no}")
                # emp_row = cursor.fetchone()
                # if emp_row:
                #     emp2 = pd.DataFrame([emp_row], columns=[desc[0] for desc in cursor.description])
                st.text_area('b', label_visibility='collapsed')
                st.subheader('Medical Surgical History')
                r7c1, r7c2 = st.columns([3,7], vertical_alignment='center')
                with r7c1:
                    st.markdown('**Personal History**')
                    st.markdown('**Medical History**')
                    st.markdown('**Surgical History**')
                with r7c2:
                    st.multiselect('b',options=['Smoker', 'Alcoholic', 'Veg', 'Mixed Diet'], label_visibility='collapsed')
                    st.multiselect('b',options=['BP', 'DM', 'Others'], label_visibility='collapsed')
                st.text_area('c', label_visibility='collapsed')
                r8c1, r8c2, r8c3, r8c4 = st.columns([3,2,4,2], gap='large')
                with r8c1:
                    st.markdown('**Family History**')
                with r8c2:
                    st.markdown('**Father**')
                    st.markdown('**Mother**')
                with r8c3:
                    st.text_input(label = 'c',label_visibility='collapsed')
                    st.text_input(label = 'd',label_visibility='collapsed')
                r9c1, r9c2 = st.columns([8,2], gap='large')
                with r9c2:
                    st.write("""
            <style>
                button[kind="primary"]{
                    all: unset;
                    background-color: #22384F;
                    color: white;
                    border-radius: 15px;
                    text-align: center;
                    cursor: pointer;
                    font-size: 20px;
                    width: 95%;
                    padding: 10px ;
                    margin-left:-10px
                }
            </style>
            """,unsafe_allow_html=True)
                    st.button('Submit', type='primary')
        else:
            # MARK: Modal
            st.title("Employee Profile")
            with st.container(border=1):
                print(st.session_state.emp_no)
                cursor.execute(f"SELECT * FROM Employee_det where emp_no = {st.session_state.emp_no}")
                emp_row = cursor.fetchone()

                # Create a DataFrame if a row is returned
                if emp_row:
                    emp = pd.DataFrame([emp_row], columns=[desc[0] for desc in cursor.description])
                    
                else:
                    st.write("No employee found with the given `emp_no`.")
                with st.container(border=1):
                    r1c1,r1c2 = st.columns([4,6])
                    cursor.execute(f"SELECT * FROM vitals WHERE emp_no = {st.session_state.emp_no}")
                    vitals = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    cursor.execute(f"SELECT * FROM consultation WHERE emp_no = {st.session_state.emp_no}")
                    consultation = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    
                    cursor.execute(f"SELECT * FROM x_ray WHERE emp_no = {st.session_state.emp_no}")
                    xray = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    cursor.execute(f"SELECT * FROM womens_pack WHERE emp_no = {st.session_state.emp_no}")
                    womens = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    

                    with r1c1:
                        st.write(f"Employee ID: {emp['emp_no'][0]}")
                        st.write(f"Name: {emp['name'][0]}")
                        st.write(f"DOB: {emp['dob'][0]}")
                
                with st.container(border=1,height=700):
                    r0r1,r0r2 = st.columns([6,4])
                    with r0r1:
                        menu = option_menu(
                            None,
                            ["Basic Details","Medical Details","Other Details"],
                            key="menu",
                            orientation="horizontal",
                            icons=['a','b','c']
                        )
                    if menu == "Basic Details":
                        r0c1,r0c2 = st.columns([5,6])
                        with r0c1:
                            # MARK: Personal Details
                            with st.container(border=1):
                                st.title("Personal Details")
                                st.write(f"**Employee ID**: {emp['emp_no'][0]}")
                                st.write(f"**Name**: {emp['name'][0]}")
                                st.write(f"**DOB**: {emp['dob'][0]}")
                                st.write(f"**Age**: {emp['age'][0]}")
                                st.write(f"**Gender**: {emp['gender'][0]}")
                                st.write("**Identification Mark**:")
                                st.markdown(f" * {emp['identification_mark'][0]}")
                        with r0c2:
                            with st.container(border=1):
                                st.title("Contact Details")
                                st.write(f"**Email**: {emp['personal_mail'][0]}")
                                st.write(f"**Office Email**: {emp['office_mail'][0]}")
                                st.write(f"**Emergency Contact Person**: {emp['emg_con_person'][0]}")
                                st.write(f"**Emergency Contact Relation**: {emp['emg_con_relation'][0]}")
                                st.write(f"**Emergency Contact Number**: {emp['emg_con_number'][0]}")
                                st.write(f"**Emergency Contact Email**: {emp['emg_con_mail'][0]}")
                                st.write(f"**Address**: {emp['address'][0]}")
                                st.write(f"**Personal Phone No.**: {emp['personal_phone_no'][0]}")
                                st.write(f"**Office Phone No.**: {emp['office_phone_no'][0]}")
                    if menu == "Medical Details":
                        r0c1,r0c2 = st.columns([4,7])
                        if not vitals.empty:
                            with r0c1:
                                with st.container(border=1, height=300):
                                    # MARK: Vitals
                                    st.title("Vitals")
                                    r01c1,r02c2 = st.columns([4,6])
                                    with r01c1:
                                        st.write(f"**Systolic**: {vitals['Systolic'][0]}")
                                        st.write(f"**Diastolic**: {vitals['Diastolic'][0]}")
                                        st.write(f"**Pulse**: {vitals['PulseRate'][0]}")
                                        st.write(f"**SpO2**: {vitals['SpO2'][0]}")
                                    with r02c2:
                                        st.write(f"**Temperature**: {vitals['Temperature'][0]} °F")
                                        st.write(f"**Weight**: {vitals['Weight'][0]} kg")
                                        st.write(f"**Height**: {vitals['Height'][0]} cm")
                                        st.write(f"**BMI**: {(float(vitals['Weight'][0]) / (float(vitals['Height'][0])/100)**2):.2f}")
                        else:
                            with r0c1:
                                st.warning("No records found")
                        with r0c2:
                            with st.container(border=1,height=580): # type: ignore
                                # MARK: Investigation
                                st.subheader("Investigations")
                                inve = st.selectbox("Select Investigation",["Hematology","RST","RFT","LFT","Thyroid","Autoimmune","Coagulation","CT","Enzymes","Lipid","Mens","Motion","MRI","Occupational","Ophthalmic","Other","Routine","Serology","Urine","USG"])
                                if inve == "Hematology":
                                    cursor.execute(f"SELECT * FROM hematology_result WHERE emp_no = {st.session_state.emp_no}")
                                    hematology = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                    st.subheader("Hematology")
                                    r2c0,r2c1 = st.columns([4,6])
                                    if not hematology.empty:
                                        # MARK: Hematology
                                        with r2c0:
                                            st.write("**Hemoglobin**: ",hematology['heamoglobin'][0])
                                            st.write("**RBC**: ",hematology['rbc_count'][0])
                                            st.write("**WBC**: ",hematology['wbc_count'][0])
                                            st.write("**Haemotocrit**: ",hematology['haemotocrit'][0])
                                            st.write("**MCV**: ",hematology['mcv'][0])
                                            st.write("**MCH**: ",hematology['mch'][0])
                                            st.write("**Eosinophil**: ",hematology['eosinophil'][0])
                                            st.write("**Basophils**: ",hematology['basophils'][0])
                                            st.write("**PBS_RBC**: ",hematology['pbs_rbc'][0])
                                        with r2c1:
                                            st.write("**MCHC**: ",hematology['mchc'][0])
                                            st.write("**RDW**: ",hematology['rdw'][0])
                                            st.write("**Platelet Count**: ",hematology['platelet'][0])
                                            st.write("**RDW**: ",hematology['rdw'][0])
                                            st.write("**Neutrophil**: ",hematology['neutrophil'][0])
                                            st.write("**Lymphocyte**: ",hematology['lymphocyte'][0])
                                            st.write("**Monocyte**: ",hematology['monocyte'][0])
                                            st.write("**ESR**: ",hematology['esr'][0])
                                    else:
                                        st.warning("No records found")

                                if inve == "RST":
                                    # MARK: RST
                                    cursor.execute(f"SELECT * FROM routine_sugartest WHERE emp_no = {st.session_state.emp_no}")
                                    st.subheader("Routine Sugar Test")
                                    sugar = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                    if not sugar.empty:
                                        r2c0,r2c1 = st.columns([4,6])
                                        with r2c0:
                                            st.write("**Fasting Glucose**: ",sugar['glucosef'][0])
                                            st.write("**Post Prandial Glucose**: ",sugar['glucosepp'][0])
                                            st.write("**Random Blood Sugar**: ",sugar['rbs'][0])
                                            st.write("**EAG**: ",sugar['eag'][0])
                                            st.write("**HbA1c**: ",sugar['hba1c'][0])
                                    else:
                                        st.warning("No records found")
                                if inve == "RFT":
                                    # MARK: RFT
                                    st.subheader("Renal Function Test")
                                    cursor.execute(f"SELECT * FROM rft_result WHERE emp_no = {st.session_state.emp_no}")
                                    rft = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                    if not rft.empty:
                                        r2c0,r2c1 = st.columns([4,6])
                                        with r2c0:
                                            st.write("**Urea**: ",rft['urea'][0])
                                            st.write("**BUN**: ",rft['bun'][0])
                                            st.write("**Serum Creatinine**: ",rft['sr_creatinine'][0])
                                            st.write("**Uric Acid**: ",rft['uric_acid'][0])
                                            st.write("**Sodium**: ",rft['sodium'][0])
                                            st.write("**Potassium**: ",rft['potassium'][0])
                                        with r2c1:
                                            st.write("**Calcium**: ",rft['calcium'][0])
                                            st.write("**Phosphorus**: ",rft['phosphorus'][0])
                                            st.write("**Chloride**: ",rft['chloride'][0])
                                            st.write("**Bicarbonate**: ",rft['bicarbonate'][0])
                                    else:
                                        st.warning("No records found")
                                if inve == "LFT":
                                    # MARK: LFT
                                    cursor.execute(f"SELECT * FROM liver_function WHERE emp_no = {st.session_state.emp_no}")
                                    liver = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                    st.subheader("Liver Function Test")
                                    if not liver.empty:
                                        r2c0,r2c1 = st.columns([4,6])
                                        with r2c0:
                                            st.write("**Total Bilirubin**: ",liver['bilirubin_total'][0])
                                            st.write("**Direct Bilirubin**: ",liver['bilirubin_direct'][0])
                                            st.write("**Indirect Bilirubin**: ",liver['bilirubin_indirect'][0])
                                            st.write("**SGOT/ALT**: ",liver['sgot_alt'][0])
                                            st.write("**Alkaline Phosphatase**: ",liver['alkaline_phosphatase'][0])
                                            st.write("**Total Protein**: ",liver['total_protein'][0])
                                        with r2c1:
                                            st.write("**Globulin**: ",liver['globulin'][0])
                                            st.write("**Alb/Glob Ratio**: ",liver['alb_globratio'][0])
                                            st.write("**Gamma GT**: ",liver['gammagt'][0])
                                            st.write("**SGPT/ALT**: ",liver['sgpt_alt'][0])
                                            st.write("**Albumin**: ",liver['albumin'][0])
                                    else:
                                        st.warning("No records found")

                                if inve == "Thyroid":
                                    # MARK: Thyroid
                                    thyroid = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                    cursor.execute(f"SELECT * FROM autoimmune_test WHERE emp_no = {st.session_state.emp_no}")
                                    st.subheader("Thyroid Function Test")
                                    if thyroid.empty:
                                        st.warning("No records found")
                                if inve == "Autoimmune":
                                    # MARK: Autoimmune
                                    autoimmune = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                    cursor.execute(f"SELECT * FROM coagulation_test WHERE emp_no = {st.session_state.emp_no}")

                                    st.subheader("Autoimmune Test")
                                    if autoimmune.empty:
                                        st.warning("No records found")
                                if inve == "Coagulation":
                                    # MARK: Coagulation
                                    cursor.execute(f"SELECT * FROM thyroid_function_test WHERE emp_no = {st.session_state.emp_no}")
                                    coagulation = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                    st.subheader("Coagulation Test")
                                    if coagulation.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**T3**: ",coagulation['t3'][0])
                                            st.write("**T4**: ",coagulation['t4'][0])
                                            st.write("**TSH**: ",coagulation['tsh'][0])
                                        with r0c2:
                                            st.write("**TSH NM AB**: ",coagulation['tsh_nm_ab'][0])

                                    st.json(coagulation.to_dict('records'))
                                if inve == "CT":
                                    # MARK: CT
                                    cursor.execute(f"SELECT * FROM ct_report WHERE emp_no = {st.session_state.emp_no}")
                                    ct = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                    if ct.empty:
                                        st.warning("No records found")
                                    st.json(ct.to_dict('records'))
                                if inve == "Enzymes":
                                    # MARK: Enzymes
                                    cursor.execute(f"SELECT * FROM enzymes_cardio WHERE emp_no = {st.session_state.emp_no}")
                                    enzymes = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                    st.subheader("Enzymes")
                                    if enzymes.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**Acid Phosphatase**: ",enzymes['acid_phosphatase'][0])
                                            st.write("**Adenosine**: ",enzymes['adenosine'][0])
                                            st.write("**Amylase**: ",enzymes['amylase'][0])
                                            st.write("**Lipase**: ",enzymes['lipase'][0])
                                            st.write("**Troponin T**: ",enzymes['troponin_t'][0])
                                            st.write("**Troponin I**: ",enzymes['troponin_i'][0])
                                        with r0c2:
                                            st.write("**CPK Total**: ",enzymes['cpk_total'][0])
                                            st.write("**CPK MB**: ",enzymes['cpk_mb'][0])
                                            st.write("**ECG**: ",enzymes['ecg'][0])
                                            st.write("**ECHO**: ",enzymes['echo'][0])
                                            st.write("**TMT**: ",enzymes['tmt'][0])

                                if inve == "Lipid":
                                    # MARK: Lipid
                                    cursor.execute(f"SELECT * FROM lipid_profile WHERE emp_no = {st.session_state.emp_no}")
                                    lipid = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                    st.subheader("Lipid Profile")
                                    if lipid.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**Total Cholesterol**: ",lipid['tcholesterol'][0])
                                            st.write("**Triglycerides**: ",lipid['triglycerides'][0])
                                            st.write("**HDL Cholesterol**: ",lipid['hdl_cholesterol'][0])
                                            st.write("**VLDL Cholesterol**: ",lipid['vldl_cholesterol'][0])
                                        with r0c2:
                                            st.write("**LDL/HDL Ratio**: ",lipid['ldlhdlratio'][0])
                                            st.write("**Chol/HDL Ratio**: ",lipid['chol_hdlratio'][0])
                                            st.write("**LDL Cholesterol**: ",lipid['ldl_cholesterol'][0])
                                if inve == "Mens":
                                    # MARK: Mens
                                    cursor.execute(f"SELECT * FROM mens_pack WHERE emp_no = {st.session_state.emp_no}")
                                    mens = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                    st.subheader("Mens Pack")
                                    if mens.empty:
                                        st.warning("No records found")
                                    else:
                                        st.write("**PSA**: ",mens['psa'][0])

                    
                                if inve == "Motion":
                                    # MARK: Motion
                                    cursor.execute(f"SELECT * FROM motion WHERE emp_no = {st.session_state.emp_no}")
                                    motion = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                    st.subheader("Motion")
                                    if motion.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**Colour**: ",motion['colour'][0])
                                            st.write("**Appearance**: ",motion['appearance'][0])
                                            st.write("**Occult Blood**: ",motion['occult_blood'][0])                                   

                                if inve == "MRI":
                                    # MARK: MRI
                                    cursor.execute(f"SELECT * FROM mri WHERE emp_no = {st.session_state.emp_no}")
                                    mri = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                    st.subheader("MRI")
                                    if mri.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**Brain**: ",mri['brain'][0])
                                            st.write("**Abdomen**: ",mri['abdomen'][0])
                                            st.write("**Pelvis**: ",mri['pelvis'][0])
                                        with r0c2:
                                            st.write("**MRI Lungs**: ",mri['mri_lungs'][0])
                                            st.write("**Spine**: ",mri['spine'][0])

                            

                                if inve == "Occupational":
                                    # MARK: Occupational
                                    cursor.execute(f"SELECT * FROM occupational_profile WHERE emp_no = {st.session_state.emp_no}")
                                    occupational = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                    st.subheader("Occupational")

                                    if occupational.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**Audiometry NM AB**: ",occupational['audiometry_nm_ab'][0])
                                            st.write("**Audiometry Comment**: ",occupational['audiometry_comment'][0])
                                        with r0c2:
                                            st.write("**PFT NM AB**: ",occupational['pft_nm_ab'][0])
                                            st.write("**PFT Comment**: ",occupational['pft_comment'][0])


                                if inve == "Ophthalmic":
                                    # MARK: Ophthalmic
                                    cursor.execute(f"SELECT * FROM ophthalmic_report WHERE emp_no = {st.session_state.emp_no}")
                                    ophthalmic = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])


                                    st.subheader("Ophthalmic")

                                    if ophthalmic.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**Vision**: ",ophthalmic['vision'][0])
                                            st.write("**Vision Comments**: ",ophthalmic['vision_comments'][0])
                                        with r0c2:
                                            st.write("**Colour Vision**: ",ophthalmic['colourvision'][0])
                                            st.write("**Colour Vision Comment**: ",ophthalmic['colourvision_comment'][0])

                                if inve == "Other":
                                    # MARK: Other
                                    cursor.execute(f"SELECT * FROM other_tests WHERE emp_no = {st.session_state.emp_no}")
                                    other = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                    st.subheader("Other Tests")
                                    if other.empty:
                                        st.warning("No records found")

                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**Pathology**: ",other['pathology'][0])
                                            st.write("**Pathology Comments**: ",other['pathology_comments'][0])

                                if inve == "Routine":
                                    # MARK: Routine
                                    cursor.execute(f"SELECT * FROM routine_culture WHERE emp_no = {st.session_state.emp_no}")
                                    routine = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                    st.subheader("Routine")
                                    if routine.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**Urine**: ",routine['urine'][0])
                                            st.write("**Motion**: ",routine['motion'][0])
                                        with r0c2:
                                            st.write("**Blood**: ",routine['blood'][0])
                                            st.write("**Sputum**: ",routine['sputum'][0])

                                if inve == "Serology":
                                    # MARK: Serology
                                    cursor.execute(f"SELECT * FROM serology_result WHERE emp_no = {st.session_state.emp_no}")
                                    serology = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    

                                    st.subheader("Serology")
                                    if serology.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**HIV Screening**: ",serology['hiv_screening'][0])
                                            st.write("**HIV Screening Comment**: ",serology['hiv_screening_comment'][0])
                                            st.write("**HBsAg**: ",serology['hbsag'][0])
                                            st.write("**HBsAg Comment**: ",serology['hbsag_comment'][0])
                                            st.write("**HCV**: ",serology['hcv'][0])
                                            st.write("**HCV Comment**: ",serology['hcv_comment'][0])
                                            st.write("**Widal**: ",serology['widal'][0])
                                            st.write("**Widal Comment**: ",serology['widal_comment'][0])
                                        with r0c2:
                                            st.write("**VDRL**: ",serology['vdrl'][0])
                                            st.write("**VDRL Comment**: ",serology['vdrl_comment'][0])
                                            st.write("**Dengue NS1**: ",serology['denguens'][0])
                                            st.write("**Dengue NS1 Comment**: ",serology['denguens_comment'][0])
                                            st.write("**Dengue IgG**: ",serology['dengueigg'][0])
                                            st.write("**Dengue IgG Comment**: ",serology['dengueigg_comment'][0])
                                            st.write("**Dengue IgM**: ",serology['dengueigm'][0])
                                            st.write("**Dengue IgM Comment**: ",serology['dengueigm_comment'][0])
                                        

                                if inve == "Urine":
                                    # MARK: Urine
                                    cursor.execute(f"SELECT * FROM urine_routine WHERE emp_no = {st.session_state.emp_no}")
                                    urine = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                    st.subheader("Urine")

                                    if urine.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**Colour**: ",urine['colour'][0])
                                            st.write("**Appearance**: ",urine['apperance'][0])
                                            st.write("**Reaction**: ",urine['reaction'][0])
                                            st.write("**Specific Gravity**: ",urine['specific_gravity'][0])
                                            st.write("**Protein Albumin**: ",urine['protein_albumin'][0])
                                            st.write("**Glucose**: ",urine['glucose'][0])
                                            st.write("**Ketone**: ",urine['ketone'][0])
                                            st.write("**Urobilinogen**: ",urine['urobilinogen'][0])
                                            st.write("**Bile Salts**: ",urine['bile_salts'][0])
                                            st.write("**Bile Pigments**: ",urine['bile_pigments'][0])
                                        with r0c2:
                                            st.write("**WBC Plus Cells**: ",urine['wbc_pluscells'][0])
                                            st.write("**RBC**: ",urine['rbc'][0])
                                            st.write("**Epithelial Cell**: ",urine['epithelial_cell'][0])
                                            st.write("**Casts**: ",urine['casts'][0])
                                            st.write("**Crystals**: ",urine['crystals'][0])
                                            st.write("**Bacteria**: ",urine['bacteria'][0])

                                if inve == "USG":
                                    # MARK: USG
                                    cursor.execute(f"SELECT * FROM usg WHERE emp_no = {st.session_state.emp_no}")
                                    usg = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                    st.subheader("USG")
                                    if usg.empty:
                                        st.warning("No records found")
                                    else:
                                        r0c1,r0c2 = st.columns([4,6])
                                        with r0c1:
                                            st.write("**Liver**: ",usg['liver'][0])
                                            st.write("**Gall Bladder**: ",usg['gall_bladder'][0])
                                            st.write("**Pancreas**: ",usg['pancreas'][0])
                                            st.write("**Kidney**: ",usg['kidney'][0])
                                            st.write("**Spleen**: ",usg['spleen'][0])
                                            st.write("**Prostate**: ",usg['prostate'][0])
                                            st.write("**Uterus**: ",usg['uterus'][0])
                                            st.write("**Ovaries**: ",usg['ovaries'][0])
                                        with r0c2:
                                            st.write("**Bladder**: ",usg['bladder'][0])
                                            st.write("**Prostate**: ",usg['prostate'][0])
                                            st.write("**Uterus**: ",usg['uterus'][0])
                                            st.write("**Ovaries**: ",usg['ovaries'][0])
                                            st.write("**Bladder**: ",usg['bladder'][0])
                                            st.write("**Prostate**: ",usg['prostate'][0])
                                            st.write("**Uterus**: ",usg['uterus'][0])
                                            st.write("**Ovaries**: ",usg['ovaries'][0])

