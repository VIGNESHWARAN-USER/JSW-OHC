import streamlit as st 
from  streamlit_option_menu import option_menu

def addReferenceRange():
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
            st.session_state.form_data["Year"] = st.text_input("Year")
            st.session_state.form_data["Batch"] = st.text_input("Batch")
            st.session_state.form_data["Hospital Name"] = st.text_input("Hospital Name")
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

                if Investigations == "RENAL FUNCTION TEST & ELECTROLYTES":
                    #Blood urea nitrogen (BUN)			Sr.Creatinine			Uric acid			Sodium			Potassium			Calcium			Phosphorus			Chloride			Bicarbonate
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

                if Investigations == "LIPID PROFILE":
                    #Triglycerides			HDL - Cholesterol			VLDL -Choleserol			LDL- Cholesterol			CHOL:HDL ratio			LDL.CHOL/HDL.CHOL Ratio
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

                if Investigations == "MOTION":
                    #Colour			Appearance			Occult Blood			Ova			Cyst			Mucus			Pus Cells			RBCs			Others i need both unit referance range for all
                    st.subheader("Colour")
                    st.session_state.form_data["Colour_Unit"] = st.text_input("Unit", key="Colour_Unit")
                    st.session_state.form_data["Colour_Referance_Range"] = st.text_input("Referance Range", key="Colour_Referance_Range")

                    st.subheader("Appearance")
                    st.session_state.form_data["Appearance_Unit"] = st.text_input("Unit", key="Appearance_Unit")
                    st.session_state.form_data["Appearance_Referance_Range"] = st.text_input("Referance Range", key="Appearance_Referance_Range")

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

                if Investigations == "MEN'S PACK":
                    #PSA (Prostate specific Antigen)
                    st.subheader("PSA (Prostate specific Antigen)")
                    st.session_state.form_data["PSA_Unit"] = st.text_input("Unit", key="PSA_Unit")
                    