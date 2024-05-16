import streamlit as st 
from  streamlit_option_menu import option_menu

def addReferenceRange(connection,cursor):
    st.title("Add Reference Range")

    if "form_data" not in st.session_state:
        st.session_state.form_data = {}
    
    # i wan t ocreation option menu for the investigations(HAEMATALOGY","ROUTINE SUGAR TESTS","RENAL FUNCTION TEST & ELECTROLYTES","LIPID PROFILE","LIVER FUNCTION TEST","THYROID FUNCTION TEST","AUTOIMMUNE TEST","COAGULATION TEST","ENZYMES & CARDIAC Profile","URINE ROUTINE","SEROLOGY","MOTION","ROUTINE CULTURE & SENSITIVITY TEST")
    r0c1,r0c2,r0c3= st.columns([3,2,4])
    with r0c1:
        
        form_name = option_menu(
            None,
            ["Basic details","Investigations", "others"],
            orientation="horizontal",
            icons=['a','a','a','a','a']
        )


    if form_name == "Basic details":
        r1c1, r1c2,r1c3 = st.columns(3)
        with r1c1:
            st.session_state.form_data["Year"] = st.text_input("Year",key="Year")
            st.session_state.form_data["Batch"] = st.text_input("Batch",key="Batch")
            st.session_state.form_data["Hospital Name"] = st.text_input("Hospital Name",key="Hospital Name")

        if st.button("Submit"):
            st.write(st.session_state.form_data)

    if form_name == "Investigations":
        r0c1,r0c2= st.columns([3,7])
        with r0c1:

            Investigations = option_menu(
            None,
            ["HAEMATALOGY","ROUTINE SUGAR TESTS","RENAL FUNCTION TEST & ELECTROLYTES","LIPID PROFILE","LIVER FUNCTION TEST","THYROID FUNCTION TEST","AUTOIMMUNE TEST","COAGULATION TEST","ENZYMES & CARDIAC Profile","URINE ROUTINE","SEROLOGY","MOTION","ROUTINE CULTURE & SENSITIVITY TEST","MEN'S PACK"],
            orientation="vertical",
            icons=['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
        )
        if "form_data" not in st.session_state:
                    st.session_state.form_data = {}
        with r0c2:
            with st.container(height=700):
                if Investigations == "HAEMATALOGY":
                    st.subheader("Hemoglobin")
                    st.session_state.form_data["Hemoglobin_Unit"] = st.text_input("Unit", key="Hemoglobin_Unit")
                    st.session_state.form_data["Hemoglobin_Referance_Range"] = st.text_input("Referance Range", key="Hemoglobin_Referance_Range")
    
                    st.subheader("Total RBC")
                    st.session_state.form_data["Total_RBC_Unit"] = st.text_input("Unit", key="Total_RBC_Unit")
                    st.session_state.form_data["Total_RBC_Referance_Range"] = st.text_input("Referance Range", key="Total_RBC_Referance_Range")
    
                    st.subheader("Total WBC")
                    st.session_state.form_data["Total_WBC_Unit"] = st.text_input("Unit", key="Total_WBC_Unit")
                    st.session_state.form_data["Total_WBC_Referance_Range"] = st.text_input("Referance Range", key="Total_WBC_Referance_Range")
    
                    st.subheader("Neutrophil")
                    st.session_state.form_data["Neutrophil_Unit"] = st.text_input("Unit", key="Neutrophil_Unit")
                    st.session_state.form_data["Neutrophil_Referance_Range"] = st.text_input("Referance Range", key="Neutrophil_Referance_Range")
    
                    st.subheader("Monocyte")
                    st.session_state.form_data["Monocyte_Unit"] = st.text_input("Unit", key="Monocyte_Unit")
                    st.session_state.form_data["Monocyte_Referance_Range"] = st.text_input("Referance Range", key="Monocyte_Referance_Range")
    
                    st.subheader("PCV")
                    st.session_state.form_data["PCV_Unit"] = st.text_input("Unit", key="PCV_Unit")
                    st.session_state.form_data["PCV_Referance_Range"] = st.text_input("Referance Range", key="PCV_Referance_Range")
    
                    st.subheader("MCV")
                    st.session_state.form_data["MCV_Unit"] = st.text_input("Unit", key="MCV_Unit")
                    st.session_state.form_data["MCV_Referance_Range"] = st.text_input("Referance Range", key="MCV_Referance_Range")
    
                    st.subheader("MCH")
                    st.session_state.form_data["MCH_Unit"] = st.text_input("Unit", key="MCH_Unit")
                    st.session_state.form_data["MCH_Referance_Range"] = st.text_input("Referance Range", key="MCH_Referance_Range")
    
                    st.subheader("Lymphocyte")
                    st.session_state.form_data["Lymphocyte_Unit"] = st.text_input("Unit", key="Lymphocyte_Unit")
                    st.session_state.form_data["Lymphocyte_Referance_Range"] = st.text_input("Referance Range", key="Lymphocyte_Referance_Range")
    
                    st.subheader("ESR")
                    st.session_state.form_data["ESR_Unit"] = st.text_input("Unit", key="ESR_Unit")
                    st.session_state.form_data["ESR_Referance_Range"] = st.text_input("Referance Range", key="ESR_Referance_Range")
    
                    st.subheader("MCHC")
                    st.session_state.form_data["MCHC_Unit"] = st.text_input("Unit", key="MCHC_Unit")
                    st.session_state.form_data["MCHC_Referance_Range"] = st.text_input("Referance Range", key="MCHC_Referance_Range")
    
                    st.subheader("Platelet Count")
                    st.session_state.form_data["Platelet_Count_Unit"] = st.text_input("Unit", key="Platelet_Count_Unit")
                    st.session_state.form_data["Platelet_Count_Referance_Range"] = st.text_input("Referance Range", key="Platelet_Count_Referance_Range")
    
                    st.subheader("RDW")
                    st.session_state.form_data["RDW_Unit"] = st.text_input("Unit", key="RDW_Unit")
                    st.session_state.form_data["RDW_Referance_Range"] = st.text_input("Referance Range", key="RDW_Referance_Range")
    
                    st.subheader("Eosinophil")
                    st.session_state.form_data["Eosinophil_Unit"] = st.text_input("Unit", key="Eosinophil_Unit")
                    st.session_state.form_data["Eosinophil_Referance_Range"] = st.text_input("Referance Range", key="Eosinophil_Referance_Range")
    
                    st.subheader("Basophil")
                    st.session_state.form_data["Basophil_Unit"] = st.text_input("Unit", key="Basophil_Unit")
                    st.session_state.form_data["Basophil_Referance_Range"] = st.text_input("Referance Range", key="Basophil_Referance_Range")
    
                    st.subheader("Preipheral Blood Smear - RBC Morphology")
                    st.session_state.form_data["RBC_Morphology_Unit"] = st.text_input("Unit", key="RBC_Morphology_Unit")
                    st.session_state.form_data["RBC_Morphology_Referance_Range"] = st.text_input("Referance Range", key="RBC_Morphology_Referance_Range")
    
                    st.subheader("Preipheral Blood Smear - Parasites")
                    st.session_state.form_data["Parasites_Unit"] = st.text_input("Unit", key="Parasites_Unit")
                    st.session_state.form_data["Parasites_Referance_Range"] = st.text_input("Referance Range", key="Parasites_Referance_Range")
    
                    st.subheader("Preipheral Blood Smear - Others")
                    st.session_state.form_data["Others_Unit"] = st.text_input("Unit", key="Others_Unit")
                    st.session_state.form_data["Others_Referance_Range"] = st.text_input("Referance Range", key="Others_Referance_Range")

                    #need to submit button
                    if st.button("Submit"):
                        st.write(st.session_state.form_data)
                
                if Investigations == "ROUTINE SUGAR TESTS":
                    #Glucose (F)			Glucose (PP)			Random Blood sugar			Estimated Average Glucose			HbA1c
                    st.subheader("Glucose (F)")
                    st.session_state.form_data["Glucose_F_Unit"] = st.text_input("Unit", key="Glucose_F_Unit")
                    st.session_state.form_data["Glucose_F_Referance_Range"] = st.text_input("Referance Range", key="Glucose_F_Referance_Range")

                    st.subheader("Glucose (PP)")
                    st.session_state.form_data["Glucose_PP_Unit"] = st.text_input("Unit", key="Glucose_PP_Unit")
                    st.session_state.form_data["Glucose_PP_Referance_Range"] = st.text_input("Referance Range", key="Glucose_PP_Referance_Range")

                    st.subheader("Random Blood sugar")
                    st.session_state.form_data["Random_Blood_sugar_Unit"] = st.text_input("Unit", key="Random_Blood_sugar_Unit")
                    st.session_state.form_data["Random_Blood_sugar_Referance_Range"] = st.text_input("Referance Range", key="Random_Blood_sugar_Referance_Range")

                    st.subheader("Estimated Average Glucose")
                    st.session_state.form_data["Estimated_Average_Glucose_Unit"] = st.text_input("Unit", key="Estimated_Average_Glucose_Unit")
                    st.session_state.form_data["Estimated_Average_Glucose_Referance_Range"] = st.text_input("Referance Range", key="Estimated_Average_Glucose_Referance_Range")

                    st.subheader("HbA1c")
                    st.session_state.form_data["HbA1c_Unit"] = st.text_input("Unit", key="HbA1c_Unit")
                    st.session_state.form_data["HbA1c_Referance_Range"] = st.text_input("Referance Range", key="HbA1c_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)



                if Investigations == "RENAL FUNCTION TEST & ELECTROLYTES":
                    #Urea    Blood urea nitrogen (BUN)			Sr.Creatinine			Uric acid			Sodium			Potassium			Calcium			Phosphorus			Chloride			Bicarbonate
                    st.subheader("Urea")
                    st.session_state.form_data["Urea_Unit"] = st.text_input("Unit", key="Urea_Unit")
                    st.session_state.form_data["Urea_Referance_Range"] = st.text_input("Referance Range", key="Urea_Referance_Range")

                    st.subheader("Blood urea nitrogen (BUN)")
                    st.session_state.form_data["Blood_urea_nitrogen_Unit"] = st.text_input("Unit", key="Blood_urea_nitrogen_Unit")
                    st.session_state.form_data["Blood_urea_nitrogen_Referance_Range"] = st.text_input("Referance Range", key="Blood_urea_nitrogen_Referance_Range")

                    st.subheader("Sr.Creatinine")
                    st.session_state.form_data["Sr_Creatinine_Unit"] = st.text_input("Unit", key="Sr_Creatinine_Unit")
                    st.session_state.form_data["Sr_Creatinine_Referance_Range"] = st.text_input("Referance Range", key="Sr_Creatinine_Referance_Range")

                    st.subheader("Uric acid")
                    st.session_state.form_data["Uric_acid_Unit"] = st.text_input("Unit", key="Uric_acid_Unit")
                    st.session_state.form_data["Uric_acid_Referance_Range"] = st.text_input("Referance Range", key="Uric_acid_Referance_Range")

                    st.subheader("Sodium")
                    st.session_state.form_data["Sodium_Unit"] = st.text_input("Unit", key="Sodium_Unit")
                    st.session_state.form_data["Sodium_Referance_Range"] = st.text_input("Referance Range", key="Sodium_Referance_Range")

                    st.subheader("Potassium")
                    st.session_state.form_data["Potassium_Unit"] = st.text_input("Unit", key="Potassium_Unit")
                    st.session_state.form_data["Potassium_Referance_Range"] = st.text_input("Referance Range", key="Potassium_Referance_Range")

                    st.subheader("Calcium")
                    st.session_state.form_data["Calcium_Unit"] = st.text_input("Unit", key="Calcium_Unit")
                    st.session_state.form_data["Calcium_Referance_Range"] = st.text_input("Referance Range", key="Calcium_Referance_Range")

                    st.subheader("Phosphorus")
                    st.session_state.form_data["Phosphorus_Unit"] = st.text_input("Unit", key="Phosphorus_Unit")
                    st.session_state.form_data["Phosphorus_Referance_Range"] = st.text_input("Referance Range", key="Phosphorus_Referance_Range")

                    st.subheader("Chloride")
                    st.session_state.form_data["Chloride_Unit"] = st.text_input("Unit", key="Chloride_Unit")
                    st.session_state.form_data["Chloride_Referance_Range"] = st.text_input("Referance Range", key="Chloride_Referance_Range")

                    st.subheader("Bicarbonate")
                    st.session_state.form_data["Bicarbonate_Unit"] = st.text_input("Unit", key="Bicarbonate_Unit")
                    st.session_state.form_data["Bicarbonate_Referance_Range"] = st.text_input("Referance Range", key="Bicarbonate_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "LIPID PROFILE":
                    # Total - Cholesterol Triglycerides			HDL - Cholesterol			VLDL -Choleserol			LDL- Cholesterol			CHOL:HDL ratio			LDL.CHOL/HDL.CHOL Ratio
                    st.subheader("Total - Cholesterol")
                    st.session_state.form_data["Total_Cholesterol_Unit"] = st.text_input("Unit", key="Total_Cholesterol_Unit")
                    st.session_state.form_data["Total_Cholesterol_Referance_Range"] = st.text_input("Referance Range", key="Total_Cholesterol_Referance_Range")
                    
                    st.subheader("Triglycerides")
                    st.session_state.form_data["Triglycerides_Unit"] = st.text_input("Unit", key="Triglycerides_Unit")
                    st.session_state.form_data["Triglycerides_Referance_Range"] = st.text_input("Referance Range", key="Triglycerides_Referance_Range")

                    st.subheader("HDL - Cholesterol")
                    st.session_state.form_data["HDL_Cholesterol_Unit"] = st.text_input("Unit", key="HDL_Cholesterol_Unit")
                    st.session_state.form_data["HDL_Cholesterol_Referance_Range"] = st.text_input("Referance Range", key="HDL_Cholesterol_Referance_Range")

                    st.subheader("VLDL -Choleserol")
                    st.session_state.form_data["VLDL_Choleserol_Unit"] = st.text_input("Unit", key="VLDL_Choleserol_Unit")
                    st.session_state.form_data["VLDL_Choleserol_Referance_Range"] = st.text_input("Referance Range", key="VLDL_Choleserol_Referance_Range")

                    st.subheader("LDL- Cholesterol")
                    st.session_state.form_data["LDL_Cholesterol_Unit"] = st.text_input("Unit", key="LDL_Cholesterol_Unit")
                    st.session_state.form_data["LDL_Cholesterol_Referance_Range"] = st.text_input("Referance Range", key="LDL_Cholesterol_Referance_Range")

                    st.subheader("CHOL:HDL ratio")
                    st.session_state.form_data["CHOL_HDL_ratio_Unit"] = st.text_input("Unit", key="CHOL_HDL_ratio_Unit")
                    st.session_state.form_data["CHOL_HDL_ratio_Referance_Range"] = st.text_input("Referance Range", key="CHOL_HDL_ratio_Referance_Range")

                    st.subheader("LDL.CHOL/HDL.CHOL Ratio")
                    st.session_state.form_data["LDL_CHOL_HDL_CHOL_Ratio_Unit"] = st.text_input("Unit", key="LDL_CHOL_HDL_CHOL_Ratio_Unit")
                    st.session_state.form_data["LDL_CHOL_HDL_CHOL_Ratio_Referance_Range"] = st.text_input("Referance Range", key="LDL_CHOL_HDL_CHOL_Ratio_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "LIVER FUNCTION TEST":
                    #Bilirubin -Total			Bilirubin -Direct			Bilirubin -indirect			SGOT /AST			SGPT /ALT			Alkaline phosphatase			Total Protein			Albumin (Serum )			 Globulin(Serum)			Alb/Glob Ratio			Gamma Glutamyl transferase
                    st.subheader("Bilirubin -Total")
                    st.session_state.form_data["Bilirubin_Total_Unit"] = st.text_input("Unit", key="Bilirubin_Total_Unit")
                    st.session_state.form_data["Bilirubin_Total_Referance_Range"] = st.text_input("Referance Range", key="Bilirubin_Total_Referance_Range")

                    st.subheader("Bilirubin -Direct")
                    st.session_state.form_data["Bilirubin_Direct_Unit"] = st.text_input("Unit", key="Bilirubin_Direct_Unit")
                    st.session_state.form_data["Bilirubin_Direct_Referance_Range"] = st.text_input("Referance Range", key="Bilirubin_Direct_Referance_Range")

                    st.subheader("Bilirubin -indirect")
                    st.session_state.form_data["Bilirubin_indirect_Unit"] = st.text_input("Unit", key="Bilirubin_indirect_Unit")
                    st.session_state.form_data["Bilirubin_indirect_Referance_Range"] = st.text_input("Referance Range", key="Bilirubin_indirect_Referance_Range")

                    st.subheader("SGOT /AST")
                    st.session_state.form_data["SGOT_AST_Unit"] = st.text_input("Unit", key="SGOT_AST_Unit")
                    st.session_state.form_data["SGOT_AST_Referance_Range"] = st.text_input("Referance Range", key="SGOT_AST_Referance_Range")

                    st.subheader("SGPT /ALT")
                    st.session_state.form_data["SGPT_ALT_Unit"] = st.text_input("Unit", key="SGPT_ALT_Unit")
                    st.session_state.form_data["SGPT_ALT_Referance_Range"] = st.text_input("Referance Range", key="SGPT_ALT_Referance_Range")

                    st.subheader("Alkaline phosphatase")
                    st.session_state.form_data["Alkaline_phosphatase_Unit"] = st.text_input("Unit", key="Alkaline_phosphatase_Unit")
                    st.session_state.form_data["Alkaline_phosphatase_Referance_Range"] = st.text_input("Referance Range", key="Alkaline_phosphatase_Referance_Range")

                    st.subheader("Total Protein")
                    st.session_state.form_data["Total_Protein_Unit"] = st.text_input("Unit", key="Total_Protein_Unit")
                    st.session_state.form_data["Total_Protein_Referance_Range"] = st.text_input("Referance Range", key="Total_Protein_Referance_Range")

                    st.subheader("Albumin (Serum )")
                    st.session_state.form_data["Albumin_Serum_Unit"] = st.text_input("Unit", key="Albumin_Serum_Unit")
                    st.session_state.form_data["Albumin_Serum_Referance_Range"] = st.text_input("Referance Range", key="Albumin_Serum_Referance_Range")

                    st.subheader("Globulin(Serum)")
                    st.session_state.form_data["Globulin_Serum_Unit"] = st.text_input("Unit", key="Globulin_Serum_Unit")
                    st.session_state.form_data["Globulin_Serum_Referance_Range"] = st.text_input("Referance Range", key="Globulin_Serum_Referance_Range")

                    st.subheader("Alb/Glob Ratio")
                    st.session_state.form_data["Alb_Glob_Ratio_Unit"] = st.text_input("Unit", key="Alb_Glob_Ratio_Unit")
                    st.session_state.form_data["Alb_Glob_Ratio_Referance_Range"] = st.text_input("Referance Range", key="Alb_Glob_Ratio_Referance_Range")

                    st.subheader("Gamma Glutamyl transferase")
                    st.session_state.form_data["Gamma_Glutamyl_transferase_Unit"] = st.text_input("Unit", key="Gamma_Glutamyl_transferase_Unit")
                    st.session_state.form_data["Gamma_Glutamyl_transferase_Referance_Range"] = st.text_input("Referance Range", key="Gamma_Glutamyl_transferase_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "THYROID FUNCTION TEST":
                    #T3- Triiodothyroine			T4 - Thyroxine			TSH- Thyroid Stimulating Hormone
                    st.subheader("T3- Triiodothyroine")
                    st.session_state.form_data["T3_Triiodothyroine_Unit"] = st.text_input("Unit", key="T3_Triiodothyroine_Unit")
                    st.session_state.form_data["T3_Triiodothyroine_Referance_Range"] = st.text_input("Referance Range", key="T3_Triiodothyroine_Referance_Range")

                    st.subheader("T4 - Thyroxine")
                    st.session_state.form_data["T4_Thyroxine_Unit"] = st.text_input("Unit", key="T4_Thyroxine_Unit")
                    st.session_state.form_data["T4_Thyroxine_Referance_Range"] = st.text_input("Referance Range", key="T4_Thyroxine_Referance_Range")

                    st.subheader("TSH- Thyroid Stimulating Hormone")
                    st.session_state.form_data["TSH_Thyroid_Stimulating_Hormone_Unit"] = st.text_input("Unit", key="TSH_Thyroid_Stimulating_Hormone_Unit")
                    st.session_state.form_data["TSH_Thyroid_Stimulating_Hormone_Referance_Range"] = st.text_input("Referance Range", key="TSH_Thyroid_Stimulating_Hormone_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "AUTOIMMUNE TEST":
                    #ANA (Antinuclear Antibody)			Anti ds DNA			Anticardiolipin Antibodies (IgG & IgM)			Rheumatoid factor
                    st.subheader("ANA (Antinuclear Antibody)")
                    st.session_state.form_data["ANA_Antinuclear_Antibody_Unit"] = st.text_input("Unit", key="ANA_Antinuclear_Antibody_Unit")
                    st.session_state.form_data["ANA_Antinuclear_Antibody_Referance_Range"] = st.text_input("Referance Range", key="ANA_Antinuclear_Antibody_Referance_Range")

                    st.subheader("Anti ds DNA")
                    st.session_state.form_data["Anti_ds_DNA_Unit"] = st.text_input("Unit", key="Anti_ds_DNA_Unit")
                    st.session_state.form_data["Anti_ds_DNA_Referance_Range"] = st.text_input("Referance Range", key="Anti_ds_DNA_Referance_Range")

                    st.subheader("Anticardiolipin Antibodies (IgG & IgM)")
                    st.session_state.form_data["Anticardiolipin_Antibodies_Unit"] = st.text_input("Unit", key="Anticardiolipin_Antibodies_Unit")
                    st.session_state.form_data["Anticardiolipin_Antibodies_Referance_Range"] = st.text_input("Referance Range", key="Anticardiolipin_Antibodies_Referance_Range")

                    st.subheader("Rheumatoid factor")
                    st.session_state.form_data["Rheumatoid_factor_Unit"] = st.text_input("Unit", key="Rheumatoid_factor_Unit")
                    st.session_state.form_data["Rheumatoid_factor_Referance_Range"] = st.text_input("Referance Range", key="Rheumatoid_factor_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "COAGULATION TEST":
                    #Prothrombin Time (PT)			PT INR			Bleeding Time (BT)			Clotting Time (CT)
                    st.subheader("Prothrombin Time (PT)")
                    st.session_state.form_data["Prothrombin_Time_Unit"] = st.text_input("Unit", key="Prothrombin_Time_Unit")
                    st.session_state.form_data["Prothrombin_Time_Referance_Range"] = st.text_input("Referance Range", key="Prothrombin_Time_Referance_Range")

                    st.subheader("PT INR")
                    st.session_state.form_data["PT_INR_Unit"] = st.text_input("Unit", key="PT_INR_Unit")
                    st.session_state.form_data["PT_INR_Referance_Range"] = st.text_input("Referance Range", key="PT_INR_Referance_Range")

                    st.subheader("Bleeding Time (BT)")
                    st.session_state.form_data["Bleeding_Time_Unit"] = st.text_input("Unit", key="Bleeding_Time_Unit")
                    st.session_state.form_data["Bleeding_Time_Referance_Range"] = st.text_input("Referance Range", key="Bleeding_Time_Referance_Range")

                    st.subheader("Clotting Time (CT)")
                    st.session_state.form_data["Clotting_Time_Unit"] = st.text_input("Unit", key="Clotting_Time_Unit")
                    st.session_state.form_data["Clotting_Time_Referance_Range"] = st.text_input("Referance Range", key="Clotting_Time_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "ENZYMES & CARDIAC Profile":
                    #Acid Phosphatase			Adenosine Deaminase			Amylase			Lipase			Troponin- T			Troponin- I			CPK - TOTAL			CPK - MB			ECG 		ECHO		TMT
                    st.subheader("Acid Phosphatase")
                    st.session_state.form_data["Acid_Phosphatase_Unit"] = st.text_input("Unit", key="Acid_Phosphatase_Unit")
                    st.session_state.form_data["Acid_Phosphatase_Referance_Range"] = st.text_input("Referance Range", key="Acid_Phosphatase_Referance_Range")

                    st.subheader("Adenosine Deaminase")
                    st.session_state.form_data["Adenosine_Deaminase_Unit"] = st.text_input("Unit", key="Adenosine_Deaminase_Unit")
                    st.session_state.form_data["Adenosine_Deaminase_Referance_Range"] = st.text_input("Referance Range", key="Adenosine_Deaminase_Referance_Range")

                    st.subheader("Amylase")
                    st.session_state.form_data["Amylase_Unit"] = st.text_input("Unit", key="Amylase_Unit")
                    st.session_state.form_data["Amylase_Referance_Range"] = st.text_input("Referance Range", key="Amylase_Referance_Range")

                    st.subheader("Lipase")
                    st.session_state.form_data["Lipase_Unit"] = st.text_input("Unit", key="Lipase_Unit")
                    st.session_state.form_data["Lipase_Referance_Range"] = st.text_input("Referance Range", key="Lipase_Referance_Range")

                    st.subheader("Troponin- T")
                    st.session_state.form_data["Troponin_T_Unit"] = st.text_input("Unit", key="Troponin_T_Unit")
                    st.session_state.form_data["Troponin_T_Referance_Range"] = st.text_input("Referance Range", key="Troponin_T_Referance_Range")

                    st.subheader("Troponin- I")
                    st.session_state.form_data["Troponin_I_Unit"] = st.text_input("Unit", key="Troponin_I_Unit")
                    st.session_state.form_data["Troponin_I_Referance_Range"] = st.text_input("Referance Range", key="Troponin_I_Referance_Range")

                    st.subheader("CPK - TOTAL")
                    st.session_state.form_data["CPK_TOTAL_Unit"] = st.text_input("Unit", key="CPK_TOTAL_Unit")
                    st.session_state.form_data["CPK_TOTAL_Referance_Range"] = st.text_input("Referance Range", key="CPK_TOTAL_Referance_Range")

                    st.subheader("CPK - MB")
                    st.session_state.form_data["CPK_MB_Unit"] = st.text_input("Unit", key="CPK_MB_Unit")
                    st.session_state.form_data["CPK_MB_Referance_Range"] = st.text_input("Referance Range", key="CPK_MB_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "URINE ROUTINE":
                    #Colour			Appearance			Reaction (pH)			Specific gravity			Protein/Albumin			Glucose (Urine)			Ketone Bodies			Urobilinogen			Bile Salts			Bile Pigments			WBC / Pus cells			Red Blood Cells			Epithelial celss			Casts			Crystals			Bacteria
                    st.subheader("Colour")
                    st.session_state.form_data["Colour_Unit"] = st.text_input("Unit", key="Colour_Unit")
                    st.session_state.form_data["Colour_Referance_Range"] = st.text_input("Referance Range", key="Colour_Referance_Range")

                    st.subheader("Appearance")
                    st.session_state.form_data["Appearance_Unit"] = st.text_input("Unit", key="Appearance_Unit")
                    st.session_state.form_data["Appearance_Referance_Range"] = st.text_input("Referance Range", key="Appearance_Referance_Range")

                    st.subheader("Reaction (pH)")
                    st.session_state.form_data["Reaction_pH_Unit"] = st.text_input("Unit", key="Reaction_pH_Unit")
                    st.session_state.form_data["Reaction_pH_Referance_Range"] = st.text_input("Referance Range", key="Reaction_pH_Referance_Range")

                    st.subheader("Specific gravity")
                    st.session_state.form_data["Specific_gravity_Unit"] = st.text_input("Unit", key="Specific_gravity_Unit")
                    st.session_state.form_data["Specific_gravity_Referance_Range"] = st.text_input("Referance Range", key="Specific_gravity_Referance_Range")

                    st.subheader("Protein/Albumin")
                    st.session_state.form_data["Protein_Albumin_Unit"] = st.text_input("Unit", key="Protein_Albumin_Unit")
                    st.session_state.form_data["Protein_Albumin_Referance_Range"] = st.text_input("Referance Range", key="Protein_Albumin_Referance_Range")

                    st.subheader("Glucose (Urine)")
                    st.session_state.form_data["Glucose_Urine_Unit"] = st.text_input("Unit", key="Glucose_Urine_Unit")
                    st.session_state.form_data["Glucose_Urine_Referance_Range"] = st.text_input("Referance Range", key="Glucose_Urine_Referance_Range")

                    st.subheader("Ketone Bodies")
                    st.session_state.form_data["Ketone_Bodies_Unit"] = st.text_input("Unit", key="Ketone_Bodies_Unit")
                    st.session_state.form_data["Ketone_Bodies_Referance_Range"] = st.text_input("Referance Range", key="Ketone_Bodies_Referance_Range")

                    st.subheader("Urobilinogen")
                    st.session_state.form_data["Urobilinogen_Unit"] = st.text_input("Unit", key="Urobilinogen_Unit")
                    st.session_state.form_data["Urobilinogen_Referance_Range"] = st.text_input("Referance Range", key="Urobilinogen_Referance_Range")

                    st.subheader("Bile Salts")
                    st.session_state.form_data["Bile_Salts_Unit"] = st.text_input("Unit", key="Bile_Salts_Unit")
                    st.session_state.form_data["Bile_Salts_Referance_Range"] = st.text_input("Referance Range", key="Bile_Salts_Referance_Range")

                    st.subheader("Bile Pigments")
                    st.session_state.form_data["Bile_Pigments_Unit"] = st.text_input("Unit", key="Bile_Pigments_Unit")
                    st.session_state.form_data["Bile_Pigments_Referance_Range"] = st.text_input("Referance Range", key="Bile_Pigments_Referance_Range")

                    st.subheader("WBC / Pus cells")
                    st.session_state.form_data["WBC_Pus_cells_Unit"] = st.text_input("Unit", key="WBC_Pus_cells_Unit")
                    st.session_state.form_data["WBC_Pus_cells_Referance_Range"] = st.text_input("Referance Range", key="WBC_Pus_cells_Referance_Range")

                    st.subheader("Red Blood Cells")
                    st.session_state.form_data["Red_Blood_Cells_Unit"] = st.text_input("Unit", key="Red_Blood_Cells_Unit")
                    st.session_state.form_data["Red_Blood_Cells_Referance_Range"] = st.text_input("Referance Range", key="Red_Blood_Cells_Referance_Range")

                    st.subheader("Epithelial celss")
                    st.session_state.form_data["Epithelial_celss_Unit"] = st.text_input("Unit", key="Epithelial_celss_Unit")
                    st.session_state.form_data["Epithelial_celss_Referance_Range"] = st.text_input("Referance Range", key="Epithelial_celss_Referance_Range")

                    st.subheader("Casts")
                    st.session_state.form_data["Casts_Unit"] = st.text_input("Unit", key="Casts_Unit")
                    st.session_state.form_data["Casts_Referance_Range"] = st.text_input("Referance Range", key="Casts_Referance_Range")

                    st.subheader("Crystals")
                    st.session_state.form_data["Crystals_Unit"] = st.text_input("Unit", key="Crystals_Unit")
                    st.session_state.form_data["Crystals_Referance_Range"] = st.text_input("Referance Range", key="Crystals_Referance_Range")

                    st.subheader("Bacteria")
                    st.session_state.form_data["Bacteria_Unit"] = st.text_input("Unit", key="Bacteria_Unit")
                    st.session_state.form_data["Bacteria_Referance_Range"] = st.text_input("Referance Range", key="Bacteria_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "SEROLOGY":
                    #Screening For HIV I & II			HBsAg			HCV			WIDAL			VDRL			Dengue NS1Ag			Dengue  IgG			Dengue IgM   i need only reference for all
                    st.subheader("Screening For HIV I & II")
                    st.session_state.form_data["Screening_For_HIV_Referance_Range"] = st.text_input("Referance Range", key="Screening_For_HIV_Referance_Range")

                    st.subheader("HBsAg")
                    st.session_state.form_data["HBsAg_Referance_Range"] = st.text_input("Referance Range", key="HBsAg_Referance_Range")

                    st.subheader("HCV")
                    st.session_state.form_data["HCV_Referance_Range"] = st.text_input("Referance Range", key="HCV_Referance_Range")

                    st.subheader("WIDAL")
                    st.session_state.form_data["WIDAL_Referance_Range"] = st.text_input("Referance Range", key="WIDAL_Referance_Range")

                    st.subheader("VDRL")
                    st.session_state.form_data["VDRL_Referance_Range"] = st.text_input("Referance Range", key="VDRL_Referance_Range")

                    st.subheader("Dengue NS1Ag")
                    st.session_state.form_data["Dengue_NS1Ag_Referance_Range"] = st.text_input("Referance Range", key="Dengue_NS1Ag_Referance_Range")

                    st.subheader("Dengue  IgG")
                    st.session_state.form_data["Dengue_IgG_Referance_Range"] = st.text_input("Referance Range", key="Dengue_IgG_Referance_Range")

                    st.subheader("Dengue IgM")
                    st.session_state.form_data["Dengue_IgM_Referance_Range"] = st.text_input("Referance Range", key="Dengue_IgM_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "MOTION":
                    #Colour  Appearance  Occult Blood  Ova  Cyst	 Mucus	Pus Cells	RBCs  Others i need both unit referance range for all
                    st.subheader("Colour")
                    st.session_state.form_data["Colour_Motion_Unit"] = st.text_input("Unit", key="Colour_Motion_Unit")
                    st.session_state.form_data["Colour_Motion_Referance_Range"] = st.text_input("Referance Range", key="Colour_Motion_Referance_Range")

                    st.subheader("Appearance")
                    st.session_state.form_data["Appearance_Motion_Unit"] = st.text_input("Unit", key="Appearance_Motion_Unit")
                    st.session_state.form_data["Appearance_Motion_Referance_Range"] = st.text_input("Referance Range", key="Appearance_Motion_Referance_Range")

                    st.subheader("Occult Blood")
                    st.session_state.form_data["Occult_Blood_Unit"] = st.text_input("Unit", key="Occult_Blood_Unit")
                    st.session_state.form_data["Occult_Blood_Referance_Range"] = st.text_input("Referance Range", key="Occult_Blood_Referance_Range")

                    st.subheader("Ova")
                    st.session_state.form_data["Ova_Unit"] = st.text_input("Unit", key="Ova_Unit")
                    st.session_state.form_data["Ova_Referance_Range"] = st.text_input("Referance Range", key="Ova_Referance_Range")

                    st.subheader("Cyst")
                    st.session_state.form_data["Cyst_Unit"] = st.text_input("Unit", key="Cyst_Unit")
                    st.session_state.form_data["Cyst_Referance_Range"] = st.text_input("Referance Range", key="Cyst_Referance_Range")

                    st.subheader("Mucus")
                    st.session_state.form_data["Mucus_Unit"] = st.text_input("Unit", key="Mucus_Unit")
                    st.session_state.form_data["Mucus_Referance_Range"] = st.text_input("Referance Range", key="Mucus_Referance_Range")

                    st.subheader("Pus Cells")
                    st.session_state.form_data["Pus_Cells_Unit"] = st.text_input("Unit", key="Pus_Cells_Unit")
                    st.session_state.form_data["Pus_Cells_Referance_Range"] = st.text_input("Referance Range", key="Pus_Cells_Referance_Range")

                    st.subheader("RBCs")
                    st.session_state.form_data["RBCs_Unit"] = st.text_input("Unit", key="RBCs_Unit")
                    st.session_state.form_data["RBCs_Referance_Range"] = st.text_input("Referance Range", key="RBCs_Referance_Range")

                    st.subheader("Others")
                    st.session_state.form_data["Others_Unit"] = st.text_input("Unit", key="Others_Unit")
                    st.session_state.form_data["Others_Referance_Range"] = st.text_input("Referance Range", key="Others_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "ROUTINE CULTURE & SENSITIVITY TEST":
                    #Urine			Motion			Sputum			Blood
                    st.subheader("Urine")
                    st.session_state.form_data["Urine_Unit"] = st.text_input("Unit", key="Urine_Unit")
                    st.session_state.form_data["Urine_Referance_Range"] = st.text_input("Referance Range", key="Urine_Referance_Range")

                    st.subheader("Motion")
                    st.session_state.form_data["Motion_Unit"] = st.text_input("Unit", key="Motion_Unit")
                    st.session_state.form_data["Motion_Referance_Range"] = st.text_input("Referance Range", key="Motion_Referance_Range")

                    st.subheader("Sputum")
                    st.session_state.form_data["Sputum_Unit"] = st.text_input("Unit", key="Sputum_Unit")
                    st.session_state.form_data["Sputum_Referance_Range"] = st.text_input("Referance Range", key="Sputum_Referance_Range")

                    st.subheader("Blood")
                    st.session_state.form_data["Blood_Unit"] = st.text_input("Unit", key="Blood_Unit")
                    st.session_state.form_data["Blood_Referance_Range"] = st.text_input("Referance Range", key="Blood_Referance_Range")

                    if st.button("Submit"):
                        st.write(st.session_state.form_data)

                if Investigations == "MEN'S PACK":
                    #PSA (Prostate specific Antigen)
                    st.subheader("PSA (Prostate specific Antigen)")
                    st.session_state.form_data["PSA_Unit"] = st.text_input("Unit", key="PSA_Unit")
                    st.session_state.form_data["PSA_Referance_Range"] = st.text_input("Referance Range", key="PSA_Referance_Range")

                    if st.button("Submit"):
                        i = st.session_state.form_data
                        st.write(i)
                                                    
                            #"Year":"2022"
                            # "Batch":"1"
                            # "Hospital Name":"manipal"
                            # "Hemoglobin_Unit":""
                            # "Hemoglobin_Referance_Range":""
                            # "Total_RBC_Unit":""
                            # "Total_RBC_Referance_Range":""
                            # "Total_WBC_Unit":""
                            # "Total_WBC_Referance_Range":""
                            # "Neutrophil_Unit":""
                            # "Neutrophil_Referance_Range":""
                            # "Monocyte_Unit":""
                            # "Monocyte_Referance_Range":""
                            # "PCV_Unit":""
                            # "PCV_Referance_Range":""
                            # "MCV_Unit":""
                            # "MCV_Referance_Range":""
                            # "MCH_Unit":""
                            # "MCH_Referance_Range":""
                            # "Lymphocyte_Unit":""
                            # "Lymphocyte_Referance_Range":""
                            # "ESR_Unit":""
                            # "ESR_Referance_Range":""
                            # "MCHC_Unit":""
                            # "MCHC_Referance_Range":""
                            # "Platelet_Count_Unit":""
                            # "Platelet_Count_Referance_Range":""
                            # "RDW_Unit":""
                            # "RDW_Referance_Range":""
                            # "Eosinophil_Unit":""
                            # "Eosinophil_Referance_Range":""
                            # "Basophil_Unit":""
                            # "Basophil_Referance_Range":""
                        insert_hematology = ("INSERT INTO haematalogy_unit_range(year, batch, hospital, heamoglobin_unit, heamoglobin_range, rbc_count_unit, rbc_count_range, wbc_count_unit, wbc_count_range, haemotocrit_unit, haemotocrit_range, mcv_unit, mcv_range, mch_unit, mch_range, mchc_unit, mchc_range, platelet_unit, platelet_range, rdw_unit, rdw_range, neutrophil_unit, neutrophil_range, lymphocyte_unit, lymphocyte_range, eosinophil_unit, eosinophil_range, monocyte_unit, monocyte_range, basophils_unit, basophils_range, esr_unit, esr_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                        hematology_data = (i["Year"], i["Batch"], i["Hospital Name"], i["Hemoglobin_Unit"], i["Hemoglobin_Referance_Range"], i["Total_RBC_Unit"], i["Total_RBC_Referance_Range"], i["Total_WBC_Unit"], i["Total_WBC_Referance_Range"], i["PCV_Unit"], i["PCV_Referance_Range"], i["MCV_Unit"], i["MCV_Referance_Range"], i["MCH_Unit"], i["MCH_Referance_Range"], i["MCHC_Unit"], i["MCHC_Referance_Range"], i["Platelet_Count_Unit"], i["Platelet_Count_Referance_Range"], i["RDW_Unit"], i["RDW_Referance_Range"], i["Neutrophil_Unit"], i["Neutrophil_Referance_Range"], i["Lymphocyte_Unit"], i["Lymphocyte_Referance_Range"], i["Eosinophil_Unit"], i["Eosinophil_Referance_Range"], i["Monocyte_Unit"], i["Monocyte_Referance_Range"], i["Basophil_Unit"], i["Basophil_Referance_Range"], i["ESR_Unit"], i["ESR_Referance_Range"])
                        cursor.execute(insert_hematology, hematology_data)
                        connection.commit()


                            # "Glucose_F_Unit":""
                            # "Glucose_F_Referance_Range":""
                            # "Glucose_PP_Unit":""
                            # "Glucose_PP_Referance_Range":""
                            # "Random_Blood_sugar_Unit":""
                            # "Random_Blood_sugar_Referance_Range":""
                            # "Estimated_Average_Glucose_Unit":""
                            # "Estimated_Average_Glucose_Referance_Range":""
                            # "HbA1c_Unit":""
                            # "HbA1c_Referance_Range":""
                        insert_routine_sugartest = ("INSERT INTO routine_sugar_tests_unit_range(year, batch, hospital, glucosef_unit, glucosef_range, glucosepp_unit, glucosepp_range, rbs_unit, rbs_range, eag_unit, eag_range, hba1c_unit, hba1c_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                        routine_sugar_data = (i["Year"], i["Batch"], i["Hospital Name"], i["Glucose_F_Unit"], i["Glucose_F_Referance_Range"], i["Glucose_PP_Unit"], i["Glucose_PP_Referance_Range"], i["Random_Blood_sugar_Unit"], i["Random_Blood_sugar_Referance_Range"], i["Estimated_Average_Glucose_Unit"], i["Estimated_Average_Glucose_Referance_Range"], i["HbA1c_Unit"], i["HbA1c_Referance_Range"])
                        cursor.execute(insert_routine_sugartest, routine_sugar_data)
                        connection.commit()

                            # "Blood_urea_nitrogen_Unit":""
                            # "Blood_urea_nitrogen_Referance_Range":""
                            # "Sr_Creatinine_Unit":""
                            # "Sr_Creatinine_Referance_Range":""
                            # "Uric_acid_Unit":""
                            # "Uric_acid_Referance_Range":""
                            # "Sodium_Unit":""
                            # "Sodium_Referance_Range":""
                            # "Potassium_Unit":""
                            # "Potassium_Referance_Range":""
                            # "Calcium_Unit":""
                            # "Calcium_Referance_Range":""
                            # "Phosphorus_Unit":""
                            # "Phosphorus_Referance_Range":""
                            # "Chloride_Unit":""
                            # "Chloride_Referance_Range":""
                            # "Bicarbonate_Unit":""
                            # "Bicarbonate_Referance_Range":""


                        insert_rft = ("INSERT INTO rft_unit_range( year, batch, hospital, urea_unit, urea_range, bun_unit, bun_range, sr_creatinine_unit, sr_creatinine_range, uric_acid_unit, uric_acid_range, sodium_unit, sodium_range, potassium_unit, potassium_range, calcium_unit, calcium_range, phosphorus_unit, phosphorus_range, chloride_unit, chloride_range, bicarbonate_unit, bicarbonate_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )")
                        rft_data = (i["Year"], i["Batch"], i["Hospital Name"],i["Urea_Unit"],i["Urea_Referance_Range"], i["Blood_urea_nitrogen_Unit"], i["Blood_urea_nitrogen_Referance_Range"], i["Sr_Creatinine_Unit"], i["Sr_Creatinine_Referance_Range"], i["Uric_acid_Unit"], i["Uric_acid_Referance_Range"], i["Sodium_Unit"], i["Sodium_Referance_Range"], i["Potassium_Unit"], i["Potassium_Referance_Range"], i["Calcium_Unit"], i["Calcium_Referance_Range"], i["Phosphorus_Unit"], i["Phosphorus_Referance_Range"], i["Chloride_Unit"], i["Chloride_Referance_Range"], i["Bicarbonate_Unit"], i["Bicarbonate_Referance_Range"])
                        cursor.execute(insert_rft, rft_data)
                        connection.commit()
                        # "Total_Cholesterol_Unit":""
                        # "Total_Cholesterol_Referance_Range":""
                        # "Triglycerides_Unit":""
                        # "Triglycerides_Referance_Range":""
                        # "HDL_Cholesterol_Unit":""
                        # "HDL_Cholesterol_Referance_Range":""
                        # "VLDL_Choleserol_Unit":""
                        # "VLDL_Choleserol_Referance_Range":""
                        # "LDL_Cholesterol_Unit":""
                        # "LDL_Cholesterol_Referance_Range":""
                        # "CHOL_HDL_ratio_Unit":""
                        # "CHOL_HDL_ratio_Referance_Range":""
                        # "LDL_CHOL_HDL_CHOL_Ratio_Unit":""
                        # "LDL_CHOL_HDL_CHOL_Ratio_Referance_Range":""

                        
                        insert_lipid_profile = ("INSERT INTO lipid_profile_unit_range(year, batch, hospital, tcholesterol_unit, tcholesterol_range, triglycerides_unit, triglycerides_range, hdl_cholesterol_unit, hdl_cholesterol_range, vldl_cholesterol_unit, vldl_cholesterol_range, ldl_cholesterol_unit, ldl_cholesterol_range, chol_hdlratio_unit, chol_hdlratio_range, ldlhdlratio_unit, ldlhdlratio_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )")
                        lipid_profile_data = (i["Year"], i["Batch"], i["Hospital Name"], i["Total_Cholesterol_Unit"], i["Total_Cholesterol_Referance_Range"], i["Triglycerides_Unit"], i["Triglycerides_Referance_Range"], i["HDL_Cholesterol_Unit"], i["HDL_Cholesterol_Referance_Range"], i["VLDL_Choleserol_Unit"], i["VLDL_Choleserol_Referance_Range"], i["LDL_Cholesterol_Unit"], i["LDL_Cholesterol_Referance_Range"], i["CHOL_HDL_ratio_Unit"], i["CHOL_HDL_ratio_Referance_Range"], i["LDL_CHOL_HDL_CHOL_Ratio_Unit"], i["LDL_CHOL_HDL_CHOL_Ratio_Referance_Range"])
                        cursor.execute(insert_lipid_profile, lipid_profile_data)
                        connection.commit()


                            # "Bilirubin_Total_Unit":""
                            # "Bilirubin_Total_Referance_Range":""
                            # "Bilirubin_Direct_Unit":""
                            # "Bilirubin_Direct_Referance_Range":""
                            # "Bilirubin_indirect_Unit":""
                            # "Bilirubin_indirect_Referance_Range":""
                            # "SGOT_AST_Unit":""
                            # "SGOT_AST_Referance_Range":""
                            # "SGPT_ALT_Unit":""
                            # "SGPT_ALT_Referance_Range":""
                            # "Alkaline_phosphatase_Unit":""
                            # "Alkaline_phosphatase_Referance_Range":""
                            # "Total_Protein_Unit":""
                            # "Total_Protein_Referance_Range":""
                            # "Albumin_Serum_Unit":""
                            # "Albumin_Serum_Referance_Range":""
                            # "Globulin_Serum_Unit":""
                            # "Globulin_Serum_Referance_Range":""
                            # "Alb_Glob_Ratio_Unit":""
                            # "Alb_Glob_Ratio_Referance_Range":""
                            # "Gamma_Glutamyl_transferase_Unit":""
                            # "Gamma_Glutamyl_transferase_Referance_Range":""
                        insert_lft = ("INSERT INTO liver_function_unit_range( year, batch, hospital, bilirubin_total_unit, bilirubin_total_range, bilirubin_direct_unit, bilirubin_direct_range, bilirubin_indirect_unit, bilirubin_indirect_range, sgot_alt_unit, sgot_alt_range, sgpt_alt_unit, sgpt_alt_range, alkaline_phosphatase_unit, alkaline_phosphatase_range, total_protein_unit, total_protein_range, albumin_unit, albumin_range, globulin_unit, globulin_range, alb_globratio_unit, alb_globratio_range, gammagt_unit, gammagt_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                        lft_data = (i["Year"], i["Batch"], i["Hospital Name"], i["Bilirubin_Total_Unit"], i["Bilirubin_Total_Referance_Range"], i["Bilirubin_Direct_Unit"], i["Bilirubin_Direct_Referance_Range"], i["Bilirubin_indirect_Unit"], i["Bilirubin_indirect_Referance_Range"], i["SGOT_AST_Unit"], i["SGOT_AST_Referance_Range"], i["SGPT_ALT_Unit"], i["SGPT_ALT_Referance_Range"], i["Alkaline_phosphatase_Unit"], i["Alkaline_phosphatase_Referance_Range"], i["Total_Protein_Unit"], i["Total_Protein_Referance_Range"], i["Albumin_Serum_Unit"], i["Albumin_Serum_Referance_Range"], i["Globulin_Serum_Unit"], i["Globulin_Serum_Referance_Range"], i["Alb_Glob_Ratio_Unit"], i["Alb_Glob_Ratio_Referance_Range"], i["Gamma_Glutamyl_transferase_Unit"], i["Gamma_Glutamyl_transferase_Referance_Range"])
                        cursor.execute(insert_lft, lft_data)
                        connection.commit()

                            # "T3_Triiodothyroine_Unit":""
                            # "T3_Triiodothyroine_Referance_Range":""
                            # "T4_Thyroxine_Unit":""
                            # "T4_Thyroxine_Referance_Range":""
                            # "TSH_Thyroid_Stimulating_Hormone_Unit":""
                            # "TSH_Thyroid_Stimulating_Hormone_Referance_Range":""
                        insert_thyroid = ("INSERT INTO thyroid_function_test_unit_range( year, batch, hospital, t3_unit, t3_range, t4_unit, t4_range, tsh_unit, tsh_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                        thyroid_data = (i["Year"], i["Batch"], i["Hospital Name"], i["T3_Triiodothyroine_Unit"], i["T3_Triiodothyroine_Referance_Range"], i["T4_Thyroxine_Unit"], i["T4_Thyroxine_Referance_Range"], i["TSH_Thyroid_Stimulating_Hormone_Unit"], i["TSH_Thyroid_Stimulating_Hormone_Referance_Range"])
                        cursor.execute(insert_thyroid, thyroid_data)
                        connection.commit()

                            # "ANA_Antinuclear_Antibody_Unit":""
                            # "ANA_Antinuclear_Antibody_Referance_Range":""
                            # "Anti_ds_DNA_Unit":""
                            # "Anti_ds_DNA_Referance_Range":""
                            # "Anticardiolipin_Antibodies_Unit":""
                            # "Anticardiolipin_Antibodies_Referance_Range":""
                            # "Rheumatoid_factor_Unit":""
                            # "Rheumatoid_factor_Referance_Range":""
                        
                        insert_autoimmune = ("INSERT INTO autoimmune_test_unit_range( year, batch, hospital, ana_unit, ana_range, adna_unit, adna_range, anticardiolipin_unit, anticardiolipin_range, rheumatoid_unit, rheumatoid_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                        autoimmune_data = (i["Year"], i["Batch"], i["Hospital Name"], i["ANA_Antinuclear_Antibody_Unit"], i["ANA_Antinuclear_Antibody_Referance_Range"], i["Anti_ds_DNA_Unit"], i["Anti_ds_DNA_Referance_Range"], i["Anticardiolipin_Antibodies_Unit"], i["Anticardiolipin_Antibodies_Referance_Range"], i["Rheumatoid_factor_Unit"], i["Rheumatoid_factor_Referance_Range"])
                        cursor.execute(insert_autoimmune, autoimmune_data)
                        connection.commit()

                            # "Prothrombin_Time_Unit":""
                            # "Prothrombin_Time_Referance_Range":""
                            # "PT_INR_Unit":""
                            # "PT_INR_Referance_Range":""
                            # "Bleeding_Time_Unit":""
                            # "Bleeding_Time_Referance_Range":""
                            # "Clotting_Time_Unit":""
                            # "Clotting_Time_Referance_Range":""

                        insert_coagulation = ("INSERT INTO coagulation_test_unit_range(  year, batch, hospital, pt_unit, pt_range, ptinr_unit, ptinr_range, bt_unit, bt_range, ct_unit, ct_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                        coagulation_data = (i["Year"], i["Batch"], i["Hospital Name"], i["Prothrombin_Time_Unit"], i["Prothrombin_Time_Referance_Range"], i["PT_INR_Unit"], i["PT_INR_Referance_Range"], i["Bleeding_Time_Unit"], i["Bleeding_Time_Referance_Range"], i["Clotting_Time_Unit"], i["Clotting_Time_Referance_Range"])
                        cursor.execute(insert_coagulation, coagulation_data)
                        connection.commit()

                            # "Acid_Phosphatase_Unit":""
                            # "Acid_Phosphatase_Referance_Range":""
                            # "Adenosine_Deaminase_Unit":""
                            # "Adenosine_Deaminase_Referance_Range":""
                            # "Amylase_Unit":""
                            # "Amylase_Referance_Range":""
                            # "Lipase_Unit":""
                            # "Lipase_Referance_Range":""
                            # "Troponin_T_Unit":""
                            # "Troponin_T_Referance_Range":""
                            # "Troponin_I_Unit":""
                            # "Troponin_I_Referance_Range":""
                            # "CPK_TOTAL_Unit":""
                            # "CPK_TOTAL_Referance_Range":""
                            # "CPK_MB_Unit":""
                            # "CPK_MB_Referance_Range":""

                        insert_enzymes = ("INSERT INTO enzymes_cardio_unit_range( year, batch, hospital, acid_phosphatase_unit, acid_phosphatase_range, adenosine_unit, adenosine_range, amylase_unit, amylase_range, lipase_unit, lipase_range, troponin_t_unit, troponin_t_range, troponin_i_unit, troponin_i_range, cpk_total_unit, cpk_total_range, cpk_mb_unit, cpk_mb_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )")
                        enzymes_data = (i["Year"], i["Batch"], i["Hospital Name"], i["Acid_Phosphatase_Unit"], i["Acid_Phosphatase_Referance_Range"], i["Adenosine_Deaminase_Unit"], i["Adenosine_Deaminase_Referance_Range"], i["Amylase_Unit"], i["Amylase_Referance_Range"], i["Lipase_Unit"], i["Lipase_Referance_Range"], i["Troponin_T_Unit"], i["Troponin_T_Referance_Range"], i["Troponin_I_Unit"], i["Troponin_I_Referance_Range"], i["CPK_TOTAL_Unit"], i["CPK_TOTAL_Referance_Range"], i["CPK_MB_Unit"], i["CPK_MB_Referance_Range"])
                        cursor.execute(insert_enzymes, enzymes_data)
                        connection.commit()

                            # "Colour_Unit":""
                            # "Colour_Referance_Range":""
                            # "Appearance_Unit":""
                            # "Appearance_Referance_Range":""
                            # "Reaction_pH_Unit":""
                            # "Reaction_pH_Referance_Range":""
                            # "Specific_gravity_Unit":""
                            # "Specific_gravity_Referance_Range":""
                            # "Protein_Albumin_Unit":""
                            # "Protein_Albumin_Referance_Range":""
                            # "Glucose_Urine_Unit":""
                            # "Glucose_Urine_Referance_Range":""
                            # "Ketone_Bodies_Unit":""
                            # "Ketone_Bodies_Referance_Range":""
                            # "Urobilinogen_Unit":""
                            # "Urobilinogen_Referance_Range":""
                            # "Bile_Salts_Unit":""
                            # "Bile_Salts_Referance_Range":""
                            # "Bile_Pigments_Unit":""
                            # "Bile_Pigments_Referance_Range":""
                            # "WBC_Pus_cells_Unit":""
                            # "WBC_Pus_cells_Referance_Range":""
                            # "Red_Blood_Cells_Unit":""
                            # "Red_Blood_Cells_Referance_Range":""
                            # "Epithelial_celss_Unit":""
                            # "Epithelial_celss_Referance_Range":""
                            # "Casts_Unit":""
                            # "Casts_Referance_Range":""
                            # "Crystals_Unit":""
                            # "Crystals_Referance_Range":""
                            # "Bacteria_Unit":""
                            # "Bacteria_Referance_Range":""

                        insert_urine_routine = ("INSERT INTO urine_routine_unit_range( year, batch, hospital, colour_unit, colour_range, apperance_unit, apperance_range, reaction_unit, reaction_range, specific_gravity_unit, specific_gravity_range, protein_albumin_unit, protein_albumin_range, glucose_unit, glucose_range, ketone_unit, ketone_range, urobilinogen_unit, urobilinogen_range, bile_salts_unit, bile_salts_range, bile_pigments_unit, bile_pigments_range, wbc_pluscells_unit, wbc_pluscells_range, rbc_unit, rbc_range, epithelial_cell_unit, epithelial_cell_range, casts_unit, casts_range, crystals_unit, crystals_range, bacteria_unit, bacteria_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                        urine_routine_data = (i["Year"], i["Batch"], i["Hospital Name"], i["Colour_Unit"], i["Colour_Referance_Range"], i["Appearance_Unit"], i["Appearance_Referance_Range"], i["Reaction_pH_Unit"], i["Reaction_pH_Referance_Range"], i["Specific_gravity_Unit"], i["Specific_gravity_Referance_Range"], i["Protein_Albumin_Unit"], i["Protein_Albumin_Referance_Range"], i["Glucose_Urine_Unit"], i["Glucose_Urine_Referance_Range"], i["Ketone_Bodies_Unit"], i["Ketone_Bodies_Referance_Range"], i["Urobilinogen_Unit"], i["Urobilinogen_Referance_Range"], i["Bile_Salts_Unit"], i["Bile_Salts_Referance_Range"], i["Bile_Pigments_Unit"], i["Bile_Pigments_Referance_Range"], i["WBC_Pus_cells_Unit"], i["WBC_Pus_cells_Referance_Range"], i["Red_Blood_Cells_Unit"], i["Red_Blood_Cells_Referance_Range"], i["Epithelial_celss_Unit"], i["Epithelial_celss_Referance_Range"], i["Casts_Unit"], i["Casts_Referance_Range"], i["Crystals_Unit"], i["Crystals_Referance_Range"], i["Bacteria_Unit"], i["Bacteria_Referance_Range"])
                        cursor.execute(insert_urine_routine, urine_routine_data)
                        connection.commit()

                            # "Screening_For_HIV_Referance_Range":""
                            # "HBsAg_Referance_Range":""
                            # "HCV_Referance_Range":""
                            # "WIDAL_Referance_Range":""
                            # "VDRL_Referance_Range":""
                            # "Dengue_NS1Ag_Referance_Range":""
                            # "Dengue_IgG_Referance_Range":""
                            # "Dengue_IgM_Referance_Range":""
                        insert_serology = ("INSERT INTO serology_result_unit_range(year, batch, hospital, hiv_screening_range, hbsag_range, hcv_range, widal_range, vdrl_range, denguens_range, dengueigg_range, dengueigm_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )")
                        serology_data = (i["Year"], i["Batch"], i["Hospital Name"], i["Screening_For_HIV_Referance_Range"], i["HBsAg_Referance_Range"], i["HCV_Referance_Range"], i["WIDAL_Referance_Range"], i["VDRL_Referance_Range"], i["Dengue_NS1Ag_Referance_Range"], i["Dengue_IgG_Referance_Range"], i["Dengue_IgM_Referance_Range"])
                        cursor.execute(insert_serology, serology_data)
                        connection.commit()

                            # "Colour_Motion_Unit":"Colour"
                            # "Colour_Motion_Referance_Range":"yellow"
                            # "Appearance_Motion_Unit":"density"
                            # "Appearance_Motion_Referance_Range":"solid"
                            # "Occult_Blood_Unit":""
                            # "Occult_Blood_Referance_Range":""
                            # "Ova_Unit":""
                            # "Ova_Referance_Range":""
                            # "Cyst_Unit":""
                            # "Cyst_Referance_Range":""
                            # "Mucus_Unit":""
                            # "Mucus_Referance_Range":""
                            # "Pus_Cells_Unit":""
                            # "Pus_Cells_Referance_Range":""
                            # "RBCs_Unit":""
                            # "RBCs_Referance_Range":""
                            # "Others_Unit":""
                            # "Others_Referance_Range":""

                        insert_motion = ("INSERT INTO motion_unit_range( year, batch, hospital, motion_colour_unit, motion_colour_range, motion_appearance_unit, motion_appearance_range, occult_blood_unit, occult_blood_range, ova_unit, ova_range, cyst_unit, cyst_range, mucus_unit, mucus_range, pus_cells_unit, pus_cells_range, rbcs_unit, rbcs_range, others_t_unit, others_t_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                        motion_data = (i["Year"], i["Batch"], i["Hospital Name"], i["Colour_Motion_Unit"], i["Colour_Motion_Referance_Range"], i["Appearance_Motion_Unit"], i["Appearance_Motion_Referance_Range"], i["Occult_Blood_Unit"], i["Occult_Blood_Referance_Range"], i["Ova_Unit"], i["Ova_Referance_Range"], i["Cyst_Unit"], i["Cyst_Referance_Range"], i["Mucus_Unit"], i["Mucus_Referance_Range"], i["Pus_Cells_Unit"], i["Pus_Cells_Referance_Range"], i["RBCs_Unit"], i["RBCs_Referance_Range"], i["Others_Unit"], i["Others_Referance_Range"])
                        cursor.execute(insert_motion, motion_data)
                        connection.commit()

                            # "Urine_Unit":""
                            # "Urine_Referance_Range":""
                            # "Motion_Unit":""
                            # "Motion_Referance_Range":""
                            # "Sputum_Unit":""
                            # "Sputum_Referance_Range":""
                            # "Blood_Unit":""
                            # "Blood_Referance_Range":""
                        insert_routine_culture = ("INSERT INTO routine_culture_unit_range( year, batch, hospital, urine_unit, urine_range, motion_unit, motion_range, sputum_unit, sputum_range, blood_unit, blood_range) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                        routine_culture_data = (i["Year"], i["Batch"], i["Hospital Name"], i["Urine_Unit"], i["Urine_Referance_Range"], i["Motion_Unit"], i["Motion_Referance_Range"], i["Sputum_Unit"], i["Sputum_Referance_Range"], i["Blood_Unit"], i["Blood_Referance_Range"])
                        cursor.execute(insert_routine_culture, routine_culture_data)
                        connection.commit()

                            # "PSA_Unit":""
                            # "PSA_Referance_Range":""

                        insert_menpack = ("INSERT INTO mens_pack_unit_range( year, batch, hospital, psa_unit, psa_range) VALUES(%s, %s, %s, %s, %s)")
                        menpack_data = (i["Year"], i["Batch"], i["Hospital Name"], i["PSA_Unit"], i["PSA_Referance_Range"])
                        cursor.execute(insert_menpack, menpack_data)
                        connection.commit()
