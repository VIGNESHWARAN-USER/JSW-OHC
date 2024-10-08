import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_option_menu import option_menu
def Appointment(connection, accessLevel):
    opt=None
    if "open_modal" not in st.session_state:
        st.session_state.open_modal = False
    if "emp_no" not in st.session_state:
        st.session_state.emp_no = None
    if accessLevel == "doctor":
        if st.session_state.open_modal:
            st.header("Doc > Appointments")
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
            
            cursor = connection.cursor()
            with st.container(height=600, border=1):
                r1c1, r1c2 = st.columns([3,10])
                with r1c1:
                    opt = option_menu(menu_title=None, menu_icon='./src/assets/Folder.png', icons=['folder','folder','folder','folder','folder','folder','folder','folder','folder'], options=['Pre Employment', 'Pre Placement', 'Annual/Periodical', 'Camps', 'Fitness After Medical Leave','Illness', 'Injury', 'Followup Visit', 'Special Work Fitness'])
                if opt == 'Pre Employment':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Pre Employment'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=600):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                                
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['height']:
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
                                            st.session_state.open_modal = False
                                            st.rerun()
                elif opt == 'Pre Placement':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Pre Placement'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=600):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                                
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['height']:
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
                                            st.session_state.open_modal = False
                                            st.rerun()
                elif opt == 'Annual/Periodical':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Annual/Periodical'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=600):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                               
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['height']:
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
                                            st.session_state.open_modal = False
                                            st.rerun()
                elif opt == 'Camps':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Camps'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=600):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                                
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['height']:
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
                                            st.session_state.open_modal = False
                                            st.rerun()
                elif opt == 'Fitness After Medical Leave':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Fitness After Medical Leave'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=600):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                                
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['height']:
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
                                            st.session_state.open_modal = False
                                            st.rerun()
                elif opt == 'Illness':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Illness'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=600):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                                
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['height']:
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
                                            st.session_state.open_modal = False
                                            st.rerun()
                elif opt == 'Injury':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Injury'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=600):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                                
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['height']:
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
                                            st.session_state.open_modal = False
                                            st.rerun()
                elif opt == 'Followup Visit':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Followup Visit'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=600):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                                
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['height']:
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
                                            st.session_state.open_modal = False
                                            st.rerun()  
                elif opt == 'Special Work Fitness':
                    cursor.execute("SELECT * FROM appointments where visit_reason = 'Special Work Fitness'")
                    emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                    with r1c2:
                        with st.container(height=600):
                            if emp.empty:
                                st.error("No records found")
                            else:
                                r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                                
                                with r2c2:
                                    st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                    for val in emp['height']:
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
                                            st.session_state.open_modal = False
                                            st.rerun()
        else:
            st.subheader('intments')
            r0c1, r0c2,r0c3 = st.columns([5,4,1])
            with r0c1:
                opt = option_menu(
                            None,
                            ["Appointments","Employee Profile"],
                            orientation="horizontal",
                            icons=['a','a']
                        )
            with r0c3:
                if st.button('close', type="primary"):
                    st.session_state.open_modal = True
                    st.rerun()
            with st.container(height=600, border=1):   
                st.markdown(f"*Visit reason :* {opt}")
                st.subheader('Basic Details')
                r1c1, r1c2, r1c3 = st.columns(3)
                with r1c1:
                    st.text_input('Patient_ID')
                    st.text_input('Gender')
                    st.text_input('Nature of Job')
                    st.text_input('Mobile No.')
                with r1c2:
                    st.text_input('Patient Name')
                    st.text_input('Department')
                    st.text_input('Aadhaar Number')
                    st.text_input('Blood Group')
                with r1c3:
                    st.text_input('Hospital')
                    st.text_input('Designation')
                    st.text_input('Address')
                st.subheader('Vitals')
                st.markdown('*Blood Preasure*')
                r2c1, r2c2 = st.columns([4,6])
                with r2c1:
                    st.text_input('Systolic')
                    st.text_input('Diolic')
                r3c1, r3c2, r3c3 = st.columns(3)
                with r3c1:
                    st.text_input('Pulse Rate')
                    st.text_input('Respiratory Rate')
                with r3c2:
                    st.text_input('sp O2')
                    st.text_input('Height')
                with r3c3:
                    st.text_input('Temperature')
                    st.text_input('Weight')
                r4c1, r4c2 = st.columns([4,6])
                with r4c1:
                    st.text_input('BMI ( in value )')
                st.subheader('Renel Function Test')
                r5c1, r5c2, r5c3 = st.columns(3)
                with r5c1:
                    st.markdown('*Name*')
                    st.write('Blood urea nitrogen (BUN) (mg/dL)')
                    st.write('Sr.Creatinine (mg/dL)')
                    st.write('Sodium (meg/dL)')
                    st.write('Calcium (mg/dL)')
                    st.write('Potassium (meg/dL)')
                    st.write('Uric acid (mg/dL)')
                    st.write('sr.urea (mg/dL)')
                    st.write('Phosphorus (mg/dL)')
                with r5c2:
                    st.markdown('*Result*')
                    st.text_input('1' ,label_visibility='collapsed')
                    st.text_input('2' ,label_visibility='collapsed')
                    st.text_input('3' ,label_visibility='collapsed')
                    st.text_input('4' ,label_visibility='collapsed')
                    st.text_input('5' ,label_visibility='collapsed')
                    st.text_input('6' ,label_visibility='collapsed')
                
                with r5c3:
                    st.markdown('*Reference Range*')
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
                with r6c1:
                    st.radio('a', options=['Fit to Join', 'Unfit', 'Conditional Fit'], label_visibility='collapsed')
                with r6c2:
                    st.text_area('a', label_visibility='collapsed')
                st.subheader('Consultant')
                st.markdown('*Remarks*')
                st.text_area('b', label_visibility='collapsed')
                st.subheader('Medical Surgical History')
                r7c1, r7c2 = st.columns([3,7], vertical_alignment='center')
                with r7c1:
                    st.markdown('*Personal History*')
                    st.markdown('*Medical History*')
                    st.markdown('*Surgical History*')
                with r7c2:
                    st.multiselect('b',options=['Smoker', 'Alcoholic', 'Veg', 'Mixed Diet'], label_visibility='collapsed')
                    st.multiselect('b',options=['BP', 'DM', 'Others'], label_visibility='collapsed')
                st.text_area('c', label_visibility='collapsed')
                r8c1, r8c2, r8c3, r8c4 = st.columns([3,1,4,2], gap='large')
                with r8c1:
                    st.markdown('*Family History*')
                with r8c2:
                    st.markdown('*Father*')
                    st.markdown('*Mother*')
                with r8c3:
                    st.text_input('c',label_visibility='collapsed')
                    st.text_input('d',label_visibility='collapsed')
                r9c1, r9c2 = st.columns([8,2], gap='large')
                with r9c2:
                    st.write("""
            <style>
                button[kind="primary"]{
                    color: white;
                    text-align: center;
                    cursor: pointer;
                    font-size: 5px;
                    width: 10%;
                    padding: 2px ;
                    
                }
            </style>
            """,unsafe_allow_html=True)
                    st.button('Submit', type='primary')       
    elif accessLevel == "nurse":
        if 'page' not in st.session_state:
            st.session_state.page = 'upload' 
        col1, col2, col3 = st.columns([1,2,8])  
        with col1:
            if st.button("Upload", key="upload_btn", type='primary'):  
                st.session_state.page = 'upload'  

        with col2:
            if st.button("Appointments", key="appointments_btn", type='primary'):  
                st.session_state.page = 'appointments' 

        # Check if the current page is 'upload'
        if st.session_state.page == 'upload':
            # File uploader for Excel files
            file_upload = st.file_uploader("Get Excel file from Contractor Upload as .xlsx file", type=['xlsx'], key="upload_file")

            if file_upload is not None:
                df = pd.read_excel(file_upload)
                expected_columns = ['Appointment ID', 'Appointment Date','Visit Reason' ,'Name', 'Date of Birth', 
                                    'Age - calculate from DOB', 'Sex', 'Aadhar No.', 
                                    'Identification Marks', 'Blood Group', 'Height in cm', 
                                    'weight in Kg', 'Name of Contractor', 'Temp Emp No.', 
                                    'Date of Joining', 'Employee No', 'Designation', 
                                    'Department', 'Nature of Job', 'Phone (Personal)', 
                                    'Mail Id (Personal)', 'Emergency Contact person', 
                                    'Emergency Contact Relation', 'Emergency Contact phone', 'Address']

                if all(col in df.columns for col in expected_columns):
                    r0c1, r0c2, r0c3 = st.columns([2, 2, 6])
                    total_records = len(df)
                    with r0c1:
                        st.write(f"Counts: {total_records}")
                        st.write("Employee Details:")
                    
                    with r0c2:
                        if st.button("Submit", type='primary'):
                            for index, row in df.iterrows():
                                query = """
                                INSERT INTO appointments (
                                    appoint_ID, appoint_date, visit_reason, emp_name, dob, age, gender, aadharno, identify_marks, 
                                    blood_group, height, weight, contractor_name, temp_emp_no, date_of_joining, emp_no, designation, 
                                    department, nature_of_job, phone_no, mail_id, emer_con_per, emer_con_rel, emer_con_phone, address
                                ) VALUES (
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                                )
                                """
                                data = (
                                    row['Appointment ID'], 
                                    row['Appointment Date'], 
                                    row['Visit Reason'],  
                                    row['Name'], 
                                    row['Date of Birth'], 
                                    row['Age - calculate from DOB'], 
                                    row['Sex'], 
                                    row['Aadhar No.'], 
                                    row['Identification Marks'], 
                                    row['Blood Group'], 
                                    row['Height in cm'], 
                                    row['weight in Kg'], 
                                    row['Name of Contractor'], 
                                    row['Temp Emp No.'], 
                                    row['Date of Joining'], 
                                    row['Employee No'], 
                                    row['Designation'], 
                                    row['Department'], 
                                    row['Nature of Job'], 
                                    row['Phone (Personal)'], 
                                    row['Mail Id (Personal)'], 
                                    row['Emergency Contact person'], 
                                    row['Emergency Contact Relation'], 
                                    row['Emergency Contact phone'], 
                                    row['Address']
                                )
                                cursor = connection.cursor()
                                cursor.execute(query, data)
                                connection.commit()
                            st.success("Data Inserted Successfully")
                    
                    st.table(df[expected_columns])
                else:
                    st.error("The uploaded file does not have the required columns.")





            

        elif st.session_state.page == 'appointments':
            if st.session_state.open_modal:
                cursor = connection.cursor()
                with st.container( border=1):
                    r1c1, r1c2 = st.columns([3,10])
                    with r1c1:
                        opt = option_menu(menu_title=None, menu_icon='./src/assets/Folder.png', icons=['folder','folder','folder','folder','folder','folder','folder','folder','folder'], options=['Pre Employment', 'Pre Placement', 'Annual/Periodical', 'Camps', 'Fitness After Medical Leave','Illness', 'Injury', 'Followup Visit', 'Special Work Fitness'])
                    if opt == 'Pre Employment':
                        cursor.execute("SELECT * FROM appointments where visit_reason = 'Pre Employment'")
                        emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                        
                        with r1c2:
                            with st.container(height=600):
                                if emp.empty:
                                    st.error("No records found")
                                else:
                                    r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                                    
                                    
                                    # Column 2: PID
                                    with r2c2:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['height']):
                                            st.text_input(label= "PID", value=val, label_visibility="collapsed", key=f"pid_{i}")
                                    
                                    # Column 3: Employee Names
                                    with r2c3:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_name']):
                                            st.text_input(label= "Name", value=val, label_visibility="collapsed", key=f"name_{i}")
                                    
                                    # Column 4: Gender
                                    with r2c4:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['gender']):
                                            st.text_input(label= "Gender", value=val, label_visibility="collapsed", key=f"gender_{i}")
                                    
                                    # Column 5: Appointment Dates
                                    with r2c5:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['appoint_date']):
                                            st.text_input(label= "Appointment", value=val, label_visibility="collapsed", key=f"appointment_{i}")
                                    
                                    # Column 6: View Details Button
                                    with r2c6:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_no']):
                                            if st.button('View', key=f'view_{val}', type='primary'):
                                                st.session_state.open_modal = False
                                                st.rerun()

                    elif opt == 'Pre Placement':
                        cursor.execute("SELECT * FROM appointments where visit_reason = 'Pre Placement'")
                        emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                        with r1c2:
                            with st.container(height=600):
                                if emp.empty:
                                    st.error("No records found")
                                else:
                                    r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1,2,1,2,1])
                                            
                                    # Column 2: PID
                                    with r2c2:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['height']):
                                            st.text_input("1", value=val, label_visibility="collapsed", key=f"pid_{i}")
                                    
                                    # Column 3: Employee Names
                                    with r2c3:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_name']):
                                            st.text_input("1", value=val, label_visibility="collapsed", key=f"name_{i}")
                                    
                                    # Column 4: Gender
                                    with r2c4:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['gender']):
                                            st.text_input("1", value=val, label_visibility="collapsed", key=f"gender_{i}")
                                    
                                    # Column 5: Appointment Date
                                    with r2c5:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['appoint_date']):
                                            st.text_input("1", value=val, label_visibility="collapsed", key=f"appointment_{i}")
                                    
                                    # Column 6: View Details Button
                                    with r2c6:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_no']):
                                            if st.button('View', key=f'view_{val}', type='primary'):
                                                st.session_state.open_modal = False
                                                st.rerun()

                    elif opt == 'Annual/Periodical':
                        cursor.execute("SELECT * FROM appointments where visit_reason = 'Annual/Periodical'")
                        emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                        
                        with r1c2:
                            with st.container(height=600):
                                if emp.empty:
                                    st.error("No records found")
                                else:
                                    r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1, 2, 1, 2, 1])
                                    
                                    
                                    # Column 2: PID
                                    with r2c2:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['height']):
                                            st.text_input("PID", value=val, label_visibility="collapsed", key=f"pid_{i}")
                                    
                                    # Column 3: Employee Names
                                    with r2c3:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_name']):
                                            st.text_input("Name", value=val, label_visibility="collapsed", key=f"name_{i}")
                                    
                                    # Column 4: Gender
                                    with r2c4:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['gender']):
                                            st.text_input("Gender", value=val, label_visibility="collapsed", key=f"gender_{i}")
                                    
                                    # Column 5: Appointment Dates
                                    with r2c5:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['appoint_date']):
                                            st.text_input("Appointment", value=val, label_visibility="collapsed", key=f"appointment_{i}")
                                    
                                    # Column 6: View Details Button
                                    with r2c6:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_no']):
                                            if st.button('View', key=f'view_{val}', type='primary'):
                                                st.session_state.open_modal = False
                                                st.rerun()


                    elif opt == 'Camps':
                        cursor.execute("SELECT * FROM appointments where visit_reason = 'Camps'")
                        emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                        
                        with r1c2:
                            with st.container(height=600):
                                if emp.empty:
                                    st.error("No records found")
                                else:
                                    r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1, 2, 1, 2, 1])
                                    
                                    
                                    # Column 2: PID
                                    with r2c2:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['height']):
                                            st.text_input("PID", value=val, label_visibility="collapsed", key=f"pid_camps_{i}")
                                    
                                    # Column 3: Employee Names
                                    with r2c3:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_name']):
                                            st.text_input("Name", value=val, label_visibility="collapsed", key=f"name_camps_{i}")
                                    
                                    # Column 4: Gender
                                    with r2c4:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['gender']):
                                            st.text_input("Gender", value=val, label_visibility="collapsed", key=f"gender_camps_{i}")
                                    
                                    # Column 5: Appointment Dates
                                    with r2c5:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['appoint_date']):
                                            st.text_input("Appointment", value=val, label_visibility="collapsed", key=f"appointment_camps_{i}")
                                    
                                    # Column 6: View Details Button
                                    with r2c6:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_no']):
                                            if st.button('View', key=f'view_camps_{val}', type='primary'):
                                                st.session_state.open_modal = False
                                                st.rerun()

                    elif opt == 'Fitness After Medical Leave':
                        cursor.execute("SELECT * FROM appointments where visit_reason = 'Fitness After Medical Leave'")
                        emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                        
                        with r1c2:
                            with st.container(height=600):
                                if emp.empty:
                                    st.error("No records found")
                                else:
                                    r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1, 2, 1, 2, 1])
                                    
                                    
                                    # Column 2: PID
                                    with r2c2:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['height']):
                                            st.text_input("PID", value=val, label_visibility="collapsed", key=f"pid_fitness_{i}")
                                    
                                    # Column 3: Employee Names
                                    with r2c3:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_name']):
                                            st.text_input("Name", value=val, label_visibility="collapsed", key=f"name_fitness_{i}")
                                    
                                    # Column 4: Gender
                                    with r2c4:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['gender']):
                                            st.text_input("Gender", value=val, label_visibility="collapsed", key=f"gender_fitness_{i}")
                                    
                                    # Column 5: Appointment Dates
                                    with r2c5:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['appoint_date']):
                                            st.text_input("Appointment", value=val, label_visibility="collapsed", key=f"appointment_fitness_{i}")
                                    
                                    # Column 6: View Details Button
                                    with r2c6:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_no']):
                                            if st.button('View', key=f'view_fitness_{val}', type='primary'):
                                                st.session_state.open_modal = False
                                                st.rerun()


                    elif opt == 'Illness':
                        cursor.execute("SELECT * FROM appointments where visit_reason = 'Illness'")
                        emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                        
                        with r1c2:
                            with st.container(height=600):
                                if emp.empty:
                                    st.error("No records found")
                                else:
                                    r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1, 2, 1, 2, 1])
                                    
                                    # Column 2: PID
                                    with r2c2:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['height']):
                                            st.text_input("PID", value=val, label_visibility="collapsed", key=f"pid_illness_{i}")
                                    
                                    # Column 3: Employee Names
                                    with r2c3:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_name']):
                                            st.text_input("Name", value=val, label_visibility="collapsed", key=f"name_illness_{i}")
                                    
                                    # Column 4: Gender
                                    with r2c4:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['gender']):
                                            st.text_input("Gender", value=val, label_visibility="collapsed", key=f"gender_illness_{i}")
                                    
                                    # Column 5: Appointment Dates
                                    with r2c5:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['appoint_date']):
                                            st.text_input("Appointment", value=val, label_visibility="collapsed", key=f"appointment_illness_{i}")
                                    
                                    # Column 6: View Details Button
                                    with r2c6:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_no']):
                                            if st.button('View', key=f'view_illness_{val}', type='primary'):
                                                st.session_state.open_modal = False
                                                st.rerun()


                    elif opt == 'Injury':
                        cursor.execute("SELECT * FROM appointments where visit_reason = 'Injury'")
                        emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                        
                        with r1c2:
                            with st.container(height=600):
                                if emp.empty:
                                    st.error("No records found")
                                else:
                                    r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1, 2, 1, 2, 1])
                                    
                                    
                                    
                                    # Column 2: PID
                                    with r2c2:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['height']):
                                            st.text_input("PID", value=val, label_visibility="collapsed", key=f"pid_injury_{i}")
                                    
                                    # Column 3: Employee Names
                                    with r2c3:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_name']):
                                            st.text_input("Name", value=val, label_visibility="collapsed", key=f"name_injury_{i}")
                                    
                                    # Column 4: Gender
                                    with r2c4:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['gender']):
                                            st.text_input("Gender", value=val, label_visibility="collapsed", key=f"gender_injury_{i}")
                                    
                                    # Column 5: Appointment Dates
                                    with r2c5:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['appoint_date']):
                                            st.text_input("Appointment", value=val, label_visibility="collapsed", key=f"appointment_injury_{i}")
                                    
                                    # Column 6: View Details Button
                                    with r2c6:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_no']):
                                            if st.button('View', key=f'view_injury_{val}', type='primary'):
                                                st.session_state.open_modal = False
                                                st.rerun()

                    elif opt == 'Followup Visit':
                        cursor.execute("SELECT * FROM appointments where visit_reason = 'Followup Visit'")
                        emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                        
                        with r1c2:
                            with st.container(height=600):
                                if emp.empty:
                                    st.error("No records found")
                                else:
                                    r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([ 1, 2, 1, 2, 1])
                                    
                                    
                                    
                                    # Column 2: PID
                                    with r2c2:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['height']):
                                            st.text_input("PID", value=val, label_visibility="collapsed", key=f"pid_followup_{i}")
                                    
                                    # Column 3: Employee Names
                                    with r2c3:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_name']):
                                            st.text_input("Name", value=val, label_visibility="collapsed", key=f"name_followup_{i}")
                                    
                                    # Column 4: Gender
                                    with r2c4:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['gender']):
                                            st.text_input("Gender", value=val, label_visibility="collapsed", key=f"gender_followup_{i}")
                                    
                                    # Column 5: Appointment Dates
                                    with r2c5:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['appoint_date']):
                                            st.text_input("Appointment", value=val, label_visibility="collapsed", key=f"appointment_followup_{i}")
                                    
                                    # Column 6: View Details Button
                                    with r2c6:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_no']):
                                            if st.button('View', key=f'view_followup_{val}', type='primary'):
                                                st.session_state.open_modal = False
                                                st.rerun()
    
                    elif opt == 'Special Work Fitness':
                        cursor.execute("SELECT * FROM appointments where visit_reason = 'Special Work Fitness'")
                        emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                        
                        with r1c2:
                            with st.container(height=600):
                                if emp.empty:
                                    st.error("No records found")
                                else:
                                    r2c2, r2c3, r2c4, r2c5, r2c6 = st.columns([1, 2, 1, 2, 1])
                                    
                                    # Column 2: PID
                                    with r2c2:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>PID</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['height']):
                                            st.text_input("PID", value=val, label_visibility="collapsed", key=f"pid_special_work_{i}")
                                    
                                    # Column 3: Employee Names
                                    with r2c3:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Name</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_name']):
                                            st.text_input("Name", value=val, label_visibility="collapsed", key=f"name_special_work_{i}")
                                    
                                    # Column 4: Gender
                                    with r2c4:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Gender</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['gender']):
                                            st.text_input("Gender", value=val, label_visibility="collapsed", key=f"gender_special_work_{i}")
                                    
                                    # Column 5: Appointment Dates
                                    with r2c5:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Appointments</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['appoint_date']):
                                            st.text_input("Appointment", value=val, label_visibility="collapsed", key=f"appointment_special_work_{i}")
                                    
                                    # Column 6: View Details Button
                                    with r2c6:
                                        st.markdown(f'<p style="color: #22384F; fontSize: 15px"><b>Details</b></p>', unsafe_allow_html=True)
                                        for i, val in enumerate(emp['emp_no']):
                                            if st.button('View', key=f'view_special_work_{val}', type='primary'):
                                                st.session_state.open_modal = False
                                                st.rerun()
            else:
                
                r0c1, r0c2,r0c3 = st.columns([5,4,1])
                with r0c1:
                    st.subheader('Appointments')
                with r0c3:
                    if st.button('close', type="primary"):
                        st.session_state.open_modal = True
                        st.rerun()
                with st.container(height=700, border=1):   
                    st.subheader('Basic Details')
                    r1c1, r1c2, r1c3 = st.columns(3)
                    with r1c1:
                        st.text_input('Patient_ID')
                        st.text_input('Gender')
                        st.text_input('Nature of Job')
                        st.text_input('Mobile No.')
                    with r1c2:
                        st.text_input('Patient Name')
                        st.text_input('Department')
                        st.text_input('Aadhaar Number')
                        st.text_input('Blood Group')
                    with r1c3:
                        st.text_input('Hospital')
                        st.text_input('Designation')
                        st.text_input('Address')
                    st.subheader('Vitals')
                    st.markdown('*Blood Preasure*')
                    r2c1, r2c2 = st.columns([4,6])
                    with r2c1:
                        st.text_input('Systolic')
                        st.text_input('Diolic')
                    r3c1, r3c2, r3c3 = st.columns(3)
                    with r3c1:
                        st.text_input('Pulse Rate')
                        st.text_input('Respiratory Rate')
                    with r3c2:
                        st.text_input('sp O2')
                        st.text_input('Height')
                    with r3c3:
                        st.text_input('Temperature')
                        st.text_input('Weight')
                    r4c1, r4c2 = st.columns([4,6])
                    with r4c1:
                        st.text_input('BMI ( in value )')
                    st.subheader('Renel Function Test')
                    r5c1, r5c2, r5c3 = st.columns(3)
                    with r5c1:
                        st.markdown('*Name*')
                        st.write('Blood urea nitrogen (BUN) (mg/dL)')
                        st.write('Sr.Creatinine (mg/dL)')
                        st.write('Sodium (meg/dL)')
                        st.write('Calcium (mg/dL)')
                        st.write('Potassium (meg/dL)')
                        st.write('Uric acid (mg/dL)')
                        st.write('sr.urea (mg/dL)')
                        st.write('Phosphorus (mg/dL)')
                    with r5c2:
                        st.markdown('*Result*')
                        st.text_input('1' ,label_visibility='collapsed')
                        st.text_input('2' ,label_visibility='collapsed')
                        st.text_input('3' ,label_visibility='collapsed')
                        st.text_input('4' ,label_visibility='collapsed')
                        st.text_input('5' ,label_visibility='collapsed')
                        st.text_input('6' ,label_visibility='collapsed')
                    
                    with r5c3:
                        st.markdown('*Reference Range*')
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
                    with r6c1:
                        st.radio('a', options=['Fit to Join', 'Unfit', 'Conditional Fit'], label_visibility='collapsed')
                    with r6c2:
                        st.text_area('a', label_visibility='collapsed')
                    st.subheader('Consultant')
                    st.markdown('*Remarks*')
                    st.text_area('b', label_visibility='collapsed')
                    st.subheader('Medical Surgical History')
                    r7c1, r7c2 = st.columns([3,7], vertical_alignment='center')
                    with r7c1:
                        st.markdown('*Personal History*')
                        st.markdown('*Medical History*')
                        st.markdown('*Surgical History*')
                    with r7c2:
                        st.multiselect('b',options=['Smoker', 'Alcoholic', 'Veg', 'Mixed Diet'], label_visibility='collapsed')
                        st.multiselect('b',options=['BP', 'DM', 'Others'], label_visibility='collapsed')
                    st.text_area('c', label_visibility='collapsed')
                    r8c1, r8c2, r8c3, r8c4 = st.columns([3,1,4,2], gap='large')
                    with r8c1:
                        st.markdown('*Family History*')
                    with r8c2:
                        st.markdown('*Father*')
                        st.markdown('*Mother*')
                    with r8c3:
                        st.text_input('c',label_visibility='collapsed')
                        st.text_input('d',label_visibility='collapsed')
                    r9c1, r9c2 = st.columns([8,2], gap='large')
                    
                    st.button('Submit', type='primary')
  


            file_upload=None
        
            if file_upload is not None:

                try:
                    df = pd.read_excel(file_upload, dtype={'Phone (Personal)': str, 'Emergency Contact  phone': str})
                except Exception as e:
                    st.error(f"Failed to read the uploaded file: {e}")
                    return


                required_columns = [
                    'Visit Reason', 'Name', 'Date of Birth', 'Age - calculate from DOB', 'Sex',
                    'Aadhar No.', 'Identification Marks', 'Blood Group', 'Height in cm', 'weight in Kg',
                    'Name of Contractor', 'Temp Emp No.', 'Date of Joining', 'Designation', 'Department (Latest & previous)',
                    'Nature of Job (Latest & previous)', 'Phone (Personal)', 'Mail Id (Personal)', 'Emergency Contact person ',
                    'Emergency Contact Relation', 'Emergency Contact phone', 'Address', 'Date for Appointment'
                ]

                missing_columns = [col for col in required_columns if col not in df.columns]
                if missing_columns:
                    st.error(f"The following required columns are missing: {', '.join(missing_columns)}")
                    return


                st.write("### Data Preview")
                st.dataframe(df.head(10))


                if st.button("Submit"):
                    st.success("Data Submitted Successfully!")
                    df.fillna("null", inplace=True)  

                data = df.to_dict(orient='records')

                cursor = connection.cursor()
                add_patient = """
                    INSERT INTO appointments (appoint_date, visit_reason, emp_name, dob, age, gender, aadharno,
                    identify_marks, blood_group, height, weight, contractor_name, temp_emp_no, date_of_joining,
                    designation, department, nature_of_job, phone_no, mail_id, emer_con_per, emer_con_rel, emer_con_phone, address)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                for i in data:
                    try:
                    
                        appoint_date = pd.to_datetime(i['Date for Appointment'], errors='coerce').strftime('%Y-%m-%d') if pd.notnull(i['Date for Appointment']) else None
                        dob = pd.to_datetime(i['Date of Birth'], errors='coerce').strftime('%Y-%m-%d') if pd.notnull(i['Date of Birth']) else None
                        doj = pd.to_datetime(i['Date of Joining'], errors='coerce').strftime('%Y-%m-%d') if pd.notnull(i['Date of Joining']) else None

                        
                        patient_data = (
                            appoint_date, i['Visit Reason'], i['Name'], dob, i['Age - calculate from DOB'], i['Sex'],
                            i['Aadhar No.'], i['Identification Marks'], i['Blood Group'], i['Height in cm'],
                            i['weight in Kg'], i['Name of Contractor'], i['Temp Emp No.'], doj, i['Designation'],
                            i['Department (Latest & previous)'], i['Nature of Job (Latest & previous)'],
                            i['Phone (Personal)'], i['Mail Id (Personal)'], i['Emergency Contact person '],
                            i['Emergency Contact Relation'], i['Emergency Contact phone'], i['Address']
                        )

                    
                        cursor.execute(add_patient, patient_data)
                    except Exception as e:
                        st.error(f"Failed to insert data for {i['Name']}: {e}")
                        continue

                # Commit and close cursor
                connection.commit()
                cursor.close()
                st.success("All data inserted successfully.")
    