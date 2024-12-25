from altair import value
import streamlit as st
import os
import pandas as pd
from streamlit_modal import Modal
from streamlit_option_menu import option_menu
def systolic_diastolic_chart(systolic, diastolic):
    systolic = int(systolic)
    diastolic = int(diastolic)
    if systolic ==0 or diastolic ==0:
        return ["0", "black"]
    elif systolic < 90 or diastolic < 60:
        return ["Hypotension", "00ff00"]
    elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
        return ["Normal", "green"]
    elif 120 < systolic <= 129 and 60 <= diastolic <= 80:
        return ["Elevated", "yellow"]
    elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
        return ["HT Stage 1", "orange"]
    elif 140 <= systolic <= 180 or 90 <= diastolic <= 120:
        return ["HT Stage 2", "red"]
    elif systolic > 180 or diastolic > 120:
        return ["HT Crisis", "#990000"]
    else:
        return "Invalid input"

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
                st.subheader("Basic Details")
        
                r1c1, r1c2, r1c3 = st.columns(3)

                with r1c1:
                    st.text_input("Name", value=st.session_state.usr_prof.get("Name", ""), placeholder="Enter your full name")
                    st.text_input("Sex", value=st.session_state.usr_prof.get("gender", ""))
                    id_marks = st.text_input("Identification Marks", value=st.session_state.usr_prof.get("Identification Marks", ""), placeholder="Enter any visible identification marks")
                with r1c2:
                    st.text_input(
                        "Date of Birth (dd/mm/yyyy)", 
                        value=st.session_state.usr_prof.get("Date of Birth", ""),
                        placeholder="Enter Date of Birth in dd/mm/yyyy"
                    )
                    st.text_input("Aadhar No.", value=st.session_state.usr_prof.get("Aadhar No.", ""), placeholder="Enter 12-digit Aadhar No.")
                    st.selectbox("Marital status",["Single","Married","Divorced", "Widowed", "Seperated"],placeholder="Select marital status")
                with r1c3:
                    st.text_input("Age", value=st.session_state.usr_prof.get("age", ""),placeholder="XX Years YY Months ZZ Days")
                    st.text_input("Blood Group", value=st.session_state.usr_prof.get("Blood Group", ""), placeholder="e.g., A+, O-")
                    
                st.subheader("Employment Details")
                r2c1, r2c2, r2c3 = st.columns(3)

                with r2c1:
                    st.text_input("Employee Number", value=st.session_state.usr_prof.get("emp_no", ""))
                    st.text_input("Designation", value=st.session_state.usr_prof.get("Designation", ""), placeholder="Enter job designation")
                    st.text_input("Nature of Job", value=st.session_state.usr_prof.get("Nature of Job", ""), placeholder="e.g., Height Works, Fire Works")
                with r2c2:
                    st.selectbox("Employer",["JSW steel" , "JSW Cement", "JSW foundation"])
                    st.text_input("Department", value=st.session_state.usr_prof.get("Department", ""), placeholder="Enter department")
                    st.date_input("Date of Joining")
                with r2c3:
                    mode = st.text_input("Mode of Joining",value=st.session_state.usr_prof.get("Nature of Job", ""))
                    if mode == "Transfer from other JSW site":
                        jswsite = st.text_input("Old JSW site name", placeholder="Enter old JSW site name")

                st.subheader("Contact Details")
                row1, row2, row3 = st.columns(3)

                with row1:
                    st.text_input("Phone (Personal)", value=st.session_state.usr_prof.get("Phone (Personal)", ""), placeholder="Enter 10-digit phone number")
                    st.text_input("Phone (Office)", value=st.session_state.usr_prof.get("Phone (Office)", ""), placeholder="Enter office phone number")
                    st.text_input("Mail Id (Emergency Contact Person)", value=st.session_state.usr_prof.get("Mail Id(emg)", ""), placeholder="Enter email")
                with row2:
                    st.text_input("Mail Id (Personal)", value=st.session_state.usr_prof.get("Mail Id (Personal)", ""), placeholder="Enter personal email")
                    st.text_input("Mail Id (Office)", value=st.session_state.usr_prof.get("Mail Id (Office)", ""), placeholder="Enter office email")
                    st.text_input("Emergency Contact Phone", value=st.session_state.usr_prof.get("Emergency Contact Phone", ""), placeholder="Enter 10-digit phone number")
                with row3:
                    st.text_input("Emergency Contact Person", value=st.session_state.usr_prof.get("Emergency Contact Person", ""), placeholder="Enter emergency contact person's name")
                    st.text_input("Emergency Contact Relation", value=st.session_state.usr_prof.get("Emergency Contact Relation", ""), placeholder="e.g., Father, Spouse")
                    st.text_area("Address", value=st.session_state.usr_prof.get("Address", ""), placeholder="Enter full address")

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
                st.header("Vitals")
                r1c1,r1c2,r1c3 = st.columns([5,3,9])
                with r1c1:
                    systolic = st.session_state.usr_prof.get("Systolic", "")
                    diastolic = st.session_state.usr_prof.get("Diastolic", "")
                    st.write("Blood Pressure")
                    st.session_state.usr_prof["Systolic"] = st.text_input(
                        "Systolic (mm Hg)", 
                        value=systolic, 
                        placeholder="Enter Systolic Pressure",
                        key="systolic"
                    )
                    st.session_state.usr_prof["Diastolic"] = st.text_input(
                        "Diastolic (mm Hg)", 
                        value=diastolic, 
                        placeholder="Enter Diastolic Pressure",
                        key="diastolic"
                    )

                with r1c2:
                    # show the charts for the systolic and diastolic based on the data input
                    st.write("""
                        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; width: 300px; height: 50px; border-radius: 10px; margin-left: 50px;"></div>
                    """, unsafe_allow_html=True)
                    st.write("""
                    <style>
                        button[kind="secondary"]{
                            all: unset;
                            background-color: #22384F;
                            color: white;
                            border-radius: 5px;
                            text-align: center;
                            cursor: pointer;
                            font-size: 20px;
                            padding: 10px;
                            
                        }
                    </style>
                    """,unsafe_allow_html=True)
                    val = st.button("🧮", type="secondary")
                with r1c3:
                    if val:
                        val,color = systolic_diastolic_chart(systolic, diastolic)
                        st.write(f"""
                            <style>
                                .chart_container {{
                                    display: flex;
                                    flex-direction: column;
                                    align-items: center;
                                    justify-content: center;
                                    width: 300px;
                                    height: 80px;
                                    border-radius: 10px;
                                    margin-left: 50px;
                                }}
                                .chart-value h1{{
                                    margin-top: 50px;
                                    margin-left: 50px;
                                    color: {color}
                                }}
                                .bar-values {{
                                    display: flex;
                                    align-items: center;
                                    justify-content: space-between;
                                    width: 300px;
                                    height: 200px;
                                }}
                                .Normal {{
                                    width: 19.5%;
                                    height: 10px;
                                    background-color: #00ff00af;
                                    border-top-left-radius: 10px;
                                    border-bottom-left-radius: 10px;
                                }}
                                .Elevated {{
                                    width: 19.5%;
                                    height: 10px;
                                    background-color: #ffff00af;
                                }}
                                .HT-Stage-1 {{
                                    width: 19.5%;
                                    height: 10px;
                                    background-color: #ff9900af;
                                }}
                                .HT-Stage-2 {{
                                    width: 19.5%;
                                    height: 10px;
                                    background-color: #ff0000af;
                                }}
                                .HT-crisis {{
                                    width: 19.5%;
                                    height: 10px;
                                    background-color: #990000af;
                                    border-top-right-radius: 10px;
                                    border-bottom-right-radius: 10px;
                                }}
                            </style>
                            <div class="chart_container">
                                <div class="chart-value"><h1>{val}</h1></div>
                                <div class="bar-values">
                                    <div class="Normal"></div>
                                    <div class="Elevated"></div>
                                    <div class="HT-Stage-1"></div>
                                    <div class="HT-Stage-2"></div>
                                    <div class="HT-crisis"></div>
                                </div>
                            </div>
                        """,unsafe_allow_html=True)
                
                r2c1, r2c2, r2c3 = st.columns(3)
                with r2c1:
                    st.session_state.usr_prof["Pulse"] = st.text_input(
                        "Pulse (Per Minute)", 
                        value=st.session_state.usr_prof.get("Pulse", ""), 
                        placeholder="Enter Pulse Rate",
                        key="pulse"
                    )
                    st.session_state.usr_prof["spo2"] = st.text_input(
                        "SpO2 (in %)", 
                        value=st.session_state.usr_prof.get("spo2", ""), 
                        placeholder="Enter SpO2 Level",
                        key="spo2"
                    )
                    st.session_state.usr_prof["BMI"] = st.text_input(
                        "BMI", 
                        value=st.session_state.usr_prof.get("BMI", ""), 
                        placeholder="Enter BMI",
                        key="bmi"
                    )

                with r2c2:
                    st.session_state.usr_prof["Respiratory Rate"] = st.text_input(
                        "Respiratory Rate (Per Minute)", 
                        value=st.session_state.usr_prof.get("Respiratory Rate", ""), 
                        placeholder="Enter Respiratory Rate",
                        key="respiratory_rate"
                    )
                    st.session_state.usr_prof["Weight"] = st.text_input(
                        "Weight (in KG)", 
                        value=st.session_state.usr_prof.get("Weight", ""), 
                        placeholder="Enter Weight",
                        key="weight"
                    )

                with r2c3:
                    st.session_state.usr_prof["Temperature"] = st.text_input(
                        "Temperature (in °F)", 
                        value=st.session_state.usr_prof.get("Temperature", ""), 
                        placeholder="Enter Body Temperature",
                        key="temperature"
                    )
                    st.session_state.usr_prof["Height"] = st.text_input(
                        "Height (in CM)", 
                        value=st.session_state.usr_prof.get("Height", ""), 
                        placeholder="Enter Height",
                        key="height"
                    )
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