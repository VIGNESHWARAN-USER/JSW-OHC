from altair import Column
from git import Reference
import streamlit as st
import os
import pandas as pd
from  streamlit_option_menu import option_menu
import numpy as np
import json
import datetime
import mysql.connector
from datetime import datetime
import re


def validate_name(name):
    if not re.match("^[A-Za-z ]+$", name):
        st.error("Name should contain only letters and spaces.")
        return False
    return True

def validate_aadhar(aadhar):
    if not re.match("^[0-9]{12}$", aadhar):
        st.error("Aadhar No. must be exactly 12 digits.")
        return False
    return True

def validate_blood_group(blood_group):
    valid_groups = {"A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"}
    if blood_group not in valid_groups:
        st.error("Invalid Blood Group. Choose from A+, A-, B+, B-, O+, O-, AB+, AB-.")
        return False
    return True

def validate_phone(phone):
    if not re.match("^[0-9]{10}$", phone):
        st.error("Phone number must be exactly 10 digits.")
        return False
    return True

def validate_email(email):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        st.error("Invalid email format.")
        return False
    return True

def validate_date_format(date_str):
    """
    Validate if the input matches the dd/mm/yyyy format and is a valid date.
    """
    try:
        return datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        st.error("Invalid date format. Please use dd/mm/yyyy.")
        return None

if "addonInput" not in st.session_state:
    st.session_state.addonInput = None

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


def Form(visitreason,select, select1, connection, cursor,accessLevel):
    st.write("""
        <style>
            div.stButton > button[kind="primary"] {
                all: unset;
                background-color: #22384F;
                color: white;
                border-radius: 5px;
                text-align: center;
                cursor: pointer;
                font-size: 10px;
                width: 25%;
                padding: 5px;
                margin-left: auto;  /* Align the button to the right */
                display: block;
            }
            div.stButton {
                display: flex;
                justify-content: flex-end;  /* Moves button container to the right */
            }
        </style>
    """, unsafe_allow_html=True)
    if select1=="Preventive":
        if visitreason=="Camps (Optional)":
            form_name = option_menu(
            None,
            ["Basic Details", "Vitals","Medical History", "Investigations", "Vaccination"],
            orientation="horizontal",
            icons=['a','a','a','a','a','a']
        )
        elif visitreason=="Special Work Fitness":
            form_name = option_menu(
            None,
            ["Basic Details", "Vitals", "Fitness", "Vaccination"],
            orientation="horizontal",
            icons=['a','a','a','a','a']
        )
        elif visitreason=="Special Work Fitness (Renewal)" or select=="Visitor":
            form_name = option_menu(
            None,
            ["Basic Details", "Vitals","Medical History", "Vaccination","Fitness"],
            orientation="horizontal",
            icons=['a','a','a','a','a','a']
        )
        elif visitreason=="Fitness After Medical Leave":
            form_name = option_menu(
            None,
            ["Basic Details","Vitals","Medical History", "Fitness","Vaccination","Medical Leave/Sickness Absence Ratio"],  #not defined
            orientation="horizontal",
            icons=['a','a','a','a','a','a','a','a']
            )
        elif visitreason=="Mock Drill" or visitreason=="BP Sugar Check":
            form_name= option_menu(
                None,
                ["Basic Details", "Vitals"],
                orientation="horizontal",
                icons=['a','a','a']
            )
        else:
            form_name = option_menu(
                None,
                ["Basic Details", "Vitals","Medical History", "Investigations","Vaccination", "Fitness"],
                orientation="horizontal",
                icons=['a','a','a','a','a','a','a']
            )
    if select1=="Curative":
        if select=="Contractor" and visitreason=="Over counter Injury Outside the premises":
            form_name = option_menu(
            None,
            ["Basic Details","Consultation","Vaccination","Prescription" ],
            orientation="horizontal",
            icons=['a','a','a','a','a','a']
            )
        elif visitreason=="Illness" or visitreason=="BP Sugar (Abnormal)" or visitreason=="Injury Outside the premises" or visitreason=="Over counter Injury Outside the premises":
            form_name = option_menu(
            None,
            ["Basic Details", "Vitals","Medical History","Vaccination","Consultation","Prescription" ],
            orientation="horizontal",
            icons=['a','a','a','a','a','a','a','a','a']
            )
        elif visitreason=="Injury":
            form_name = option_menu(
            None,
            ["Basic Details","Vaccination","Prescription"],
            orientation="horizontal",
            icons=['a','a','a','a']
            )
        elif visitreason=="Over counter Injury":
            form_name = option_menu(
            None,
            ["Basic Details","Vaccination","Consultation","Prescription"],
            orientation="horizontal",
            icons=['a','a','a','a','a','a']
            )
        elif select!="Contractor"and visitreason=="Follow up Visits":
            form_name = option_menu(
            None,
            ["Basic Details","Vitals","Investigations","Consultation","Vaccination","Prescription"],
            orientation="horizontal",
            icons=['a','a','a','a','a','a','a']
            )
        else:
            form_name = option_menu(
            None,
            ["Basic Details", "Vitals","Consultation","Vaccination","Prescription" ],
            orientation="horizontal",
            icons=['a','a','a','a','a','a']
            )


            
    if form_name == "Basic Details":
        st.subheader("Basic Details")
        
        r1c1, r1c2, r1c3 = st.columns(3)

        with r1c1:
            name = st.text_input("Name", value=st.session_state.form_data.get("Name", ""), placeholder="Enter your full name")
            if name and not validate_name(name):
                st.stop()

            dob_input = st.text_input(
                "Date of Birth (dd/mm/yyyy)", 
                value=st.session_state.form_data.get("Date of Birth", ""),
                placeholder="Enter Date of Birth in dd/mm/yyyy"
            )

            if dob_input:
                dob = validate_date_format(dob_input)
                if dob:
                    # Store validated DOB in session state
                    st.session_state.form_data["Date of Birth"] = dob

            sex = st.selectbox("Sex", options=["Male", "Female", "Other"], 
                            index=["Male", "Female", "Other"].index(st.session_state.form_data.get("Sex", "Male")))

            aadhar = st.text_input("Aadhar No.", value=st.session_state.form_data.get("Aadhar No.", ""), placeholder="Enter 12-digit Aadhar No.")
            if aadhar and not validate_aadhar(aadhar):
                st.stop()

            id_marks = st.text_input("Identification Marks", value=st.session_state.form_data.get("Identification Marks", ""), placeholder="Enter any visible identification marks")
            blood_group = st.text_input("Blood Group", value=st.session_state.form_data.get("Blood Group", ""), placeholder="e.g., A+, O-")
            if blood_group and not validate_blood_group(blood_group):
                st.stop()

            
        with r1c2:
            emp_no = st.text_input("Employee No.", value=st.session_state.form_data.get("Employee No.", ""), placeholder="Enter employee number")
            doj = st.text_input(
                "Date of Birth (dd/mm/yyyy)", 
                value=st.session_state.form_data.get("Date of Birth", ""), 
                placeholder="Enter Date of Birth in dd/mm/yyyy",
                key="date_of_birth"
            )

            if doj:
                dob = validate_date_format(doj)
                if dob:
                    # Store validated DOB in session state
                    st.session_state.form_data["Date of Birth"] = dob

            designation = st.text_input("Designation", value=st.session_state.form_data.get("Designation", ""), placeholder="Enter job designation")
            department = st.text_input("Department", value=st.session_state.form_data.get("Department", ""), placeholder="Enter department")
            job_nature = st.text_input("Nature of Job", value=st.session_state.form_data.get("Nature of Job", ""), placeholder="e.g., Height Works, Fire Works")
            personal_phone = st.text_input("Phone (Personal)", value=st.session_state.form_data.get("Phone (Personal)", ""), placeholder="Enter 10-digit phone number")
            if personal_phone and not validate_phone(personal_phone):
                st.stop()

            office_phone = st.text_input("Phone (Office)", value=st.session_state.form_data.get("Phone (Office)", ""), placeholder="Enter office phone number")

        with r1c3:
            personal_email = st.text_input("Mail Id (Personal)", value=st.session_state.form_data.get("Mail Id (Personal)", ""), placeholder="Enter personal email")
            if personal_email and not validate_email(personal_email):
                st.stop()

            office_email = st.text_input("Mail Id (Office)", value=st.session_state.form_data.get("Mail Id (Office)", ""), placeholder="Enter office email")
            if office_email and not validate_email(office_email):
                st.stop()

            emergency_contact_person = st.text_input("Emergency Contact Person", value=st.session_state.form_data.get("Emergency Contact Person", ""), placeholder="Enter emergency contact person's name")
            emergency_contact_relation = st.text_input("Emergency Contact Relation", value=st.session_state.form_data.get("Emergency Contact Relation", ""), placeholder="e.g., Father, Spouse")
            emergency_contact_phone = st.text_input("Emergency Contact Phone", value=st.session_state.form_data.get("Emergency Contact Phone", ""), placeholder="Enter 10-digit phone number")
            if emergency_contact_phone and not validate_phone(emergency_contact_phone):
                st.stop()

            address = st.text_area("Address", value=st.session_state.form_data.get("Address", ""), placeholder="Enter full address")

        r2c1, r2c2, r2c3 = st.columns([5, 2, 3])        
        with r2c3:
            if st.button("Add Data", type="primary"):
                emp_id = st.session_state.form_data['Employee ID']
                sql = """
                INSERT INTO basicdetails (
                    emp_no, PatientName, PatientAge, Gender,
                    MobileNo, Address, Department, Work, BloodGroup, Vaccinated, vistreason, hospital, status
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (
                    emp_id,
                    st.session_state.form_data["Employee Name"],
                    st.session_state.form_data["Employee Age"],
                    st.session_state.form_data["Gender"],
                    st.session_state.form_data["Mobile No."],
                    st.session_state.form_data["Address"],
                    st.session_state.form_data["Department"],
                    st.session_state.form_data["Work"],
                    st.session_state.form_data["Blood Group"],
                    st.session_state.form_data["Vaccination Status"],
                    st.session_state.form_data["Visit Reason"],
                    st.session_state.form_data["Reference Type"],
                    st.session_state.form_data["Health status"]
                )
                try:
                    # Execute the SQL INSERT command
                    cursor.execute(sql, values)
                    connection.commit()  # Commit the changes to the database
                    st.success("Data Added Successfully")  # Show success message
                except mysql.connector.Error as e:
                    st.error(f"Error inserting data: {e}")  
    elif form_name == "Vitals":
        st.header("Vitals")
        r1c1,r1c2,r1c3 = st.columns([5,3,9])
        with r1c1:
            systolic = st.session_state.form_data.get("Systolic", "")
            diastolic = st.session_state.form_data.get("Diastolic", "")
            st.write("Blood Pressure")
            st.session_state.form_data["Systolic"] = st.text_input(
                "Systolic (mm Hg)", 
                value=systolic, 
                placeholder="Enter Systolic Pressure",
                key="systolic"
            )
            st.session_state.form_data["Diastolic"] = st.text_input(
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
            st.session_state.form_data["Pulse"] = st.text_input(
                "Pulse (Per Minute)", 
                value=st.session_state.form_data.get("Pulse", ""), 
                placeholder="Enter Pulse Rate",
                key="pulse"
            )
            st.session_state.form_data["spo2"] = st.text_input(
                "SpO2 (in %)", 
                value=st.session_state.form_data.get("spo2", ""), 
                placeholder="Enter SpO2 Level",
                key="spo2"
            )
            st.session_state.form_data["BMI"] = st.text_input(
                "BMI", 
                value=st.session_state.form_data.get("BMI", ""), 
                placeholder="Enter BMI",
                key="bmi"
            )

        with r2c2:
            st.session_state.form_data["Respiratory Rate"] = st.text_input(
                "Respiratory Rate (Per Minute)", 
                value=st.session_state.form_data.get("Respiratory Rate", ""), 
                placeholder="Enter Respiratory Rate",
                key="respiratory_rate"
            )
            st.session_state.form_data["Weight"] = st.text_input(
                "Weight (in KG)", 
                value=st.session_state.form_data.get("Weight", ""), 
                placeholder="Enter Weight",
                key="weight"
            )

        with r2c3:
            st.session_state.form_data["Temperature"] = st.text_input(
                "Temperature (in °F)", 
                value=st.session_state.form_data.get("Temperature", ""), 
                placeholder="Enter Body Temperature",
                key="temperature"
            )
            st.session_state.form_data["Height"] = st.text_input(
                "Height (in CM)", 
                value=st.session_state.form_data.get("Height", ""), 
                placeholder="Enter Height",
                key="height"
            )

        # Button for saving data
        r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
        with r3c3:
            if st.button("Add Data", type="primary"):
                try:
                    # Validation constraints
                    emp_id = st.session_state.form_data.get('Employee ID')
                    if not emp_id:
                        st.error("Employee ID is missing!")
                        return
                    
                    systolic = st.session_state.form_data["Systolic"]
                    diastolic = st.session_state.form_data["Diastolic"]
                    if not systolic.isdigit() or not diastolic.isdigit():
                        st.error("Systolic and Diastolic must be numeric values!")
                        return

                    pulse = st.session_state.form_data["Pulse"]
                    if pulse and not pulse.isdigit():
                        st.error("Pulse must be a numeric value!")
                        return

                    spo2 = st.session_state.form_data["spo2"]
                    if spo2 and (not spo2.isdigit() or int(spo2) < 0 or int(spo2) > 100):
                        st.error("SpO2 must be a percentage value between 0 and 100!")
                        return

                    weight = st.session_state.form_data["Weight"]
                    height = st.session_state.form_data["Height"]
                    if weight and not weight.isdigit():
                        st.error("Weight must be a numeric value!")
                        return
                    if height and not height.isdigit():
                        st.error("Height must be a numeric value!")
                        return

                    # Insert data into the database
                    cursor.execute("""
                        INSERT INTO vitals (emp_no, Systolic, Diastolic, PulseRate, entry_date, Spo2, BMI, RespiratoryRate, Weight, Temperature, Height)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        emp_id,
                        systolic,
                        diastolic,
                        pulse,
                        datetime.now().date(),
                        spo2,
                        st.session_state.form_data["BMI"],
                        st.session_state.form_data["Respiratory Rate"],
                        weight,
                        st.session_state.form_data["Temperature"],
                        height
                    ))
                    connection.commit()
                    st.success("Data successfully added!")
                except Exception as e:
                    st.error(f"Error saving data: {e}")
                    

    elif form_name == "Investigations":
        
        inv_form = ["HAEMATALOGY","ROUTINE SUGAR TESTS","RENAL FUNCTION TEST & ELECTROLYTES","LIPID PROFILE","LIVER FUNCTION TEST","THYROID FUNCTION TEST","AUTOIMMUNE TEST","COAGULATION TEST","ENZYMES & CARDIAC Profile","URINE ROUTINE","SEROLOGY","MOTION","ROUTINE CULTURE & SENSITIVITY TEST","Men's Pack","Women's Pack","Occupational Profile","Others TEST","OPHTHALMIC REPORT","X-RAY","USG","CT","MRI"]


        select_inv = st.selectbox("Select Investigation Form", inv_form)

        if select_inv == "HAEMATALOGY":
        
            r1c1, r1c2, r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Hemoglobin"] = st.text_input("Hemoglobin", value=st.session_state.form_data.get("Hemoglobin", ""))
                st.session_state.form_data["Total RBC"] = st.text_input("Total RBC", value=st.session_state.form_data.get("Total RBC", ""))
                st.session_state.form_data["Total WBC"] = st.text_input("Total WBC", value=st.session_state.form_data.get("Total WBC", ""))
                st.session_state.form_data["Neutrophil"] = st.text_input("Neutrophil", value=st.session_state.form_data.get("Neutrophil", ""))
                st.session_state.form_data["Monocyte"] = st.text_input("Monocyte", value=st.session_state.form_data.get("Monocyte", ""))
                st.session_state.form_data["PCV"] = st.text_input("PCV", value=st.session_state.form_data.get("PCV", ""))
                st.session_state.form_data["MCV"] = st.text_input("MCV", value=st.session_state.form_data.get("MCV", ""))
                st.session_state.form_data["MCH"] = st.text_input("MCH", value=st.session_state.form_data.get("MCH", ""))
                st.session_state.form_data["Lymphocyte"] = st.text_input("Lymphocyte", value=st.session_state.form_data.get("Lymphocyte", ""))
                st.session_state.form_data["ESR"] = st.text_input("ESR", value=st.session_state.form_data.get("ESR", ""))
                st.session_state.form_data["MCHC"] = st.text_input("MCHC", value=st.session_state.form_data.get("MCHC", ""))
                st.session_state.form_data["Platelet Count"] = st.text_input("Platelet Count", value=st.session_state.form_data.get("Platelet Count", ""))
                st.session_state.form_data["RDW"] = st.text_input("RDW", value=st.session_state.form_data.get("RDW", ""))
                st.session_state.form_data["Eosinophil"] = st.text_input("Eosinophil", value=st.session_state.form_data.get("Eosinophil", ""))
                st.session_state.form_data["Basophil"] = st.text_input("Basophil", value=st.session_state.form_data.get("Basophil", ""))
            with r1c2:
                st.text_input("Unit (in %)", key="hemoglobin")
                st.text_input("Unit (in %)", key="rbc")
                st.text_input("Unit (in %)", key="wbc")
                st.text_input("Unit (in %)", key="neutro")
                st.text_input("Unit (in %)", key="mono")
                st.text_input("Unit (in %)", key="pvc")
                st.text_input("Unit (in %)", key="mvc")
                st.text_input("Unit (in %)", key="mch")
                st.text_input("Unit (in %)", key="lymph")
                st.text_input("Unit (in %)", key="esr")
                st.text_input("Unit (in %)", key="mchc")
                st.text_input("Unit (in %)", key="platelet")
                st.text_input("Unit (in %)", key="rdw")
                st.text_input("Unit (in %)", key="euso")
                st.text_input("Unit (in %)", key="baso")
            with r1c3:
                st.text_input("Reference Range", key="hemoglobin1")
                st.text_input("Reference Range", key="rbc1")
                st.text_input("Reference Range", key="wbc1")
                st.text_input("Reference Range", key="neutro1")
                st.text_input("Reference Range", key="mono1")
                st.text_input("Reference Range", key="pvc1")
                st.text_input("Reference Range", key="mvc1")
                st.text_input("Reference Range", key="mch1")
                st.text_input("Reference Range", key="lymph1")
                st.text_input("Reference Range", key="esr1")
                st.text_input("Reference Range", key="mchc1")
                st.text_input("Reference Range", key="platelet1")
                st.text_input("Reference Range", key="rdw1")
                st.text_input("Reference Range", key="euso1")
                st.text_input("Reference Range", key="baso1")
            st.session_state.form_data["Preipheral Blood Smear - RBC Morphology"] = st.text_area("Preipheral Blood Smear - RBC Morphology", value=st.session_state.form_data.get("Preipheral Blood Smear - RBC Morphology", ""))
            st.session_state.form_data["Preipheral Blood Smear - Parasites"] = st.text_area("Preipheral Blood Smear - Parasites", value=st.session_state.form_data.get("Preipheral Blood Smear - Parasites", ""))
            st.session_state.form_data["Preipheral Blood Smear - Others"] = st.text_area("Preipheral Blood Smear - Others", value=st.session_state.form_data.get("Preipheral Blood Smear - Others", ""))

            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])

            with r3c3:
                if st.button("Add Data", type="primary"):

                                    # Prepare data for insertion
                    sql = """
                        INSERT INTO hematology_result (
                            emp_no, entry_date, 
                            heamoglobin, 
                            rbc_count,  
                            wbc_count, 
                            haemotocrit,
                            mcv, 
                            mch, 
                            mchc, 
                            platelet, 
                            rdw, 
                            neutrophil, 
                            lymphocyte, 
                            eosinophil, 
                            monocyte,  
                            basophils, 
                            esr, 
                            pbs_rbc, pbc_parasites, pbc_others, year, hospital
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    data = (
                        st.session_state.form_data['Employee ID'],  # emp_no
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data["Hemoglobin"],  # heamoglobin, unit
                        st.session_state.form_data["Total RBC"],  # rbc_count, unit
                        st.session_state.form_data["Total WBC"],  # wbc_count, unit
                        st.session_state.form_data["PCV"],  # haemotocrit, unit
                        st.session_state.form_data["MCV"],  # mcv, unit
                        st.session_state.form_data["MCH"],  # mch, unit
                        st.session_state.form_data["MCHC"],  # mchc, unit
                        st.session_state.form_data["Platelet Count"],  # platelet, unit
                        st.session_state.form_data["RDW"],  # rdw, unit
                        st.session_state.form_data["Neutrophil"],  # neutrophil, unit
                        st.session_state.form_data["Lymphocyte"],  # lymphocyte, unit
                        st.session_state.form_data["Eosinophil"],  # eosinophil, unit
                        st.session_state.form_data["Monocyte"],  # monocyte, unit
                        st.session_state.form_data["Basophil"],  # basophils, unit
                        st.session_state.form_data["ESR"],  # esr, unit
                        st.session_state.form_data["Preipheral Blood Smear - RBC Morphology"],  # pbs_rbc
                        st.session_state.form_data["Preipheral Blood Smear - Parasites"],  # pbc_parasites
                        st.session_state.form_data["Preipheral Blood Smear - Others"],  # pbc_others
                        datetime.now().year,  
                        st.session_state.form_data["Reference Type"], 
                    )

                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.success("Data Inserted Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error inserting data: {e}")
        

        if select_inv == "ROUTINE SUGAR TESTS":
            r1c1, r1c2, r1c3 = st.columns(3)
            
            
            
            with r1c1:
                st.session_state.form_data["Glucose (F)"] = st.text_input("Glucose (F)", value=st.session_state.form_data.get("Glucose (F)", ""))
                st.session_state.form_data["Glucose (PP)"] = st.text_input("Glucose (PP)", value=st.session_state.form_data.get("Glucose (PP)", ""))
                st.session_state.form_data["Random Blood sugar"] = st.text_input("Random Blood sugar", value=st.session_state.form_data.get("Random Blood sugar", ""))
                st.session_state.form_data["Estimated Average Glucose"] = st.text_input("Estimated Average Glucose", value=st.session_state.form_data.get("Estimated Average Glucose", ""))
                st.session_state.form_data["HbA1c"] = st.text_input("HbA1c", value=st.session_state.form_data.get("HbA1c", ""))
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="glucosef1")
                st.text_input("Unit (in mg/dL)", key="glucosepp1")
                st.text_input("Unit (in mg/dL)", key="RBS1")
                st.text_input("Unit (in mg/dL)", key="EAG1")
                st.text_input("Unit (in %)", key="hba1c1")
            with r1c3:
                st.text_input("Reference Range", key="glucosef")
                st.text_input("Reference Range", key="glucosepp")
                st.text_input("Reference Range", key="RBS")
                st.text_input("Reference Range", key="EAG")
                st.text_input("Reference Range", key="hba1c")
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):

                    # Prepare data for insertion
                    sql = """
                        INSERT INTO routine_sugartest (
                            entry_date, emp_no, glucosef, glucosepp, rbs,
                            eag, hba1c, year, hospital, batch
                        ) VALUES (
                            %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s
                        )
                    """
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # Use the fetched emp_no
                        st.session_state.form_data["Glucose (F)"],  # glucosef
                        st.session_state.form_data["Glucose (PP)"],  # glucosepp
                        st.session_state.form_data["Random Blood sugar"],  # rbs
                        st.session_state.form_data["Estimated Average Glucose"],  # eag
                        st.session_state.form_data["HbA1c"],  # hba1c
                        datetime.now().year,  # year
                        st.session_state.form_data["Reference Type"],  # hospital (replace with actual hospital name)
                        'your_batch'  # batch (replace with actual batch number)
                    )

                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.success("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")

                

        if select_inv == "RENAL FUNCTION TEST & ELECTROLYTES":
            if 'BUN Range' not in st.session_state.form_data:
                st.session_state.form_data['BUN Range'] = ""
            if 'emp_no' not in st.session_state:
                st.session_state.emp_no = st.text_input("Employee No", value="")  # Replace with actual logic to fetch emp_no

            r1c1, r1c2, r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Urea"] = st.text_input("Urea", value=st.session_state.form_data.get("Urea", ""))
                st.session_state.form_data["BUN"] = st.text_input("BUN", value=st.session_state.form_data.get("BUN", ""))
                st.session_state.form_data["Calcium"] = st.text_input("Calcium", value=st.session_state.form_data.get("Calcium", ""))
                st.session_state.form_data["Sodium"] = st.text_input("Sodium", value=st.session_state.form_data.get("Sodium", ""))
                st.session_state.form_data["Potassium"] = st.text_input("Potassium", value=st.session_state.form_data.get("Potassium", ""))
                st.session_state.form_data["Phosphorus"] = st.text_input("Phosphorus", value=st.session_state.form_data.get("Phosphorus", ""))
                st.session_state.form_data["Serum Creatinine"] = st.text_input("Serum Creatinine", value=st.session_state.form_data.get("Serum Creatinine", ""))
                st.session_state.form_data["Uric Acid"] = st.text_input("Uric Acid", value=st.session_state.form_data.get("Uric Acid", ""))
                st.session_state.form_data["Chloride"] = st.text_input("Chloride", value=st.session_state.form_data.get("Chloride", ""))
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="urea1")
                st.text_input("Unit (in mg/dL)", key="bun1")
                st.text_input("Unit (in mg/dL)", key="calcium1")
                st.text_input("Unit (in mg/dL)", key="sodium1")
                st.text_input("Unit (in mg/dL)", key="pot1")
                st.text_input("Unit (in mg/dL)", key="phos1")
                st.text_input("Unit (in mg/dL)", key="serum1")
                st.text_input("Unit (in mg/dL)", key="uric1")
                st.text_input("Unit (in mg/dL)", key="chlo1")
            with r1c3:
                st.text_input("Referance Range", key="urea")
                st.text_input("Referance Range", key="bun")
                st.text_input("Referance Range", key="calcium")
                st.text_input("Referance Range", key="sodium")
                st.text_input("Referance Range", key="pot")
                st.text_input("Referance Range", key="phos")
                st.text_input("Referance Range", key="serum")
                st.text_input("Referance Range", key="uric")
                st.text_input("Referance Range", key="chlo")
            r2c1, r2c2, r2c3 = st.columns(3)
                        

            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare data for insertion
                    sql = """
                        INSERT INTO rft_result (
                            entry_date, emp_no, urea, 
                            bun, 
                            sr_creatinine, 
                            uric_acid, 
                            sodium, 
                            potassium, 
                            calcium, 
                            phosphorus, 
                            chloride, 
                            year, hospital, batch
                        ) VALUES (
                            %s, %s, %s,
                            %s, %s, %s,
                            %s, %s, %s,
                            %s, %s, %s,
                            %s, %s
                        )
                    """
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Urea"],
                        st.session_state.form_data["BUN"], 
                        st.session_state.form_data["Serum Creatinine"], 
                        st.session_state.form_data["Uric Acid"], 
                        st.session_state.form_data["Sodium"], 
                        st.session_state.form_data["Potassium"], 
                        st.session_state.form_data["Calcium"], 
                        st.session_state.form_data["Phosphorus"], 
                        st.session_state.form_data["Chloride"], 
                        datetime.now().year,  # year
                        st.session_state.form_data["Reference Type"],  # hospital (replace with actual hospital name)
                        'your_batch'  # batch (replace with actual batch number)
                    )

                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")

        
        elif select_inv == "LIPID PROFILE":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Initialize keys if they don't exist
            lipid_keys = [
                "Total Cholesterol",
                "Triglycerides",
                "HDL - Cholesterol",
                "LDL- Cholesterol",
                "CHOL HDL ratio",
                "VLDL -Choleserol",
                "LDL.CHOL/HDL.CHOL Ratio"
            ]
            
            for key in lipid_keys:
                if key not in st.session_state.form_data:
                    st.session_state.form_data[key] = ""

            # Creating input fields
            r1c1, r1c2, r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Total Cholesterol"] = st.text_input("Total Cholesterol", value=st.session_state.form_data.get("Total Cholesterol", ""))
                st.session_state.form_data["Triglycerides"] = st.text_input("Triglycerides", value=st.session_state.form_data.get("Triglycerides", ""))
                st.session_state.form_data["HDL - Cholesterol"] = st.text_input("HDL - Cholesterol", value=st.session_state.form_data.get("HDL - Cholesterol", ""))
                st.session_state.form_data["LDL- Cholesterol"] = st.text_input("LDL- Cholesterol", value=st.session_state.form_data.get("LDL- Cholesterol", ""))
                st.session_state.form_data["CHOL HDL ratio"] = st.text_input("CHOL HDL ratio", value=st.session_state.form_data.get("CHOL HDL ratio", ""))
                st.session_state.form_data["VLDL -Choleserol"] = st.text_input("VLDL -Choleserol", value=st.session_state.form_data.get("VLDL -Choleserol", ""))
                st.session_state.form_data["LDL.CHOL/HDL.CHOL Ratio"] = st.text_input("LDL.CHOL/HDL.CHOL Ratio", value=st.session_state.form_data.get("LDL.CHOL/HDL.CHOL Ratio", ""))
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="chle1")
                st.text_input("Unit (in mg/dL)", key="trig1")
                st.text_input("Unit (in mg/dL)", key="hdl1")
                st.text_input("Unit (in mg/dL)", key="ldl1")
                st.text_input("Unit (in mg/dL)", key="cholr1")
                st.text_input("Unit (in mg/dL)", key="vldl1")
                st.text_input("Unit (in mg/dL)", key="ldl/1")
            with r1c3:
                st.text_input("Referance Range", key="chle")
                st.text_input("Referance Range", key="trig")
                st.text_input("Referance Range", key="hdl")
                st.text_input("Referance Range", key="ldl")
                st.text_input("Referance Range", key="cholr")
                st.text_input("Referance Range", key="vldl")
                st.text_input("Referance Range", key="ldl/")

            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO lipid_profile (
                            entry_date, emp_no,
                            tcholesterol, triglycerides,
                            hdl_cholesterol, ldl_cholesterol,
                            chol_hdlratio, vldl_cholesterol,
                            ldlhdlratio
                        ) VALUES (
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s, %s,
                            %s
                        )
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Total Cholesterol"],
                        st.session_state.form_data["Triglycerides"],
                        st.session_state.form_data["HDL - Cholesterol"],
                        st.session_state.form_data["LDL- Cholesterol"],
                        st.session_state.form_data["CHOL HDL ratio"],
                        st.session_state.form_data["VLDL -Choleserol"],
                        st.session_state.form_data["LDL.CHOL/HDL.CHOL Ratio"]
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    
            


        
        elif select_inv == "LIVER FUNCTION TEST":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for liver function test
            r1c1, r1c2, r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Bilirubin - Total"] = st.text_input("Bilirubin - Total", value=st.session_state.form_data.get("Bilirubin - Total", ""))
                st.session_state.form_data["Bilirubin - Direct"] = st.text_input("Bilirubin - Direct", value=st.session_state.form_data.get("Bilirubin - Direct", ""))
                st.session_state.form_data["Bilirubin - Indirect"] = st.text_input("Bilirubin - Indirect", value=st.session_state.form_data.get("Bilirubin - Indirect", ""))
                st.session_state.form_data["SGOT /AST"] = st.text_input("SGOT /AST", value=st.session_state.form_data.get("SGOT /AST", ""))
                st.session_state.form_data["SGPT /ALT"] = st.text_input("SGPT /ALT", value=st.session_state.form_data.get("SGPT /ALT", ""))
                st.session_state.form_data["Alkaline phosphatase"] = st.text_input("Alkaline phosphatase", value=st.session_state.form_data.get("Alkaline phosphatase", ""))
                st.session_state.form_data["Total Protein"] = st.text_input("Total Protein", value=st.session_state.form_data.get("Total Protein", ""))
                st.session_state.form_data["Albumin (Serum )"] = st.text_input("Albumin (Serum )", value=st.session_state.form_data.get("Albumin (Serum )", ""))
                st.session_state.form_data["Globulin(Serum)"] = st.text_input("Globulin(Serum)", value=st.session_state.form_data.get("Globulin(Serum)", ""))
                st.session_state.form_data["Alb/Glob Ratio"] = st.text_input("Alb/Glob Ratio", value=st.session_state.form_data.get("Alb/Glob Ratio", ""))
                st.session_state.form_data["Gamma Glutamyl transferase"] = st.text_input("Gamma Glutamyl transferase", value=st.session_state.form_data.get("Gamma Glutamyl transferase", ""))
            with r1c2:
                st.text_input("Unit in (mg/dL)", key="bilit1")
                st.text_input("Unit in (mg/dL)", key="bilid1")
                st.text_input("Unit in (mg/dL)", key="bili1")
                st.text_input("Unit in (mg/dL)", key="ast1")
                st.text_input("Unit in (mg/dL)", key="alt1")
                st.text_input("Unit in (mg/dL)", key="alkaline1")
                st.text_input("Unit in (mg/dL)", key="protien1")
                st.text_input("Unit in (mg/dL)", key="albumin1")
                st.text_input("Unit in (mg/dL)", key="globulin1")
                st.text_input("Unit in (mg/dL)", key="glob1")
                st.text_input("Unit in (mg/dL)", key="gamma1")
            with r1c3:
                st.text_input("Referance Range", key="bilit")
                st.text_input("Referance Range", key="bilid")
                st.text_input("Referance Range", key="bili")
                st.text_input("Referance Range", key="ast")
                st.text_input("Referance Range", key="alt")
                st.text_input("Referance Range", key="alkaline")
                st.text_input("Referance Range", key="protien")
                st.text_input("Referance Range", key="albumin")
                st.text_input("Referance Range", key="globulin")
                st.text_input("Referance Range", key="glob")
                st.text_input("Referance Range", key="gamma")

            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO liver_function (
                            entry_date, emp_no,
                            bilirubin_total, bilirubin_direct, bilirubin_indirect,
                            sgot_alt, sgpt_alt, alkaline_phosphatase,
                            total_protein, albumin, globulin,
                            alb_globratio, gammagt
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                        )
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Bilirubin - Total"],
                        st.session_state.form_data["Bilirubin - Direct"],
                        st.session_state.form_data["Bilirubin - Indirect"],
                        st.session_state.form_data["SGOT /AST"],
                        st.session_state.form_data["SGPT /ALT"],
                        st.session_state.form_data["Alkaline phosphatase"],
                        st.session_state.form_data["Total Protein"],
                        st.session_state.form_data["Albumin (Serum )"],
                        st.session_state.form_data["Globulin(Serum)"],
                        st.session_state.form_data["Alb/Glob Ratio"],
                        st.session_state.form_data["Gamma Glutamyl transferase"]
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    


        
        elif select_inv == "THYROID FUNCTION TEST":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for thyroid function test
            r1c1, r1c2, r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["T3- Triiodothyroine"] = st.text_input("T3- Triiodothyroine", value=st.session_state.form_data.get("T3- Triiodothyroine", ""))
                st.session_state.form_data["T4 - Thyroxine"] = st.text_input("T4 - Thyroxine", value=st.session_state.form_data.get("T4 - Thyroxine", ""))
                st.session_state.form_data["TSH- Thyroid Stimulating Hormone"] = st.text_input("TSH- Thyroid Stimulating Hormone", value=st.session_state.form_data.get("TSH- Thyroid Stimulating Hormone", ""))
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="t31")
                st.text_input("Unit (in mg/dL)", key="t41")
                st.text_input("Unit (in mg/dL)", key="tsh1")
            with r1c3:
                st.text_input("Reference Range", key="t3")
                st.text_input("Reference Range", key="t4")
                st.text_input("Reference Range", key="tsh")
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])

            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO thyroid_function_test (
                            entry_date, emp_no,
                            t3, t4, tsh
                        ) VALUES (%s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["T3- Triiodothyroine"],
                        st.session_state.form_data["T4 - Thyroxine"],
                        st.session_state.form_data["TSH- Thyroid Stimulating Hormone"]
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.success("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    

            # Displaying the form data
            



        elif select_inv == "AUTOIMMUNE TEST":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Autoimmune Test
            r1c1, r1c2, r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["ANA (Antinuclear Antibody)"] = st.text_input("ANA (Antinuclear Antibody)", value=st.session_state.form_data.get("ANA (Antinuclear Antibody)", ""))
                st.session_state.form_data["Anti ds DNA"] = st.text_input("Anti ds DNA", value=st.session_state.form_data.get("Anti ds DNA", ""))
                st.session_state.form_data["Rheumatoid factor"] = st.text_input("Rheumatoid factor", value=st.session_state.form_data.get("Rheumatoid factor", ""))
                st.session_state.form_data["Anticardiolipin Antibodies (IgG & IgM)"] = st.text_input("Anticardiolipin Antibodies (IgG & IgM)", value=st.session_state.form_data.get("Anticardiolipin Antibodies (IgG & IgM)", ""))
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="ana1")
                st.text_input("Unit (in mg/dL)", key="dna1")
                st.text_input("Unit (in mg/dL)", key="rheu1")
                st.text_input("Unit (in mg/dL)", key="antib1")
            with r1c3:
                st.text_input("Reference Range", key="ana")
                st.text_input("Reference Range", key="dna")
                st.text_input("Reference Range", key="rheu")
                st.text_input("Reference Range", key="antib")
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])

            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO autoimmune_test (
                            entry_date, emp_no,
                            ana, adna, rheumatoid, anticardiolipin
                        ) VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["ANA (Antinuclear Antibody)"],
                        st.session_state.form_data["Anti ds DNA"],
                        st.session_state.form_data["Rheumatoid factor"],
                        st.session_state.form_data["Anticardiolipin Antibodies (IgG & IgM)"]
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.success("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    

            # Displaying the form data
            


        elif select_inv == "COAGULATION TEST":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Coagulation Test
            r1c1, r1c2, r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Prothrombin Time (PT)"] = st.text_input("Prothrombin Time (PT)", value=st.session_state.form_data.get("Prothrombin Time (PT)", ""))
                st.session_state.form_data["PT INR"] = st.text_input("PT INR", value=st.session_state.form_data.get("PT INR", ""))
                st.session_state.form_data["Clotting Time (CT)"] = st.text_input("Clotting Time (CT)", value=st.session_state.form_data.get("Clotting Time (CT)", ""))
                st.session_state.form_data["Bleeding Time (BT)"] = st.text_input("Bleeding Time (BT)", value=st.session_state.form_data.get("Bleeding Time (BT)", ""))
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="pt1")
                st.text_input("Unit (in mg/dL)", key="ptinr1")
                st.text_input("Unit (in mg/dL)", key="ct1")
                st.text_input("Unit (in mg/dL)", key="bt1")
            with r1c3:
                st.text_input("Reference Range", key="pt")
                st.text_input("Reference Range", key="ptinr")
                st.text_input("Reference Range", key="ct")
                st.text_input("Reference Range", key="bt")
            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO coagulation_test (
                            entry_date, emp_no,
                            pt, ptinr, bt, ct
                        ) VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Prothrombin Time (PT)"],
                        st.session_state.form_data["PT INR"],
                        st.session_state.form_data["Bleeding Time (BT)"],
                        st.session_state.form_data["Clotting Time (CT)"]
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.success("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    

            
            


        elif select_inv == "ENZYMES & CARDIAC Profile":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Enzymes & Cardiac Profile
            r1c1, r1c2, r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Acid Phosphatase"] = st.text_input("Acid Phosphatase", value=st.session_state.form_data.get("Acid Phosphatase", ""))
                st.session_state.form_data["Adenosine Deaminase"] = st.text_input("Adenosine Deaminase", value=st.session_state.form_data.get("Adenosine Deaminase", ""))
                st.session_state.form_data["Amylase"] = st.text_input("Amylase", value=st.session_state.form_data.get("Amylase", ""))
                st.session_state.form_data["ECG"] = st.selectbox("ECG", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["ECG"] == "Abnormal":
                    st.session_state.form_data["ECG-Comments"] = st.text_area("ECG-Comments", value=st.session_state.form_data.get("ECG-Comments", ""))
                st.session_state.form_data["Troponin- T"] = st.text_input("Troponin- T", value=st.session_state.form_data.get("Troponin- T", ""))
                st.session_state.form_data["CPK - TOTAL"] = st.text_input("CPK - TOTAL", value=st.session_state.form_data.get("CPK - TOTAL", ""))
                st.session_state.form_data["ECHO"] = st.selectbox("ECHO", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["ECHO"] == "Abnormal":
                    st.session_state.form_data["ECHO-Comments"] = st.text_area("ECHO-Comments", value=st.session_state.form_data.get("ECHO-Comments", ""))
                st.session_state.form_data["Lipase"] = st.text_input("Lipase", value=st.session_state.form_data.get("Lipase", ""))
                st.session_state.form_data["CPK - MB"] = st.text_input("CPK - MB", value=st.session_state.form_data.get("CPK - MB", ""))
                st.session_state.form_data["TMT"] = st.selectbox("TMT", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["TMT"] == "Abnormal":
                    st.session_state.form_data["TMT-Comments"] = st.text_area("TMT-Comments", value=st.session_state.form_data.get("TMT-Comments", ""))
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="acid1")
                st.text_input("Unit (in mg/dL)", key="adeno1")
                st.text_input("Unit (in mg/dL)", key="amylase1")
                st.text_input("Unit (in mg/dL)", key="ecg1")
                st.text_input("Unit (in mg/dL)", key="trop1")
                st.text_input("Unit (in mg/dL)", key="cpkt1")
                st.text_input("Unit (in mg/dL)", key="echo1")
                st.text_input("Unit (in mg/dL)", key="lipase1")
                st.text_input("Unit (in mg/dL)", key="cpk1")
                st.text_input("Unit (in mg/dL)", key="tmt1")
                
            with r1c3:
                st.text_input("Reference Range", key="acid")
                st.text_input("Reference Range", key="adeno")
                st.text_input("Reference Range", key="amylase")
                st.text_input("Reference Range", key="ecg")
                st.text_input("Reference Range", key="trop")
                st.text_input("Reference Range", key="cpkt")
                st.text_input("Reference Range", key="echo")
                st.text_input("Reference Range", key="lipase")
                st.text_input("Reference Range", key="cpk")
                st.text_input("Reference Range", key="tmt")
            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO enzymes_cardio (
                            entry_date, emp_no,
                            acid_phosphatase, adenosine, amylase,
                            ecg, ecg_comments, troponin_t, troponin_i,
                            cpk_total, echo, echo_comments, lipase,
                            cpk_mb, tmt, tmt_comments
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Acid Phosphatase"],
                        st.session_state.form_data["Adenosine Deaminase"],
                        st.session_state.form_data["Amylase"],
                        st.session_state.form_data["ECG"],
                        st.session_state.form_data.get("ECG-Comments", ""),
                        st.session_state.form_data["Troponin- T"],
                        st.session_state.form_data["Troponin- I"],
                        st.session_state.form_data["CPK - TOTAL"],
                        st.session_state.form_data["ECHO"],
                        st.session_state.form_data.get("ECHO-Comments", ""),
                        st.session_state.form_data["Lipase"],
                        st.session_state.form_data["CPK - MB"],
                        st.session_state.form_data["TMT"],
                        st.session_state.form_data.get("TMT-Comments", "")
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
            



        elif select_inv == "URINE ROUTINE":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Urine Routine
            r1c1, r1c2, r1c3 = st.columns(3)
            
            with r1c1:
                st.session_state.form_data["Colour"] = st.text_input("Colour", value=st.session_state.form_data.get("Colour", ""))
                st.session_state.form_data["Appearance"] = st.text_input("Appearance", value=st.session_state.form_data.get("Appearance", ""))
                st.session_state.form_data["Reaction (pH)"] = st.text_input("Reaction (pH)", value=st.session_state.form_data.get("Reaction (pH)", ""))
                st.session_state.form_data["Specific gravity"] = st.text_input("Specific gravity", value=st.session_state.form_data.get("Specific gravity", ""))
                st.session_state.form_data["Crystals"] = st.text_input("Crystals", value=st.session_state.form_data.get("Crystals", ""))
                st.session_state.form_data["Bacteria"] = st.text_input("Bacteria", value=st.session_state.form_data.get("Bacteria", ""))
                st.session_state.form_data["Protein/Albumin"] = st.text_input("Protein/Albumin", value=st.session_state.form_data.get("Protein/Albumin", ""))
                st.session_state.form_data["Glucose (Urine)"] = st.text_input("Glucose (Urine)", value=st.session_state.form_data.get("Glucose (Urine)", ""))
                st.session_state.form_data["Ketone Bodies"] = st.text_input("Ketone Bodies", value=st.session_state.form_data.get("Ketone Bodies", ""))
                st.session_state.form_data["Urobilinogen"] = st.text_input("Urobilinogen", value=st.session_state.form_data.get("Urobilinogen", ""))
                st.session_state.form_data["Casts"] = st.text_input("Casts", value=st.session_state.form_data.get("Casts", ""))
                st.session_state.form_data["Bile Salts"] = st.text_input("Bile Salts", value=st.session_state.form_data.get("Bile Salts", ""))
                st.session_state.form_data["Bile Pigments"] = st.text_input("Bile Pigments", value=st.session_state.form_data.get("Bile Pigments", ""))
                st.session_state.form_data["WBC / Pus cells"] = st.text_input("WBC / Pus cells", value=st.session_state.form_data.get("WBC / Pus cells", ""))
                st.session_state.form_data["Red Blood Cells"] = st.text_input("Red Blood Cells", value=st.session_state.form_data.get("Red Blood Cells", ""))
                st.session_state.form_data["Epithelial cells"] = st.text_input("Epithelial cells", value=st.session_state.form_data.get("Epithelial cells", ""))

            with r1c2:
                st.text_input("Unit (in mg/dL)", key="colour_unit")
                st.text_input("Unit (in mg/dL)", key="appearance_unit")
                st.text_input("Unit (in mg/dL)", key="reaction_unit")
                st.text_input("Unit (in mg/dL)", key="specific_gravity_unit")
                st.text_input("Unit (in mg/dL)", key="crystals_unit")
                st.text_input("Unit (in mg/dL)", key="bacteria_unit")
                st.text_input("Unit (in mg/dL)", key="protein_albumin_unit")
                st.text_input("Unit (in mg/dL)", key="glucose_unit")
                st.text_input("Unit (in mg/dL)", key="ketone_unit")
                st.text_input("Unit (in mg/dL)", key="urobilinogen_unit")
                st.text_input("Unit (in mg/dL)", key="casts_unit")
                st.text_input("Unit (in mg/dL)", key="bile_salts_unit")
                st.text_input("Unit (in mg/dL)", key="bile_pigments_unit")
                st.text_input("Unit (in mg/dL)", key="wbc_pus_cells_unit")
                st.text_input("Unit (in mg/dL)", key="red_blood_cells_unit")
                st.text_input("Unit (in mg/dL)", key="epithelial_cells_unit")

                
            with r1c3:
                st.text_input("Reference Range ", key="colour_reference_range")
                st.text_input("Reference Range ", key="appearance_reference_range")
                st.text_input("Reference Range ", key="reaction_reference_range")
                st.text_input("Reference Range ", key="specific_gravity_reference_range")
                st.text_input("Reference Range ", key="crystals_reference_range")
                st.text_input("Reference Range ", key="bacteria_reference_range")
                st.text_input("Reference Range ", key="protein_albumin_reference_range")
                st.text_input("Reference Range ", key="glucose_reference_range")
                st.text_input("Reference Range ", key="ketone_reference_range")
                st.text_input("Reference Range ", key="urobilinogen_reference_range")
                st.text_input("Reference Range", key="casts_reference_range")
                st.text_input("Reference Range ", key="bile_salts_reference_range")
                st.text_input("Reference Range ", key="bile_pigments_reference_range")
                st.text_input("Reference Range ", key="wbc_pus_cells_reference_range")
                st.text_input("Reference Range ", key="red_blood_cells_reference_range")
                st.text_input("Reference Range ", key="epithelial_cells_reference_range")

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion (add your SQL connection logic)
                    sql = """
                        INSERT INTO urine_routine (
                            entry_date, emp_no,
                            colour, appearance, reaction_ph, specific_gravity,
                            protein_albumin, glucose_urine, ketone_bodies,
                            urobilinogen, casts, bile_salts,
                            bile_pigments, wbc_pus_cells, red_blood_cells,
                            epithelial_cells, crystals, bacteria
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Colour"],
                        st.session_state.form_data["Appearance"],
                        st.session_state.form_data["Reaction (pH)"],
                        st.session_state.form_data["Specific gravity"],
                        st.session_state.form_data["Protein/Albumin"],
                        st.session_state.form_data["Glucose (Urine)"],
                        st.session_state.form_data["Ketone Bodies"],
                        st.session_state.form_data["Urobilinogen"],
                        st.session_state.form_data["Casts"],
                        st.session_state.form_data["Bile Salts"],
                        st.session_state.form_data["Bile Pigments"],
                        st.session_state.form_data["WBC / Pus cells"],
                        st.session_state.form_data["Red Blood Cells"],
                        st.session_state.form_data["Epithelial cells"],
                        st.session_state.form_data["Crystals"],
                        st.session_state.form_data["Bacteria"]
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.success("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    



        elif select_inv == "SEROLOGY":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Serology tests
            r1c1, r1c2, r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["Screening For HIV I & II"] = st.text_input("Screening For HIV I & II", value=st.session_state.form_data.get("Screening For HIV I & II", ""))
                st.session_state.form_data["HBsAg"] = st.text_input("HBsAg", value=st.session_state.form_data.get("HBsAg", ""))
                st.session_state.form_data["HCV"] = st.text_input("HCV", value=st.session_state.form_data.get("HCV", ""))
                st.session_state.form_data["VDRL"] = st.text_input("VDRL", value=st.session_state.form_data.get("VDRL", ""))
                st.session_state.form_data["Dengue NS1Ag"] = st.text_input("Dengue NS1Ag", value=st.session_state.form_data.get("Dengue NS1Ag", ""))
                st.session_state.form_data["Dengue IgG"] = st.text_input("Dengue IgG", value=st.session_state.form_data.get("Dengue IgG", ""))
                st.session_state.form_data["Dengue IgM"] = st.text_input("Dengue IgM", value=st.session_state.form_data.get("Dengue IgM", ""))
                st.session_state.form_data["WIDAL"] = st.text_input("WIDAL", value=st.session_state.form_data.get("WIDAL", ""))
                
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="hiv_screening_unit")
                st.text_input("Unit (in mg/dL)", key="hbsag_unit")
                st.text_input("Unit (in mg/dL)", key="hcv_unit")
                st.text_input("Unit (in mg/dL)", key="vdrl_unit")
                st.text_input("Unit (in mg/dL)", key="dengue_ns1ag_unit")
                st.text_input("Unit (in mg/dL)", key="dengue_igg_unit")
                st.text_input("Unit (in mg/dL)", key="dengue_igm_unit")
                st.text_input("Unit (in mg/dL)", key="widal_unit")

            with r1c3:
                st.text_input("Reference Range", key="screening_for_hiv_range")
                st.text_input("Reference Range", key="hbsag_range")
                st.text_input("Reference Range", key="hcv_range")
                st.text_input("Reference Range", key="vdrl_range")
                st.text_input("Reference Range", key="dengue_ns1ag_range")
                st.text_input("Reference Range", key="dengue_igg_range")
                st.text_input("Reference Range", key="dengue_igm_range")
                st.text_input("Reference Range", key="widal_range")

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion (add your SQL connection logic)
                    sql = """
                        INSERT INTO serology_result (
                            entry_date, emp_no,
                            hiv_screening, hbsag, hcv, 
                            vdrl, denguens, dengueigg, 
                            dengueigm, widal
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Screening For HIV I & II"],
                        st.session_state.form_data["HBsAg"],
                        st.session_state.form_data["HCV"],
                        st.session_state.form_data["VDRL"],
                        st.session_state.form_data["Dengue NS1Ag"],
                        st.session_state.form_data["Dengue IgG"],
                        st.session_state.form_data["Dengue IgM"],
                        st.session_state.form_data["WIDAL"]
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                

            # Displaying the form data
            


        elif select_inv == "MOTION":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Motion tests
            r1c1, r1c2, r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["Colour (Motion)"] = st.text_input("Colour (Motion)", value=st.session_state.form_data.get("Colour (Motion)", ""))
                st.session_state.form_data["Appearance (Motion)"] = st.text_input("Appearance (Motion)", value=st.session_state.form_data.get("Appearance (Motion)", ""))
                st.session_state.form_data["Occult Blood"] = st.text_input("Occult Blood", value=st.session_state.form_data.get("Occult Blood", ""))
                st.session_state.form_data["Cyst"] = st.text_input("Cyst", value=st.session_state.form_data.get("Cyst", ""))
                st.session_state.form_data["Mucus"] = st.text_input("Mucus", value=st.session_state.form_data.get("Mucus", ""))
                st.session_state.form_data["Pus Cells"] = st.text_input("Pus Cells", value=st.session_state.form_data.get("Pus Cells", ""))
                st.session_state.form_data["Ova"] = st.text_input("Ova", value=st.session_state.form_data.get("Ova", ""))
                st.session_state.form_data["RBCs"] = st.text_input("RBCs", value=st.session_state.form_data.get("RBCs", ""))
                st.session_state.form_data["Others"] = st.text_input("Others", value=st.session_state.form_data.get("Others", ""))

            with r1c2:
                st.text_input("Unit (in mg/dL)", key="colour_motion_unit")
                st.text_input("Unit (in mg/dL)", key="appearance_motion_unit")
                st.text_input("Unit (in mg/dL)", key="occult_blood_unit")
                st.text_input("Unit (in mg/dL)", key="cyst_unit")
                st.text_input("Unit (in mg/dL)", key="mucus_unit")
                st.text_input("Unit (in mg/dL)", key="pus_cells_unit")
                st.text_input("Unit (in mg/dL)", key="ova_unit")
                st.text_input("Unit (in mg/dL)", key="rbcs_unit")
                st.text_input("Unit (in mg/dL)", key="others_unit")

            with r1c3:
                st.text_input("Reference Range", key="colour_motion_range")
                st.text_input("Reference Range", key="appearance_motion_range")
                st.text_input("Reference Range", key="occult_blood_range")
                st.text_input("Reference Range", key="cyst_range")
                st.text_input("Reference Range", key="mucus_range")
                st.text_input("Reference Range", key="pus_cells_range")
                st.text_input("Reference Range", key="ova_range")
                st.text_input("Reference Range", key="rbcs_range")
                st.text_input("Reference Range", key="others_range")

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion (add your SQL connection logic)
                    sql = """
                        INSERT INTO motion (
                            entry_date, emp_no,
                            colour, appearance, occult_blood, 
                            cyst, mucus, pus_cells, 
                            ova, rbcs, others_t
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Colour (Motion)"],
                        st.session_state.form_data["Appearance (Motion)"],
                        st.session_state.form_data["Occult Blood"],
                        st.session_state.form_data["Cyst"],
                        st.session_state.form_data["Mucus"],
                        st.session_state.form_data["Pus Cells"],
                        st.session_state.form_data["Ova"],
                        st.session_state.form_data["RBCs"],
                        st.session_state.form_data["Others"]
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                  
            


        elif select_inv == "ROUTINE CULTURE & SENSITIVITY TEST":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Routine Culture & Sensitivity tests
            r1c1, r1c2, r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["Urine"] = st.text_input("Urine", value=st.session_state.form_data.get("Urine", ""))
                st.session_state.form_data["Motion"] = st.text_input("Motion", value=st.session_state.form_data.get("Motion", ""))
                st.session_state.form_data["Sputum"] = st.text_input("Sputum", value=st.session_state.form_data.get("Sputum", ""))
                st.session_state.form_data["Blood"] = st.text_input("Blood", value=st.session_state.form_data.get("Blood", ""))

            with r1c2:
                st.text_input("Unit (in mg/dL)", key="urine_unit")
                st.text_input("Unit (in mg/dL)", key="motion_unit")
                st.text_input("Unit (in mg/dL)", key="sputum_unit")
                st.text_input("Unit (in mg/dL)", key="blood_unit")
                
            with r1c3:
                st.text_input("Reference Range", key="urine_range")
                st.text_input("Reference Range", key="motion_range")
                st.text_input("Reference Range", key="sputum_range")
                st.text_input("Reference Range", key="blood_range")


            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion (add your SQL connection logic)
                    sql = """
                        INSERT INTO routine_culture (
                            entry_date, emp_no,
                            urine, motion, sputum, blood
                        ) VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Urine"],
                        st.session_state.form_data["Motion"],
                        st.session_state.form_data["Sputum"],
                        st.session_state.form_data["Blood"]
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    
            


        elif select_inv == "Men's Pack":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input field for PSA (Prostate Specific Antigen)
            r1c1, r1c2, r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["PSA (Prostate specific Antigen)"] = st.text_input("PSA (Prostate specific Antigen)", 
                    value=st.session_state.form_data.get("PSA (Prostate specific Antigen)", "")
                )
                
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="psa")
                
            with r1c3:
                st.text_input("Reference Range", key="p_sa")

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion (add your SQL connection logic)
                    sql = """
                        INSERT INTO mens_pack (
                            entry_date, emp_no,
                            psa
                        ) VALUES (%s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["PSA (Prostate specific Antigen)"]
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
            

        
        elif select_inv == "Women's Pack":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Mammogram and PAP Smear
            r1c1, r1c2, r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Mammogram"] = st.selectbox("Mammogram", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["Mammogram"] == "Abnormal":
                    st.session_state.form_data["Mammogram-Comments"] = st.text_area("Mammogram-Comments", 
                        value=st.session_state.form_data.get("Mammogram-Comments", "")
                    )
                st.session_state.form_data["PAP Smear"] = st.selectbox("PAP Smear", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["PAP Smear"] == "Abnormal":
                    st.session_state.form_data["PAP Smear-Comments"] = st.text_area("PAP Smear-Comments", 
                        value=st.session_state.form_data.get("PAP Smear-Comments", "")
                    )
                    
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="manmogram")
                st.text_input("Unit (in mg/dL)", key="pap")
                
                    
            with r1c3:
                st.text_input("Reference Range", key="manmogram1")
                st.text_input("Reference Range", key="pap1")
                    

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion (add your SQL connection logic)
                    sql = """
                        INSERT INTO womens_pack (
                            entry_date, emp_no,
                            mammogram_nm_ab, mammogram_comment,
                            pap_nm_ab, pap_comment
                        ) VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Mammogram"],
                        st.session_state.form_data.get("Mammogram-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["PAP Smear"],
                        st.session_state.form_data.get("PAP Smear-Comments", "")  # Comment if Abnormal
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
            


        elif select_inv == "Occupational Profile":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Audiometry and PFT
            r1c1, r1c2, r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["Audiometry"] = st.selectbox("Audiometry", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["Audiometry"] == "Abnormal":
                    st.session_state.form_data["Audiometry-Comments"] = st.text_area("Audiometry-Comments", 
                        value=st.session_state.form_data.get("Audiometry-Comments", "")
                    )

                st.session_state.form_data["PFT"] = st.selectbox("PFT", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["PFT"] == "Abnormal":
                    st.session_state.form_data["PFT-Comments"] = st.text_area("PFT-Comments", 
                        value=st.session_state.form_data.get("PFT-Comments", "")
                    )
                    
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="audio")
                st.text_input("Unit (in mg/dL)", key="pft")
                
                    
            with r1c3:
                st.text_input("Reference Range", key="audio1")
                st.text_input("Reference Range", key="pft1")

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])

            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion (add your SQL connection logic)
                    sql = """
                        INSERT INTO occupational_profile (
                            entry_date, emp_no,
                            audiometry_nm_ab, audiometry_comment,
                            pft_nm_ab, pft_comment
                        ) VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Audiometry"],
                        st.session_state.form_data.get("Audiometry-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["PFT"],
                        st.session_state.form_data.get("PFT-Comments", "")  # Comment if Abnormal
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")

        
        elif select_inv == "Others TEST":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Pathology
            r1c1, r1c2, r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["Pathology"] = st.selectbox("Pathology", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["Pathology"] == "Abnormal":
                    st.session_state.form_data["Pathology-Comments"] = st.text_area("Pathology-Comments", 
                        value=st.session_state.form_data.get("Pathology-Comments", "")
                    )
                    
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="path")
                
                
                    
            with r1c3:
                st.text_input("Reference Range", key="path1")

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])

            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO other_tests (
                            entry_date, emp_no,
                            pathology, pathology_comments
                        ) VALUES (%s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Pathology"],
                        st.session_state.form_data.get("Pathology-Comments", "")  # Comment if Abnormal
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")


        elif select_inv == "OPHTHALMIC REPORT":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for Vision and Color Vision
            r1c1, r1c2, r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["Vision"] = st.selectbox("Vision", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["Vision"] == "Abnormal":
                    st.session_state.form_data["Vision-Comments"] = st.text_area("Vision-Comments", 
                        value=st.session_state.form_data.get("Vision-Comments", "")
                    )
                st.session_state.form_data["Color Vision"] = st.selectbox("Color Vision", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["Color Vision"] == "Abnormal":
                    st.session_state.form_data["Color Vision-Comments"] = st.text_area("Color Vision-Comments", 
                        value=st.session_state.form_data.get("Color Vision-Comments", "")
                    )
                    
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="vision")
                st.text_input("Unit (in mg/dL)", key="color")
                
                    
            with r1c3:
                st.text_input("Reference Range", key="vision1")
                st.text_input("Reference Range", key="color1")

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])

            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO ophthalmic_report (
                            entry_date, emp_no,
                            vision, vision_comments,
                            colourvision, colourvision_comment
                        ) VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["Vision"],
                        st.session_state.form_data.get("Vision-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["Color Vision"],
                        st.session_state.form_data.get("Color Vision-Comments", "")  # Comment if Abnormal
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    
            

        
        elif select_inv == "X-RAY":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for X-RAY results
            r1c1, r1c2, r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["X-RAY Chest"] = st.selectbox("X-RAY Chest", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY Chest"] == "Abnormal":
                    st.session_state.form_data["X-RAY Chest-Comments"] = st.text_area("X-RAY Chest-Comments", 
                        value=st.session_state.form_data.get("X-RAY Chest-Comments", "")
                    )
                st.session_state.form_data["X-RAY KUB"] = st.selectbox("X-RAY KUB", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY KUB"] == "Abnormal":
                    st.session_state.form_data["X-RAY KUB-Comments"] = st.text_area("X-RAY KUB-Comments", 
                        value=st.session_state.form_data.get("X-RAY KUB-Comments", "")
                    )
                st.session_state.form_data["X-RAY Spine"] = st.selectbox("X-RAY Spine", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY Spine"] == "Abnormal":
                    st.session_state.form_data["X-RAY Spine-Comments"] = st.text_area("X-RAY Spine-Comments", 
                        value=st.session_state.form_data.get("X-RAY Spine-Comments", "")
                    )
                st.session_state.form_data["X-RAY Pelvis"] = st.selectbox("X-RAY Pelvis", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY Pelvis"] == "Abnormal":
                    st.session_state.form_data["X-RAY Pelvis-Comments"] = st.text_area("X-RAY Pelvis-Comments", 
                        value=st.session_state.form_data.get("X-RAY Pelvis-Comments", "")
                    )
                st.session_state.form_data["X-RAY Abdomen"] = st.selectbox("X-RAY Abdomen", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY Abdomen"] == "Abnormal":
                    st.session_state.form_data["X-RAY Abdomen-Comments"] = st.text_area("X-RAY Abdomen-Comments", 
                        value=st.session_state.form_data.get("X-RAY Abdomen-Comments", "")
                    )
                    
                    
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="x-ray")
                st.text_input("Unit (in mg/dL)", key="xkub")
                st.text_input("Unit (in mg/dL)", key="xspine")
                st.text_input("Unit (in mg/dL)", key="xpelvis")
                st.text_input("Unit (in mg/dL)", key="xabdomen")
                
                
                    
            with r1c3:
                st.text_input("Reference Range", key="x-ray1")
                st.text_input("Reference Range", key="xkub1")
                st.text_input("Reference Range", key="xspine1")
                st.text_input("Reference Range", key="xpelvis1")
                st.text_input("Reference Range", key="xabdomen1")
                

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])

            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO x_ray (
                            entry_date, emp_no,
                            chest_nm_ab, chest_comment,
                            kub_nm_ab, kub_comment,
                            spine_nm_ab, spine_comment,
                            pelvis_nm_ab, pelvis_comment,
                            abdomen_nm_ab, abdomen_comment
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["X-RAY Chest"],
                        st.session_state.form_data.get("X-RAY Chest-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["X-RAY KUB"],
                        st.session_state.form_data.get("X-RAY KUB-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["X-RAY Spine"],
                        st.session_state.form_data.get("X-RAY Spine-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["X-RAY Pelvis"],
                        st.session_state.form_data.get("X-RAY Pelvis-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["X-RAY Abdomen"],
                        st.session_state.form_data.get("X-RAY Abdomen-Comments", "")  # Comment if Abnormal
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    
            

                
        elif select_inv == "USG":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for USG results
            r1c1, r1c2, r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["USG ABDOMEN"] = st.selectbox("USG ABDOMEN", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["USG ABDOMEN"] == "Abnormal":
                    st.session_state.form_data["USG ABDOMEN-Comments"] = st.text_area("USG ABDOMEN-Comments", 
                        value=st.session_state.form_data.get("USG ABDOMEN-Comments", "")
                    )
                st.session_state.form_data["USG KUB"] = st.selectbox("USG KUB", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["USG KUB"] == "Abnormal":
                    st.session_state.form_data["USG KUB-Comments"] = st.text_area("USG KUB-Comments", 
                        value=st.session_state.form_data.get("USG KUB-Comments", "")
                    )
                st.session_state.form_data["USG Pelvis"] = st.selectbox("USG Pelvis", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["USG Pelvis"] == "Abnormal":
                    st.session_state.form_data["USG Pelvis-Comments"] = st.text_area("USG Pelvis-Comments", 
                        value=st.session_state.form_data.get("USG Pelvis-Comments", "")
                    )
                st.session_state.form_data["USG Neck"] = st.selectbox("USG Neck", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["USG Neck"] == "Abnormal":
                    st.session_state.form_data["USG Neck-Comments"] = st.text_area("USG Neck-Comments", 
                        value=st.session_state.form_data.get("USG Neck-Comments", "")
                    )
                    
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="usg")
                st.text_input("Unit (in mg/dL)", key="kub")
                st.text_input("Unit (in mg/dL)", key="pelvis")
                st.text_input("Unit (in mg/dL)", key="neck")
                
                
                    
            with r1c3:
                st.text_input("Reference Range", key="usg1")
                st.text_input("Reference Range", key="kub1")
                st.text_input("Reference Range", key="pelvis1")
                st.text_input("Reference Range", key="neck1")
                

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])

            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO usg (
                            entry_date, emp_no,
                            abdomen, abdomen_comments,
                            kub, kub_comments,
                            pelvis, pelvis_comments,
                            neck, neck_comments
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["USG ABDOMEN"],
                        st.session_state.form_data.get("USG ABDOMEN-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["USG KUB"],
                        st.session_state.form_data.get("USG KUB-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["USG Pelvis"],
                        st.session_state.form_data.get("USG Pelvis-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["USG Neck"],
                        st.session_state.form_data.get("USG Neck-Comments", "")  # Comment if Abnormal
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
            

        
        elif select_inv == "CT":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for CT results
            r1c1, r1c2, r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["CT Brain"] = st.selectbox("CT Brain", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["CT Brain"] == "Abnormal":
                    st.session_state.form_data["CT Brain-Comments"] = st.text_area("CT Brain-Comments", 
                        value=st.session_state.form_data.get("CT Brain-Comments", "")
                    )
                st.session_state.form_data["CT Lungs"] = st.selectbox("CT Lungs", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["CT Lungs"] == "Abnormal":
                    st.session_state.form_data["CT Lungs-Comments"] = st.text_area("CT Lungs-Comments", 
                        value=st.session_state.form_data.get("CT Lungs-Comments", "")
                    )
                st.session_state.form_data["CT Abdomen"] = st.selectbox("CT Abdomen", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["CT Abdomen"] == "Abnormal":  
                    st.session_state.form_data["CT Abdomen-Comments"] = st.text_area("CT Abdomen-Comments", 
                        value=st.session_state.form_data.get("CT Abdomen-Comments", "")
                    )
                st.session_state.form_data["CT Spine"] = st.selectbox("CT Spine", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["CT Spine"] == "Abnormal":
                    st.session_state.form_data["CT Spine-Comments"] = st.text_area("CT Spine-Comments", 
                        value=st.session_state.form_data.get("CT Spine-Comments", "")
                    )
                st.session_state.form_data["CT Pelvis"] = st.selectbox("CT Pelvis", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["CT Pelvis"] == "Abnormal":
                    st.session_state.form_data["CT Pelvis-Comments"] = st.text_area("CT Pelvis-Comments", 
                        value=st.session_state.form_data.get("CT Pelvis-Comments", "")
                    )
                    
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="ct")
                st.text_input("Unit (in mg/dL)", key="ctlungs")
                st.text_input("Unit (in mg/dL)", key="ctabdomen")
                st.text_input("Unit (in mg/dL)", key="ctspine")
                st.text_input("Unit (in mg/dL)", key="ctpelvis")
                
                    
            with r1c3:
                st.text_input("Reference Range", key="ct1")
                st.text_input("Reference Range", key="ctlungs1")
                st.text_input("Reference Range", key="ctabdomen1")
                st.text_input("Reference Range", key="ctspine1")
                st.text_input("Reference Range", key="ctpelvis1")

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO ct_report (
                            entry_date, emp_no,
                            brain, brain_comment,
                            ct_lungs, ct_lungs_comment,
                            abdomen, abdomen_comment,
                            spine, spine_comment,
                            pelvis, pelvis_comment
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["CT Brain"],
                        st.session_state.form_data.get("CT Brain-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["CT Lungs"],
                        st.session_state.form_data.get("CT Lungs-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["CT Abdomen"],
                        st.session_state.form_data.get("CT Abdomen-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["CT Spine"],
                        st.session_state.form_data.get("CT Spine-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["CT Pelvis"],
                        st.session_state.form_data.get("CT Pelvis-Comments", "")  # Comment if Abnormal
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    
            

        
        elif select_inv == "MRI":
            # Ensure the form_data is initialized
            if 'form_data' not in st.session_state:
                st.session_state.form_data = {}

            # Creating input fields for MRI results
            r1c1, r1c2, r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["MRI Brain"] = st.selectbox("MRI Brain", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["MRI Brain"] == "Abnormal":
                    st.session_state.form_data["MRI Brain-Comments"] = st.text_area("MRI Brain-Comments", 
                        value=st.session_state.form_data.get("MRI Brain-Comments", "")
                    )
                st.session_state.form_data["MRI Lungs"] = st.selectbox("MRI Lungs", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["MRI Lungs"] == "Abnormal":
                    st.session_state.form_data["MRI Lungs-Comments"] = st.text_area("MRI Lungs-Comments", 
                        value=st.session_state.form_data.get("MRI Lungs-Comments", "")
                    )
                st.session_state.form_data["MRI Abdomen"] = st.selectbox("MRI Abdomen", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["MRI Abdomen"] == "Abnormal":
                    st.session_state.form_data["MRI Abdomen-Comments"] = st.text_area("MRI Abdomen-Comments", 
                        value=st.session_state.form_data.get("MRI Abdomen-Comments", "")
                    )
                st.session_state.form_data["MRI Spine"] = st.selectbox("MRI Spine", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["MRI Spine"] == "Abnormal":
                    st.session_state.form_data["MRI Spine-Comments"] = st.text_area("MRI Spine-Comments", 
                        value=st.session_state.form_data.get("MRI Spine-Comments", "")
                    )
                st.session_state.form_data["MRI Pelvis"] = st.selectbox("MRI Pelvis", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["MRI Pelvis"] == "Abnormal":
                    st.session_state.form_data["MRI Pelvis-Comments"] = st.text_area("MRI Pelvis-Comments", 
                        value=st.session_state.form_data.get("MRI Pelvis-Comments", "")
                    )
                    
            with r1c2:
                st.text_input("Unit (in mg/dL)", key="mri")
                st.text_input("Unit (in mg/dL)", key="mrilungs")
                st.text_input("Unit (in mg/dL)", key="mriabdomen")
                st.text_input("Unit (in mg/dL)", key="mrispine")
                st.text_input("Unit (in mg/dL)", key="mripelvis")
                
                    
            with r1c3:
                st.text_input("Reference Range", key="mri1")
                st.text_input("Reference Range", key="mrilungs1")
                st.text_input("Reference Range", key="mriabdomen1")
                st.text_input("Reference Range", key="mrispine1")
                st.text_input("Reference Range", key="mripelvis1")

            # Save button layout
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])

            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Prepare SQL insertion
                    sql = """
                        INSERT INTO mri (
                            entry_date, emp_no,
                            brain, brain_comments,
                            mri_lungs, mri_lungs_comments,
                            abdomen, abdomen_comments,
                            spine, spine_comments,
                            pelvis, pelvis_comments
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """

                    data = (
                        datetime.now().date(),  # entry_date
                        st.session_state.form_data['Employee ID'],  # emp_no
                        st.session_state.form_data["MRI Brain"],
                        st.session_state.form_data.get("MRI Brain-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["MRI Lungs"],
                        st.session_state.form_data.get("MRI Lungs-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["MRI Abdomen"],
                        st.session_state.form_data.get("MRI Abdomen-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["MRI Spine"],
                        st.session_state.form_data.get("MRI Spine-Comments", ""),  # Comment if Abnormal
                        st.session_state.form_data["MRI Pelvis"],
                        st.session_state.form_data.get("MRI Pelvis-Comments", "")  # Comment if Abnormal
                    )

                    # Assuming you have already established a connection
                    try:
                        cursor.execute(sql, data)
                        connection.commit()
                        st.write("Data Saved Successfully")
                    except mysql.connector.Error as e:
                        st.write(f"Error saving data: {e}")
                    
            

        
        
    elif form_name == "Fitness":
            st.header("Fitness")

            col1, col2 = st.columns(2)

            
            with col1:
                choice_tremors = st.radio("Tremors", ( "Positive", "Negative"), key="tremors_choice",index=None)

        
            with col2:
                choice_romberg = st.radio("Romberg Test", ( "Positive", "Negative"), key="romberg_choice",index=None)

            
            with col1:
                choice_acrophobia = st.radio("Acrophobia", ("Positive", "Negative"), key="acrophobia_choice",index=None)
                
            with col2:
                choice_trendelenberg = st.radio("Trendelenberg Test", ( "Positive", "Negative"), key="trendelenberg_choice",index=None)


            st.markdown("### Job Nature (Select Multiple Options)")
            st.multiselect("Select the options",["Heightworks","2","3","4","5"])
            if(accessLevel=="doctor"):    
                st.radio("Overall Fitness",("Fit to join","Unfit","Conditional fit"),index=None)
                st.text_area("Notable Remark")
            # Layout for Add Data button
            r3c1, r3c2, r3c3 = st.columns([6, 4, 4])

            with r3c3:
                if st.button("Add Data", type="primary"):
                    # Collect form data
                    patient_id = st.session_state.form_data.get('Employee ID')  # Assuming you have Employee ID from the earlier form
                    fitness_status = ", ".join(st.session_state.form_data["Fitness"])  # Join selected fitness options
                    fitness_comments = st.session_state.form_data["Fitness-Comments"]

                    # Insert the data into the MySQL fitness table
                    insert_query = f"""
                    INSERT INTO fitness (PatientID, Status, comments, emp_no)
                    VALUES ('{patient_id}', '{fitness_status}', '{fitness_comments}', '{emp_no}')
                    """

                    try:
                        # Execute the insert query
                        cursor.execute(insert_query)
                        connection.commit()  # Ensure to commit the transaction
                        st.success("Data Saved Successfully")
                    except Exception as e:
                        st.error(f"Error saving data: {str(e)}")
            if(accessLevel=='doctor'):
                st.subheader("Generate Form")
                selected_forms = st.multiselect("Form",["Form 17","Form 27","Form 39","Form 40","Form 38"])
                if st.button("Submit"):
                    # Check the selected forms
                    individual_forms = ["Form 27", "Form 40", "Form 38"]
                    group_forms = ["Form 17", "Form 39"]

                    selected_individual = [form for form in selected_forms if form in individual_forms]
                    selected_group = [form for form in selected_forms if form in group_forms]

                    # Display Individual Forms
                    if selected_individual:
                        st.subheader("Individual Forms Selected")
                        for form in selected_individual:
                            st.write(f"- {form}")

                    # Display Group Forms
                    if selected_group:
                        st.subheader("Group Forms Selected")
                        for form in selected_group:
                            st.write(f"- {form}")
            
        
    elif form_name == "Consultation":
        st.header("Consultation")

        # Reason for visit
        if(visitreason == "Annual / Periodic" or visitreason == "Periodic (FH)"):
            st.session_state.form_data["Remarks"] = st.text_area("Remarks", value=st.session_state.form_data.get("Remarks", ""))
            st.file_uploader("Upload Self Declaration", type=['xlsx'], key="Self-declaration")
            st.file_uploader("Upload Reports", type=['xlsx'], key="Reports")
        elif(visitreason in ["Camps (Mandatory)", "Camps (Optional)", "Illness", "Follow up Visits", "BP Sugar (Abnormal)", "Injury Outside the premises"]):
            st.session_state.form_data["Remarks"] = st.text_area("Remarks", value=st.session_state.form_data.get("Remarks", ""))
            st.file_uploader("Upload Reports", type=['xlsx'], key="Reports")
            if(select1 == "Unhealthy" and visitreason in ["Illness", "Follow up Visits", "BP Sugar (Abnormal)", "Injury Outside the premises"]):
                st.session_state.form_data["Diagnosis"] = st.text_area("Diagnosis", value=st.session_state.form_data.get("Diagnosis", ""))
                st.session_state.form_data["Complaints"] = st.text_area("Complaints", value=st.session_state.form_data.get("Complaints", ""))
        elif(select1 == "Unhealthy" and visitreason in ["Over counter Illness", "Over counter Injury"]):
            st.session_state.form_data["Complaints"] = st.text_area("Complaints", value=st.session_state.form_data.get("Complaints", ""))
            st.session_state.form_data["Diagnosis"] = st.text_area("Diagnosis", value=st.session_state.form_data.get("Diagnosis", ""))
            
            st.session_state.form_data["Notble Remarks"] = st.text_area("Notable Remarks", value=st.session_state.form_data.get("Notable Remarks", ""))        
        elif(visitreason in ["Special Work Fitness", "Special Work Fitness (Renewal)"]):
            st.file_uploader("Upload Self Declaration", type=['xlsx'], key="Self-declaration")
        elif(visitreason == "Fitness After Medical Leave"):
            st.file_uploader("Upload Self Declaration", type=['xlsx'], key="Self-declaration")
            st.file_uploader("Upload FC External", type=['xlsx'], key="FC-external")
            st.file_uploader("Upload Reports", type=['xlsx'], key="Reports")
        elif(visitreason == "Over counter Injury Outside the premises" or (visitreason == None and select1 == "Unhealthy")):
            st.session_state.form_data["Remarks"] = st.text_area("Remarks", value=st.session_state.form_data.get("Remarks", ""))
            st.session_state.form_data["Diagnosis"] = st.text_area("Diagnosis", value=st.session_state.form_data.get("Diagnosis", ""))
            st.session_state.form_data["Complaints"] = st.text_area("Complaints", value=st.session_state.form_data.get("Complaints", ""))

        else:
            st.session_state.form_data["Remarks"] = st.text_area("Remarks", value=st.session_state.form_data.get("Remarks", ""))
            st.file_uploader("Upload Self Declaration", type=['xlsx'], key="Self-declaration")
            st.file_uploader("Upload FC External", type=['xlsx'], key="FC-external")
            st.file_uploader("Upload Reports", type=['xlsx'], key="Reports")

        st.header("Referral")

        # Condition Type Radio Button
        condition_type = st.radio(
            "Condition Type",
            (
                "Occupational (Illness/Injury/Disease)", 
                "Non-occupational (Injury)", 
                "Domestic (Injury)", 
                "Commutation (Injury)", 
                "Others (Comment)"
            ),
            index=None
        )

        # Text input for investigation
        investigation = st.text_input(
            "Investigation",
            placeholder="Suggest to do FBS/HbA1c"
        )

        # Text input for advice
        advice = st.text_input(
            "Advice",
            placeholder="E.g., Diet/Exercise/Salt/Hydration/BP/Sugar Control, Alcohol Abstinence, Fat-free/Oil-free"
        )

        # Referral Radio Button
        referral = st.radio(
            "Referral",
            ("Yes", "No"),
            index=None
        )

        # Text input for hospital name
        hospital_name = st.text_input(
            "Name of the Hospital",
            placeholder="Comments..."
        )

        # Text input for doctor name
        doctor_name = st.text_input(
            "Doctor Name",
            placeholder="Comments..."
        )

        # Columns layout
        col1, col2 = st.columns(2)

        # You can add content to col1 and col2 if needed
        

        

        st.write("""
            <div style='float:right;margin-right:100px;margin-top:25px'>
            </div>
            
            <!-- Dropdown for Consulted Dr -->
            <label for="consultedBy">Consulted Dr:</label>
            <select style='height:35px;width:150px;text-align:center;background-color:rgb(240,242,246);border:none;border-radius:5px;' name="consultedBy" id="consultedBy">
                <option value="DrX">Dr. X</option>
                <option value="DrY">Dr. Y</option>
                <option value="DrZ">Dr. Z</option>
            </select>
        """, unsafe_allow_html=True)

        if st.button("Submit", type="primary"):
            # Collect form data
            emp_no = st.session_state.form_data.get('Employee ID')  # Assuming Employee ID was collected earlier
            complaints = st.session_state.form_data.get("Complaints", "")
            diagnosis = st.session_state.form_data.get("Diagnosis", "")
            remarks = st.session_state.form_data.get("Remarks", "")
            
            # Construct the SQL query to insert data into the consultation table
            insert_query = f"""
            INSERT INTO consultation (emp_no, entry_date, complaints, diagnosis, remarks)
            VALUES ('{emp_no}', CURDATE(), '{complaints}', '{diagnosis}', '{remarks}')
            """

            try:
                # Execute the query
                cursor.execute(insert_query)
                connection.commit()  # Commit transaction
                st.success("Consultation Data Saved Successfully")
            except Exception as e:
                st.error(f"Error saving consultation data: {str(e)}")
            finally:
                st.rerun()  # Rerun the app to reset the state
        


    elif form_name == "Medical History":
        
        # Personal History -> multi select box
        #     Smoker
        #     Alcoholic
        #     Veg
        #     Mixed Diet
        # Medical History - multi select box
        #     BP
        #     DM
        #     Others
        # Surgical History -> header
        #     Family History -> sub header
        #         Father    -> text_area
        #         Mother    -> text_area

        # Personal History Section
        st.markdown("<h3 style='margin-left:30px;'> Personal History </h4>", unsafe_allow_html=True)

        # List of personal habits and dietary preferences
        personal_history_options = [
            {"Habit": "Smoker", "Details": "E.g., past 5 years, 10 per day"},
            {"Habit": "Alcoholic", "Details": "E.g., past 10 years, occasional, quarter a day"},
            {"Habit": "Paan, Beetal Chewer", "Details": "E.g., frequency or duration"},
            {"Habit": "Pure Veg", "Details": ""},
            {"Habit": "Eggetarian", "Details": ""},
            {"Habit": "Mixed Diet", "Details": ""}
        ]

        st.subheader("Smoking")
        smoker = st.selectbox("Are you a smoker?", ["Yes", "No"])
        if smoker == "Yes":
            smoking_duration = st.number_input("How many years have you been smoking?", min_value=1, max_value=50)
            cigarettes_per_day = st.number_input("How many cigarettes do you smoke per day?", min_value=1, max_value=50)

        # Alcohol Consumption Section
        st.subheader("Alcohol Consumption")
        alcoholic = st.selectbox("Do you consume alcohol?", ["Yes", "No"])
        if alcoholic == "Yes":
            drinking_duration = st.number_input("How many years have you been drinking?", min_value=1, max_value=50)
            drinking_frequency = st.radio("How often do you drink?", ["Occasional", "Daily", "Weekly"])
            if drinking_frequency == "Daily":
                daily_quantity = st.text_input("Daily consumption (e.g., 'quarter a day')")

        # Paan, Betel Chewing Section
        st.subheader("Paan/Betel Chewing")
        chewer = st.selectbox("Do you chew paan or betel?", ["Yes", "No"])
        if chewer == "Yes":
            chewing_duration = st.number_input("How many years have you been chewing?", min_value=1, max_value=50)

        # Display radio buttons for dietary preferences
        pure_veg = st.radio(
            "Dietary Preference",
            options=["Pure Veg", "Eggetarian", "Mixed Diet"],
            index=0,  # Default selection
            help="Select your dietary preference."
        )

        # Append data to the personal history
        st.session_state.form_data["PersonalHistory"] = [{"Habit": "Diet", "Details": pure_veg}]


        # Personal Medical History Section
        st.markdown("<h4 style='margin-left:30px;'> Medical History </h4>", unsafe_allow_html=True)

        # List of conditions
        conditions = [
            "HTN", "DM", "Epileptic", "Hyper thyroid", "Hypo thyroid", "Asthma",
            "CVS", "CNS", "RS", "GIT", "KUB", "CANCER", 
            "Defective Colour Vision", "OTHERS"
        ]

        # Data structure to store medical history
        personal_medical_history = []

        # Input fields for each condition
        for condition in conditions:
            st.markdown(f"### {condition}")
            detail = st.text_input(f"Detail for {condition}", key=f"{condition}_detail", placeholder="E.g., 10 years")
            comments = st.text_area(f"Comments for {condition}", key=f"{condition}_comments", placeholder="E.g., On Ayurvedic medicines")
            personal_medical_history.append({
                "Condition": condition,
                "Detail": detail,
                "Comments": comments
            })

        # Additional fields for female workers
        st.markdown("<h5 style='margin-left:30px;'> Female Workers </h5>", unsafe_allow_html=True)

        female_history = {
            "Obstetric": st.text_area(
                "Obstetric History", key="obstetric_history", 
                placeholder="E.g., G3 P1 L1 A1; P2 L1 A1"
            ),
            "Gynec": st.text_area(
                "Gynaecological History", key="gynec_history",
                placeholder="Add any gynecological details"
            )
        }

        # Save the data in session state
        st.session_state.form_data["PersonalMedicalHistory"] = personal_medical_history
        st.session_state.form_data["FemaleHistory"] = female_history



        # Surgical History Section
        st.header("Surgical History")
        surgical_comments = st.text_area(
            "Comments",
            placeholder="Enter details about any past surgeries...",
            help="Provide details about any past surgical procedures."
        )
        st.session_state.form_data["Surgical History"] = surgical_comments

        columns = ["Relationship", "Status", "Reason (if Expired)", "Remarks (Health Condition)"]
        parents_data = [
            {"Relationship": "FATHER", "Status": "", "Reason": "", "Remarks": ""},
            {"Relationship": "Paternal Grandfather", "Status": "", "Reason": "", "Remarks": ""},
            {"Relationship": "Paternal Grandmother", "Status": "", "Reason": "", "Remarks": ""},
            {"Relationship": "MOTHER", "Status": "", "Reason": "", "Remarks": ""},
            {"Relationship": "Maternal Grandfather", "Status": "", "Reason": "", "Remarks": ""},
            {"Relationship": "Maternal Grandmother", "Status": "", "Reason": "", "Remarks": ""},
        ]

        st.markdown("<h4 style='margin-left:30px;'> Children </h4>", unsafe_allow_html=True)

        # Number of children to record
        num_children = st.number_input(
            "Enter the number of children", min_value=1, max_value=10, step=1, key="num_children"
        )

        # Initialize the children data structure
        children = []

        for i in range(1, num_children + 1):
            st.markdown(f"<h5 style='margin-left:30px;'> Child {i} </h5>", unsafe_allow_html=True)
            child = {
                "No.": i,
                "Sex": st.selectbox(
                    f"Sex for Child {i}", options=["Male", "Female"], key=f"child_{i}_sex"
                ),
                "Date of Birth": st.date_input(
                    f"Date of Birth for Child {i}", key=f"child_{i}_dob"
                ),
                "Status": st.selectbox(
                    f"Status for Child {i}", options=["Alive", "Expired"], key=f"child_{i}_status"
                ),
                "Reason (if Expired)": st.text_input(
                    f"Reason (if Expired) for Child {i}",
                    key=f"child_{i}_reason",
                    placeholder="Provide reason if child is expired"
                ),
                "Remarks": st.text_input(
                    f"Remarks (Health condition) for Child {i}",
                    key=f"child_{i}_remarks",
                    placeholder="For example, autism, congenital disorder, etc."
                ),
            }
            children.append(child)

        # Save the children data in session state
        st.session_state.form_data["Children"] = children

        # Parents & Grandparents Section
        st.markdown("<h4 style='margin-left:30px;'> Parents & Grandparents </h4>", unsafe_allow_html=True)

        # Display input fields for each row in Parents & Grandparents table
        for row in parents_data:
            st.markdown(f"{row['Relationship']}")
            row["Status"] = st.selectbox(
                "Status", ["", "Alive", "Expired"], key=f"{row['Relationship']}_status"
            )
            row["Reason"] = st.text_input("Reason (if Expired)", key=f"{row['Relationship']}_reason")
            row["Remarks"] = st.text_area("Remarks (Health Condition)", key=f"{row['Relationship']}_remarks",placeholder="Health condition for eg stroke..") 
        st.session_state.form_data["ParentsDetails"] = parents_data

        # Conditions Section
        st.markdown("<h4 style='margin-left:30px;'> Health Conditions </h4>", unsafe_allow_html=True)

        conditions = [
            {"Condition": "HTN", "Relationship": []},
            {"Condition": "DM", "Relationship": []},
            {"Condition": "Epileptic", "Relationship": []},
            {"Condition": "Hyper thyroid", "Relationship": []},
            {"Condition": "Hypo thyroid", "Relationship": []},
            {"Condition": "Asthma", "Relationship": []},
            {"Condition": "CVS", "Relationship": []},
            {"Condition": "CNS", "Relationship": []},
            {"Condition": "RS", "Relationship": []},
            {"Condition": "GIT", "Relationship": []},
            {"Condition": "KUB", "Relationship": []},
            {"Condition": "Cancer", "Relationship": []},
            {"Condition": "Others", "Relationship": []},
        ]

        relationships = ["Father: BP", "Father: DM", "Mother: BP", "Mother: DM", "Others"]

        for condition in conditions:
            if condition["Condition"] == "CVS":
                # Multiselect for CVS
                condition["Relationship"] = st.multiselect(
                    f"Relationship for {condition['Condition']}",
                    relationships,
                    key=f"{condition['Condition']}_relationship"
                )
                # Additional text box for remarks in CVS
                condition["Remarks"] = st.text_input(
                    f"Remarks for {condition['Condition']}",
                    key=f"{condition['Condition']}_remarks",
                    placeholder="Eg :Father stent, maternal grandmother pacemaker"
                )
            else:
                # Multiselect for other conditions
                condition["Relationship"] = st.multiselect(
                    f"Relationship for {condition['Condition']}",
                    relationships,
                    key=f"{condition['Condition']}_relationship"
                )

        # Save to session state
        st.session_state.form_data["HealthConditions"] = conditions

        # Dropdown for Nurse and Doctor
        st.write("""
            <div style='float:right;margin-right:100px;margin-top:25px'>
            </div>
            <label for="submittedBy">Submitted By Nurse:</label>
            <select style='height:35px;width:150px;text-align:center;background-color:rgb(240,242,246);border:none;border-radius:5px;' name="submittedBy" id="submittedBy">
                <option value="Nurse1">Nurse 1</option>
                <option value="Nurse2">Nurse 2</option>
                <option value="Nurse3">Nurse 3</option>
            </select>
            <label for="bookedTo">Patient Booked to Dr:</label>
            <select style='height:35px;width:150px;text-align:center;background-color:rgb(240,242,246);border:none;border-radius:5px;' name="bookedTo" id="bookedTo">
                <option value="DrA">Dr. A</option>
                <option value="DrB">Dr. B</option>
                <option value="DrC">Dr. C</option>
            </select>
        """, unsafe_allow_html=True)

        r3c1,r3c2,r3c3 = st.columns([6,4,4])

        

        
        
        with r3c3:
            if st.button("Add Data", type="primary"):
                st.write("Data Saved")
                st.session_state.form_data["visitreason"] = visitreason
                st.rerun()

            if st.button("Submit", type="primary"):
                i = st.session_state.form_data  # Form data collected

                try:
                    # Step 1: Get the current date
                    today = datetime.now()
                    day = today.strftime("%d")
                    month = today.strftime("%m")
                    year = today.strftime("%y")

                    # Step 2: Query database for the current date's entries
                    cursor.execute("SELECT COUNT(*) FROM medicalpersonalhist WHERE entry_date = %s", (today.date(),))
                    count = cursor.fetchone()[0]

                    # Step 3: Generate the OHCVisitno
                    auto_increment_no = f"{count + 1:03d}"  # Format with leading zeroes (001, 002, ...)
                    OHCVisitno = f"{auto_increment_no}{day}{month}{year}"

                    # Temporary Debug Output
                    st.write(f"Debug Info: auto_increment_no = {auto_increment_no}, day = {day}, month = {month}, year = {year}")
                    st.write(f"Generated OHCVisitno: {OHCVisitno}")

                    # Step 4: Insert the data into the database
                    insert_basicdetails = (
                        "INSERT INTO medicalpersonalhist (emp_no, entry_date, OHCVisitno, personal_history, medical_history, "
                        "surgical_history, father, mother, diet, smoker, alcoholic, drug_allergy, food_allergy, other_allergy) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    )
                    basicdetails_data = (
                        i.get('Employee ID'), today.date(), OHCVisitno, 
                        i.get('Personal History'), i.get('Medical History'), i.get('Surgical History'),
                        i.get('Father'), i.get('Mother'), i.get('Diet'),
                        i.get('Smoker'), i.get('Alcoholic'), i.get('Drug Allergy'),
                        i.get('Food Allergy'), i.get('Other Allergy')
                    )
                    cursor.execute(insert_basicdetails, basicdetails_data)
                    connection.commit()

                    st.success(f"Data saved successfully! Generated OHCVisitno: {OHCVisitno}")
                except Exception as e:
                    st.error(f"Error: {e}")

                try:
                    insert_vitals = ("INSERT INTO vitals(emp_no, entry_date, Systolic, Diastolic, PulseRate, SpO2, Temperature, RespiratoryRate, Height, Weight, BMI) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)") 
                    vitals_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Systolic"), i.get("Diastolic"), i.get("Pulse"), i.get("spo2"), i.get("Temperature"), i.get("Respiratory Rate"), i.get("Height"), i.get("Weight"), i.get("BMI"))
                    cursor.execute(insert_vitals, vitals_values)
                    connection.commit()
                    st.write("Vitals Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in vitals")

                
                try:
                    insert_hematology = ("INSERT INTO hematology_result(emp_no, entry_date, heamoglobin,  rbc_count, wbc_count, haemotocrit, mcv, mch, mchc, platelet, rdw, neutrophil, lymphocyte, eosinophil, monocyte, basophils, esr, pbs_rbc, pbc_parasites, pbc_others) VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)")
                    hematology_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Hemoglobin"), i.get("Total RBC"), i.get("Total WBC"), i.get("PCV"), i.get("MCV"), i.get("MCH"), i.get("MCHC"), i.get("Platelet Count"), i.get("RDW"), i.get("Neutrophil"), i.get("Lymphocyte"), i.get("Eosinophil"), i.get("Monocyte"), i.get("Basophil"), i.get("ESR"), i.get("Preipheral Blood Smear - RBC Morphology"), i.get("Preipheral Blood Smear - Parasites"), i.get("Preipheral Blood Smear - Others"))
                    cursor.execute(insert_hematology, hematology_values)
                    connection.commit()
                    st.write("Hematology Inserted")

                except Exception as e:
                    st.write(e)
                    st.write("Error in hematology")

                try:
                    insert_rst = ("INSERT INTO routine_sugartest(emp_no, entry_date, glucosef, glucosepp, rbs, eag, hba1c) VALUES(%s, %s, %s, %s, %s, %s, %s)")
                    rst_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Glucose (F)"), i.get("Glucose (PP)"), i.get("Random Blood sugar"), i.get("Estimated Average Glucose"), i.get("HbA1c"))
                    cursor.execute(insert_rst, rst_values)
                    connection.commit()
                    st.write("Data Submitted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in rst")

                try:
                    insert_rft = ("INSERT INTO rft_result(entry_date, emp_no, urea, bun, sr_creatinine, uric_acid, sodium, potassium, calcium, phosphorus, chloride, bicarbonate ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                    rft_values = (i.get("Visit Date"), i.get('Employee ID'), i.get("Urea"), i.get("Blood urea nitrogen (BUN)"), i.get("Sr.Creatinine"), i.get("Uric acid"), i.get("Sodium"), i.get("Potassium"), i.get("Calcium"), i.get("Phosphorus"), i.get("Chloride"), i.get("Bicarbonate"))                    
                    cursor.execute(insert_rft, rft_values)
                    connection.commit()
                    st.write("RFT Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in rft")

                    
                try:
                    insert_lipid_prof = ("INSERT INTO lipid_profile(emp_no, entry_date, tcholesterol,triglycerides, hdl_cholesterol, vldl_cholesterol, ldl_cholesterol, chol_hdlratio, ldlhdlratio) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    lipid_prof_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Total Cholesterol"), i.get("Triglycerides"), i.get("HDL - Cholesterol"), i.get("VLDL -Choleserol"), i.get("LDL- Cholesterol"), i.get("CHOL HDL ratio"), i.get("LDL.CHOL/HDL.CHOL Ratio"))                    
                    cursor.execute(insert_lipid_prof, lipid_prof_values)
                    connection.commit()
                    st.write("Lipid Profile Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in lipid profile")

                try:
                    insert_lft = ("INSERT INTO liver_function(emp_no, entry_date, bilirubin_total, bilirubin_direct, bilirubin_indirect, sgot_alt, sgpt_alt, alkaline_phosphatase, total_protein, albumin, globulin, alb_globratio, gammagt) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")
                    lft_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Bilirubin - Total"), i.get("Bilirubin - Direct"), i.get("Bilirubin - Indirect"), i.get("SGOT /AST"), i.get("SGPT /ALT"), i.get("Alkaline phosphatase"), i.get("Total Protein"), i.get("Albumin (Serum )"), i.get("Globulin(Serum)"), i.get("Alb/Glob Ratio"), i.get("Gamma Glutamyl transferase"))                    
                    cursor.execute(insert_lft, lft_values)
                    connection.commit()
                    st.write("LFT Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in lft")
                
                try:
                    insert_tft = ("INSERT INTO thyroid_function_test(emp_no, entry_date, t3, t4, tsh) VALUES(%s, %s, %s, %s, %s)")
                    tft_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("T3- Triiodothyroine"), i.get("T4 - Thyroxine"), i.get("TSH- Thyroid Stimulating Hormone"))                    
                    cursor.execute(insert_tft, tft_values)
                    connection.commit()
                    st.write("TFT Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in tft")

                try:
                    insert_ait = ("INSERT INTO autoimmune_test(emp_no, entry_date, ana, adna, anticardiolipin, rheumatoid) VALUES(%s, %s, %s, %s, %s, %s)")
                    ait_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("ANA (Antinuclear Antibody)"), i.get("Anti ds DNA"), i.get("Anticardiolipin Antibodies (IgG & IgM)"), i.get("Rheumatoid factor"))
                    cursor.execute(insert_ait, ait_values)
                    connection.commit()
                    st.write("AIT Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in ait")

                try:
                    insert_coagulation = ("INSERT INTO coagulation_test(emp_no, entry_date, pt, ptinr, bt, ct) VALUES(%s, %s, %s, %s, %s, %s)")
                    coagulation_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Prothrombin Time (PT)"), i.get("PT INR"), i.get("Bleeding Time (BT)"), i.get("Clotting Time (CT)"))
                    cursor.execute(insert_coagulation, coagulation_values)
                    connection.commit()
                    st.write("Coagulation Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in coagulation")

                try:
                    insert_enzymes_cardio = ("INSERT INTO enzymes_cardio(emp_no, entry_date,acid_phosphatase,adenosine,amylase,lipase,troponin_t, troponin_i, cpk_total, cpk_mb, ecg, ecg_comments, echo,echo_comments, tmt, tmt_comments) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    enzymes_cardio_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Acid Phosphatase"), i.get("Adenosine Deaminase"), i.get("Amylase"), i.get("Lipase"), i.get("Troponin- T"), i.get("Troponin- I"), i.get("CPK - Total"), i.get("CPK - MB"), i.get("ECG"), i.get("ECG-Comments"), i.get("ECHO"), i.get("ECHO-Comments"), i.get("TMT"), i.get("TMT-Comments"))
                    cursor.execute(insert_enzymes_cardio, enzymes_cardio_values)
                    connection.commit()
                    st.write("Enzymes Cardio Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in enzymes cardio")
                
                try:
                    insert_urine_routine = ("INSERT INTO urine_routine(emp_no, entry_date, colour, apperance, reaction, specific_gravity, protein_albumin, glucose, ketone, urobilinogen, bile_salts, bile_pigments, wbc_pluscells, rbc, epithelial_cell, casts, crystals, bacteria) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    urine_routine_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Colour"), i.get("Appearance"), i.get("Reaction (pH)"), i.get("Specific Gravity"), i.get("Protein/Albumin"), i.get("Glucose (Urine)"), i.get("Ketone Bodies"), i.get("Urobilinogen"), i.get("Bile Salts"), i.get("Bile Pigments"), i.get("WBC / Pus cells"), i.get("Red Blood Cells"), i.get("Epithelial celss"), i.get("Casts"), i.get("Crystals"), i.get("Bacteria"))
                    cursor.execute(insert_urine_routine, urine_routine_values)
                    connection.commit()
                    st.write("Urine Routine Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in urine routine")

                try:
                    insert_serology = ("INSERT INTO serology_result(emp_no, entry_date, hiv_screening , hbsag, hcv, widal, vdrl, denguens, dengueigg, dengueigm) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    serology_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Screening For HIV I & II"), i.get("HBsAg"), i.get("HCV"), i.get("WIDAL"), i.get("VDRL"), i.get("Dengue NS1Ag"), i.get("Dengue IgG"), i.get("Dengue IgM"))
                    cursor.execute(insert_serology, serology_values)
                    connection.commit()
                    st.write("Serology Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in serology")

                try:
                    insert_motion = ("INSERT INTO motion(emp_no, entry_date, colour, appearance, occult_blood, ova, cyst, mucus, pus_cells, rbcs, others_t) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    motion_values = (i.get('Employee ID'), i.get("Visi Date"), i.get("Colour (Motion)"), i.get("Appearance (Motion)"), i.get("Occult Blood"), i.get("Ova"), i.get("Cyst"), i.get("Mucus"), i.get("Pus Cells"), i.get("RBCs"), i.get("Others"))
                    cursor.execute(insert_motion, motion_values)
                    connection.commit()
                    st.write("Motion Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in motion")

                try:
                    insert_routie_culture = ("INSERT INTO routine_culture(emp_no, entry_date, urine, motion, sputum, blood) VALUES( %s, %s, %s, %s, %s, %s)")
                    routine_culture_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Urine"), i.get("Motion"), i.get("Sputum"), i.get("Blood"))
                    cursor.execute(insert_routie_culture, routine_culture_values)
                    connection.commit()
                    st.write("Routine Culture Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in routine culture")

                try:
                    insert_mens_pack = ("INSERT INTO mens_pack(emp_no, entry_date, psa) VALUES(%s, %s, %s)")
                    mens_pack_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("PSA (Prostate specific Antigen)"))
                    cursor.execute(insert_mens_pack, mens_pack_values)
                    connection.commit()
                    st.write("Mens Pack Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in mens pack")
                
                try:
                    insert_womens_pack = ("INSERT INTO womens_pack(emp_no, entry_date, mammogram_nm_ab, mammogram_comment, pap_nm_ab, pap_comment) VALUES(%s, %s, %s, %s, %s, %s)")
                    womens_pack_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Mammogram"), i.get("Mammogram-Comments"), i.get("PAP Smear"), i.get("PAP Smear-Comments"))
                    cursor.execute(insert_womens_pack, womens_pack_values)
                    connection.commit()
                    st.write("Womens Pack Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in womens pack")

                try:
                    insert_occupational_profile = ("INSERT INTO occupational_profile(emp_no, entry_date, audiometry_nm_ab, audiometry_comment, pft_nm_ab, pft_comment) VALUES(%s, %s, %s, %s, %s, %s)")
                    occupational_profile_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Audiometry"), i.get("Audiometry-Comments"), i.get("PFT"), i.get("PFT-Comments"))
                    cursor.execute(insert_occupational_profile, occupational_profile_values)
                    connection.commit()
                    st.write("Occupational Profile Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in occupational profile")
                

                try:
                    insert_other_test = ("INSERT INTO other_tests(emp_no, entry_date, pathology, pathology_comments) VALUES(%s, %s, %s, %s)")
                    other_test_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Pathology"), i.get("Pathology-Comments"))
                    cursor.execute(insert_other_test, other_test_values)
                    connection.commit()
                    st.write("Other Test Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in other test")

                try:
                    insert_ophthalmic_report = ("INSERT INTO ophthalmic_report(emp_no, entry_date, vision, vision_comments, colourvision, colourvision_comment) VALUES(%s, %s, %s, %s, %s, %s)")
                    ophthalmic_report_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Vision"), i.get("Vision-Comments"), i.get("Colour Vision"), i.get("Colour Vision-Comments"))
                    cursor.execute(insert_ophthalmic_report, ophthalmic_report_values)
                    connection.commit()
                    st.write("Ophthalmic Report Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in ophthalmic report")

                try:
                    insert_x_ray = ("INSERT INTO x_ray(emp_no, entry_date, chest_nm_ab, chest_comment, spine_nm_ab, spine_comment, abdomen_nm_ab, abdomen_comment, kub_nm_ab, kub_comment, pelvis_nm_ab, pelvis_comment) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    x_ray_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("X-RAY Chest"), i.get("X-RAY Chest-Comments"), i.get("X-RAY Spine"), i.get("X-RAY Spine-Comments"), i.get("X-RAY Abdomen"), i.get("X-RAY Abdomen-Comments"), i.get("X-RAY KUB"), i.get("X-RAY KUB-Comments"), i.get("X-RAY Pelvis"), i.get("X-RAY Pelvis-Comments"))
                    cursor.execute(insert_x_ray, x_ray_values)
                    connection.commit()
                    st.write("X-Ray Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in x-ray")
                
                try:
                    insert_usg = ("INSERT INTO usg(emp_no, entry_date, abdomen, abdomen_comments, pelvis, pelvis_comments,neck, neck_comments, kub, kub_comments) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    usg_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("USG ABDOMEN"), i.get("USG ABDOMEN-Comments"), i.get("USG Pelvis"), i.get("USG Pelvis-Comments"), i.get("USG Neck"), i.get("USG Neck-Comments"), i.get("USG KUB"), i.get("USG KUB-Comments"))
                    cursor.execute(insert_usg, usg_values)
                    connection.commit()
                    st.write("USG Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in usg")
                
                try:
                    insert_ct_report = ("INSERT INTO ct_report(emp_no, entry_date, brain, brain_comment, abdomen, abdomen_comment, pelvis, pelvis_comment, ct_lungs, ct_lungs_comment, spine, spine_comment) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    ct_report_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("CT Brain"), i.get("CT Brain-Comments"), i.get("CT Abdomen"), i.get("CT Abdomen-Comments"), i.get("CT Pelvis"), i.get("CT Pelvis-Comments"), i.get("CT Lungs"), i.get("CT Lungs-Comments"), i.get("CT Spine"), i.get("CT Spine-Comments"))
                    cursor.execute(insert_ct_report, ct_report_values)
                    connection.commit()
                    st.write("CT Report Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in ct report")

                try:
                    insert_mri_report = ("INSERT INTO mri(emp_no, entry_date, brain, brain_comments, abdomen, abdomen_comments, pelvis, pelvis_comments, mri_lungs, mri_lungs_comments, spine, spine_comments) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    mri_report_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("MRI Brain"), i.get("MRI Brain-Comments"), i.get("MRI Abdomen"), i.get("MRI Abdomen-Comments"), i.get("MRI Pelvis"), i.get("MRI Pelvis-Comments"), i.get("MRI Lungs"), i.get("MRI Lungs-Comments"), i.get("MRI Spine"), i.get("MRI Spine-Comments"))
                    cursor.execute(insert_mri_report, mri_report_values)
                    connection.commit()
                    st.write("MRI Report Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in mri report")
                
                try:
                    insert_consultation = ("INSERT INTO consultation(emp_no, entry_date, complaints, diagnosis, remarks) VALUES(%s, %s, %s, %s, %s)")
                    consultation_values = (i.get('Employee ID'), i.get("Visit Date"), i.get("Complaints"), i.get("Diagnosis"), i.get("Remarks"))
                    cursor.execute(insert_consultation, consultation_values)
                    connection.commit()
                    st.write("Consultation Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in consultation")

                try:
                    insert_medical_history = ("INSERT INTO medicalpersonalhist(emp_no, entry_date, personal_history, medical_history, father, mother) VALUES(%s, %s, %s, %s, %s, %s)")
                    medical_history_values = (i.get('Employee ID'), i.get("Visit Date"), json.dumps(i.get("Personal History")), json.dumps(i.get("Medical History")), i.get("Father"), i.get("Mother"))
                    cursor.execute(insert_medical_history, medical_history_values)
                    connection.commit()
                    st.write("Medical History Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in medical history")

                    
        

    if form_name == "Prescription":
        def get_medicines_by_category(connection, category):
            cursor = connection.cursor()
            query = "SELECT medicine_name FROM pharmacy_inventory WHERE category = %s"
            cursor.execute(query, (category,))
            result = cursor.fetchall()
            cursor.close()
            # Flatten the result and return a list of medicine names
            return [row[0] for row in result]
        def reduce_medicine_quantity(connection, medicine_name, quantity):
            cursor = connection.cursor()
            # Debug information
            print(f"Trying to reduce quantity for {medicine_name} by {quantity}")
            
            # Update quantity
            query = "UPDATE pharmacy_inventory SET quantity = quantity - %s WHERE medicine_name = %s AND quantity >= %s"
            cursor.execute(query, (quantity, medicine_name, quantity))
            connection.commit()
        # Check if rows were affected (if the quantity is reduced)
        if cursor.rowcount == 0:
            #print(f"Medicine {medicine_name} does not have enough stock or does not exist")
            pass
        cursor.close()
    # In the elif block (as described earlier)
        if form_name == "Prescription":
            
            tablets = get_medicines_by_category(connection, "Tablets")
            injections = get_medicines_by_category(connection, "Injection")
            creams = get_medicines_by_category(connection, "Creams")
            others = get_medicines_by_category(connection, "Other")

            tablets = get_medicines_by_category(connection, "Tablets")
            injections = get_medicines_by_category(connection, "Injection")
            creams = get_medicines_by_category(connection, "Creams")
            others = get_medicines_by_category(connection, "Other")

        st.header("Prescription")

        st.write("""
            <style>
                button[kind="primary"] {
                    all: unset;
                    background-color: #22384F;
                    color: white;
                    border-radius: 5px;
                    text-align: center;
                    cursor: pointer;
                    font-size: 20px;
                    width: 10%;
                    padding: 10px;
                    margin-left:1000px;
                }
            </style>
        """, unsafe_allow_html=True)

        # Tablets Section
        st.subheader("Tablets")
        c1, c2, c3, c4, c5 = st.columns([3, 2, 2, 2, 2])
        with c1:
            tablet1 = st.selectbox("Name of the Drug", tablets, index=None, key="tablet1")
            tablet2 = st.selectbox("Name of the Drug", tablets, index=None, key="tablet2")
        with c2:
            qty1 = st.text_input("Qty", key="qty1")
            qty2 = st.text_input("Qtys", key="qty2")

        if st.button("Add Tablets", type='primary'):
            try:
                qty1 = int(qty1)
                qty2 = int(qty2)
                reduce_medicine_quantity(connection, tablet1, qty1)
                reduce_medicine_quantity(connection, tablet2, qty2)
                st.success(f"{tablet1} and {tablet2} quantities updated successfully!")
            except ValueError:
                st.error("Please enter valid quantities.")

        # Injections Section
        st.subheader("Injections")
        c1, c2, c3, c4, c5 = st.columns([3, 2, 2, 2, 2])
        with c1:
            injection1 = st.selectbox("Name of the Drug", injections, index=None, key="injection1")
            injection2 = st.selectbox("Name of the Drug", injections, index=None, key="injection2")
        with c2:
            qty3 = st.text_input("Qty", key="qty3")
            qty4 = st.text_input("Qtys", key="qty4")

        if st.button("Add Injections", type="primary"):
            try:
                qty3 = int(qty3)
                qty4 = int(qty4)
                reduce_medicine_quantity(connection, injection1, qty3)
                reduce_medicine_quantity(connection, injection2, qty4)
                st.success(f"{injection1} and {injection2} quantities updated successfully!")
            except ValueError:
                st.error("Please enter valid quantities.")

        # Creams Section
        st.subheader("Creams")
        c1, c2, c3, c4, c5 = st.columns([3, 2, 2, 2, 2])
        with c1:
            cream1 = st.selectbox("Name of the Drug", creams, index=None, key="cream1")
            cream2 = st.selectbox("Name of the Drug", creams, index=None, key="cream2")
        with c2:
            qty5 = st.text_input("Qty", key="qty5")
            qty6 = st.text_input("Qtys", key="qty6")

        if st.button("Add Creams", type="primary"):
            try:
                qty5 = int(qty5)
                qty6 = int(qty6)
                reduce_medicine_quantity(connection, cream1, qty5)
                reduce_medicine_quantity(connection, cream2, qty6)
                st.success(f"{cream1} and {cream2} quantities updated successfully!")
            except ValueError:
                st.error("Please enter valid quantities.")

        # Others Section
        st.subheader("Others")
        c1, c2, c3, c4, c5 = st.columns([3, 2, 2, 2, 2])
        with c1:
            other1 = st.selectbox("Name of the Drug", others, index=None, key="other1")
            other2 = st.selectbox("Name of the Drug", others, index=None, key="other2")
        with c2:
            qty7 = st.text_input("Qty", key="qty7")
            qty8 = st.text_input("Qtys", key="qty8")

        if st.button("Add Others", type="primary"):
            try:
                qty7 = int(qty7)
                qty8 = int(qty8)
                reduce_medicine_quantity(connection, other1, qty7)
                reduce_medicine_quantity(connection, other2, qty8)
                st.success(f"{other1} and {other2} quantities updated successfully!")
            except ValueError:
                st.error("Please enter valid quantities.")

        # Close the database connection
        connection.close()
            

    elif form_name == "Vaccination":
        
        st.subheader("Vaccination Information")
        r0c1, r0c2 = st.columns([4, 6])
        with r0c1:
            
            st.markdown("<b style='color: #22384F'>Select Vaccine</b>", unsafe_allow_html=True)
            # Select existing vaccine or add a new one
            vaccine = st.selectbox(
                'Select Vaccine',
                ['Select', 'Vaccine 1', 'Vaccine 2', 'Vaccine 3', 'Add New Vaccine'],
                label_visibility='collapsed'  # Added option to add new vaccine
            )
            
            if vaccine == 'Add New Vaccine':
                new_vaccine = st.text_input("Enter New Vaccine Name")  # Input for new vaccine name
                if new_vaccine:
                    st.write(f"New Vaccine Added: {new_vaccine}")
                    vaccine = new_vaccine  # Set the vaccine to the newly entered name
            st.markdown("<b style='color: #22384F'>Status</b>", unsafe_allow_html=True)
            st.selectbox("Status", ["Full", "Partial"], label_visibility='collapsed')

        with r0c2:
            # Columns for entering Normal Doses & Booster Dose
            r3c1, r3c2 = st.columns(2)
            
                
            with r3c1:
                st.markdown("<b style='color: #22384F'>Normal Doses</b>", unsafe_allow_html=True)
                # Create 5 input fields for Normal Doses with numbering
                normal_doses = []
                normal_doses_names = []
                for i in range(1, 6):
                    # Remove default date
                    dose_date = st.date_input(f"Dose {i} Date", key=f"normal_dose_{i}")  # No default date
                    dose_name = st.text_input(f"Dose {i} Name", key=f"normal_dose_name{i}")
                    normal_doses.append(dose_date)
                    normal_doses_names.append(dose_name)
            with r3c2:
                st.markdown("<b style='color: #22384F'>Booster Dose</b>", unsafe_allow_html=True)
                # Create 5 input fields for Booster Doses with numbering
                booster_doses = []
                booster_doses_names = []
                for i in range(1, 6):
                    # Remove default date
                    booster_date = st.date_input(f"Booster {i} Date", key=f"booster_dose_{i}")
                    booster_date_name = st.text_input(f"Booster {i} Name", key=f"booster_dose_name{i}")  # No default date
                    booster_doses.append(booster_date)
                    booster_doses_names.append(booster_date_name)
            # Display the entered details when the user submits
            if st.button("Submit", type='primary'):
                st.subheader("Entered Vaccination Details")
                st.write(f"Vaccine: {vaccine}")
                st.write("Normal Doses Dates:")
                for i, dose in enumerate(normal_doses, 1):
                    st.write(f"{i} Dose: {dose}")
                
                st.write("Booster Doses Dates:")
                for i, booster in enumerate(booster_doses, 1):
                    st.write(f"{i} Booster: {booster}")
def New_Visit(connection,cursor, accessLevel):
    if "form_data" not in st.session_state:
        st.session_state.form_data = {} 
    st.header("NewVisit")

    global select1, select

    with st.container(border=1):
        rc1, rc2, rc3 = st.columns([1,3,2])
        with rc1:
            st.header("Get User")
        with rc2:
            st.session_state.form_data['Employee ID'] = st.text_input('Employee ID', value=st.session_state.form_data.get('Employee ID', ""))
        with rc3: 
            if st.button("Get Info", type="primary"):  
                cursor.execute(f"SELECT * FROM Employee_det WHERE emp_no = '{st.session_state.form_data['Employee ID']}'")
                data = cursor.fetchone()
                if data is not None:
                    
                    st.session_state.form_data["Visit Reason"] = "Pre Employment"  # Hardcoded value
                    st.session_state.form_data["Employee Name"] = data[1]
                    st.session_state.form_data["Employee Age"] = data[3]
                    st.session_state.form_data['Gender'] = data[4]
                    st.session_state.form_data['Mobile No.'] = data[14][1:] if data[14] else ""
                    st.session_state.form_data['Address'] = data[22] if data[22] is not None else ""
                    st.session_state.form_data['Department'] = data[12]
                    st.session_state.form_data['Work'] = data[11]
                    st.session_state.form_data['Blood Group'] = data[7]
                    st.session_state.form_data['Vaccination Status'] = data[9]
                else:
                    st.warning("No basic Data Found")
                cursor.execute(f"SELECT * FROM vitals WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if  len(df)!=0:
                    st.session_state.form_data["Systolic"] = df[-1][3]
                    st.session_state.form_data["Diastolic"] = df[-1][4]
                    st.session_state.form_data["Pulse"] = df[-1][5]
                    st.session_state.form_data["Temperature"] = df[-1][7]
                    st.session_state.form_data["Respiratory Rate"] = df[-1][8]
                    st.session_state.form_data["spo2"] = df[-1][6]
                    st.session_state.form_data["BMI"] = df[-1][11]
                    st.session_state.form_data["Weight"] = df[-1][10]
                    st.session_state.form_data["Height"] = df[-1][9]
                else:
                    st.warning("No Vitals found")
                cursor.execute(f"SELECT * FROM medicalpersonalhist WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Personal History"] = df[0][3]
                    st.session_state.form_data["Medical History"] = df[0][4]
                    st.session_state.form_data["Surgical History"] = df[0][5]
                    st.session_state.form_data["Father"] = df[-1][6]
                    st.session_state.form_data["Mother"] = df[-1][7]
                else:
                    st.warning("No Medical History found")
                cursor.execute(f"SELECT * FROM hematology_result WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Hemoglobin"] = df[-1][3]
                    st.session_state.form_data["Total RBC"] = df[-1][6]
                    st.session_state.form_data["Total WBC"] = df[-1][9]
                    st.session_state.form_data["Neutrophil"] = df[-1][30]
                    st.session_state.form_data["Monocyte"] = df[-1][39]
                    # st.session_state.form_data["PCV"] = df[-1][]
                    st.session_state.form_data["MCV"] = df[-1][15]
                    st.session_state.form_data["MCH"] = df[-1][18]
                    st.session_state.form_data["Lymphocyte"] = df[-1][33]
                    st.session_state.form_data["ESR"] = df[-1][45]            
                    st.session_state.form_data["MCHC"] = df[-1][21]
                    st.session_state.form_data["Platelet Count"] = df[-1][24]
                    st.session_state.form_data["RDW"] = df[-1][27]
                    st.session_state.form_data["Eosinophil"] = df[-1][36]
                    st.session_state.form_data["Basophil"] = df[-1][42]
                    st.session_state.form_data["Preipheral Blood Smear - RBC Morphology"] = df[-1][48]
                    st.session_state.form_data["Preipheral Blood Smear - Parasites"] = df[-1][49]
                    st.session_state.form_data["Preipheral Blood Smear - Others"] = df[-1][50]
                else:
                    st.warning("No Hematology Result found")
                cursor.execute(f"SELECT * FROM routine_sugartest WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Glucose (F)"] = df[-1][3]
                    st.session_state.form_data["Glucose (PP)"] = df[-1][6]
                    st.session_state.form_data["Random Blood sugar"] = df[-1][9]
                    st.session_state.form_data["Estimated Average Glucose"] = df[-1][12]
                    st.session_state.form_data["HbA1c"] = df[-1][15]
                    st.session_state.form_data['Employee ID'] = df[-1][2]
                else:
                    st.warning("No Routine Sugar Test Result found")
                cursor.execute(f"SELECT * FROM rft_result WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Urea"] = df[-1][3]
                    st.session_state.form_data['BUN'] = df[-1][6]
                    st.session_state.form_data["Serum Creatinine"] = df[-1][9]
                    st.session_state.form_data["Uric Acid"] = df[-1][12] 
                    st.session_state.form_data["Sodium"] = df[-1][15]
                    st.session_state.form_data["Potassium"] = df[-1][18]
                    st.session_state.form_data["Calcium"] = df[-1][21]
                    st.session_state.form_data["Phosphorus"] = df[-1][24]
                    st.session_state.form_data["Chloride"] = df[-1][27]
                else:
                    st.warning("No Renal Function Test Result found")
                cursor.execute(f"SELECT * FROM lipid_profile WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Total Cholesterol"] = df[-1][3]
                    st.session_state.form_data["Triglycerides"] = df[-1][6]
                    st.session_state.form_data["HDL - Cholesterol"] = df[-1][9]
                    st.session_state.form_data["LDL- Cholesterol"] = df[-1][15]
                    st.session_state.form_data["CHOL HDL ratio"] = df[-1][18]
                    st.session_state.form_data["VLDL -Choleserol"] = df[-1][12]
                    st.session_state.form_data["LDL.CHOL/HDL.CHOL Ratio"] = df[-1][21]
                else:
                    st.warning("No Lipid Profile Test Result found")
                cursor.execute(f"SELECT * FROM liver_function WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Bilirubin - Total"] = df[-1][3] 
                    st.session_state.form_data["Bilirubin - Direct"] = df[-1][6] 
                    st.session_state.form_data["Bilirubin - Indirect"] = df[-1][9]
                    st.session_state.form_data["SGOT /AST"] = df[-1][12] 
                    st.session_state.form_data["SGPT /ALT"] = df[-1][15] 
                    st.session_state.form_data["Alkaline phosphatase"] = df[-1][18] 
                    st.session_state.form_data["Total Protein"] = df[-1][21] 
                    st.session_state.form_data["Albumin (Serum )"] = df[-1][24] 
                    st.session_state.form_data["Globulin(Serum)"] = df[-1][27] 
                    st.session_state.form_data["Alb/Glob Ratio"] = df[-1][30] 
                    st.session_state.form_data["Gamma Glutamyl transferase"] = df[-1][33] 
                else:
                    st.warning("No Liver Function Test Result found")
                cursor.execute(f"SELECT * FROM thyroid_function_test WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["T3- Triiodothyroine"] = df[-1][3]
                    st.session_state.form_data["T4 - Thyroxine"] = df[-1][6] 
                    st.session_state.form_data["TSH- Thyroid Stimulating Hormone"] = df[-1][7]  
                else:
                    st.warning("No Thyroid Function Test Result found")
                cursor.execute(f"SELECT * FROM autoimmune_test WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["ANA (Antinuclear Antibody)"] = df[-1][3]
                    st.session_state.form_data["Anti ds DNA"] = df[-1][6] 
                    st.session_state.form_data["Rheumatoid factor"] = df[-1][12] 
                    st.session_state.form_data["Anticardiolipin Antibodies (IgG & IgM)"] = df[-1][9] 
                else:
                    st.warning("No Auto Inumme Test Result found")
                cursor.execute(f"SELECT * FROM coagulation_test WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Prothrombin Time (PT)"] = df[-1][3] 
                    st.session_state.form_data["PT INR"] = df[-1][6] 
                    st.session_state.form_data["Bleeding Time (BT)"] = df[-1][9] 
                    st.session_state.form_data["Clotting Time (CT)"] = df[-1][12] 
                else:
                    st.warning("No Coagulation Test Result found")
                cursor.execute(f"SELECT * FROM enzymes_cardio WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    
                    st.session_state.form_data["Acid Phosphatase"] = df[-1][3] 
                    st.session_state.form_data["Adenosine Deaminase"] = df[-1][6] 
                    st.session_state.form_data["Amylase"] = df[-1][9] 
                    st.session_state.form_data["ECG"] = df[-1][27] 
                    st.session_state.form_data["ECG-Comments"] = df[-1][28] 
                    st.session_state.form_data["Troponin- T"] = df[-1][15] 
                    st.session_state.form_data["Troponin- I"] = df[-1][18] 
                    st.session_state.form_data["CPK - TOTAL"] = df[-1][21] 
                    st.session_state.form_data["ECHO"] = df[-1][29] 
                    st.session_state.form_data["ECHO-Comments"] = df[-1][30] 
                    st.session_state.form_data["Lipase"] = df[-1][12] 
                    st.session_state.form_data["CPK - MB"] = df[-1][24]
                    st.session_state.form_data["TMT"] = df[-1][31] 
                    st.session_state.form_data["TMT-Comments"] = df[-1][32] 
                    st.warning("No Enzymes Cardio Test Result found")
                cursor.execute(f"SELECT * FROM urine_routine WHERE emp_no =  {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Colour"] = df[-1][3] 
                    st.session_state.form_data["Appearance"] = df[-1][6] 
                    st.session_state.form_data["Reaction (pH)"] = df[-1][9] 
                    st.session_state.form_data["Specific gravity"] = df[-1][12] 
                    st.session_state.form_data["Crystals"] = df[-1][45] 
                    st.session_state.form_data["Bacteria"] = df[-1][48]
                    st.session_state.form_data["Protein/Albumin"] = df[-1][15] 
                    st.session_state.form_data["Glucose (Urine)"] = df[-1][18] 
                    st.session_state.form_data["Ketone Bodies"] = df[-1][21] 
                    st.session_state.form_data["Urobilinogen"] = df[-1][24] 
                    st.session_state.form_data["Casts"] = df[-1][42] 
                    st.session_state.form_data["Bile Salts"] = df[-1][27] 
                    st.session_state.form_data["Bile Pigments"] = df[-1][30] 
                    st.session_state.form_data["WBC / Pus cells"] = df[-1][33] 
                    st.session_state.form_data["Red Blood Cells"] = df[-1][36] 
                    st.session_state.form_data["Epithelial cells"] = df[-1][39]  
                else:
                    st.warning("No Urine Routine Test Result found")
                cursor.execute(f"SELECT * FROM serology_result WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Screening For HIV I & II"] = df[-1][3] 
                    st.session_state.form_data["HBsAg"] = df[-1][6] 
                    st.session_state.form_data["HCV"] = df[-1][9] 
                    st.session_state.form_data["VDRL"] = df[-1][15]
                    st.session_state.form_data["Dengue NS1Ag"] = df[-1][18] 
                    st.session_state.form_data["Dengue IgG"] = df[-1][21] 
                    st.session_state.form_data["Dengue IgM"] = df[-1][24] 
                    st.session_state.form_data["WIDAL"] = df[-1][12]  
    
                else:
                    st.warning("No Serology Result found")
                cursor.execute(f"SELECT * FROM motion WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Colour (Motion)"] = df[-1][3] 
                    st.session_state.form_data["Appearance (Motion)"] = df[-1][6] 
                    st.session_state.form_data["Occult Blood"] = df[-1][9] 
                    st.session_state.form_data["Cyst"] = df[-1][15] 
                    st.session_state.form_data["Mucus"] = df[-1][18] 
                    st.session_state.form_data["Pus Cells"] = df[-1][21]
                    st.session_state.form_data["Ova"] = df[-1][12] 
                    st.session_state.form_data["RBCs"] = df[-1][24] 
                    st.session_state.form_data["Others"] = df[-1][27] 
                else:
                    st.warning("No Motion Result found")
                cursor.execute(f"SELECT * FROM routine_culture WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Urine"] = df[-1][3]
                    st.session_state.form_data["Motion"] = df[-1][6] 
                    st.session_state.form_data["Sputum"] = df[-1][9]
                    st.session_state.form_data["Blood"] = df[-1][12] 
                else:
                    st.warning("No Routine Cultre Sensitivity Result found")
                cursor.execute(f"SELECT * FROM mens_pack WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["PSA (Prostate specific Antigen)"] = df[-1][3]
                else:
                    st.warning("No Men's Pack Result found")
                cursor.execute(f"SELECT * FROM womens_pack WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Mammogram"] = df[-1][3] 
                    st.session_state.form_data["Mammogram-Comments"] = df[-1][4] 
                    st.session_state.form_data["PAP Smear"] = df[-1][5] 
                    st.session_state.form_data["PAP Smear-Comments"] = df[-1][6] 
                else:
                    st.warning("No Women's Pack Result found")
                cursor.execute(f"SELECT * FROM occupational_profile WHERE emp_no =  {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0:
                    st.session_state.form_data["Audiometry"] = df[-1][3] 
                    st.session_state.form_data["Audiometry-Comments"] = df[-1][4] 
                    st.session_state.form_data["PFT"] = df[-1][5] 
                    st.session_state.form_data["PFT-Comments"] = df[-1][6]  
                else:
                    st.warning("No Occupational Profile found")
                cursor.execute(f"SELECT * FROM other_tests WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Pathology"] = df[-1][3] 
                    st.session_state.form_data["Pathology-Comments"] = df[-1][4]
                else:
                    st.warning("No Other Test Result found")
                cursor.execute(f"SELECT * FROM ophthalmic_report WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["Vision"] = df[-1][3] 
                    st.session_state.form_data["Vision-Comments"] = df[-1][4] 
                    st.session_state.form_data["Color Vision"] = df[-1][5] 
                    st.session_state.form_data["Color Vision-Comments"] = df[-1][6] 
                else:
                    st.warning("No Ophthalmic Test Result found")
                cursor.execute(f"SELECT * FROM x_ray WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    
                    st.session_state.form_data["X-RAY Chest"] =df[-1][3] 
                    st.session_state.form_data["X-RAY Chest-Comments"] =df[-1][4] 
                    st.session_state.form_data["X-RAY KUB"] =df[-1][9] 
                    st.session_state.form_data["X-RAY KUB-Comments"] =df[-1][10] 
                    st.session_state.form_data["X-RAY Spine"] =df[-1][5] 
                    st.session_state.form_data["X-RAY Spine-Comments"] =df[-1][6] 
                    st.session_state.form_data["X-RAY Pelvis"] =df[-1][11] 
                    st.session_state.form_data["X-RAY Pelvis-Comments"] =df[-1][12] 
                    st.session_state.form_data["X-RAY Abdomen"] =df[-1][7] 
                    st.session_state.form_data["X-RAY Abdomen-Comments"] =df[-1][8] 
                else:
                    st.warning("No X-Ray Test Result found")
                cursor.execute(f"SELECT * FROM usg WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    
                    st.session_state.form_data["USG ABDOMEN"] = df[-1][3] 
                    st.session_state.form_data["USG ABDOMEN-Comments"] = df[-1][4] 
                    st.session_state.form_data["USG KUB"] = df[-1][9] 
                    st.session_state.form_data["USG KUB-Comments"] = df[-1][10] 
                    st.session_state.form_data["USG Pelvis"] = df[-1][5] 
                    st.session_state.form_data["USG Pelvis-Comments"] = df[-1][6]  
                    st.session_state.form_data["USG Neck"] = df[-1][7] 
                    st.session_state.form_data["USG Neck-Comments"] = df[-1][8] 
                        
                else:
                    st.warning("No USG Test Result found")
                cursor.execute(f"SELECT * FROM ct_report WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    st.session_state.form_data["CT Brain"] = df[-1][3] 
                    st.session_state.form_data["CT Brain-Comments"] = df[-1][4] 
                    st.session_state.form_data["CT Lungs"] = df[-1][9] 
                    st.session_state.form_data["CT Lungs-Comments"] = df[-1][10] 
                    st.session_state.form_data["CT Abdomen"] = df[-1][5]   
                    st.session_state.form_data["CT Abdomen-Comments"] = df[-1][6] 
                    st.session_state.form_data["CT Spine"] = df[-1][11] 
                    st.session_state.form_data["CT Spine-Comments"] = df[-1][12] 
                    st.session_state.form_data["CT Pelvis"] = df[-1][7] 
                    st.session_state.form_data["CT Pelvis-Comments"] = df[-1][8]  
                else:
                    st.warning("No CT Test Result found")
                cursor.execute(f"SELECT * FROM mri WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                df = cursor.fetchall()
                if len(df)!=0: 
                    
                    st.session_state.form_data["MRI Brain"] = df[-1][3] 
                    st.session_state.form_data["MRI Brain-Comments"] = df[-1][4]  
                    st.session_state.form_data["MRI Lungs"] = df[-1][9]
                    st.session_state.form_data["MRI Lungs-Comments"] = df[-1][10]
                    st.session_state.form_data["MRI Abdomen"] = df[-1][5] 
                    st.session_state.form_data["MRI Abdomen-Comments"] = df[-1][6] 
                    st.session_state.form_data["MRI Spine"] = df[-1][11] 
                    st.session_state.form_data["MRI Spine-Comments"] = df[-1][12] 
                    st.session_state.form_data["MRI Pelvis"] = df[-1][7]
                    st.session_state.form_data["MRI Pelvis-Comments"] = df[-1][8]
                else:
                    st.warning("No MRI Test Result found")
                # cursor.execute(f"SELECT * FROM fitness WHERE emp_no = {st.session_state.form_data['Employee ID']};")
                # df = cursor.fetchall()
                # if len(df)!=0: 
                #     st.session_state.form_data["Fitness"] = df[-1][3]
                #     st.session_state.form_data["Fitness-Comments"] = df[-1][3] 
                # else:
                #     st.warning("No MRI Test Result found")
    
        r0c1, r0c2 = st.columns([5, 5])

        with r0c1:
            # First selectbox for Employee, Contractor, Visitor
            select = st.selectbox(
                "Select Type", 
                options=["Employee", "Contractor", "Visitor"]
            )

        with r0c2:
            # Second selectbox for Healthy, Unhealthy
            select1 = st.selectbox(
                "Select Type of Visit",
                options=["Preventive", "Curative"]
            )
            st.session_state.form_data["Health status"] = select1

            if select1 == "Preventive":
                selected = st.selectbox(
                            "Select Register",
                            options=["Pre Employment","Pre Employment (Food Handler)","Pre Placement","Annual / Periodical","Periodical (Food Handler)","Camps (Mandatory)","Camps (Optional)","Special Work Fitness","Special Work Fitness (Renewal)","Fitness After Medical Leave","Mock Drill","BP Sugar Check ( Normal Value)"])
            else:
                selected = st.selectbox(
                            "Select Register",
                            options=["Illness","Over Counter Illness","Injury","Over Counter Injury","Followup Visits","BP Sugar Chart","Injury Outside the Premises","Over Counter Injury Outside the Premises","Alcohol Abuse"]
                    )
        with r0c1:
            if select1 == "Preventive":
                if selected == "Pre employment" or selected == "Pre Employment (Food Handler)" or selected == "Pre Placement" or selected == "Annual / Periodical" or selected == "Periodical (Food Handler)" or selected == "Camps (Mandatory)" or selected == "Camps (Optional)":
                    select2 = "Medical Examination"
                    st.text_input("Select Purpose", value = select2)
                elif selected == "Special Work Fitness" or selected == "Special Work Fitness (Renewal)":
                    select2 = "Periodic Work Fitness"
                    st.text_input("Select Purpose", value = select2)
                else:
                    select2 = selected
                    st.text_input("Select Purpose", value = select2)
            else:
                if selected == "Illness" or selected == "Over Counter Illness" or selected == "Injury" or selected == "Over Counter Injury" or selected == "Followup Visits" or selected == "BP Sugar Chart" or selected == "Injury Outside the Premises" or selected == "Over Counter Injury Outside the Premises":
                    select2 = "Out Patient"
                    st.text_input("Select Purpose", value = select2)
                else:
                    select2 = selected
                    st.text_input("Select Purpose", value = select2)
        if selected == "Camps (Mandatory)" or selected == "Camps (Optional)":
            st.session_state.addonInput = st.text_input("Enter the name of the camp:")
        if selected  == "Annual / Periodical":
            col1, col2, col3 = st.columns([3,3,3])
            with col1:
                st.text_input("Enter feild")
            with col2: 
                st.text_input("Enter Batch")
            with col3:
                st.text_input('Enter Year')
             
    with st.container(border=1): #initially height was 700
        if select=="Visitor" and select1=="Preventive":
            Form(None,select,select1,connection,cursor)
        elif select=="Visitor" and select1=="Curative":
            Form(None,select,select1,connection,cursor)
        else:
            Form(selected,select,select1,connection,cursor,accessLevel)
            