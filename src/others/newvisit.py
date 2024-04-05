import streamlit as st
import os
import pandas as p
from  streamlit_option_menu import option_menu
import numpy as np



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


def Form(visitreason):

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
    if "form_data" not in st.session_state:
        st.session_state.form_data = {"visitreason": visitreason} 
        st.rerun()
    form_name = option_menu(
        None,
        ["Basic Details", "Vitals", "Investigations", "Consultation", "Medical History"],
        orientation="horizontal",
        icons=['a','a','a','a','a']
    )

    if form_name == "Basic Details":
        st.subheader("Basic Details")
        r0c1,r0c2 = st.columns([1,1])
        with r0c1:
            st.session_state.form_data["Visit Date"] = st.text_input("Visit Date", value=st.session_state.form_data.get("Visit Date", ""))
        with r0c2:
            st.session_state.form_data["Visit Time"] = st.selectbox('Select the hospital for the referrence range', ["manipal","Dharan","Poornima"], index=0)
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
            if st.button("Cancel", type="primary"):
                st.write("Cancelled")
                st.session_state.form_data = {"visitreason": visitreason}
                st.rerun()
        with r2c3:
            if st.button("Next", type="primary"):    
                st.write("Data Saved")
                st.session_state.form_data["visitreason"] = visitreason
                st.rerun()
        st.write(st.session_state.form_data)
    
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
        with r3c2:
            if st.button("Cancel", type="primary"):
                st.write("Cancelled")
                st.session_state.form_data = {"visitreason": visitreason}
                st.rerun()
        with r3c3:
            if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
                st.session_state.form_data["Random Blood sugarEstimated Average Glucose"] = st.text_input("Random Blood sugarEstimated Average Glucose", value=st.session_state.form_data.get("Random Blood sugarEstimated Average Glucose",""))
                st.session_state.form_data["Estimated Average Glucose"] = st.text_input("Estimated Average Glucose", value=st.session_state.form_data.get("Estimated Average Glucose",""))
            with r1c3:
                st.session_state.form_data["HbA1c"] = st.text_input("HbA1c", value=st.session_state.form_data.get("HbA1c",""))
            
            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            st.write(st.session_state.form_data)

        elif select_inv == "MOTION":
            # Colour			Appearance			Occult Blood			Ova			Cyst			Mucus			Pus Cells			RBCs			Others

            r1c1, r1c2,r1c3 = st.columns(3)
            with r1c1:
                st.session_state.form_data["Colour"] = st.text_input("Colour", value=st.session_state.form_data.get("Colour",""))
                st.session_state.form_data["Appearance"] = st.text_input("Appearance", value=st.session_state.form_data.get("Appearance",""))
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()

            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()

            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()

            with r3c3:
                if st.button("Next", type="primary"):
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

            with r1c3:
                st.session_state.form_data["X-RAY Abdomen"] = st.selectbox("X-RAY Abdomen", ["Normal", "Abnormal"], index=0)
                if st.session_state.form_data["X-RAY Abdomen"] == "Abnormal":
                    st.session_state.form_data["X-RAY Abdomen-Comments"] = st.text_area("X-RAY Abdomen-Comments", value=st.session_state.form_data.get("X-RAY Abdomen-Comments",""))

            r3c1,r3c2,r3c3 = st.columns([6,4,4])
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()

            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            
            with r3c3:
                if st.button("Next", type="primary"):
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
            with r3c2:
                if st.button("Cancel", type="primary"):
                    st.write("Cancelled")
                    st.session_state.form_data = {"visitreason": visitreason}
                    st.rerun()
            
            with r3c3:
                if st.button("Next", type="primary"):
                    st.write("Data Saved")
                    st.session_state.form_data["visitreason"] = visitreason
                    st.rerun()
            
            st.write(st.session_state.form_data)
        
        
        
    elif form_name == "Consultation":
        st.header("Consultation")
        # Complaints         Diagnosis       Remarks

        r1c1, r2c2 = st.columns([6,4])
        with r1c1:
            st.session_state.form_data["Complaints"] = st.text_area("Complaints", value=st.session_state.form_data.get("Complaints",""))
            st.session_state.form_data["Diagnosis"] = st.text_area("Diagnosis", value=st.session_state.form_data.get("Diagnosis",""))
            st.session_state.form_data["Remarks"] = st.text_area("Remarks", value=st.session_state.form_data.get("Remarks",""))
        
        r3c1,r3c2,r3c3 = st.columns([6,4,4])
        with r3c2:
            if st.button("Cancel", type="primary"):
                st.write("Cancelled")
                st.session_state.form_data = {"visitreason": visitreason}
                st.rerun()
        
        with r3c3:
            if st.button("Next", type="primary"):
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
        st.markdown("<h3 style='margin-left:30px;'> Family History </h3>", unsafe_allow_html=True)
        r1c1, r1c2, r1c3 = st.columns([1,6,2])

        with r1c2:
            st.session_state.form_data["Father"] = st.text_area("Father",value=st.session_state.form_data.get("Father", ""))
            st.session_state.form_data["Mother"] = st.text_area("Mother",value=st.session_state.form_data.get("Mother", ""))

        r3c1,r3c2,r3c3 = st.columns([6,4,4])
        with r3c2:
            if st.button("Cancel", type="primary"):
                st.write("Cancelled")
                st.session_state.form_data = {"visitreason": visitreason}
                st.rerun()
        
        with r3c3:
            if st.button("Next", type="primary"):
                st.write("Data Saved")
                st.session_state.form_data["visitreason"] = visitreason
                st.rerun()
        
        st.write(st.session_state.form_data)



def New_Visit(cursor):
    st.header("NewVisit")

    r1c1,r1c2 = st.columns([4,6])
    with r1c1:
        select = option_menu(
            None, 
            ["Healthy", "Unhealthy"], 
            orientation="horizontal",
            icons=['a','a']
    )

    n1c1, n1c2 = st.columns([2,7])

    with n1c1:
        global selected
        if select == "Healthy":
            selected = option_menu(
                "Healthy", 
                ["Pre Employment", "Pre Employment(FH)", "Pre Employment(CC)","Pre Placement", "Annual / Periodic", "Periodic (FH)","Camps (Mandatory)", "Camps (Optional)"],
                menu_icon='building-fill-add',
                icons=['a','a','a','a','a','a','a','a','a','a','a',],
                default_index=0
            )
        if select == "Unhealthy":
            selected = option_menu(
                "Unhealthy",
                ["Illness", "Over counter Illness", "Injury", "Over counter Injury", "Follow up Visits", "BP Sugar (Abnormal)","Injury Outside the premises"],
                menu_icon='building-fill-add',
                icons=['a','a','a','a','a','a','a','a','a','a','a',],
                default_index=0
            )
    
    with n1c2:
        with st.container(border=1, height=700):
            if selected == "Pre Employment":
                Form("Pre Employment")
            
            elif selected == "Pre Employment(FH)":
                Form("Pre Employment(FH)")
            
            elif selected == "Pre Employment(CC)":
                Form("Pre Employment(CC)")
            
            elif selected == "Pre Placement":
                Form("Pre Placement")
            
            elif selected == "Annual / Periodic":
                Form("Annual / Periodic")
            
            elif selected == "Periodic (FH)":
                Form("Periodic (FH)")
            
            elif selected == "Camps (Mandatory)":
                Form("Camps (Mandatory)")
            
            elif selected == "Camps (Optional)":
                Form("Camps (Optional)")
            
            elif selected == "Illness":
                Form("Illness")
            
            elif selected == "Over counter Illness":
                Form("Over counter Illness")                    
            
            elif selected == "Injury":
                Form("Injury")
            
            elif selected == "Over counter Injury":
                Form("Over counter Injury")
            
            elif selected == "Follow up Visits":
                Form("Follow up Visits")
            
            elif selected == "BP Sugar (Abnormal)":
                Form("BP Sugar (Abnormal)")
            
            elif selected == "Injury Outside the premises":
                Form("Injury Outside the premises")
            
            else:
                st.write("Select a visit reason")