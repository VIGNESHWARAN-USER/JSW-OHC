from altair import value
import streamlit as st
import os
import pandas as pd
from streamlit_modal import Modal
from streamlit_option_menu import option_menu


if 'edit' not in st.session_state:
    st.session_state.edit = False
if 'button_label' not in st.session_state:
    st.session_state.button_label = "Edit"
def show_data(emp):
    # MARK: Show Data
    for i in range(len(emp)):
        with st.container(border=1):
            r1c1,r1c3 = st.columns([7,3])
            if len(emp):
                with r1c1:
                    st.html(f"""
                            <style>
                                button[kind="primary"]{{
                                    all: unset;
                                    background-color: #22384F;
                                    color: white;
                                    border-radius: 50px;
                                    text-align: center;
                                    cursor: pointer;
                                    font-size: 20px;
                                    width: 65%;
                                    padding: 10px ;
                                }}
                                .cnt{{
                                    width: 100%;
                                    margin-left:20px;
                                    display: flex;
                                    align-items: center;
                                
                                }}
                                .cnt img{{
                                    width: 50px;
                                    height: 50px;
                                    border-radius: 50px;
                                    
                                }}
                                .cnt div{{
                                    margin-top: 14px;
                                    margin-left: 20px;
                                    display: flex;
                                    justify-content: center;
                                    align-items: center;                                
                                    color: #333;
                                }}
                            </style>
                            <div class="cnt">
                                <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="width:50px; border-radius:50px">
                                <b style="margin: 20px;" >{emp[i]["emp_no"]}</b>
                                <b style="margin: 20px;" >{emp[i]["name"]}</b>
                            </div>
                        """)
                with r1c3:
                    st.html("""
                        <div style="width:50px;height:3px display:flex; alignItems: center"></div>
                            """)
                    if st.button("View",key=i,type="primary"):
                        st.session_state.open_modal = True
                        st.session_state.usr_prof = emp[i]
                        st.rerun()

def fetch_vaccination_details(emp_no, vaccination_type):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT id AS `S no.`, 
               vaccination_type AS `Disease`, 
               normal_doses AS `Dose`, 
               booster_doses AS `Booster`
        FROM vaccination_details
        WHERE emp_no = %s AND vaccination_type = %s
    """
    cursor.execute(query, (emp_no, vaccination_type))
    results = cursor.fetchall()
    conn.close()
    return results

def set_data(emp):
    st.session_state.data = emp.to_dict('records')

def Search(cursor):
    modal = Modal(
        "Employee Profile",
        key="modal",
    )
    if "usr_prof" not in st.session_state:
        st.session_state.usr_prof = {}
    if "searchinp" not in st.session_state:
        st.session_state.searchinp = ""
    if "data" not in st.session_state:
        st.session_state.data = {}
    if "open_modal" not in st.session_state:
        st.session_state.open_modal = False
    
    if st.session_state.open_modal == False:
        st.title("Employee Profile")
        search1, search2,search3 = st.columns([7,1,3])
        with search1:
            search_val = st.text_input("Search by employee ID",placeholder="Search by Patient ID")
        with search2:
            st.write("<div><br></div>", unsafe_allow_html=True)
            if st.button("Search", type="primary"):
                st.session_state.searchinp = search_val
                cursor.execute(f"SELECT * FROM Employee_det WHERE emp_no like '%{st.session_state.searchinp}%' ")
                emp = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                if emp.empty:
                    st.error("No records found")
                else:
                    set_data(emp)

        r0c1,r0c2 = st.columns([7,3])
        with r0c1:
            show_data(st.session_state.data)


    else:
        # MARK: Modal
        st.title("Employee Profile")
        r0c1, r0c2 = st.columns([8,2], vertical_alignment='center')
        with r0c1:
            with st.container(border=1):
                r1c1, r1c2, r1c3 = st.columns([2,3,4])
                cursor.execute(f"SELECT * FROM vitals WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                vitals = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                cursor.execute(f"SELECT * FROM consultation WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                consultation = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                
                cursor.execute(f"SELECT * FROM x_ray WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                xray = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                cursor.execute(f"SELECT * FROM womens_pack WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                womens = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                
            with r1c1:
                st.image('./src/assets/Male User.png', width=160)
            with r1c2:
                st.write(f"Name: {st.session_state.usr_prof['name']}")
                st.write(f"Employee ID: {st.session_state.usr_prof['emp_no']}")
                st.write(f"Aadhar No: {st.session_state.usr_prof['aadhar_no']}")
            with r1c3:
                st.write(f"Blood Grp: {st.session_state.usr_prof['blood_group']}")
                st.write(f"Department: {st.session_state.usr_prof['department']}")
                st.write(f"Phone No: {st.session_state.usr_prof['office_phone_no'][1:]}")
        with r0c2:
            st.html(f"""
                        <style>
                            button[kind="primary"]{{
                                all: unset;
                                background-color: #22384F;
                                color: white;
                                border-radius: 10px;
                                text-align: center;
                                cursor: pointer;
                                font-size: 20px;
                                width: 65%;
                                padding: 10px ;
                            }}
                        </style>
                        
                    """)
            st.button("Active",key=1,type="primary")
        with st.container(border=1):
            menu = option_menu(
                    None,
                    ["Details","Vitals", "Medical/Surgical History", "Visit Reason", "Vaccinations"],
                    key="menu",
                    orientation="horizontal",
                    icons=['a','b','c', 'a','b','c','a','b','c']
                )
            if menu == "Details":
                st.markdown("### Personal Details : ")
                r0c1,r0c2,r0c3 = st.columns([10,1,10])
                with r0c1:
                # MARK: Personal Details
                    # st.markdown(f"""
                    #     *Age*: {st.text_input( label = "Age", label_visibility='collapsed', value = st.session_state.usr_prof.get('age', 'N/A'))}<br>
                    #     *DOB*: {st.session_state.usr_prof.get('dob', 'N/A')}<br>
                    #     *Sex*: {st.session_state.usr_prof.get('gender', 'N/A')}<br>
                    #     *Aadhar No*: {st.session_state.usr_prof.get('aadhar_no', 'N/A')}
                    # """, unsafe_allow_html=True)
                    rr0c1, rr0c2 = st.columns(2)
                    with rr0c1:
                        st.write('Age :')
                        st.write('\n')
                        st.write('DOB :')
                        st.write('\n')
                        st.write("Sex :")
                        st.write('\n')
                        st.write("Aadhar No:")
                    with rr0c2:
                        st.text_input(label = "age", label_visibility='collapsed', value=st.session_state.usr_prof.get('age', 'N/A'))
                        st.text_input(label = "dob", label_visibility='collapsed', value=st.session_state.usr_prof.get('dob', 'N/A'))
                        st.text_input(label = "sex", label_visibility='collapsed', value=st.session_state.usr_prof.get('gender', 'N/A'))
                        st.text_input(label = "adno", label_visibility='collapsed', value=st.session_state.usr_prof.get('aadhar_no', 'N/A'))

                with r0c3:
                    # st.write(f"*Mail ID (Personal)*: {st.session_state.usr_prof['personal_mail']}")
                    # st.write("*Identification Mark*:")
                    # st.markdown(f" * {st.session_state.usr_prof['identification_mark']}")
                    rr0c1, rr0c2 = st.columns(2)
                    with rr0c1:
                        st.write('Mail ID :')
                        st.write('\n')
                        st.write('Identification Mark :')
                        st.write('\n')
                        st.write('\n')
                        st.write('Marital Status :')
                    with rr0c2:
                        st.text_input(label = "age", label_visibility='collapsed', value=st.session_state.usr_prof.get('personal_mail', 'N/A'))
                        st.text_input(label = "dob", label_visibility='collapsed', value=st.session_state.usr_prof.get('identification_mark', 'N/A'))
                        st.selectbox("",options=["Single","Married","Seperated","Divorced","Widowed"])

                        
                st.write("\n")
                st.write("\n")
                st.write("\n")
                st.write("\n")

                st.markdown("### Employment Details : ")
                r0c1,r0c2,r0c3 = st.columns([10,1,10])
                with r0c1:
                # MARK: Personal Details
                    # st.markdown(f"""
                    #     *Employee No*: {st.session_state.usr_prof.get('emp_no', 'N/A')}<br>
                    #     *Designation*: {st.session_state.usr_prof.get('designation', 'N/A')}<br>
                    #     *Department H/O*: {st.session_state.usr_prof.get('department', 'N/A')}
                    # """, unsafe_allow_html=True)
                    rr0c1, rr0c2 = st.columns(2)
                    with rr0c1:
                        st.write('\n')
                        st.write('\n')
                        st.write('Employer :')
                        st.write('\n')
                        st.write('Designation :')
                        st.write('\n')
                        st.write("Department H/O :")
                    with rr0c2:
                        st.selectbox("",options=["JSW steel","JSW cement","JSW foundation"])
                        st.text_input(label = "des", label_visibility='collapsed', value=st.session_state.usr_prof.get('designation', 'N/A'))
                        st.text_input(label = "dept", label_visibility='collapsed', value=st.session_state.usr_prof.get('department', 'N/A'))
                                                # Define the data for the employment history
                        employment_history = [
                            {"date": "2022-01-15", "department": "Department A"},
                            {"date": "2023-03-22", "department": "Department B"},
                            {"date": "2024-07-10", "department": "Department C"}
                        ]

                        # Add the View More button
                        if st.button("View More", key="view_more_dept"):
                            st.subheader("Employment History - Department H/O")
                            
                            # Display the history in a table format
                            for record in employment_history:
                                st.markdown(f"**Date:** {record['date']}")
                                st.markdown(f"**Department:** {record['department']}")
                                st.markdown("---")  # Separator for clarity


                print("       ")
                with r0c3:
                    # st.write(f"*Mail ID (Office)*: {st.session_state.usr_prof['office_mail']}")
                    # st.write(f"*Nature of Job H/O*:{st.session_state.usr_prof['nature_of_job']}")
                    # st.write(f"*Employer*:{st.session_state.usr_prof['personal_mail']}")
                    # st.write(f"*Contractor*:{st.session_state.usr_prof['personal_mail']}")
                    rr0c1, rr0c2 = st.columns(2)
                    with rr0c1:
                        st.write('\n')
                        st.write('\n')
                        st.write('Mode of Joining :')
                        st.write('\n')
                        st.write('Nature of Jo H/O :')
                        st.write('\n')
                        st.write('\n')
                        st.write('\n')
                        st.write('\n')
                        st.write("Date of Joining :")
                        
    
                    with rr0c2:
                        # Define the options for the selectbox
                        employee_status = st.selectbox("",
                            options=["New Joinee", "Transfer in from other JSW sites"]
                        )

                        # Conditional display based on the selected option
                        if employee_status == "Transfer in from other JSW sites":
                            # Show a text area with a placeholder
                            st.text_area(
                                label="Transfer Details",
                                placeholder="e.g., JSW Power Dolvi (mention site details)",
                                key="transfer_details"
                            )

                        st.text_input(label = "job", label_visibility='collapsed', value=st.session_state.usr_prof.get('nature_of_job', 'N/A'))
                        if st.button("View More", key="view_more_dept1"):
                            st.write("Additional information for Department H/O...")
                        st.text_input(label = "mep", label_visibility='collapsed', value=st.session_state.usr_prof.get('employer', 'N/A'))
                          
                st.write("\n")
                st.write("\n")
                st.write("\n")
                st.write("\n")

                st.markdown("### Contact Details : ")
                r0c1,r0c2,r0c3 = st.columns([10,1,10])  # Define two main columns with specific width ratio
                with r0c1:
                    # MARK: Personal Details
                    rr0c1, rr0c2 = st.columns(2)  # Define sub-columns for Employee details
                    with rr0c1:
                        st.write('Phone (Personal) :')
                        st.write('\n')
                        st.write('Phone (Office) :')
                        st.write('\n')
                        st.write('Mail ID (Personal) :')
                        st.write('\n')
                        st.write('Mail ID (Office) :')
                        st.write('\n')
                        st.write('Emergency Contact person (Name) :')
                        
                    with rr0c2:
                        # Use unique keys for each input field to avoid duplication
                        st.text_input(label="eno", label_visibility='collapsed', value=st.session_state.usr_prof.get('personal_phone_no', 'N/A'), key="eno_key")
                        st.text_input(label="des", label_visibility='collapsed', value=st.session_state.usr_prof.get('office_phone_no', 'N/A'), key="des_key")
                        st.text_input(label="permail", label_visibility='collapsed', value=st.session_state.usr_prof.get('personal_mail', 'N/A'), key="permail_key")
                        st.text_input(label="offmail", label_visibility='collapsed', value=st.session_state.usr_prof.get('office_mail', 'N/A'), key="offmail_key")
                        st.text_input(label="emgper", label_visibility='collapsed', value=st.session_state.usr_prof.get('emg_con_person', 'N/A'), key="emgper_key")
                        

                with r0c3:
                    # MARK: Contact Details
                    rr0c1, rr0c2 = st.columns(2)  # Define sub-columns for the contact details
                    with rr0c1:
                        st.write('Emergency Contact Relationship :')
                        st.write('\n')
                        st.write('Emergency Contact phone :')
                        st.write('\n')
                        st.write('Mail ID (Emergency Contact phone) :')
                        st.write('\n')
                        st.write("Address :")
                    
                    with rr0c2:
                        # Use unique keys for each input field to avoid duplication
                        st.text_input(label="mail", label_visibility='collapsed', value=st.session_state.usr_prof.get('office_mail', 'N/A'), key="mail_key")
                        st.text_input(label="job", label_visibility='collapsed', value=st.session_state.usr_prof.get('nature_of_job', 'N/A'), key="job_key")
                        st.text_input(label="mailid", label_visibility='collapsed', value=st.session_state.usr_prof.get('personal_mail', 'N/A'), key="mailid_key")
                        st.selectbox("",options=["Permanent","Residence"])

                st.write("\n")
                st.write("\n")
                st.write("\n")
                st.write("\n")


                st.markdown("### Employment Status : ")
                r0c1,r0c2,r0c3 = st.columns([10,1,10])
                with r0c1:
                # MARK: Personal Details
                    # st.markdown(f"""
                    #     *Age*: {st.text_input( label = "Age", label_visibility='collapsed', value = st.session_state.usr_prof.get('age', 'N/A'))}<br>
                    #     *DOB*: {st.session_state.usr_prof.get('dob', 'N/A')}<br>
                    #     *Sex*: {st.session_state.usr_prof.get('gender', 'N/A')}<br>
                    #     *Aadhar No*: {st.session_state.usr_prof.get('aadhar_no', 'N/A')}
                    # """, unsafe_allow_html=True)
                    rr0c1, rr0c2 = st.columns(2)
                    with rr0c1:
                        st.write('Active From :')
                        st.write('\n')
                        st.write('Transferred to dolvi on:')
                        st.write('\n')
                        st.write("Resined on :")
                        st.write('\n')
                        st.write("Retired on:")
                    with rr0c2:
                        st.text_input(label = "activeform", label_visibility='collapsed', value=st.session_state.usr_prof.get('active_form', 'N/A'))
                        st.text_input(label = "trn", label_visibility='collapsed', value=st.session_state.usr_prof.get('transferred_to_dolvi_on', 'N/A'))
                        st.text_input(label = "res", label_visibility='collapsed', value=st.session_state.usr_prof.get('resined_on', 'N/A'))
                        st.text_input(label = "ret", label_visibility='collapsed', value=st.session_state.usr_prof.get('retired_on', 'N/A'))

                with r0c3:
                    # st.write(f"*Mail ID (Personal)*: {st.session_state.usr_prof['personal_mail']}")
                    # st.write("*Identification Mark*:")
                    # st.markdown(f" * {st.session_state.usr_prof['identification_mark']}")
                    rr0c1, rr0c2 = st.columns(2)
                    with rr0c1:
                        st.write('Deceased on :')
                        st.write('\n')
                        st.write('Unauthorized Absence from  :')
                        st.write('\n')
                        st.write('Others (Specify) on :')
                    with rr0c2:
                        st.text_input(label = "dec", label_visibility='collapsed', value=st.session_state.usr_prof.get('deceased_on', 'N/A'))
                        st.text_input(label = "uaf", label_visibility='collapsed', value=st.session_state.usr_prof.get('unauthorized_absence_from', 'N/A'))
                        st.text_input(label = "oth", label_visibility='collapsed', value=st.session_state.usr_prof.get('others_on', 'N/A'))

            if menu == "Medical/Surgical History":
                # Personal History Section (Smoker, Alcoholic, Diet)
                st.subheader("Personal History")
                col1, col2 = st.columns(2)
                
                with col1:
                    # Fetching and displaying Smoker status
                    smoker = st.radio("Smoker", options=["Yes", "No"], index=0 if st.session_state.usr_prof.get('personal_history', {}).get('smoker', 'No') == "Yes" else 1)
                    
                    # Fetching and displaying Alcoholic status
                    alcoholic = st.radio("Alcoholic", options=["Yes", "No"], index=0 if st.session_state.usr_prof.get('personal_history', {}).get('alcoholic', 'No') == "Yes" else 1)
                
                with col2:
                    # Fetching and displaying Diet preference
                    diet = st.radio("Diet", options=["Veg", "Non-Veg", "Mixed"], index=["Veg", "Non-Veg", "Mixed"].index(st.session_state.usr_prof.get('personal_history', {}).get('diet', 'Mixed')))

                # Medical History Section (HTN, DM, Epileptic, Thyroid, Rheumatoid, Others)
                st.subheader("Medical History")
                col1, col2 = st.columns(2)

                with col1:
                    # Fetching and displaying checkboxes for medical conditions
                    htn = st.checkbox("HTN (Hypertension)", value=st.session_state.usr_prof.get('usr_prof', {}).get('htn', False))
                    dm = st.checkbox("DM (Diabetes)", value=st.session_state.usr_prof.get('usr_prof', {}).get('dm', False))
                    epileptic = st.checkbox("Epileptic", value=st.session_state.usr_prof.get('usr_prof', {}).get('epileptic', False))

                with col2:
                    thyroid = st.checkbox("Thyroid", value=st.session_state.usr_prof.get('usr_prof', {}).get('thyroid', False))
                    rheumatoid = st.checkbox("Rheumatoid", value=st.session_state.usr_prof.get('usr_prof', {}).get('rheumatoid', False))
                    others = st.text_area("Other Medical Conditions (Comments)", value=st.session_state.usr_prof.get('usr_prof', {}).get('others', ''))

                # Surgical History Section (Not-null options)
                st.subheader("Surgical History")
                surgical_history = st.text_input("Surgical History Details (Not null)", placeholder="Enter surgical history...", value=st.session_state.usr_prof.get('surgical_history', ''))

                # Allergy History Section (Drug, Food, Others)
                st.subheader("Allergy History")
                col1, col2 = st.columns(2)

                with col1:
                    drug_allergy = st.text_area("Drug Allergy (Comments)", value=st.session_state.usr_prof.get('allergy_history', {}).get('drug', ''))
                    food_allergy = st.text_area("Food Allergy (Comments)", value=st.session_state.usr_prof.get('allergy_history', {}).get('food', ''))

                with col2:
                    other_allergy = st.text_area("Other Allergies (Comments)", value=st.session_state.usr_prof.get('allergy_history', {}).get('others', ''))

                # Family History Section (Father, Mother)
                st.subheader("Family History")
                father_col, mother_col = st.columns(2)

                with father_col:
                    st.write("*Father's Medical History*")
                    father_smoker = st.radio("Father Smoker", options=["Yes", "No"], index=0 if st.session_state.usr_prof.get('family_history', {}).get('father', {}).get('smoker', 'No') == "Yes" else 1)
                    father_htn = st.checkbox("Father - HTN", value=st.session_state.usr_prof.get('family_history', {}).get('father', {}).get('htn', False))
                    father_dm = st.checkbox("Father - DM", value=st.session_state.usr_prof.get('family_history', {}).get('father', {}).get('dm', False))

                with mother_col:
                    st.write("*Mother's Medical History*")
                    mother_smoker = st.radio("Mother Smoker", options=["Yes", "No"], index=0 if st.session_state.usr_prof.get('family_history', {}).get('mother', {}).get('smoker', 'No') == "Yes" else 1)
                    mother_htn = st.checkbox("Mother - HTN", value=st.session_state.usr_prof.get('family_history', {}).get('mother', {}).get('htn', False))
                    mother_dm = st.checkbox("Mother - DM", value=st.session_state.usr_prof.get('family_history', {}).get('mother', {}).get('dm', False))
            
            if menu == "Vitals":
                r0c1,r0c2 = st.columns([5,6])
                with r0c1:
                # # MARK: Personal Details
                #     st.markdown(f"""
                #         <b>Blood Pressure</b><br/>
                #         *Systolic*: {vitals['Systolic'][0]}<br>
                #         *Diastolic*: {vitals['Diastolic'][0]}<br>
                #         *Pulse Rate*: {vitals['PulseRate'][0]}<br>
                #         *SPO2*: {vitals['SpO2'][0]}
                #         *Respiratory Rate*: {vitals['RespiratoryRate'][0]}
                #     """, unsafe_allow_html=True)
                    rr0c1, rr0c2 = st.columns(2)
                    with rr0c1:
                        st.write('Blood Pressure :')
                        st.write('\n')
                        st.write('Systolic :')
                        st.write('\n')
                        st.write("Diastolic :")
                        st.write('\n')
                        st.write("Pulse Rate :")
                        st.write('\n')
                        st.write("Respiratory Rate :")
                    with rr0c2:
                        st.text_input(label = "BMI1", label_visibility='collapsed' ,value=vitals['Systolic'][0])
                        st.text_input(label = "Height1", label_visibility='collapsed', value=vitals['Diastolic'][0])
                        st.text_input(label = "Temperature1", label_visibility='collapsed', value=vitals['PulseRate'][0])
                        st.text_input(label = "Weight1", label_visibility='collapsed', value=vitals['SpO2'][0])
                        st.text_input(label = "Weight1", label_visibility='collapsed', value=vitals['RespiratoryRate'][0])
                    
                with r0c2:
                # # MARK: Personal Details
                #     st.markdown(f"""
                #         <b>Blood Pressure</b><br/>
                #         *Systolic*: {vitals['Systolic'][0]}<br>
                #         *Diastolic*: {vitals['Diastolic'][0]}<br>
                #         *Pulse Rate*: {vitals['PulseRate'][0]}<br>
                #         *SPO2*: {vitals['SpO2'][0]}
                #         *Respiratory Rate*: {vitals['RespiratoryRate'][0]}
                #     """, unsafe_allow_html=True)
                    rr0c1, rr0c2 = st.columns(2)
                    with rr0c1:
                        st.write('BMI :')
                        st.write('\n')
                        st.write('Height :')
                        st.write('\n')
                        st.write("Temperature :")
                        st.write('\n')
                        st.write("Weight :")
                    with rr0c2:
                        st.text_input(label = "BMI", label_visibility='collapsed' ,value=vitals['BMI'][0])
                        st.text_input(label = "Height", label_visibility='collapsed', value=vitals['Height'][0])
                        st.text_input(label = "Temperature", label_visibility='collapsed', value=vitals['Temperature'][0])
                        st.text_input(label = "Weight", label_visibility='collapsed', value=vitals['Weight'][0])
                # with r0c2:
                #     st.write(f"*BMI (in Value)*: {vitals['BMI'][0]}")
                #     st.write(f"*Height*: {vitals['Height'][0]}")
                #     st.write(f"*Temperature*: {vitals['Temperature'][0]}")
                #     st.write(f"*Weight*: {vitals['Weight'][0]}")
            if menu == "Visit Reason":
                r0c1,r0c2 = st.columns([3,6])
                with r0c1:
                # MARK: Personal Details
                    st.write("*Select the Year*")
                    st.date_input('Date', label_visibility='collapsed')
                    st.write("*Select the Reason*")
                    menu1 = option_menu(
                    None,
                    menu_icon='./src/assets/Folder.png',
                    options=["Pre Employment", "Pre Placement","Annual/Periodical","Camps", "Fitness After Medical Leave", "Illness", "Injury", "Followup Visit", "Special Work Fitness"],
                    key="menu1",
                    icons=['a','b','c', 'a','b','c','a','b','c']
                    )
                with r0c2:
                    if menu1 == "Camps":
                        menu2 = option_menu(
                        None,
                        menu_icon='./src/assets/Folder.png',
                        options=["Mandatory Camps", "Optional Camps"],
                        key="menu2",
                        orientation='horizontal',
                        icons=['a','b']
                        )
                        r3c1, r3c2, r3c3, r3c4, r3c5 = st.columns([2,2,2,2,2])
                        with r3c1:
                            st.markdown("<b style = 'color: #22384F'>Hospital Name</b>", unsafe_allow_html=True)
                        with r3c2:
                            st.markdown("<b style = 'color: #22384F'>Purpose</b>", unsafe_allow_html=True)
                        with r3c3:
                            st.markdown("<b style = 'color: #22384F'>Doctor</b>", unsafe_allow_html=True)
                        with r3c4:
                            st.markdown("<b style = 'color: #22384F'>Visited Date</b>", unsafe_allow_html=True)
                        with r3c5:
                            st.markdown("<b style = 'color: #22384F'>Details</b>", unsafe_allow_html=True)
                    else:
                        r3c1, r3c2, r3c3, r3c4, r3c5 = st.columns([2,2,2,2,2])
                        with r3c1:
                            st.markdown("<b style = 'color: #22384F'>Hospital Name</b>", unsafe_allow_html=True)
                        with r3c2:
                            st.markdown("<b style = 'color: #22384F'>Purpose</b>", unsafe_allow_html=True)
                        with r3c3:
                            st.markdown("<b style = 'color: #22384F'>Doctor</b>", unsafe_allow_html=True)
                        with r3c4:
                            st.markdown("<b style = 'color: #22384F'>Visited Date</b>", unsafe_allow_html=True)
                        with r3c5:
                            st.markdown("<b style = 'color: #22384F'>Details</b>", unsafe_allow_html=True)
            if menu == "Vaccinations":
                r0c1, r0c2 = st.columns([4, 8])
                with r0c1:
                    st.subheader("Vaccination Information")
                    vaccine = st.selectbox(
                        'Select Vaccine',
                        ['Select', 'Vaccine 1', 'Vaccine 2', 'Vaccine 3']  # Replace with actual vaccine names
                    )
                    
                with r0c2:
                    # Columns for displaying Normal Doses & Booster Dose
                    r3c1, r3c2 = st.columns([6, 6])

                    with r3c1:
                        st.markdown("<b style='color: #22384F'>Normal Doses</b>", unsafe_allow_html=True)
                        # Create 5 rows for Normal Doses
                        for i in range(1, 6):
                            st.write(f"Dose {i}: [Date]")  # Replace with actual dose details

                    with r3c2:
                        st.markdown("<b style='color: #22384F'>Booster Dose</b>", unsafe_allow_html=True)
                        # Create 5 rows for Booster Doses
                        for i in range(1, 6):
                            st.write(f"Booster {i}: [Date]")  # Replace with actual booster dose details



    if st.button("close"):
        st.session_state.open_modal = False
        st.rerun()