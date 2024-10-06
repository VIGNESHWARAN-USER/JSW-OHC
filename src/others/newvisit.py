import streamlit as st
import os
import pandas as p
from  streamlit_option_menu import option_menu
import numpy as np
import json
import datetime



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


def Form(visitreason,select, select1, connection, cursor):

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
    if "form_data" not in st.session_state:
        st.session_state.form_data = {"visitreason": visitreason} 
        st.rerun()

    if select1=="Healthy":
        if visitreason=="Camps (Optional)":
            form_name = option_menu(
            None,
            ["Basic Details", "Vitals","Medical History", "Investigations",  "Consultation"],
            orientation="horizontal",
            icons=['a','a','a','a','a']
        )
        elif visitreason=="Special Work Fitness":
            form_name = option_menu(
            None,
            ["Basic Details", "Vitals", "Fitness", "Consultation"],
            orientation="horizontal",
            icons=['a','a','a','a']
        )
        elif visitreason=="Special Work Fitness (Renewal)" or select=="Visitor":
            form_name = option_menu(
            None,
            ["Basic Details", "Vitals","Medical History", "Fitness", "Consultation"],
            orientation="horizontal",
            icons=['a','a','a','a','a']
        )
        elif visitreason=="Fitness After Medical Leave":
            form_name = option_menu(
            None,
            ["Basic Details","Vitals","Medical History", "Fitness", "Consultation","Medical Leave/Sickness Absence Ratio"],  #not defined
            orientation="horizontal",
            icons=['a','a','a','a','a','a','a']
            )
        elif visitreason=="Mock Drill" or visitreason=="BP Sugar Check":
            form_name= option_menu(
                None,
                ["Basic Details", "Vitals"],
                orientation="horizontal",
                icons=['a','a']
            )
        else:
            form_name = option_menu(
                None,
                ["Basic Details", "Vitals","Medical History", "Investigations", "Fitness", "Consultation"],
                orientation="horizontal",
                icons=['a','a','a','a','a','a']
            )
    if select1=="Unhealthy":
        if select=="Contractor" and visitreason=="Over counter Injury Outside the premises":
            form_name = option_menu(
            None,
            ["Basic Details","Consultation","Prescription","Referral" ],
            orientation="horizontal",
            icons=['a','a','a','a','a']
            )
        elif visitreason=="Illness" or visitreason=="BP Sugar (Abnormal)" or visitreason=="Injury Outside the premises" or visitreason=="Over counter Injury Outside the premises":
            form_name = option_menu(
            None,
            ["Basic Details", "Vitals","Medical History","Consultation","Prescription","Referral" ],
            orientation="horizontal",
            icons=['a','a','a','a','a','a','a','a']
            )
        elif visitreason=="Injury":
            form_name = option_menu(
            None,
            ["Basic Details","Prescription","Referral"],
            orientation="horizontal",
            icons=['a','a','a']
            )
        elif visitreason=="Over counter Injury":
            form_name = option_menu(
            None,
            ["Basic Details","Consultation","Prescription","Referral"],
            orientation="horizontal",
            icons=['a','a','a','a','a']
            )
        elif select!="Contractor"and visitreason=="Follow up Visits":
            form_name = option_menu(
            None,
            ["Basic Details","Vitals","Investigations","Consultation","Prescription","Referral"],
            orientation="horizontal",
            icons=['a','a','a','a','a','a',]
            )
        else:
            form_name = option_menu(
            None,
            ["Basic Details", "Vitals","Consultation","Prescription","Referral" ],
            orientation="horizontal",
            icons=['a','a','a','a','a',]
            )

            
    if form_name == "Basic Details":
        st.subheader("Basic Details")
        r0c1,r0c2 = st.columns([1,1])
        with r0c1:
            st.session_state.form_data["Visit Date"] = st.text_input("Visit Date", value=st.session_state.form_data.get("Visit Date", ""))
        with r0c2:
            st.session_state.form_data["Reference Type"] = st.selectbox('Select the hospital for the referrence range', ["manipal","Dharan","Poornima"], index=0)
        r1c1,r1c2,r1c3 = st.columns(3)
        with r1c1:
            st.session_state.form_data["Employee ID"] = st.text_input("Employee ID",value=st.session_state.form_data.get("Employee ID",""))
            st.session_state.form_data["Gender"] = st.text_input("Gender", value=st.session_state.form_data.get("Gender",""))
            st.session_state.form_data["Mobile No."] = st.text_input("Mobile No.",value=st.session_state.form_data.get("Mobile No.",""))

        with r1c2:
            st.session_state.form_data["Employee Name"] = st.text_input("Employee Name", value=st.session_state.form_data.get("Employee Name",""))
            st.session_state.form_data["Department"] = st.text_input("Department",value=st.session_state.form_data.get("Department",""))
            st.session_state.form_data["Blood Group"] = st.text_input("Blood Group",value=st.session_state.form_data.get("Blood Group",""))
        with r1c3:
            st.session_state.form_data["Employee Age"] = st.text_input("Employee Age",value=st.session_state.form_data.get("Employee Age",""))
            st.session_state.form_data["Work"] = st.text_input("Work",value=st.session_state.form_data.get("Work",""))
            st.session_state.form_data["Vaccination Status"] = st.text_input("Vaccination Status",value=st.session_state.form_data.get("Vaccination Status",""))
        st.session_state.form_data["Address"] = st.text_area("Address",value=st.session_state.form_data.get("Address",""))

        r2c1,r2c2,r2c3 = st.columns([6,4,4])
        st.write("""
            <style>
                button[kind="primary"]{
                    background-color: #22384F;
                    color: white;
                    border-radius: 5px;
                    text-align: center;
                    cursor: pointer;
                    font-size: 20px;
                    width: 95%;
                    padding: 10px ;
                    margin-left:-10px
                }
            </style>
            """,unsafe_allow_html=True)
        with r2c2:
            if st.button("Get Info", type="primary"): # MARK: Get Info
                cursor.execute(f"SELECT * FROM Employee_det WHERE emp_no = '{st.session_state.form_data['Employee ID']}'")
                data = cursor.fetchone()
                if data is not None:
                    st.session_state.form_data["Visit Date"] = datetime.datetime.now().strftime("%d-%m-%Y")
                    st.session_state.form_data["Employee Name"] = data[1]
                    st.session_state.form_data["Employee Age"] = data[3]
                    st.session_state.form_data['Gender'] = data[4]
                    st.session_state.form_data['Mobile No.'] = data[14][1:]
                    st.session_state.form_data['Address'] = data[22]
                    st.session_state.form_data['Department'] = data[12]
                    st.session_state.form_data['Work'] = data[11]
                    st.session_state.form_data['Blood Group'] = data[7]
                    st.session_state.form_data['Vaccination Status'] = data[9]
                    st.rerun()  
                else:
                    st.write(":red-background[:red[No data found]]")
        
        with r2c3:
            if st.button("Add Data", type="primary"):    
                st.write("Data Saved")
                st.session_state.form_data["visitreason"] = visitreason
                st.rerun()
    
    elif form_name == "Vitals":
        st.header("Vitals")
        r1c1,r1c2,r1c3 = st.columns([5,3,9])
        with r1c1:
            systolic = st.session_state.form_data.get("Systolic", "0")
            diastolic = st.session_state.form_data.get("Diastolic", "0")

            st.session_state.form_data["Systolic"] = st.text_input("Systolic", value=systolic,)
            st.session_state.form_data["Diastolic"] = st.text_input("Diastolic", value=diastolic)

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
        
        r2c1,r2c2,r2c3 = st.columns(3)
        with r2c1:
            st.session_state.form_data["Pulse"] = st.text_input("Pulse", value=st.session_state.form_data.get("Pulse",""))
            st.session_state.form_data["spo2"] = st.text_input("SpO2", value=st.session_state.form_data.get("spo2",""))
            st.session_state.form_data["BMI"] = st.text_input("BMI", value=st.session_state.form_data.get("BMI",""))
        with r2c2:
            st.session_state.form_data["Respiratory Rate"] = st.text_input("Respiratory Rate", value=st.session_state.form_data.get("Respiratory Rate",""))
            st.session_state.form_data["Weight"] = st.text_input("Weight", value=st.session_state.form_data.get("Weight",""))
            
        with r2c3:
            st.session_state.form_data["Temperature"] = st.text_input("Temperature", value=st.session_state.form_data.get("Temperature",""))
            st.session_state.form_data["Height"] = st.text_input("Height", value=st.session_state.form_data.get("Height",""))

        r3c1,r3c2,r3c3 = st.columns([6,4,4])
        st.write("""
            <style>
                button[kind="primary"]{
                    all: unset;
                    background-color: #22384F;
                    color: white;
                    border-radius: 5px;
                    text-align: center;
                    cursor: pointer;
                    font-size: 20px;
                    width: 95%;
                    padding: 10px ;
                    margin-left:-10px
                }
            </style>
            """,unsafe_allow_html=True)
        
        with r3c3:
            if st.button("Add Data", type="primary"):
                st.write("Data Saved")
                st.session_state.form_data["visitreason"] = visitreason
                st.rerun()
        st.write(st.session_state.form_data)
        
    elif form_name == "Investigations":
        st.header("Investigations")

        inv_form = ["HAEMATALOGY","ROUTINE SUGAR TESTS","RENAL FUNCTION TEST & ELECTROLYTES","LIPID PROFILE","LIVER FUNCTION TEST","THYROID FUNCTION TEST","AUTOIMMUNE TEST","COAGULATION TEST","ENZYMES & CARDIAC Profile","URINE ROUTINE","SEROLOGY","MOTION","ROUTINE CULTURE & SENSITIVITY TEST","Men's Pack","Women's Pack","Occupational Profile","Others TEST","OPHTHALMIC REPORT","X-RAY","USG","CT","MRI"]


        select_inv = st.selectbox("Select Investigation Form", inv_form)

        if select_inv == "HAEMATALOGY":
            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Hemoglobin"] = st.text_input("Hemoglobin", value=st.session_state.form_data.get("Hemoglobin",""))
                st.session_state.form_data["Total RBC"] = st.text_input("Total RBC", value=st.session_state.form_data.get("Total RBC",""))
                st.session_state.form_data["Total WBC"] = st.text_input("Total WBC", value=st.session_state.form_data.get("Total WBC",""))
                st.session_state.form_data["Neutrophil"] = st.text_input("Neutrophil", value=st.session_state.form_data.get("Neutrophil",""))
                st.session_state.form_data["Monocyte"] = st.text_input("Monocyte", value=st.session_state.form_data.get("Monocyte",""))

            with r1c2:
                st.session_state.form_data["PCV"] = st.text_input("PCV", value=st.session_state.form_data.get("PCV",""))
                st.session_state.form_data["MCV"] = st.text_input("MCV", value=st.session_state.form_data.get("MCV",""))
                st.session_state.form_data["MCH"] = st.text_input("MCH", value=st.session_state.form_data.get("MCH",""))
                st.session_state.form_data["Lymphocyte"] = st.text_input("Lymphocyte", value=st.session_state.form_data.get("Lymphocyte",""))
                st.session_state.form_data["ESR"] = st.text_input("ESR", value=st.session_state.form_data.get("ESR",""))
            with r1c3:
                st.session_state.form_data["MCHC"] = st.text_input("MCHC", value=st.session_state.form_data.get("MCHC",""))
                st.session_state.form_data["Platelet Count"] = st.text_input("Platelet Count", value=st.session_state.form_data.get("Platelet Count",""))
                st.session_state.form_data["RDW"] = st.text_input("RDW", value=st.session_state.form_data.get("RDW",""))
                st.session_state.form_data["Eosinophil"] = st.text_input("Eosinophil", value=st.session_state.form_data.get("Eosinophil",""))
                st.session_state.form_data["Basophil"] = st.text_input("Basophil", value=st.session_state.form_data.get("Basophil",""))
            st.session_state.form_data["Preipheral Blood Smear - RBC Morphology"] = st.text_area("Preipheral Blood Smear - RBC Morphology", value=st.session_state.form_data.get("Preipheral Blood Smear - RBC Morphology",""))
            st.session_state.form_data["Preipheral Blood Smear - Parasites"] = st.text_area("Preipheral Blood Smear - Parasites", value=st.session_state.form_data.get("Preipheral Blood Smear - Parasites",""))
            st.session_state.form_data["Preipheral Blood Smear - Others"] = st.text_area("Preipheral Blood Smear - Others", value=st.session_state.form_data.get("Preipheral Blood Smear - Others",""))


            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)

        elif select_inv == "ROUTINE SUGAR TESTS":
            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Glucose (F)"] = st.text_input("Glucose (F)", value=st.session_state.form_data.get("Glucose (F)",""))
                st.session_state.form_data["Glucose (PP)"] = st.text_input("Glucose (PP)", value=st.session_state.form_data.get("Glucose (PP)",""))
            with r1c2:
                st.session_state.form_data["Random Blood sugar"] = st.text_input("Random Blood sugar", value=st.session_state.form_data.get("Random Blood sugar",""))
                st.session_state.form_data["Estimated Average Glucose"] = st.text_input("Estimated Average Glucose", value=st.session_state.form_data.get("Estimated Average Glucose",""))
            with r1c3:
                st.session_state.form_data["HbA1c"] = st.text_input("HbA1c", value=st.session_state.form_data.get("HbA1c",""))
            
            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)


        elif select_inv == "RENAL FUNCTION TEST & ELECTROLYTES":
            # Urea			Blood urea nitrogen (BUN)			Sr.Creatinine			Uric acid			Sodium			Potassium			Calcium			Phosphorus			Chloride			Bicarbonatel
            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Urea"] = st.text_input("Urea", value=st.session_state.form_data.get("Urea",""))
                st.session_state.form_data["Blood urea nitrogen (BUN)"] = st.text_input("Blood urea nitrogen (BUN)", value=st.session_state.form_data.get("Blood urea nitrogen (BUN)",""))
                st.session_state.form_data["Sr.Creatinine"] = st.text_input("Sr.Creatinine", value=st.session_state.form_data.get("Sr.Creatinine",""))
                st.session_state.form_data["Uric acid"] = st.text_input("Uric acid", value=st.session_state.form_data.get("Uric acid",""))
            with r1c2:
                st.session_state.form_data["Sodium"] = st.text_input("Sodium", value=st.session_state.form_data.get("Sodium",""))
                st.session_state.form_data["Potassium"] = st.text_input("Potassium", value=st.session_state.form_data.get("Potassium",""))
                st.session_state.form_data["Calcium"] = st.text_input("Calcium", value=st.session_state.form_data.get("Calcium",""))
            with r1c3:
                st.session_state.form_data["Phosphorus"] = st.text_input("Phosphorus", value=st.session_state.form_data.get("Phosphorus",""))
                st.session_state.form_data["Chloride"] = st.text_input("Chloride", value=st.session_state.form_data.get("Chloride",""))
                st.session_state.form_data["Bicarbonate"] = st.text_input("Bicarbonate", value=st.session_state.form_data.get("Bicarbonate",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)

        
        elif select_inv == "LIPID PROFILE":
            # Total Cholesterol			Triglycerides			HDL - Cholesterol			VLDL -Choleserol			LDL- Cholesterol			CHOL:HDL ratio			LDL.CHOL/HDL.CHOL Ratio
            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Total Cholesterol"] = st.text_input("Total Cholesterol", value=st.session_state.form_data.get("Total Cholesterol",""))
                st.session_state.form_data["Triglycerides"] = st.text_input("Triglycerides", value=st.session_state.form_data.get("Triglycerides",""))
                st.session_state.form_data["HDL - Cholesterol"] = st.text_input("HDL - Cholesterol", value=st.session_state.form_data.get("HDL - Cholesterol",""))
            with r1c2:
                st.session_state.form_data["LDL- Cholesterol"] = st.text_input("LDL- Cholesterol", value=st.session_state.form_data.get("LDL- Cholesterol",""))
                st.session_state.form_data["CHOL HDL ratio"] = st.text_input("CHOL HDL ratio", value=st.session_state.form_data.get("CHOL HDL ratio",""))
            with r1c3:
                st.session_state.form_data["VLDL -Choleserol"] = st.text_input("VLDL -Choleserol", value=st.session_state.form_data.get("VLDL -Choleserol",""))
                st.session_state.form_data["LDL.CHOL/HDL.CHOL Ratio"] = st.text_input("LDL.CHOL/HDL.CHOL Ratio", value=st.session_state.form_data.get("LDL.CHOL/HDL.CHOL Ratio",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)

        
        elif select_inv == "LIVER FUNCTION TEST":
            # Bilirubin -Total			Bilirubin -Direct			Bilirubin -indirect			SGOT /AST			SGPT /ALT			Alkaline phosphatase			Total Protein			Albumin (Serum )			 Globulin(Serum)			Alb/Glob Ratio			Gamma Glutamyl transferase
            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Bilirubin - Total"] = st.text_input("Bilirubin - Total", value=st.session_state.form_data.get("Bilirubin - Total",""))
                st.session_state.form_data["Bilirubin - Direct"] = st.text_input("Bilirubin - Direct", value=st.session_state.form_data.get("Bilirubin - Direct",""))
                st.session_state.form_data["Bilirubin - Indirect"] = st.text_input("Bilirubin - Indirect", value=st.session_state.form_data.get("Bilirubin - Indirect",""))
                st.session_state.form_data["SGOT /AST"] = st.text_input("SGOT /AST", value=st.session_state.form_data.get("SGOT /AST",""))
            with r1c2:
                st.session_state.form_data["SGPT /ALT"] = st.text_input("SGPT /ALT", value=st.session_state.form_data.get("SGPT /ALT",""))
                st.session_state.form_data["Alkaline phosphatase"] = st.text_input("Alkaline phosphatase", value=st.session_state.form_data.get("Alkaline phosphatase",""))
                st.session_state.form_data["Total Protein"] = st.text_input("Total Protein", value=st.session_state.form_data.get("Total Protein",""))
                st.session_state.form_data["Albumin (Serum )"] = st.text_input("Albumin (Serum )", value=st.session_state.form_data.get("Albumin (Serum )",""))
            with r1c3:
                st.session_state.form_data["Globulin(Serum)"] = st.text_input("Globulin(Serum)", value=st.session_state.form_data.get("Globulin(Serum)",""))
                st.session_state.form_data["Alb/Glob Ratio"] = st.text_input("Alb/Glob Ratio", value=st.session_state.form_data.get("Alb/Glob Ratio",""))
                st.session_state.form_data["Gamma Glutamyl transferase"] = st.text_input("Gamma Glutamyl transferase", value=st.session_state.form_data.get("Gamma Glutamyl transferase",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)
        
        elif select_inv == "THYROID FUNCTION TEST":
            # T3- Triiodothyroine			T4 - Thyroxine			TSH- Thyroid Stimulating Hormone
            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["T3- Triiodothyroine"] = st.text_input("T3- Triiodothyroine", value=st.session_state.form_data.get("T3- Triiodothyroine",""))
                st.session_state.form_data["T4 - Thyroxine"] = st.text_input("T4 - Thyroxine", value=st.session_state.form_data.get("T4 - Thyroxine",""))
            with r1c2:
                st.session_state.form_data["TSH- Thyroid Stimulating Hormone"] = st.text_input("TSH- Thyroid Stimulating Hormone", value=st.session_state.form_data.get("TSH- Thyroid Stimulating Hormone",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)


        elif select_inv == "AUTOIMMUNE TEST":
            # ANA (Antinuclear Antibody)			Anti ds DNA			Anticardiolipin Antibodies (IgG & IgM)			Rheumatoid factor
            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["ANA (Antinuclear Antibody)"] = st.text_input("ANA (Antinuclear Antibody)", value=st.session_state.form_data.get("ANA (Antinuclear Antibody)",""))
                st.session_state.form_data["Anti ds DNA"] = st.text_input("Anti ds DNA", value=st.session_state.form_data.get("Anti ds DNA",""))
            with r1c2:
                st.session_state.form_data["Rheumatoid factor"] = st.text_input("Rheumatoid factor", value=st.session_state.form_data.get("Rheumatoid factor",""))
            with r1c3:
                st.session_state.form_data["Anticardiolipin Antibodies (IgG & IgM)"] = st.text_input("Anticardiolipin Antibodies (IgG & IgM)", value=st.session_state.form_data.get("Anticardiolipin Antibodies (IgG & IgM)",""))
            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)

        elif select_inv == "COAGULATION TEST":
            # Prothrombin Time (PT)			PT INR			Bleeding Time (BT)			Clotting Time (CT)
            r1c1, r1c2,r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["Prothrombin Time (PT)"] = st.text_input("Prothrombin Time (PT)", value=st.session_state.form_data.get("Prothrombin Time (PT)",""))
                st.session_state.form_data["PT INR"] = st.text_input("PT INR", value=st.session_state.form_data.get("PT INR",""))
            with r1c2:
                st.session_state.form_data["Bleeding Time (BT)"] = st.text_input("Bleeding Time (BT)", value=st.session_state.form_data.get("Bleeding Time (BT)",""))
            with r1c3:
                st.session_state.form_data["Clotting Time (CT)"] = st.text_input("Clotting Time (CT)", value=st.session_state.form_data.get("Clotting Time (CT)",""))            


            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)

        elif select_inv == "ENZYMES & CARDIAC Profile":
            # Acid Phosphatase			Adenosine Deaminase			Amylase			Lipase			Troponin- T			Troponin- I			CPK - TOTAL			CPK - MB			ECG 		ECHO		TMT

            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Acid Phosphatase"] = st.text_input("Acid Phosphatase", value=st.session_state.form_data.get("Acid Phosphatase",""))
                st.session_state.form_data["Adenosine Deaminase"] = st.text_input("Adenosine Deaminase", value=st.session_state.form_data.get("Adenosine Deaminase",""))
                st.session_state.form_data["Amylase"] = st.text_input("Amylase", value=st.session_state.form_data.get("Amylase",""))
                st.session_state.form_data["ECG"] = st.selectbox("ECG", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["ECG"] == "Abnormal":
                    st.session_state.form_data["ECG-Comments"] = st.text_area("ECG-Comments", value=st.session_state.form_data.get("ECG-Comments",""))
            with r1c2:
                st.session_state.form_data["Troponin- T"] = st.text_input("Troponin- T", value=st.session_state.form_data.get("Troponin- T",""))
                st.session_state.form_data["Troponin- I"] = st.text_input("Troponin- I", value=st.session_state.form_data.get("Troponin- I",""))
                st.session_state.form_data["CPK - TOTAL"] = st.text_input("CPK - TOTAL", value=st.session_state.form_data.get("CPK - TOTAL",""))
                st.session_state.form_data["ECHO"] = st.selectbox("ECHO", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["ECHO"] == "Abnormal":
                    st.session_state.form_data["ECHO-Comments"] = st.text_area("ECHO-Comments", value=st.session_state.form_data.get("ECHO-Comments",""))
            with r1c3:
                st.session_state.form_data["Lipase"] = st.text_input("Lipase", value=st.session_state.form_data.get("Lipase",""))
                st.session_state.form_data["CPK - MB"] = st.text_input("CPK - MB", value=st.session_state.form_data.get("CPK - MB",""))
                st.session_state.form_data["TMT"] = st.selectbox("TMT", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["TMT"] == "Abnormal":
                    st.session_state.form_data["TMT-Comments"] = st.text_area("TMT-Comments", value=st.session_state.form_data.get("TMT-Comments",""))


            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)


        elif select_inv == "URINE ROUTINE":
            # Colour			Appearance			Reaction (pH)			Specific gravity			Protein/Albumin			Glucose (Urine)			Ketone Bodies			Urobilinogen			Bile Salts			Bile Pigments			WBC / Pus cells			Red Blood Cells			Epithelial celss			Casts			Crystals			Bacteria

            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Colour"] = st.text_input("Colour", value=st.session_state.form_data.get("Colour",""))
                st.session_state.form_data["Appearance"] = st.text_input("Appearance", value=st.session_state.form_data.get("Appearance",""))
                st.session_state.form_data["Reaction (pH)"] = st.text_input("Reaction (pH)", value=st.session_state.form_data.get("Reaction (pH)",""))
                st.session_state.form_data["Specific gravity"] = st.text_input("Specific gravity", value=st.session_state.form_data.get("Specific gravity",""))
                st.session_state.form_data["Crystals"] = st.text_input("Crystals", value=st.session_state.form_data.get("Crystals",""))
                st.session_state.form_data["Bacteria"] = st.text_input("Bacteria", value=st.session_state.form_data.get("Bacteria",""))

            with r1c2:
                st.session_state.form_data["Protein/Albumin"] = st.text_input("Protein/Albumin", value=st.session_state.form_data.get("Protein/Albumin",""))
                st.session_state.form_data["Glucose (Urine)"] = st.text_input("Glucose (Urine)", value=st.session_state.form_data.get("Glucose (Urine)",""))
                st.session_state.form_data["Ketone Bodies"] = st.text_input("Ketone Bodies", value=st.session_state.form_data.get("Ketone Bodies",""))
                st.session_state.form_data["Urobilinogen"] = st.text_input("Urobilinogen", value=st.session_state.form_data.get("Urobilinogen",""))
                st.session_state.form_data["Casts"] = st.text_input("Casts", value=st.session_state.form_data.get("Casts",""))
            
            with r1c3:
                st.session_state.form_data["Bile Salts"] = st.text_input("Bile Salts", value=st.session_state.form_data.get("Bile Salts",""))
                st.session_state.form_data["Bile Pigments"] = st.text_input("Bile Pigments", value=st.session_state.form_data.get("Bile Pigments",""))
                st.session_state.form_data["WBC / Pus cells"] = st.text_input("WBC / Pus cells", value=st.session_state.form_data.get("WBC / Pus cells",""))
                st.session_state.form_data["Red Blood Cells"] = st.text_input("Red Blood Cells", value=st.session_state.form_data.get("Red Blood Cells",""))
                st.session_state.form_data["Epithelial celss"] = st.text_input("Epithelial celss", value=st.session_state.form_data.get("Epithelial celss",""))


            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)


        elif select_inv == "SEROLOGY":
            # Screening For HIV I & II			HBsAg			HCV			WIDAL			VDRL			Dengue NS1Ag			Dengue  IgG			Dengue IgM

            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Screening For HIV I & II"] = st.text_input("Screening For HIV I & II", value=st.session_state.form_data.get("Screening For HIV I & II",""))
                st.session_state.form_data["HBsAg"] = st.text_input("HBsAg", value=st.session_state.form_data.get("HBsAg",""))
                st.session_state.form_data["HCV"] = st.text_input("HCV", value=st.session_state.form_data.get("HCV",""))
            with r1c2:
                st.session_state.form_data["VDRL"] = st.text_input("VDRL", value=st.session_state.form_data.get("VDRL",""))
                st.session_state.form_data["Dengue NS1Ag"] = st.text_input("Dengue NS1Ag", value=st.session_state.form_data.get("Dengue NS1Ag",""))
                st.session_state.form_data["Dengue IgG"] = st.text_input("Dengue IgG", value=st.session_state.form_data.get("Dengue IgG",""))
            with r1c3:
                st.session_state.form_data["Dengue IgM"] = st.text_input("Dengue IgM", value=st.session_state.form_data.get("Dengue IgM",""))
                st.session_state.form_data["WIDAL"] = st.text_input("WIDAL", value=st.session_state.form_data.get("WIDAL",""))
                

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)

        elif select_inv == "MOTION":
            # Colour			Appearance			Occult Blood			Ova			Cyst			Mucus			Pus Cells			RBCs			Others

            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Colour (Motion)"] = st.text_input("Colour (Motion)", value=st.session_state.form_data.get("Colour (Motion)",""))
                st.session_state.form_data["Appearance (Motion)"] = st.text_input("Appearance (Motion)", value=st.session_state.form_data.get("Appearance (Motion)",""))
                st.session_state.form_data["Occult Blood"] = st.text_input("Occult Blood", value=st.session_state.form_data.get("Occult Blood",""))
            with r1c2:
                st.session_state.form_data["Cyst"] = st.text_input("Cyst", value=st.session_state.form_data.get("Cyst",""))
                st.session_state.form_data["Mucus"] = st.text_input("Mucus", value=st.session_state.form_data.get("Mucus",""))
                st.session_state.form_data["Pus Cells"] = st.text_input("Pus Cells", value=st.session_state.form_data.get("Pus Cells",""))
            with r1c3:
                st.session_state.form_data["Ova"] = st.text_input("Ova", value=st.session_state.form_data.get("Ova",""))
                st.session_state.form_data["RBCs"] = st.text_input("RBCs", value=st.session_state.form_data.get("RBCs",""))
                st.session_state.form_data["Others"] = st.text_input("Others", value=st.session_state.form_data.get("Others",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)

        elif select_inv == "ROUTINE CULTURE & SENSITIVITY TEST":
            # Urine			Motion			Sputum			Blood

            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Urine"] = st.text_input("Urine", value=st.session_state.form_data.get("Urine",""))
                st.session_state.form_data["Motion"] = st.text_input("Motion", value=st.session_state.form_data.get("Motion",""))
            with r1c2:
                st.session_state.form_data["Sputum"] = st.text_input("Sputum", value=st.session_state.form_data.get("Sputum",""))
            with r1c3:
                st.session_state.form_data["Blood"] = st.text_input("Blood", value=st.session_state.form_data.get("Blood",""))


            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)

        elif select_inv == "Men's Pack":
            # PSA (Prostate specific Antigen)

            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["PSA (Prostate specific Antigen)"] = st.text_input("PSA (Prostate specific Antigen)", value=st.session_state.form_data.get("PSA (Prostate specific Antigen)",""))
            
            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            
            st.write(st.session_state.form_data)
        
        elif select_inv == "Women's Pack":
            # Mammogram		PAP Smear

            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Mammogram"] = st.selectbox("Mammogram", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["Mammogram"] == "Abnormal":
                    st.session_state.form_data["Mammogram-Comments"] = st.text_area("Mammogram-Comments", value=st.session_state.form_data.get("Mammogram-Comments",""))
            with r1c2:
                st.session_state.form_data["PAP Smear"] = st.selectbox("PAP Smear", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["PAP Smear"] == "Abnormal":
                    st.session_state.form_data["PAP Smear-Comments"] = st.text_area("PAP Smear-Comments", value=st.session_state.form_data.get("PAP Smear-Comments",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)

        elif select_inv == "Occupational Profile":
            # Audiometry 		PFT

            r1c1, r1c2,r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["Audiometry"] = st.selectbox("Audiometry", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["Audiometry"] == "Abnormal":
                    st.session_state.form_data["Audiometry-Comments"] = st.text_area("Audiometry-Comments", value=st.session_state.form_data.get("Audiometry-Comments",""))

            with r1c2:
                st.session_state.form_data["PFT"] = st.selectbox("PFT", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["PFT"] == "Abnormal":
                    st.session_state.form_data["PFT-Comments"] = st.text_area("PFT-Comments", value=st.session_state.form_data.get("PFT-Comments",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            

            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()

            st.write(st.session_state.form_data)
        
        elif select_inv == "Others TEST":
            # Pathology 

            r1c1, r1c2,r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["Pathology"] = st.selectbox("Pathology", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["Pathology"] == "Abnormal":
                    st.session_state.form_data["Pathology-Comments"] = st.text_area("Pathology-Comments", value=st.session_state.form_data.get("Pathology-Comments",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            

            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()

            st.write(st.session_state.form_data)

        elif select_inv == "OPHTHALMIC REPORT":
            # Vision		Color Vision

            r1c1, r1c2,r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["Vision"] = st.selectbox("Vision", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["Vision"] == "Abnormal":
                    st.session_state.form_data["Vision-Comments"] = st.text_area("Vision-Comments", value=st.session_state.form_data.get("Vision-Comments",""))

            with r1c2:
                st.session_state.form_data["Color Vision"] = st.selectbox("Color Vision", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["Color Vision"] == "Abnormal":
                    st.session_state.form_data["Color Vision-Comments"] = st.text_area("Color Vision-Comments", value=st.session_state.form_data.get("Color Vision-Comments",""))
            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            

            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()

            st.write(st.session_state.form_data)
        
        elif select_inv == "X-RAY":
            # Chest		Spine		Abdomen		KUB		Pelvis
            
            r1c1, r1c2,r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["X-RAY Chest"] = st.selectbox("X-RAY Chest", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY Chest"] == "Abnormal":
                    st.session_state.form_data["X-RAY Chest-Comments"] = st.text_area("X-RAY Chest-Comments", value=st.session_state.form_data.get("X-RAY Chest-Comments",""))
                st.session_state.form_data["X-RAY KUB"] = st.selectbox("X-RAY KUB", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY KUB"] == "Abnormal":
                    st.session_state.form_data["X-RAY KUB-Comments"] = st.text_area("X-RAY KUB-Comments", value=st.session_state.form_data.get("X-RAY KUB-Comments",""))
            
            with r1c2:
                st.session_state.form_data["X-RAY Spine"] = st.selectbox("X-RAY Spine", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY Spine"] == "Abnormal":
                    st.session_state.form_data["X-RAY Spine-Comments"] = st.text_area("X-RAY Spine-Comments", value=st.session_state.form_data.get("X-RAY Spine-Comments",""))
                st.session_state.form_data["X-RAY Pelvis"] = st.selectbox("X-RAY Pelvis", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY Pelvis"] == "Abnormal":
                    st.session_state.form_data["X-RAY Pelvis-Comments"] = st.text_area("X-RAY Pelvis-Comments", value=st.session_state.form_data.get("X-RAY Pelvis-Comments",""))

            with r1c3:
                st.session_state.form_data["X-RAY Abdomen"] = st.selectbox("X-RAY Abdomen", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY Abdomen"] == "Abnormal":
                    st.session_state.form_data["X-RAY Abdomen-Comments"] = st.text_area("X-RAY Abdomen-Comments", value=st.session_state.form_data.get("X-RAY Abdomen-Comments",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            

            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()

            st.write(st.session_state.form_data)
                
        elif select_inv == "USG":
            # ABDOMEN		Pelvis		Neck		KUB

            r1c1, r1c2,r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["USG ABDOMEN"] = st.selectbox("USG ABDOMEN", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["USG ABDOMEN"] == "Abnormal":
                    st.session_state.form_data["USG ABDOMEN-Comments"] = st.text_area("USG ABDOMEN-Comments", value=st.session_state.form_data.get("USG ABDOMEN-Comments",""))
                st.session_state.form_data["USG KUB"] = st.selectbox("USG KUB", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["USG KUB"] == "Abnormal":
                    st.session_state.form_data["USG KUB-Comments"] = st.text_area("USG KUB-Comments", value=st.session_state.form_data.get("USG KUB-Comments",""))

            with r1c2:
                st.session_state.form_data["USG Pelvis"] = st.selectbox("USG Pelvis", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["USG Pelvis"] == "Abnormal":
                    st.session_state.form_data["USG Pelvis-Comments"] = st.text_area("USG Pelvis-Comments", value=st.session_state.form_data.get("USG Pelvis-Comments",""))
            
            with r1c3:
                st.session_state.form_data["USG Neck"] = st.selectbox("USG Neck", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["USG Neck"] == "Abnormal":
                    st.session_state.form_data["USG Neck-Comments"] = st.text_area("USG Neck-Comments", value=st.session_state.form_data.get("USG Neck-Comments",""))
                

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            
            st.write(st.session_state.form_data)
        
        elif select_inv == "CT":
            # Brain		Abdomen		Pelvis		CT Lungs		Spine

            r1c1, r1c2,r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["CT Brain"] = st.selectbox("CT Brain", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["CT Brain"] == "Abnormal":
                    st.session_state.form_data["CT Brain-Comments"] = st.text_area("CT Brain-Comments", value=st.session_state.form_data.get("CT Brain-Comments",""))
                st.session_state.form_data["CT Lungs"] = st.selectbox("CT Lungs", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["CT Lungs"] == "Abnormal":
                    st.session_state.form_data["CT Lungs-Comments"] = st.text_area("CT Lungs-Comments", value=st.session_state.form_data.get("CT Lungs-Comments",""))
            
            with r1c2:
                st.session_state.form_data["CT Abdomen"] = st.selectbox("CT Abdomen", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["CT Abdomen"] == "Abnormal":  
                    st.session_state.form_data["CT Abdomen-Comments"] = st.text_area("CT Abdomen-Comments", value=st.session_state.form_data.get("CT Abdomen-Comments",""))
                st.session_state.form_data["CT Spine"] = st.selectbox("CT Spine", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["CT Spine"] == "Abnormal":
                    st.session_state.form_data["CT Spine-Comments"] = st.text_area("CT Spine-Comments", value=st.session_state.form_data.get("CT Spine-Comments",""))
            
            with r1c3:
                st.session_state.form_data["CT Pelvis"] = st.selectbox("CT Pelvis", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["CT Pelvis"] == "Abnormal":
                    st.session_state.form_data["CT Pelvis-Comments"] = st.text_area("CT Pelvis-Comments", value=st.session_state.form_data.get("CT Pelvis-Comments",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            
            st.write(st.session_state.form_data)
        
        elif select_inv == "MRI":
            # Brain		Abdomen		Pelvis		CT Lungs		Spine

            r1c1, r1c2,r1c3 = st.columns(3)

            with r1c1:
                st.session_state.form_data["MRI Brain"] = st.selectbox("MRI Brain", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["MRI Brain"] == "Abnormal":
                    st.session_state.form_data["MRI Brain-Comments"] = st.text_area("MRI Brain-Comments", value=st.session_state.form_data.get("MRI Brain-Comments",""))
                st.session_state.form_data["MRI Lungs"] = st.selectbox("MRI Lungs", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["MRI Lungs"] == "Abnormal":
                    st.session_state.form_data["MRI Lungs-Comments"] = st.text_area("MRI Lungs-Comments", value=st.session_state.form_data.get("MRI Lungs-Comments",""))
            
            with r1c2:
                st.session_state.form_data["MRI Abdomen"] = st.selectbox("MRI Abdomen", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["MRI Abdomen"] == "Abnormal":
                    st.session_state.form_data["MRI Abdomen-Comments"] = st.text_area("MRI Abdomen-Comments", value=st.session_state.form_data.get("MRI Abdomen-Comments",""))
                st.session_state.form_data["MRI Spine"] = st.selectbox("MRI Spine", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["MRI Spine"] == "Abnormal":
                    st.session_state.form_data["MRI Spine-Comments"] = st.text_area("")
            
            with r1c3:
                st.session_state.form_data["MRI Pelvis"] = st.selectbox("MRI Pelvis", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["MRI Pelvis"] == "Abnormal":
                    st.session_state.form_data["MRI Pelvis-Comments"] = st.text_area("MRI Pelvis-Comments", value=st.session_state.form_data.get("MRI Pelvis-Comments", ""))


            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            
            
            with r3c3:
                if st.button("Add Data", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            
            st.write(st.session_state.form_data)
        
    elif form_name == "Fitness":
        st.header("Fitness")
        # Fit to Join
        # Unfit
        # Conditional Fit
        # Fitness Res. Duty
        # Fitness with conditional
        # Height Work
        # Confined Space
        # Gasline
        # SCBA
        # Fire Rescue

        # i need to create a multi select box for the above options
        st.session_state.form_data["Fitness"] = st.multiselect("Fitness", ["Fit to Join", "Unfit", "Conditional Fit", "Fitness Res. Duty", "Fitness with conditional", "Height Work", "Confined Space", "Gasline", "SCBA", "Fire Rescue"])

        st.session_state.form_data["Fitness-Comments"] = st.text_area("Fitness-Comments", value=st.session_state.form_data.get("Fitness-Comments",""))
        



        r3c1,r3c2,r3c3 = st.columns([6,4,4])
        

        with r3c3:
            if st.button("Add Data", type="primary"):
                st.write("Data Saved")
                st.session_state.form_data["visitreason"] = visitreason
                st.rerun()
            
        st.write(st.session_state.form_data)
        
    elif form_name == "Consultation":
        st.header("Consultation")
        # Complaints         Diagnosis       Remarks
        
        if(visitreason=="Annual / Periodic" or visitreason=="Periodic (FH)"):
            st.session_state.form_data["Remarks"] = st.text_area("Remarks", value=st.session_state.form_data.get("Remarks",""))
            st.file_uploader("Upload Self Declaration", type=['xlsx'],key="Self-declaration")
            st.file_uploader("Upload Reports", type=['xlsx'],key="Reports")
        elif(visitreason=="Camps (Mandatory)" or visitreason=="Camps (Optional)"or visitreason=="Illness") or visitreason=="Follow up Visits" or visitreason=="BP Sugar (Abnormal)" or visitreason=="Injury Outside the premises":
            st.session_state.form_data["Remarks"] = st.text_area("Remarks", value=st.session_state.form_data.get("Remarks",""))
            st.file_uploader("Upload Reports", type=['xlsx'],key="Reports")
            if(select1=="Unhealthy" and (visitreason=="Illness" or visitreason=="Follow up Visits" or visitreason=="BP Sugar (Abnormal)" or visitreason=="Injury Outside the premises")):
                st.session_state.form_data["Diagnosis"] = st.text_area("Diagnosis", value=st.session_state.form_data.get("Diagnosis",""))
                st.session_state.form_data["Complaints"] = st.text_area("Complaints", value=st.session_state.form_data.get("Complaints",""))
        elif(select1=="Unhealthy" and (visitreason=="Over counter Illness" or visitreason=="Over counter Injury")):
                st.session_state.form_data["Diagnosis"] = st.text_area("Diagnosis", value=st.session_state.form_data.get("Diagnosis",""))
                st.session_state.form_data["Complaints"] = st.text_area("Complaints", value=st.session_state.form_data.get("Complaints",""))        
        elif(visitreason=="Special Work Fitness" or visitreason=="Special Work Fitness (Renewal)"):
            st.file_uploader("Upload Self Declaration", type=['xlsx'],key="Self-declaration")
        elif(visitreason=="Fitness After Medical Leave"):
            st.file_uploader("Upload Self Declaration", type=['xlsx'],key="Self-declaration")
            st.file_uploader("Upload FC External", type=['xlsx'],key="FC-external")
            st.file_uploader("Upload Reports", type=['xlsx'],key="Reports")
        elif(visitreason=="Over counter Injury Outside the premises" or (visitreason==None and select1=="Unhealthy")):
            st.session_state.form_data["Remarks"] = st.text_area("Remarks", value=st.session_state.form_data.get("Remarks",""))
            st.session_state.form_data["Diagnosis"] = st.text_area("Diagnosis", value=st.session_state.form_data.get("Diagnosis",""))
            st.session_state.form_data["Complaints"] = st.text_area("Complaints", value=st.session_state.form_data.get("Complaints",""))
            
        else:
            st.session_state.form_data["Remarks"] = st.text_area("Remarks", value=st.session_state.form_data.get("Remarks",""))
            st.file_uploader("Upload Self Declaration", type=['xlsx'],key="Self-declaration")
            st.file_uploader("Upload FC External", type=['xlsx'],key="FC-external")
            st.file_uploader("Upload Reports", type=['xlsx'],key="Reports")
        

        
        #r3c1,r3c2,r3c3 = st.columns([3,3,3])
        st.write("""
                 <div style='float:right;marin-right:100px;margin-top:25px'>
                 <label for="doctor">Submitted By:</label>
                    <select style='height:35px;width:100px;text-align:center;background-color:rgb(240,242,246);border:none;border-radius:5px;' name="doctor" id="doctor">
                        <option value="SK">SK</option>
                        <option value="Nurse">Nurse</option>
                    </select>
                 <label for="doctor">Assign Doctor:</label>
                    <select style='height:35px;width:100px;text-align:center;background-color:rgb(240,242,246);border:none;border-radius:5px;' name="doctor" id="doctor">
                        <option value="SK">SK</option>
                        <option value="Nurse">Nurse</option>
                    </select>
                 </div>""",unsafe_allow_html=True)
        if st.button("Submit", type="primary"):
            st.write("Data Saved")
            st.session_state.form_data["visitreason"] = visitreason
            st.rerun()
        
        st.write(st.session_state.form_data)

    elif form_name == "Medical History":
        st.header("Medical History")
        
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

        st.session_state.form_data["Personal History"] = st.multiselect("Personal History", ["Smoker", "Alcoholic", "Veg", "Mixed Diet"])
        st.session_state.form_data["Medical History"] = st.multiselect("Medical History", ["BP", "DM", "Others"])

        st.header("Surgical History")

        st.text_area("comments")
        
        st.markdown("<h3 style='margin-left:30px;'> Family History </h3>", unsafe_allow_html=True)


        r1c1, r1c2, r1c3 = st.columns([1,6,2])

        with r1c2:
            st.session_state.form_data["Father"] = st.text_area("Father",value=st.session_state.form_data.get("Father", ""))
            st.session_state.form_data["Mother"] = st.text_area("Mother",value=st.session_state.form_data.get("Mother", ""))

        r3c1,r3c2,r3c3 = st.columns([6,4,4])
        
        
        with r3c3:
            if st.button("Add Data", type="primary"):
                st.write("Data Saved")
                st.session_state.form_data["visitreason"] = visitreason
                st.rerun()
            if st.button("Submit", type = "primary"):
                i = st.session_state.form_data # MARK: Data Insert
                try:
                    insert_basicdetails = ("INSERT INTO basic_details (emp_no, entry_date, PatientAge, PatientName, Gender, Department, Work, MobileNo, BloodGroup, Vaccinated, Address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                    basicdetails_data = (i.get("Employee ID"), i.get("Visit Date"), i.get("Employee Age"), i.get("Employee Name"), i.get("Gender"), i.get("Department"), i.get("Work"),i.get("Mobile No."), i.get("Blood Group"), i.get("Vaccination Status"), i.get("Address"))
                    cursor.execute(insert_basicdetails, basicdetails_data)
                    connection.commit()
                except Exception as e:
                    st.write(e)
                    st.write("Error in basic details")


                try:
                    insert_vitals = ("INSERT INTO vitals(emp_no, entry_date, Systolic, Diastolic, PulseRate, SpO2, Temperature, RespiratoryRate, Height, Weight, BMI) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)") 
                    vitals_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Systolic"), i.get("Diastolic"), i.get("Pulse"), i.get("spo2"), i.get("Temperature"), i.get("Respiratory Rate"), i.get("Height"), i.get("Weight"), i.get("BMI"))
                    cursor.execute(insert_vitals, vitals_values)
                    connection.commit()
                    st.write("Vitals Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in vitals")

                
                try:
                    insert_hematology = ("INSERT INTO hematology_result(emp_no, entry_date, heamoglobin,  rbc_count, wbc_count, haemotocrit, mcv, mch, mchc, platelet, rdw, neutrophil, lymphocyte, eosinophil, monocyte, basophils, esr, pbs_rbc, pbc_parasites, pbc_others) VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)")
                    hematology_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Hemoglobin"), i.get("Total RBC"), i.get("Total WBC"), i.get("PCV"), i.get("MCV"), i.get("MCH"), i.get("MCHC"), i.get("Platelet Count"), i.get("RDW"), i.get("Neutrophil"), i.get("Lymphocyte"), i.get("Eosinophil"), i.get("Monocyte"), i.get("Basophil"), i.get("ESR"), i.get("Preipheral Blood Smear - RBC Morphology"), i.get("Preipheral Blood Smear - Parasites"), i.get("Preipheral Blood Smear - Others"))
                    cursor.execute(insert_hematology, hematology_values)
                    connection.commit()
                    st.write("Hematology Inserted")

                except Exception as e:
                    st.write(e)
                    st.write("Error in hematology")

                try:
                    insert_rst = ("INSERT INTO routine_sugartest(emp_no, entry_date, glucosef, glucosepp, rbs, eag, hba1c) VALUES(%s, %s, %s, %s, %s, %s, %s)")
                    rst_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Glucose (F)"), i.get("Glucose (PP)"), i.get("Random Blood sugar"), i.get("Estimated Average Glucose"), i.get("HbA1c"))
                    cursor.execute(insert_rst, rst_values)
                    connection.commit()
                    st.write("Data Submitted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in rst")

                try:
                    insert_rft = ("INSERT INTO rft_result(entry_date, emp_no, urea, bun, sr_creatinine, uric_acid, sodium, potassium, calcium, phosphorus, chloride, bicarbonate ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                    rft_values = (i.get("Visit Date"), i.get("Employee ID"), i.get("Urea"), i.get("Blood urea nitrogen (BUN)"), i.get("Sr.Creatinine"), i.get("Uric acid"), i.get("Sodium"), i.get("Potassium"), i.get("Calcium"), i.get("Phosphorus"), i.get("Chloride"), i.get("Bicarbonate"))                    
                    cursor.execute(insert_rft, rft_values)
                    connection.commit()
                    st.write("RFT Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in rft")

                    
                try:
                    insert_lipid_prof = ("INSERT INTO lipid_profile(emp_no, entry_date, tcholesterol,triglycerides, hdl_cholesterol, vldl_cholesterol, ldl_cholesterol, chol_hdlratio, ldlhdlratio) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    lipid_prof_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Total Cholesterol"), i.get("Triglycerides"), i.get("HDL - Cholesterol"), i.get("VLDL -Choleserol"), i.get("LDL- Cholesterol"), i.get("CHOL HDL ratio"), i.get("LDL.CHOL/HDL.CHOL Ratio"))                    
                    cursor.execute(insert_lipid_prof, lipid_prof_values)
                    connection.commit()
                    st.write("Lipid Profile Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in lipid profile")

                try:
                    insert_lft = ("INSERT INTO liver_function(emp_no, entry_date, bilirubin_total, bilirubin_direct, bilirubin_indirect, sgot_alt, sgpt_alt, alkaline_phosphatase, total_protein, albumin, globulin, alb_globratio, gammagt) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")
                    lft_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Bilirubin - Total"), i.get("Bilirubin - Direct"), i.get("Bilirubin - Indirect"), i.get("SGOT /AST"), i.get("SGPT /ALT"), i.get("Alkaline phosphatase"), i.get("Total Protein"), i.get("Albumin (Serum )"), i.get("Globulin(Serum)"), i.get("Alb/Glob Ratio"), i.get("Gamma Glutamyl transferase"))                    
                    cursor.execute(insert_lft, lft_values)
                    connection.commit()
                    st.write("LFT Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in lft")
                
                try:
                    insert_tft = ("INSERT INTO thyroid_function_test(emp_no, entry_date, t3, t4, tsh) VALUES(%s, %s, %s, %s, %s)")
                    tft_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("T3- Triiodothyroine"), i.get("T4 - Thyroxine"), i.get("TSH- Thyroid Stimulating Hormone"))                    
                    cursor.execute(insert_tft, tft_values)
                    connection.commit()
                    st.write("TFT Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in tft")

                try:
                    insert_ait = ("INSERT INTO autoimmune_test(emp_no, entry_date, ana, adna, anticardiolipin, rheumatoid) VALUES(%s, %s, %s, %s, %s, %s)")
                    ait_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("ANA (Antinuclear Antibody)"), i.get("Anti ds DNA"), i.get("Anticardiolipin Antibodies (IgG & IgM)"), i.get("Rheumatoid factor"))
                    cursor.execute(insert_ait, ait_values)
                    connection.commit()
                    st.write("AIT Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in ait")

                try:
                    insert_coagulation = ("INSERT INTO coagulation_test(emp_no, entry_date, pt, ptinr, bt, ct) VALUES(%s, %s, %s, %s, %s, %s)")
                    coagulation_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Prothrombin Time (PT)"), i.get("PT INR"), i.get("Bleeding Time (BT)"), i.get("Clotting Time (CT)"))
                    cursor.execute(insert_coagulation, coagulation_values)
                    connection.commit()
                    st.write("Coagulation Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in coagulation")

                try:
                    insert_enzymes_cardio = ("INSERT INTO enzymes_cardio(emp_no, entry_date,acid_phosphatase,adenosine,amylase,lipase,troponin_t, troponin_i, cpk_total, cpk_mb, ecg, ecg_comments, echo,echo_comments, tmt, tmt_comments) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    enzymes_cardio_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Acid Phosphatase"), i.get("Adenosine Deaminase"), i.get("Amylase"), i.get("Lipase"), i.get("Troponin- T"), i.get("Troponin- I"), i.get("CPK - Total"), i.get("CPK - MB"), i.get("ECG"), i.get("ECG-Comments"), i.get("ECHO"), i.get("ECHO-Comments"), i.get("TMT"), i.get("TMT-Comments"))
                    cursor.execute(insert_enzymes_cardio, enzymes_cardio_values)
                    connection.commit()
                    st.write("Enzymes Cardio Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in enzymes cardio")
                
                try:
                    insert_urine_routine = ("INSERT INTO urine_routine(emp_no, entry_date, colour, apperance, reaction, specific_gravity, protein_albumin, glucose, ketone, urobilinogen, bile_salts, bile_pigments, wbc_pluscells, rbc, epithelial_cell, casts, crystals, bacteria) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    urine_routine_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Colour"), i.get("Appearance"), i.get("Reaction (pH)"), i.get("Specific Gravity"), i.get("Protein/Albumin"), i.get("Glucose (Urine)"), i.get("Ketone Bodies"), i.get("Urobilinogen"), i.get("Bile Salts"), i.get("Bile Pigments"), i.get("WBC / Pus cells"), i.get("Red Blood Cells"), i.get("Epithelial celss"), i.get("Casts"), i.get("Crystals"), i.get("Bacteria"))
                    cursor.execute(insert_urine_routine, urine_routine_values)
                    connection.commit()
                    st.write("Urine Routine Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in urine routine")

                try:
                    insert_serology = ("INSERT INTO serology_result(emp_no, entry_date, hiv_screening , hbsag, hcv, widal, vdrl, denguens, dengueigg, dengueigm) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    serology_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Screening For HIV I & II"), i.get("HBsAg"), i.get("HCV"), i.get("WIDAL"), i.get("VDRL"), i.get("Dengue NS1Ag"), i.get("Dengue IgG"), i.get("Dengue IgM"))
                    cursor.execute(insert_serology, serology_values)
                    connection.commit()
                    st.write("Serology Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in serology")

                try:
                    insert_motion = ("INSERT INTO motion(emp_no, entry_date, colour, appearance, occult_blood, ova, cyst, mucus, pus_cells, rbcs, others_t) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    motion_values = (i.get("Employee ID"), i.get("Visi Date"), i.get("Colour (Motion)"), i.get("Appearance (Motion)"), i.get("Occult Blood"), i.get("Ova"), i.get("Cyst"), i.get("Mucus"), i.get("Pus Cells"), i.get("RBCs"), i.get("Others"))
                    cursor.execute(insert_motion, motion_values)
                    connection.commit()
                    st.write("Motion Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in motion")

                try:
                    insert_routie_culture = ("INSERT INTO routine_culture(emp_no, entry_date, urine, motion, sputum, blood) VALUES( %s, %s, %s, %s, %s, %s)")
                    routine_culture_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Urine"), i.get("Motion"), i.get("Sputum"), i.get("Blood"))
                    cursor.execute(insert_routie_culture, routine_culture_values)
                    connection.commit()
                    st.write("Routine Culture Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in routine culture")

                try:
                    insert_mens_pack = ("INSERT INTO mens_pack(emp_no, entry_date, psa) VALUES(%s, %s, %s)")
                    mens_pack_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("PSA (Prostate specific Antigen)"))
                    cursor.execute(insert_mens_pack, mens_pack_values)
                    connection.commit()
                    st.write("Mens Pack Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in mens pack")
                
                try:
                    insert_womens_pack = ("INSERT INTO womens_pack(emp_no, entry_date, mammogram_nm_ab, mammogram_comment, pap_nm_ab, pap_comment) VALUES(%s, %s, %s, %s, %s, %s)")
                    womens_pack_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Mammogram"), i.get("Mammogram-Comments"), i.get("PAP Smear"), i.get("PAP Smear-Comments"))
                    cursor.execute(insert_womens_pack, womens_pack_values)
                    connection.commit()
                    st.write("Womens Pack Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in womens pack")

                try:
                    insert_occupational_profile = ("INSERT INTO occupational_profile(emp_no, entry_date, audiometry_nm_ab, audiometry_comment, pft_nm_ab, pft_comment) VALUES(%s, %s, %s, %s, %s, %s)")
                    occupational_profile_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Audiometry"), i.get("Audiometry-Comments"), i.get("PFT"), i.get("PFT-Comments"))
                    cursor.execute(insert_occupational_profile, occupational_profile_values)
                    connection.commit()
                    st.write("Occupational Profile Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in occupational profile")
                

                try:
                    insert_other_test = ("INSERT INTO other_tests(emp_no, entry_date, pathology, pathology_comments) VALUES(%s, %s, %s, %s)")
                    other_test_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Pathology"), i.get("Pathology-Comments"))
                    cursor.execute(insert_other_test, other_test_values)
                    connection.commit()
                    st.write("Other Test Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in other test")

                try:
                    insert_ophthalmic_report = ("INSERT INTO ophthalmic_report(emp_no, entry_date, vision, vision_comments, colourvision, colourvision_comment) VALUES(%s, %s, %s, %s, %s, %s)")
                    ophthalmic_report_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Vision"), i.get("Vision-Comments"), i.get("Colour Vision"), i.get("Colour Vision-Comments"))
                    cursor.execute(insert_ophthalmic_report, ophthalmic_report_values)
                    connection.commit()
                    st.write("Ophthalmic Report Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in ophthalmic report")

                try:
                    insert_x_ray = ("INSERT INTO x_ray(emp_no, entry_date, chest_nm_ab, chest_comment, spine_nm_ab, spine_comment, abdomen_nm_ab, abdomen_comment, kub_nm_ab, kub_comment, pelvis_nm_ab, pelvis_comment) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    x_ray_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("X-RAY Chest"), i.get("X-RAY Chest-Comments"), i.get("X-RAY Spine"), i.get("X-RAY Spine-Comments"), i.get("X-RAY Abdomen"), i.get("X-RAY Abdomen-Comments"), i.get("X-RAY KUB"), i.get("X-RAY KUB-Comments"), i.get("X-RAY Pelvis"), i.get("X-RAY Pelvis-Comments"))
                    cursor.execute(insert_x_ray, x_ray_values)
                    connection.commit()
                    st.write("X-Ray Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in x-ray")
                
                try:
                    insert_usg = ("INSERT INTO usg(emp_no, entry_date, abdomen, abdomen_comments, pelvis, pelvis_comments,neck, neck_comments, kub, kub_comments) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    usg_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("USG ABDOMEN"), i.get("USG ABDOMEN-Comments"), i.get("USG Pelvis"), i.get("USG Pelvis-Comments"), i.get("USG Neck"), i.get("USG Neck-Comments"), i.get("USG KUB"), i.get("USG KUB-Comments"))
                    cursor.execute(insert_usg, usg_values)
                    connection.commit()
                    st.write("USG Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in usg")
                
                try:
                    insert_ct_report = ("INSERT INTO ct_report(emp_no, entry_date, brain, brain_comment, abdomen, abdomen_comment, pelvis, pelvis_comment, ct_lungs, ct_lungs_comment, spine, spine_comment) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    ct_report_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("CT Brain"), i.get("CT Brain-Comments"), i.get("CT Abdomen"), i.get("CT Abdomen-Comments"), i.get("CT Pelvis"), i.get("CT Pelvis-Comments"), i.get("CT Lungs"), i.get("CT Lungs-Comments"), i.get("CT Spine"), i.get("CT Spine-Comments"))
                    cursor.execute(insert_ct_report, ct_report_values)
                    connection.commit()
                    st.write("CT Report Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in ct report")

                try:
                    insert_mri_report = ("INSERT INTO mri(emp_no, entry_date, brain, brain_comments, abdomen, abdomen_comments, pelvis, pelvis_comments, mri_lungs, mri_lungs_comments, spine, spine_comments) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    mri_report_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("MRI Brain"), i.get("MRI Brain-Comments"), i.get("MRI Abdomen"), i.get("MRI Abdomen-Comments"), i.get("MRI Pelvis"), i.get("MRI Pelvis-Comments"), i.get("MRI Lungs"), i.get("MRI Lungs-Comments"), i.get("MRI Spine"), i.get("MRI Spine-Comments"))
                    cursor.execute(insert_mri_report, mri_report_values)
                    connection.commit()
                    st.write("MRI Report Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in mri report")
                
                try:
                    insert_consultation = ("INSERT INTO consultation(emp_no, entry_date, complaints, diagnosis, remarks) VALUES(%s, %s, %s, %s, %s)")
                    consultation_values = (i.get("Employee ID"), i.get("Visit Date"), i.get("Complaints"), i.get("Diagnosis"), i.get("Remarks"))
                    cursor.execute(insert_consultation, consultation_values)
                    connection.commit()
                    st.write("Consultation Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in consultation")

                try:
                    insert_medical_history = ("INSERT INTO medicalpersonalhist(emp_no, entry_date, personal_history, medical_history, father, mother) VALUES(%s, %s, %s, %s, %s, %s)")
                    medical_history_values = (i.get("Employee ID"), i.get("Visit Date"), json.dumps(i.get("Personal History")), json.dumps(i.get("Medical History")), i.get("Father"), i.get("Mother"))
                    cursor.execute(insert_medical_history, medical_history_values)
                    connection.commit()
                    st.write("Medical History Inserted")
                except Exception as e:
                    st.write(e)
                    st.write("Error in medical history")

                    
        st.write(st.session_state.form_data)

    elif form_name=="Prescription":
        st.header("Prescription")
        st.write("""
            <style>
                button[kind="primary"]{
                    all: unset;
                    background-color: #22384F;
                    color: white;
                    border-radius: 5px;
                    text-align: center;
                    cursor: pointer;
                    font-size: 20px;
                    width: 10%;
                    padding: 10px ;
                    margin-left:1000px;
                    
                }
            </style>
            """,unsafe_allow_html=True)
        st.subheader("Tablets")
        c1,c2,c3,c4,c5=st.columns([3,2,2,2,2])
        with c1:
            st.selectbox("Name of the Drug",["Drug1","Drug2","Drug3"],index=None)
            st.selectbox("Name of the Drug",["Drug_1","Drug2","Drug3"],index=None)
        with c2:
            st.text_input("Qty")
            st.text_input("Qtys")
        with c3:
            st.selectbox("Timing",["M","AN","N","Stat"],index=None)
            st.selectbox("Timing",["M","AN","N_","Stat"],index=None)
        with c4:
            st.selectbox("Food",["BF","AF_","WF"],index=None)
            st.selectbox("Food",["BF","AF","WF"],index=None)
        with c5:
            st.text_input("Day", placeholder="Comments...")
            st.text_input("Days", placeholder="Comments...")
        st.button("Add",type='primary')
        
        st.subheader("Injection")
        c1,c2,c3,c4,c5=st.columns([3,2,2,2,2])

        with c1:            
            st.selectbox("Name of the Drug",["Drug1","Drug2","Drug3"],index=None,key="d1")
            st.selectbox("Name of the Drug",["Drug_1","Drug2","Drug3"],index=None,key="d2")
        with c2:
            st.text_input("Qty",key="q1")
            st.text_input("Qtys",key="q2")
            
        st.button("Add",key="a1",type="primary")

        st.subheader("Creams")
        c1,c2,c3,c4,c5=st.columns([3,2,2,2,2])
        with c1:            
            st.selectbox("Name of the Drug",["Drug1","Drug2","Drug3"],index=None,key="d3")
            st.selectbox("Name of the Drug",["Drug_1","Drug2","Drug3"],index=None,key="d4")
        with c2:
            st.text_input("Qty",key="q3")
            st.text_input("Qtys",key="q4")
        st.button("Add",key="a2",type="primary")
        
        st.subheader("Others")
        c1,c2,c3,c4,c5=st.columns([3,2,2,2,2])      
        with c1:            
            st.selectbox("Name of the Drug",["Drug1","Drug2","Drug3"],index=None,key="d5")
            st.selectbox("Name of the Drug",["Drug_1","Drug2","Drug3"],index=None,key="d6")
        with c2:
            st.text_input("Qty",key="q5")
            st.text_input("Qtys",key="q6")
        st.button("Add",key="a3",type="primary")


        st.markdown("""
            <div id="custom-button-container" style='margin-top:20px;'>
                <button id="custom-button">Submit</button>
                <select id="opt">
                    <option >SK</option>
                    <option >DR</option>
                    <option >AD</option>
                </select>
                <h4 id="let">Submited By</h4>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            <style>
            #let{
                float:right;
                margin-left:80px;
                    position:absolute;
            }
            </style>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            <style>
            #opt {
                background-color: #22384F;
                color: white;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 16px;
                    width:10%;
                cursor: pointer;
                float:right;
                margin-right:60px;
            }
            </style>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            <style>
            #custom-button {
                background-color: #22384F;
                color: white;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
                float:right;
                margin-right:30px;
            }
            </style>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            <div id="custom-button-container">
                <button id="custom-button">Generate Prescription</button>
            </div>
            """, unsafe_allow_html=True)
            

    elif form_name=="Referral":
        st.header("Referral")
        referral = st.radio("Referral", ("Yes", "No"))
        hospital_name = st.text_input("Name of the Hospital", placeholder="Comments...")
        doctor_name = st.text_input("Doctor name", placeholder="Comments...")
        condition_type = st.radio("Condition Type", ("Occupational", "Non-occupational", "Domestic"))
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Clear"):
                referral = None
                hospital_name = ""
                doctor_name = ""
                condition_type = None
        with col2:
            if st.button("Submit"):
                st.success("Form submitted successfully!")
                st.write("Referral:", referral)
                st.write("Hospital Name:", hospital_name)
                st.write("Doctor Name:", doctor_name)
                st.write("Condition Type:", condition_type)


def New_Visit(connection,cursor):
    st.header("NewVisit")

    n1c1, n1c2 = st.columns([2,7])

    with n1c1:
        global selected,select
        with n1c1:
            select = option_menu(
                None, 
                ["Employee", "Contractor","Visitor"], 
                orientation="vertical",
                icons=['a','a','a'],
            )
            
            select1 = option_menu(
                select, 
                ["Healthy", "Unhealthy"], 
                orientation="horizontal",
                icons=['a','a']
            )
            if select!="Visitor" and select1=="Healthy":
                select2 = option_menu(
                "Healthy", 
                ["Medical Examination", "Periodic Work Fitness","Fitness After Medical Leave","Mock Drill","BP Sugar Check"], 
                orientation="vertical",
                icons=['a','a','a','a','a']
                )
                if select=="Contractor" and select2 == "Medical Examination":
                    selected = option_menu(
                        "Medical Examination", 
                        ["Pre Employment", "Pre Employment(FH)","Pre Employment(CC)","Pre Placement", "Annual / Periodic", "Camps (Mandatory)", "Camps (Optional)"],
                        menu_icon='building-fill-add',
                        icons=['a','a','a','a','a','a','a','a','a','a','a',],
                        default_index=0
                    )
                elif select2 == "Medical Examination":
                    selected = option_menu(
                        "Medical Examination", 
                        ["Pre Employment", "Pre Employment(FH)","Pre Placement", "Annual / Periodic", "Periodic (FH)","Camps (Mandatory)", "Camps (Optional)"],
                        menu_icon='building-fill-add',
                        icons=['a','a','a','a','a','a','a','a','a','a','a',],
                        default_index=0
                    )
                elif select2 == "Periodic Work Fitness":
                    selected = option_menu(
                        "Periodic Work Fitness",
                        ["Special Work Fitness","Special Work Fitness (Renewal)"],
                        menu_icon='building-fill-add',
                        icons=['a','a',]
                    )
                elif select2=="Fitness After Medical Leave":
                    selected = option_menu(
                        "Fitness After Medical Leave",
                        ["Fitness After Medical Leave"],
                        menu_icon='building-fill-add',
                        icons=['a',]
                    )
                elif select2=="Mock Drill" or select2=="BP Sugar Check":
                    selected = option_menu(
                        select2,
                        [select2],
                        menu_icon='building-fill-add',
                        icons=['a',]
                    )
            
            if select!="Visitor" and select1 == "Unhealthy":
                select2 = option_menu(
                "Unhealthy", 
                ["Out Patient"], 
                orientation="vertical",
                icons=['a']
                )
                if select2=="Out Patient":
                    selected = option_menu(
                        "Out Patient",
                        ["Illness", "Over counter Illness", "Injury", "Over counter Injury", "Follow up Visits", "BP Sugar (Abnormal)","Injury Outside the premises","Over counter Injury Outside the premises"],
                        menu_icon='building-fill-add',
                        icons=['a','a','a','a','a','a','a','a','a','a','a',],
                        default_index=0,
                    )
        
        with n1c2:
            with st.container(border=1, height=900): #initially height was 700
                if select=="Visitor" and select1=="Healthy":
                    Form(None,select,select1,connection,cursor)
                elif select=="Visitor" and select1=="Unhealthy":
                    Form(None,select,select1,connection,cursor)
                elif selected == "Pre Employment":
                    Form("Pre Employment",select,select1,connection,cursor)
                
                elif selected == "Pre Employment(FH)":
                    Form("Pre Employment(FH)",select,select1,connection,cursor)
                
                elif selected == "Pre Employment(CC)":
                    Form("Pre Employment(CC)",select,select1,connection,cursor)
                
                elif selected == "Pre Placement":
                    Form("Pre Placement",select,select1,connection,cursor)
                
                elif selected == "Annual / Periodic":
                    Form("Annual / Periodic",select,select1,connection,cursor)
                
                elif selected == "Periodic (FH)":
                    Form("Periodic (FH)",select,select1,connection,cursor)
                
                elif selected == "Camps (Mandatory)":
                    Form("Camps (Mandatory)",select,select1,connection,cursor)
                
                elif selected == "Camps (Optional)":
                    Form("Camps (Optional)",select,select1,connection,cursor)



                elif selected=="Special Work Fitness":
                    Form("Special Work Fitness",select,select1,connection,cursor)

                elif selected=="Special Work Fitness (Renewal)":
                    Form("Special Work Fitness (Renewal)",select,select1,connection,cursor)

                elif selected=="Fitness After Medical Leave":
                    Form("Fitness After Medical Leave",select,select1,connection,cursor)
                elif selected=="Mock Drill" or selected=="BP Sugar Check":
                    Form(selected,select,select1,connection,cursor)


                    
                
                elif selected == "Illness":
                    Form("Illness",select,select1,connection,cursor)
                
                elif selected == "Over counter Illness":
                    Form("Over counter Illness",select,select1,connection,cursor)                    
                
                elif selected == "Injury":
                    Form("Injury",select,select1,connection,cursor)
                
                elif selected == "Over counter Injury":
                    Form("Over counter Injury",select,select1,connection,cursor)
                
                elif selected == "Follow up Visits":
                    Form("Follow up Visits",select,select1,connection,cursor)
                
                elif selected == "BP Sugar (Abnormal)":
                    Form("BP Sugar (Abnormal)",select,select1,connection,cursor)
                
                elif selected == "Injury Outside the premises":
                    Form("Injury Outside the premises",select,select1,connection,cursor)

                elif selected == "Over counter Injury Outside the premises":
                    Form("Over counter Injury Outside the premises",select,select1,connection,cursor)
                else:
                    st.write("Select a visit reason", selected)