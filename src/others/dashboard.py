import streamlit as st
import os
import pandas as pd
import json

def Dashboard(connection,cursor,accessLevel):
    st.header("Dashboard")
    
    # Initialize the variables
    if "total_census" not in st.session_state:
        st.session_state.total_census = 0 
    if "total_healthy" not in st.session_state:
        st.session_state.total_healthy = 0
    if "total_unhealthy" not in st.session_state:
        st.session_state.total_unhealthy = 0
    if "appointments" not in st.session_state:
        st.session_state.appointments = 0

    r1c1,r1c2 = st.columns([2,7])
    with r1c1:
        st.write("<div style='width:100px;height:25px'></div>",unsafe_allow_html=True)
        date = st.date_input("Select a Date")
    with r1c2:
        uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx'])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file,header=[0,1,2])
        df.fillna("null", inplace=True)
        data_dict = df.to_dict(orient='records')
        def convert_to_nested_dict(d_list):
            result = []
            for d in d_list:
                temp_dict = {}
                for keys, value in d.items():
                    temp = temp_dict
                    for key in keys[:-1]:
                        temp = temp.setdefault(key, {})
                    temp[keys[-1]] = value
                result.append(temp_dict)
            return result


        dataitem = convert_to_nested_dict(data_dict)
        # st.write(dataitem[0])
        if st.button("Submit"):
            st.write("Data Submitted")
            for i in dataitem:
                # st.write(i)
                # insert the data into the database
                   
                vitals = ("INSERT INTO vitals(emp_no, Systolic, Diastolic, PulseRate, SpO2, Temperature, RespiratoryRate, Height, Weight, BMI)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                
                vital_values = (i['Details']['Basic detail']['EMP NO'],
                                i['General Test']['Vitals']['Systolic BP'],
                                i['General Test']['Vitals']['Diastolic BP'],
                                i['General Test']['Vitals']['Pulse Rate'],
                                None if i['General Test']['Vitals']['sp O2'] == 'null' else i['General Test']['Vitals']['sp O2'],
                                None if i['General Test']['Vitals']['Temperature']=='null' else i['General Test']['Vitals']['Temperature'],
                                i['General Test']['Vitals']['Respiratory Rate'],
                                i['General Test']['Vitals']['Height'],
                                i['General Test']['Vitals']['weight'],
                                None if i['General Test']['Vitals']['BMI']=='null' else i['General Test']['Vitals']['BMI'])
                cursor.execute(vitals, vital_values)

                hematology = ("INSERT INTO hematology_result( emp_no, heamoglobin, heamoglobin_unit, heamoglobin_range, rbc_count, rbc_count_unit, rbc_count_range, wbc_count, wbc_count_unit, wbc_count_range, haemotocrit, haemotocrit_unit, haemotocrit_range, mcv, mcv_unit, mcv_range, mch, mch_unit, mch_range, mchc, mchc_unit, mchc_range, platelet, platelet_unit, platelet_range, rdw, rdw_unit, rdw_range, neutrophil, neutrophil_unit, neutrophil_range, lymphocyte, lymphocyte_unit, lymphocyte_range, eosinophil, eosinophil_unit, eosinophil_range, monocyte, monocyte_unit, monocyte_range, basophils, basophils_unit, basophils_range, esr, esr_unit, esr_range, pbs_rbc, pbc_parasites, pbc_others)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                hematology_values = (i['Details']['Basic detail']['EMP NO'],
                                    i["HAEMATALOGY"]['Haemoglobin']['RESULT'],
                                    i["HAEMATALOGY"]['Haemoglobin']['UNIT'],
                                    i["HAEMATALOGY"]['Haemoglobin']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['Red Blood Cell (RBC) Count']['RESULT'],
                                    i["HAEMATALOGY"]['Red Blood Cell (RBC) Count']['UNIT'],
                                    i["HAEMATALOGY"]['Red Blood Cell (RBC) Count']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['WBC Count (TC)']['RESULT'],
                                    i["HAEMATALOGY"]['WBC Count (TC)']['UNIT'],
                                    i["HAEMATALOGY"]['WBC Count (TC)']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['Haemotocrit (PCV)']['RESULT'],
                                    i["HAEMATALOGY"]['Haemotocrit (PCV)']['UNIT'],
                                    i["HAEMATALOGY"]['Haemotocrit (PCV)']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['MCV']['RESULT'],
                                    i["HAEMATALOGY"]['MCV']['UNIT'],
                                    i["HAEMATALOGY"]['MCV']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['MCH']['RESULT'],
                                    i["HAEMATALOGY"]['MCH']['UNIT'],
                                    i["HAEMATALOGY"]['MCH']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['MCHC']['RESULT'],
                                    i["HAEMATALOGY"]['MCHC']['UNIT'],
                                    i["HAEMATALOGY"]['MCHC']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['Platelet Count']['RESULT'],
                                    i["HAEMATALOGY"]['Platelet Count']['UNIT'],
                                    i["HAEMATALOGY"]['Platelet Count']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['RDW (CV)']['RESULT'],
                                    i["HAEMATALOGY"]['RDW (CV)']['UNIT'],
                                    i["HAEMATALOGY"]['RDW (CV)']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['Neutrophil']['RESULT'],
                                    i["HAEMATALOGY"]['Neutrophil']['UNIT'],
                                    i["HAEMATALOGY"]['Neutrophil']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['Lymphocyte']['RESULT'],
                                    i["HAEMATALOGY"]['Lymphocyte']['UNIT'],
                                    i["HAEMATALOGY"]['Lymphocyte']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['Eosinophil']['RESULT'],
                                    i["HAEMATALOGY"]['Eosinophil']['UNIT'],
                                    i["HAEMATALOGY"]['Eosinophil']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['Monocyte']['RESULT'],
                                    i["HAEMATALOGY"]['Monocyte']['UNIT'],
                                    i["HAEMATALOGY"]['Monocyte']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['Basophils']['RESULT'],
                                    i["HAEMATALOGY"]['Basophils']['UNIT'],
                                    i["HAEMATALOGY"]['Basophils']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['Erythrocyte Sedimentation Rate (ESR)']['RESULT'],
                                    i["HAEMATALOGY"]['Erythrocyte Sedimentation Rate (ESR)']['UNIT'],
                                    i["HAEMATALOGY"]['Erythrocyte Sedimentation Rate (ESR)']['REFERENCE RANGE'],
                                    i["HAEMATALOGY"]['Peripheral Blood Smear - RBC Morphology']['COMMENTS'],
                                    i["HAEMATALOGY"]['Peripheral Blood Smear - Parasites']['COMMENTS'],
                                    i["HAEMATALOGY"]['Peripheral Blood Smear - Others']['COMMENTS'])
                cursor.execute(hematology, hematology_values) 


                routinesugartest = ("INSERT INTO routine_sugartest"
                "(emp_no, glucosef, glucosef_unit, glucosef_range, "
                "glucosepp, glucosepp_unit, glucosepp_range, "
                "rbs, rbs_unit, rbs_range, eag, eag_unit, eag_range, "
                "hba1c, hba1c_unit, hba1c_range) "
                "VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                routinesugartest_values = (i['Details']['Basic detail']['EMP NO'],
                                        i['ROUTINE SUGAR TESTS']['Glucose (F)']['RESULT'],
                                        i['ROUTINE SUGAR TESTS']['Glucose (F)']['UNIT'],
                                        i['ROUTINE SUGAR TESTS']['Glucose (F)']['REFERENCE RANGE'],
                                        i['ROUTINE SUGAR TESTS']['Glucose (PP)']['RESULT'],
                                        i['ROUTINE SUGAR TESTS']['Glucose (PP)']['UNIT'],
                                        i['ROUTINE SUGAR TESTS']['Glucose (PP)']['REFERENCE RANGE'],
                                        i['ROUTINE SUGAR TESTS']['Random Blood sugar']['RESULT'],
                                        i['ROUTINE SUGAR TESTS']['Random Blood sugar']['UNIT'],
                                        i['ROUTINE SUGAR TESTS']['Random Blood sugar']['REFERENCE RANGE'],
                                        i['ROUTINE SUGAR TESTS']['Estimated Average Glucose']['RESULT'],
                                        i['ROUTINE SUGAR TESTS']['Estimated Average Glucose']['UNIT'],
                                        i['ROUTINE SUGAR TESTS']['Estimated Average Glucose']['REFERENCE RANGE'],
                                        i['ROUTINE SUGAR TESTS']['HbA1c']['RESULT'],
                                        i['ROUTINE SUGAR TESTS']['HbA1c']['UNIT'],
                                        i['ROUTINE SUGAR TESTS']['HbA1c']['REFERENCE RANGE'])
                cursor.execute(routinesugartest, routinesugartest_values)

                        
                renalfunctiontest = ("INSERT INTO rft_result "
                                     "( emp_no, urea, urea_unit, urea_range, "
                                        "bun, bun_unit, bun_range, "
                                        "sr_creatinine, sr_creatinine_unit, sr_creatinine_range, "
                                        "uric_acid, uric_acid_unit, uric_acid_range, "
                                        "sodium, sodium_unit, sodium_range, "
                                        "potassium, potassium_unit, potassium_range, "
                                        "calcium, calcium_unit, calcium_range, "
                                        "phosphorus, phosphorus_unit, phosphorus_range, "
                                        "chloride, chloride_unit, chloride_range, "
                                        "bicarbonate, bicarbonate_unit, bicarbonate_range) "
                                        "VALUES "
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                renalfunctiontest_values = (i['Details']['Basic detail']['EMP NO'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Urea']['RESULT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Urea']['UNIT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Urea']['REFERENCE RANGE'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Blood urea nitrogen (BUN)']['RESULT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Blood urea nitrogen (BUN)']['UNIT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Blood urea nitrogen (BUN)']['REFERENCE RANGE'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Sr.Creatinine']['RESULT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Sr.Creatinine']['UNIT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Sr.Creatinine']['REFERENCE RANGE'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Uric acid']['RESULT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Uric acid']['UNIT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Uric acid']['REFERENCE RANGE'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Sodium']['RESULT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Sodium']['UNIT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Sodium']['REFERENCE RANGE'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Potassium']['RESULT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Potassium']['UNIT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Potassium']['REFERENCE RANGE'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Calcium']['RESULT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Calcium']['UNIT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Calcium']['REFERENCE RANGE'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Phosphorus']['RESULT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Phosphorus']['UNIT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Phosphorus']['REFERENCE RANGE'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Chloride']['RESULT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Chloride']['UNIT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Chloride']['REFERENCE RANGE'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Bicarbonate']['RESULT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Bicarbonate']['UNIT'],
                                            i["RENAL FUNCTION TEST & ELECTROLYTES"]['Bicarbonate']['REFERENCE RANGE'])
                cursor.execute(renalfunctiontest, renalfunctiontest_values)

                lipidprofile = ("INSERT INTO lipid_profile "
                "( emp_no, tcholesterol, tcholesterol_unit, tcholesterol_range, "
                "triglycerides, triglycerides_unit, triglycerides_range, "
                "hdl_cholesterol, hdl_cholesterol_unit, hdl_cholesterol_range, "
                "vldl_cholesterol, vldl_cholesterol_unit, vldl_cholesterol_range, "
                "ldl_cholesterol, ldl_cholesterol_unit, ldl_cholesterol_range, "
                "chol_hdlratio, chol_hdlratio_unit, chol_hdlratio_range, "
                "ldlhdlratio, ldlhdlratio_unit, ldlhdlratio_range) "
                "VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                lipidprofile_values = (i['Details']['Basic detail']['EMP NO'],
                                    i["LIPID PROFILE"]['Total Cholesterol']['RESULT'],
                                    i["LIPID PROFILE"]['Total Cholesterol']['UNIT'],
                                    i["LIPID PROFILE"]['Total Cholesterol']['REFERENCE RANGE'],
                                    i["LIPID PROFILE"]['Triglycerides']['RESULT'],
                                    i["LIPID PROFILE"]['Triglycerides']['UNIT'],
                                    i["LIPID PROFILE"]['Triglycerides']['REFERENCE RANGE'],
                                    i["LIPID PROFILE"]['HDL - Cholesterol']['RESULT'],
                                    i["LIPID PROFILE"]['HDL - Cholesterol']['UNIT'],
                                    i["LIPID PROFILE"]['HDL - Cholesterol']['REFERENCE RANGE'],
                                    i["LIPID PROFILE"]['VLDL -Choleserol']['RESULT'],
                                    i["LIPID PROFILE"]['VLDL -Choleserol']['UNIT'],
                                    i["LIPID PROFILE"]['VLDL -Choleserol']['REFERENCE RANGE'],
                                    i["LIPID PROFILE"]['LDL- Cholesterol']['RESULT'],
                                    i["LIPID PROFILE"]['LDL- Cholesterol']['UNIT'],
                                    i["LIPID PROFILE"]['LDL- Cholesterol']['REFERENCE RANGE'],
                                    i["LIPID PROFILE"]['CHOL:HDL ratio']['RESULT'],
                                    i["LIPID PROFILE"]['CHOL:HDL ratio']['UNIT'],
                                    i["LIPID PROFILE"]['CHOL:HDL ratio']['REFERENCE RANGE'],
                                    i["LIPID PROFILE"]['LDL.CHOL/HDL.CHOL Ratio']['RESULT'],
                                    i["LIPID PROFILE"]['LDL.CHOL/HDL.CHOL Ratio']['UNIT'],
                                    i["LIPID PROFILE"]['LDL.CHOL/HDL.CHOL Ratio']['REFERENCE RANGE'])
                cursor.execute(lipidprofile, lipidprofile_values)

                liverfunctiontest = ("INSERT INTO liver_function "
                "( emp_no, bilirubin_total, bilirubin_total_unit, bilirubin_total_range, "
                "bilirubin_direct, bilirubin_direct_unit, bilirubin_direct_range, "
                "bilirubin_indirect, bilirubin_indirect_unit, bilirubin_indirect_range, "
                "sgot_alt, sgot_alt_unit, sgot_alt_range, "
                "sgpt_alt, sgpt_alt_unit, sgpt_alt_range,"
                "alkaline_phosphatase, alkaline_phosphatase_unit, alkaline_phosphatase_range, "
                "total_protein, total_protein_unit, total_protein_range, "
                "albumin, albumin_unit, albumin_range, "
                "globulin, globulin_unit, globulin_range, "
                "alb_globratio, alb_globratio_unit, alb_globratio_range, "
                "gammagt, gammagt_unit, gammagt_range) "
                "VALUES "
                "( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s, %s)")

                liverfunctiontest_values = (i['Details']['Basic detail']['EMP NO'],
                                            i["LIVER FUNCTION TEST"]['Bilirubin -Total']['RESULT'],
                                            i["LIVER FUNCTION TEST"]['Bilirubin -Total']['UNIT'],
                                            i["LIVER FUNCTION TEST"]['Bilirubin -Total']['REFERENCE RANGE'],
                                            i["LIVER FUNCTION TEST"]['Bilirubin -Direct']['RESULT'],
                                            i["LIVER FUNCTION TEST"]['Bilirubin -Direct']['UNIT'],
                                            i["LIVER FUNCTION TEST"]['Bilirubin -Direct']['REFERENCE RANGE'],
                                            i["LIVER FUNCTION TEST"]['Bilirubin -indirect']['RESULT'],
                                            i["LIVER FUNCTION TEST"]['Bilirubin -indirect']['UNIT'],
                                            i["LIVER FUNCTION TEST"]['Bilirubin -indirect']['REFERENCE RANGE'],
                                            i["LIVER FUNCTION TEST"]['SGOT /AST']['RESULT'],
                                            i["LIVER FUNCTION TEST"]['SGOT /AST']['UNIT'],
                                            i["LIVER FUNCTION TEST"]['SGOT /AST']['REFERENCE RANGE'],
                                            i["LIVER FUNCTION TEST"]['SGPT /ALT']['RESULT'],
                                            i["LIVER FUNCTION TEST"]['SGPT /ALT']['UNIT'],
                                            i["LIVER FUNCTION TEST"]['SGPT /ALT']['REFERENCE RANGE'],
                                            i["LIVER FUNCTION TEST"]['Alkaline phosphatase']['RESULT'],
                                            i["LIVER FUNCTION TEST"]['Alkaline phosphatase']['UNIT'],
                                            i["LIVER FUNCTION TEST"]['Alkaline phosphatase']['REFERENCE RANGE'],
                                            i["LIVER FUNCTION TEST"]['Total Protein']['RESULT'],
                                            i["LIVER FUNCTION TEST"]['Total Protein']['UNIT'],
                                            i["LIVER FUNCTION TEST"]['Total Protein']['REFERENCE RANGE'],
                                            i["LIVER FUNCTION TEST"]['Albumin (Serum )']['RESULT'],
                                            i["LIVER FUNCTION TEST"]['Albumin (Serum )']['UNIT'],
                                            i["LIVER FUNCTION TEST"]['Albumin (Serum )']['REFERENCE RANGE'],
                                            i["LIVER FUNCTION TEST"][' Globulin(Serum)']['RESULT'],
                                            i["LIVER FUNCTION TEST"][' Globulin(Serum)']['UNIT'],
                                            i["LIVER FUNCTION TEST"][' Globulin(Serum)']['REFERENCE RANGE'],
                                            i["LIVER FUNCTION TEST"]['Alb/Glob Ratio']['RESULT'],
                                            i["LIVER FUNCTION TEST"]['Alb/Glob Ratio']['UNIT'],
                                            i["LIVER FUNCTION TEST"]['Alb/Glob Ratio']['REFERENCE RANGE'],
                                            i["LIVER FUNCTION TEST"]['Gamma Glutamyl transferase']['RESULT'],
                                            i["LIVER FUNCTION TEST"]['Gamma Glutamyl transferase']['UNIT'],
                                            i["LIVER FUNCTION TEST"]['Gamma Glutamyl transferase']['REFERENCE RANGE'])
                cursor.execute(liverfunctiontest, liverfunctiontest_values)

                thyroidfunctiontest = ("INSERT INTO thyroid_function_test "
                                        "(emp_no, t3, t3_unit, t3_range, "
                                        "t4, t4_unit, t4_range, "
                                        "tsh, tsh_unit, tsh_range, tsh_nm_ab) "
                                        "VALUES "
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                
                thyroidfunctiontest_values = (i['Details']['Basic detail']['EMP NO'],
                                            i["THYROID FUNCTION TEST"]['T3- Triiodothyroine']['RESULT'],
                                            i["THYROID FUNCTION TEST"]['T3- Triiodothyroine']['UNIT'],
                                            i["THYROID FUNCTION TEST"]['T3- Triiodothyroine']['REFERENCE RANGE'],
                                            i["THYROID FUNCTION TEST"]['T4 - Thyroxine']['RESULT'],
                                            i["THYROID FUNCTION TEST"]['T4 - Thyroxine']['UNIT'],
                                            i["THYROID FUNCTION TEST"]['T4 - Thyroxine']['REFERENCE RANGE'],
                                            i["THYROID FUNCTION TEST"]['TSH- Thyroid Stimulating Hormone']['RESULT'],
                                            i["THYROID FUNCTION TEST"]['TSH- Thyroid Stimulating Hormone']['UNIT'],
                                            i["THYROID FUNCTION TEST"]['TSH- Thyroid Stimulating Hormone']['REFERENCE RANGE'],
                                            i["THYROID FUNCTION TEST"]['TSH- Thyroid Stimulating Hormone']['NORMAL / ABNORMAL'])
                cursor.execute(thyroidfunctiontest, thyroidfunctiontest_values)

                autoimmunetest = ("INSERT INTO autoimmune_test "
                "( emp_no, ana, ana_unit, ana_range, "
                "adna, adna_unit, adna_range, "
                "anticardiolipin, anticardiolipin_unit, anticardiolipin_range, "
                "rheumatoid, rheumatoid_unit, rheumatoid_range) "
                "VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                autoimmunetest_values = (i['Details']['Basic detail']['EMP NO'],
                                    i["AUTOIMMUNE TEST"]['ANA (Antinuclear Antibody)']['RESULT'],
                                    i["AUTOIMMUNE TEST"]['ANA (Antinuclear Antibody)']['UNIT'],
                                    i["AUTOIMMUNE TEST"]['ANA (Antinuclear Antibody)']['REFERENCE RANGE'],
                                    i["AUTOIMMUNE TEST"]['Anti ds DNA']['RESULT'],
                                    i["AUTOIMMUNE TEST"]['Anti ds DNA']['UNIT'],
                                    i["AUTOIMMUNE TEST"]['Anti ds DNA']['REFERENCE RANGE'],
                                    i["AUTOIMMUNE TEST"]['Anticardiolipin Antibodies (IgG & IgM)']['RESULT'],
                                    i["AUTOIMMUNE TEST"]['Anticardiolipin Antibodies (IgG & IgM)']['UNIT'],
                                    i["AUTOIMMUNE TEST"]['Anticardiolipin Antibodies (IgG & IgM)']['REFERENCE RANGE'],
                                    i["AUTOIMMUNE TEST"]['Rheumatoid factor']['RESULT'],
                                    i["AUTOIMMUNE TEST"]['Rheumatoid factor']['UNIT'],
                                    i["AUTOIMMUNE TEST"]['Rheumatoid factor']['REFERENCE RANGE'])
                cursor.execute(autoimmunetest, autoimmunetest_values)

                coagulationtest = ("INSERT INTO coagulation_test "
                "(emp_no, pt, pt_unit, pt_range, ptinr, ptinr_unit, ptinr_range, "
                "bt, bt_unit, bt_range, ct, ct_unit, ct_range) "
                "VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                coagulationtest_values = (i['Details']['Basic detail']['EMP NO'],
                                    i["COAGULATION TEST"]['Prothrombin Time (PT)']['RESULT'],
                                    i["COAGULATION TEST"]['Prothrombin Time (PT)']['UNIT'],
                                    i["COAGULATION TEST"]['Prothrombin Time (PT)']['REFERENCE RANGE'],
                                    i["COAGULATION TEST"]['PT INR']['RESULT'],
                                    i["COAGULATION TEST"]['PT INR']['UNIT'],
                                    i["COAGULATION TEST"]['PT INR']['REFERENCE RANGE'],
                                    i["COAGULATION TEST"]['Bleeding Time (BT)']['RESULT'],
                                    i["COAGULATION TEST"]['Bleeding Time (BT)']['UNIT'],
                                    i["COAGULATION TEST"]['Bleeding Time (BT)']['REFERENCE RANGE'],
                                    i["COAGULATION TEST"]['Clotting Time (CT)']['RESULT'],
                                    i["COAGULATION TEST"]['Clotting Time (CT)']['UNIT'],
                                    i["COAGULATION TEST"]['Clotting Time (CT)']['REFERENCE RANGE'])
                cursor.execute(coagulationtest, coagulationtest_values)

                enzymesandcardiacprofile = ("INSERT INTO enzymes_cardio "
                "(emp_no, acid_phosphatase, acid_phosphatase_unit, acid_phosphatase_range, "
                "adenosine, adenosine_unit, adenosine_range, "
                "amylase, amylase_unit, amylase_range, "
                "lipase, lipase_unit, lipase_range, "
                "troponin_t, troponin_t_unit, troponin_t_range, "
                "troponin_i, troponin_i_unit, troponin_i_range, "
                "cpk_total, cpk_total_unit, cpk_total_range, "
                "cpk_mb, cpk_mb_unit, cpk_mb_range, "
                "ecg, ecg_comments, echo, echo_comments, tmt, tmt_comments) "
                "VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                enzymesandcardiacprofile_values = (i['Details']['Basic detail']['EMP NO'],
                                                i["ENZYMES & CARDIAC Profile"]['Acid Phosphatase']['RESULT'],
                                                i["ENZYMES & CARDIAC Profile"]['Acid Phosphatase']['UNIT'],
                                                i["ENZYMES & CARDIAC Profile"]['Acid Phosphatase']['REFERENCE RANGE'],
                                                i["ENZYMES & CARDIAC Profile"]['Adenosine Deaminase']['RESULT'],
                                                i["ENZYMES & CARDIAC Profile"]['Adenosine Deaminase']['UNIT'],
                                                i["ENZYMES & CARDIAC Profile"]['Adenosine Deaminase']['REFERENCE RANGE'],
                                                i["ENZYMES & CARDIAC Profile"]['Amylase']['RESULT'],
                                                i["ENZYMES & CARDIAC Profile"]['Amylase']['UNIT'],
                                                i["ENZYMES & CARDIAC Profile"]['Amylase']['REFERENCE RANGE'],
                                                i["ENZYMES & CARDIAC Profile"]['Lipase']['RESULT'],
                                                i["ENZYMES & CARDIAC Profile"]['Lipase']['UNIT'],
                                                i["ENZYMES & CARDIAC Profile"]['Lipase']['REFERENCE RANGE'],
                                                i["ENZYMES & CARDIAC Profile"]['Troponin- T']['RESULT'],
                                                i["ENZYMES & CARDIAC Profile"]['Troponin- T']['UNIT'],
                                                i["ENZYMES & CARDIAC Profile"]['Troponin- T']['REFERENCE RANGE'],
                                                i["ENZYMES & CARDIAC Profile"]['Troponin- I']['RESULT'],
                                                i["ENZYMES & CARDIAC Profile"]['Troponin- I']['UNIT'],
                                                i["ENZYMES & CARDIAC Profile"]['Troponin- I']['REFERENCE RANGE'],
                                                i["ENZYMES & CARDIAC Profile"]['CPK - TOTAL']['RESULT'],
                                                i["ENZYMES & CARDIAC Profile"]['CPK - TOTAL']['UNIT'],
                                                i["ENZYMES & CARDIAC Profile"]['CPK - TOTAL']['REFERENCE RANGE'],
                                                i["ENZYMES & CARDIAC Profile"]['CPK - MB']['RESULT'],
                                                i["ENZYMES & CARDIAC Profile"]['CPK - MB']['UNIT'],
                                                i["ENZYMES & CARDIAC Profile"]['CPK - MB']['REFERENCE RANGE'],
                                                i["ENZYMES & CARDIAC Profile"]['ECG ']['NORMAL / ABNORMAL'],
                                                i["ENZYMES & CARDIAC Profile"]['ECG ']['COMMENTS(If Abnormal)'],
                                                i["ENZYMES & CARDIAC Profile"]['ECHO']['NORMAL / ABNORMAL'],
                                                i["ENZYMES & CARDIAC Profile"]['ECHO']['COMMENTS(If Abnormal)'],
                                                i["ENZYMES & CARDIAC Profile"]['TMT']['NORMAL / ABNORMAL'],
                                                i["ENZYMES & CARDIAC Profile"]['TMT']['COMMENTS(If Abnormal)'])
                cursor.execute(enzymesandcardiacprofile, enzymesandcardiacprofile_values)

                urineroutine = ("INSERT INTO urine_routine "
                "(emp_no, colour, colour_unit, colour_range, "
                "apperance, apperance_unit, apperance_range, "
                "reaction, reaction_unit, reaction_range, "
                "specific_gravity, specific_gravity_unit, specific_gravity_range, "
                "protein_albumin, protein_albumin_unit, protein_albumin_range, "
                "glucose, glucose_unit, glucose_range, "
                "ketone, ketone_unit, ketone_range, "
                "urobilinogen, urobilinogen_unit, urobilinogen_range, "
                "bile_salts, bile_salts_unit, bile_salts_range, "
                "bile_pigments, bile_pigments_unit, bile_pigments_range, "
                "wbc_pluscells, wbc_pluscells_unit, wbc_pluscells_range, "
                "rbc, rbc_unit, rbc_range, "
                "epithelial_cell, epithelial_cell_unit, epithelial_cell_range, "
                "casts, casts_unit, casts_range, "
                "crystals, crystals_unit, crystals_range, "
                "bacteria, bacteria_unit, bacteria_range) "
                "VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                urineroutine_values = (i['Details']['Basic detail']['EMP NO'],
                                    i["URINE ROUTINE"]['Colour']['RESULT'],
                                    i["URINE ROUTINE"]['Colour']['UNIT'],
                                    i["URINE ROUTINE"]['Colour']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Appearance']['RESULT'],
                                    i["URINE ROUTINE"]['Appearance']['UNIT'],
                                    i["URINE ROUTINE"]['Appearance']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Reaction (pH)']['RESULT'],
                                    i["URINE ROUTINE"]['Reaction (pH)']['UNIT'],
                                    i["URINE ROUTINE"]['Reaction (pH)']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Specific gravity']['RESULT'],
                                    i["URINE ROUTINE"]['Specific gravity']['UNIT'],
                                    i["URINE ROUTINE"]['Specific gravity']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Protein/Albumin']['RESULT'],
                                    i["URINE ROUTINE"]['Protein/Albumin']['UNIT'],
                                    i["URINE ROUTINE"]['Protein/Albumin']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Glucose (Urine)']['RESULT'],
                                    i["URINE ROUTINE"]['Glucose (Urine)']['UNIT'],
                                    i["URINE ROUTINE"]['Glucose (Urine)']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Ketone Bodies']['RESULT'],
                                    i["URINE ROUTINE"]['Ketone Bodies']['UNIT'],
                                    i["URINE ROUTINE"]['Ketone Bodies']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Urobilinogen']['RESULT'],
                                    i["URINE ROUTINE"]['Urobilinogen']['UNIT'],
                                    i["URINE ROUTINE"]['Urobilinogen']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Bile Salts']['RESULT'],
                                    i["URINE ROUTINE"]['Bile Salts']['UNIT'],
                                    i["URINE ROUTINE"]['Bile Salts']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Bile Pigments']['RESULT'],
                                    i["URINE ROUTINE"]['Bile Pigments']['UNIT'],
                                    i["URINE ROUTINE"]['Bile Pigments']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['WBC / Pus cells']['RESULT'],
                                    i["URINE ROUTINE"]['WBC / Pus cells']['UNIT'],
                                    i["URINE ROUTINE"]['WBC / Pus cells']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Red Blood Cells']['RESULT'],
                                    i["URINE ROUTINE"]['Red Blood Cells']['UNIT'],
                                    i["URINE ROUTINE"]['Red Blood Cells']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Epithelial celss']['RESULT'],
                                    i["URINE ROUTINE"]['Epithelial celss']['UNIT'],
                                    i["URINE ROUTINE"]['Epithelial celss']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Casts']['RESULT'],
                                    i["URINE ROUTINE"]['Casts']['UNIT'],
                                    i["URINE ROUTINE"]['Casts']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Crystals']['RESULT'],
                                    i["URINE ROUTINE"]['Crystals']['UNIT'],
                                    i["URINE ROUTINE"]['Crystals']['REFERENCE RANGE'],
                                    i["URINE ROUTINE"]['Bacteria']['RESULT'],
                                    i["URINE ROUTINE"]['Bacteria']['UNIT'],
                                    i["URINE ROUTINE"]['Bacteria']['REFERENCE RANGE'])
                cursor.execute(urineroutine, urineroutine_values)

                serology = ("INSERT INTO serology_result "
                "(emp_no, hiv_screening, hiv_screening_range, hiv_screening_comment, "
                "hbsag, hbsag_range, hbsag_comment, "
                "hcv, hcv_range, hcv_comment, "
                "widal, widal_range, widal_comment, "
                "vdrl, vdrl_range, vdrl_comment, "
                "denguens, denguens_range, denguens_comment, "
                "dengueigg, dengueigg_range, dengueigg_comment, "
                "dengueigm, dengueigm_range, dengueigm_comment) "
                "VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                serology_values = (i['Details']['Basic detail']['EMP NO'],
                                i["SEROLOGY"]['Screening For HIV I & II']['RESULT'],
                                i["SEROLOGY"]['Screening For HIV I & II']['REFERENCE RANGE'],
                                i["SEROLOGY"]['Screening For HIV I & II']['Comment'],
                                i["SEROLOGY"]['HBsAg']['RESULT'],
                                i["SEROLOGY"]['HBsAg']['REFERENCE RANGE'],
                                i["SEROLOGY"]['HBsAg']['Comment'],
                                i["SEROLOGY"]['HCV']['RESULT'],
                                i["SEROLOGY"]['HCV']['REFERENCE RANGE'],
                                i["SEROLOGY"]['HCV']['Comment'],
                                i["SEROLOGY"]['WIDAL']['RESULT'],
                                i["SEROLOGY"]['WIDAL']['REFERENCE RANGE'],
                                i["SEROLOGY"]['WIDAL']['Comment'],
                                i["SEROLOGY"]['VDRL']['RESULT'],
                                i["SEROLOGY"]['VDRL']['REFERENCE RANGE'],
                                i["SEROLOGY"]['VDRL']['Comment'],
                                i["SEROLOGY"]['Dengue NS1Ag']['RESULT'],
                                i["SEROLOGY"]['Dengue NS1Ag']['REFERENCE RANGE'],
                                i["SEROLOGY"]['Dengue NS1Ag']['Comment'],
                                i["SEROLOGY"]['Dengue  IgG']['RESULT'],
                                i["SEROLOGY"]['Dengue  IgG']['REFERENCE RANGE'],
                                i["SEROLOGY"]['Dengue  IgG']['Comment'],
                                i["SEROLOGY"]['Dengue IgM']['RESULT'],
                                i["SEROLOGY"]['Dengue IgM']['REFERENCE RANGE'],
                                i["SEROLOGY"]['Dengue IgM']['Comment'])
                cursor.execute(serology, serology_values)

                motion = ("INSERT INTO motion "
                "(emp_no, colour, colour_unit, colour_range, "
                "appearance, appearance_unit, appearance_range, "
                "occult_blood, occult_blood_unit, occult_blood_range, "
                "ova, ova_unit, ova_range, "
                "cyst, cyst_unit, cyst_range, "
                "mucus, mucus_unit, mucus_range, "
                "pus_cells, pus_cells_unit, pus_cells_range, "
                "rbcs, rbcs_unit, rbcs_range, "
                "others_t, others_t_unit, others_t_range) "
                "VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                motion_values = (i['Details']['Basic detail']['EMP NO'],
                            i["MOTION"]['Colour']['RESULT'],
                            i["MOTION"]['Colour']['UNIT'],
                            i["MOTION"]['Colour']['REFERENCE RANGE'],
                            i["MOTION"]['Appearance']['RESULT'],
                            i["MOTION"]['Appearance']['UNIT'],
                            i["MOTION"]['Appearance']['REFERENCE RANGE'],
                            i["MOTION"]['Occult Blood']['RESULT'],
                            i["MOTION"]['Occult Blood']['UNIT'],
                            i["MOTION"]['Occult Blood']['REFERENCE RANGE'],
                            i["MOTION"]['Ova']['RESULT'],
                            i["MOTION"]['Ova']['UNIT'],
                            i["MOTION"]['Ova']['REFERENCE RANGE'],
                            i["MOTION"]['Cyst']['RESULT'],
                            i["MOTION"]['Cyst']['UNIT'],
                            i["MOTION"]['Cyst']['REFERENCE RANGE'],
                            i["MOTION"]['Mucus']['RESULT'],
                            i["MOTION"]['Mucus']['UNIT'],
                            i["MOTION"]['Mucus']['REFERENCE RANGE'],
                            i["MOTION"]['Pus Cells']['RESULT'],
                            i["MOTION"]['Pus Cells']['UNIT'],
                            i["MOTION"]['Pus Cells']['REFERENCE RANGE'],
                            i["MOTION"]['RBCs']['RESULT'],
                            i["MOTION"]['RBCs']['UNIT'],
                            i["MOTION"]['RBCs']['REFERENCE RANGE'],
                            i["MOTION"]['Others']['RESULT'],
                            i["MOTION"]['Others']['UNIT'],
                            i["MOTION"]['Others']['REFERENCE RANGE'])
                cursor.execute(motion, motion_values)

                routinetest = ("INSERT INTO routine_culture "
                "(emp_no, urine, urine_unit, urine_range, "
                "motion, motion_unit, motion_range, "
                "sputum, sputum_unit, sputum_range, "
                "blood, blood_unit, blood_range) "
                "VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                routinetest_values = (i['Details']['Basic detail']['EMP NO'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Urine']['RESULT'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Urine']['UNIT'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Urine']['REFERENCE RANGE'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Motion']['RESULT'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Motion']['UNIT'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Motion']['REFERENCE RANGE'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Sputum']['RESULT'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Sputum']['UNIT'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Sputum']['REFERENCE RANGE'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Blood']['RESULT'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Blood']['UNIT'],
                                    i["ROUTINE CULTURE & SENSITIVITY TEST"]['Blood']['REFERENCE RANGE'])
                cursor.execute(routinetest, routinetest_values)

                menspack = ("INSERT INTO mens_pack "
                "( emp_no, psa, psa_unit, psa_range) "
                "VALUES "
                "(%s, %s, %s, %s)")

                menspack_values = (i['Details']['Basic detail']['EMP NO'],
                                    i["Men's Pack"]["PSA (Prostate specific Antigen)"]['RESULT'],
                                    i["Men's Pack"]["PSA (Prostate specific Antigen)"]['UNIT'],
                                    i["Men's Pack"]["PSA (Prostate specific Antigen)"]['REFERENCE RANGE'])
                cursor.execute(menspack, menspack_values)

                womenspack = ("INSERT INTO womens_pack "
                            "( emp_no, mammogram_nm_ab, mammogram_comment,  pap_nm_ab, pap_comment) "
                            "VALUES "
                            "( %s, %s, %s, %s, %s)")

                womenspack_values = (i['Details']['Basic detail']['EMP NO'],
                                    i["Women's Pack"]['Mammogram']['NORMAL / ABNORMAL'],
                                    i["Women's Pack"]['Mammogram']['COMMENTS'],
                                    i["Women's Pack"]['PAP Smear']['NORMAL / ABNORMAL'],
                                    i["Women's Pack"]['PAP Smear']['COMMENTS'])
                cursor.execute(womenspack, womenspack_values)

                occupationalprofile = ("INSERT INTO occupational_profile "
                "( emp_no,  audiometry_nm_ab, audiometry_comment,  pft_nm_ab, pft_comment) "
                "VALUES "
                "( %s, %s, %s, %s, %s)")  


                occupationalprofile_values = (i['Details']['Basic detail']['EMP NO'],
                                            i["Occupational Profile"]['Audiometry ']['NORMAL / ABNORMAL'],
                                            i["Occupational Profile"]['Audiometry ']['COMMENTS'],
                                            i["Occupational Profile"]['PFT']['NORMAL / ABNORMAL'],
                                            i["Occupational Profile"]['PFT']['COMMENTS'])  
                cursor.execute(occupationalprofile, occupationalprofile_values)

                otherstest = ("INSERT INTO other_tests "
                "( emp_no, pathology, pathology_comments) "
                "VALUES "
                "( %s, %s, %s)")

                otherstest_values = (i['Details']['Basic detail']['EMP NO'],
                                    i["Others TEST"]['Pathology ']['NORMAL / ABNORMAL'],
                                    i["Others TEST"]['Pathology ']['COMMENTS'])
                cursor.execute(otherstest, otherstest_values)

                ophthalmicreport = ("INSERT INTO ophthalmic_report "
                "( emp_no, vision, vision_comments, colourvision, colourvision_comment) "
                "VALUES "
                "( %s, %s, %s, %s, %s)")

                ophthalmicreport_values = (i['Details']['Basic detail']['EMP NO'],
                                        i["OPHTHALMIC REPORT"]['Vision']['NORMAL / ABNORMAL'],
                                        i["OPHTHALMIC REPORT"]['Vision']['COMMENTS'],
                                        i["OPHTHALMIC REPORT"]['Color Vision']['NORMAL / ABNORMAL'],
                                        i["OPHTHALMIC REPORT"]['Color Vision']['COMMENTS'])
                cursor.execute(ophthalmicreport, ophthalmicreport_values)

                xray = ("INSERT INTO x_ray "
                "( emp_no, chest_nm_ab, chest_comment, "
                "spine_nm_ab, spine_comment, "
                "abdomen_nm_ab, abdomen_comment, "
                "kub_nm_ab, kub_comment, "
                "pelvis_nm_ab, pelvis_comment) "
                "VALUES "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                xray_values = (i['Details']['Basic detail']['EMP NO'],
                            i["X-RAY"]['Chest']['NORMAL / ABNORMAL'],
                            i["X-RAY"]['Chest']['COMMENTS (If Abnormal)'],
                            i["X-RAY"]['Spine']['NORMAL / ABNORMAL'],
                            i["X-RAY"]['Spine']['COMMENTS (If Abnormal)'],
                            i["X-RAY"]['Abdomen']['NORMAL / ABNORMAL'],
                            i["X-RAY"]['Abdomen']['COMMENTS (If Abnormal)'],
                            i["X-RAY"]['KUB']['NORMAL / ABNORMAL'],
                            i["X-RAY"]['KUB']['COMMENTS (If Abnormal)'],
                            i["X-RAY"]['Pelvis']['NORMAL / ABNORMAL'],
                            i["X-RAY"]['Pelvis']['COMMENTS (If Abnormal)'])

                cursor.execute(xray, xray_values)

                usg = ("INSERT INTO usg "
                "( emp_no, abdomen, abdomen_comments, "
                "pelvis, pelvis_comments, "
                "neck, neck_comments, "
                "kub, kub_comments) "
                "VALUES "
                "( %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                
                usg_values = (i['Details']['Basic detail']['EMP NO'],
                            i["USG "]['ABDOMEN']['NORMAL / ABNORMAL'],
                            i["USG "]['ABDOMEN']['COMMENTS (If Abnormal)'],
                            i["USG "]['Pelvis']['NORMAL / ABNORMAL'],
                            i["USG "]['Pelvis']['COMMENTS (If Abnormal)'],
                            i["USG "]['Neck']['NORMAL / ABNORMAL'],
                            i["USG "]['Neck']['COMMENTS (If Abnormal)'],
                            i["USG "]['KUB']['NORMAL / ABNORMAL'],
                            i["USG "]['KUB']['COMMENTS (If Abnormal)'])

                cursor.execute(usg, usg_values)
                
                ct = ("INSERT INTO ct_report "
                "( emp_no, brain, brain_comment, "
                "abdomen, abdomen_comment, "
                "pelvis, pelvis_comment, "
                "ct_lungs, ct_lungs_comment, "
                "spine, spine_comment) "
                "VALUES "
                "( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                ct_values = (i['Details']['Basic detail']['EMP NO'],
                            i["CT"]['Brain']['NORMAL / ABNORMAL'],
                            i["CT"]['Brain']['COMMENTS (If Abnormal)'],
                            i["CT"]['Abdomen']['NORMAL / ABNORMAL'],
                            i["CT"]['Abdomen']['COMMENTS (If Abnormal)'],
                            i["CT"]['Pelvis']['NORMAL / ABNORMAL'],
                            i["CT"]['Pelvis']['COMMENTS (If Abnormal)'],
                            i["CT"]['CT Lungs']['NORMAL / ABNORMAL'],
                            i["CT"]['CT Lungs']['COMMENTS (If Abnormal)'],
                            i["CT"]['Spine']['NORMAL / ABNORMAL'],
                            i["CT"]['Spine']['COMMENTS (If Abnormal)'])

                cursor.execute(ct, ct_values)

                mri = ("INSERT INTO mri "
                "(emp_no, brain, brain_comments, "
                "abdomen, abdomen_comments, "
                "pelvis, pelvis_comments, "
                "ct_lungs, ct_lungs_comments, "
                "spine, spine_comments) "
                "VALUES "
                "( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                mri_values = (i['Details']['Basic detail']['EMP NO'],
                            i["MRI"]['Brain']['NORMAL / ABNORMAL'],
                            i["MRI"]['Brain']['COMMENTS (If Abnormal)'],
                            i["MRI"]['Abdomen']['NORMAL / ABNORMAL'],
                            i["MRI"]['Abdomen']['COMMENTS (If Abnormal)'],
                            i["MRI"]['Pelvis']['NORMAL / ABNORMAL'],
                            i["MRI"]['Pelvis']['COMMENTS (If Abnormal)'],
                            i["MRI"]['CT Lungs']['NORMAL / ABNORMAL'],
                            i["MRI"]['CT Lungs']['COMMENTS (If Abnormal)'],
                            i["MRI"]['Spine']['NORMAL / ABNORMAL'],
                            i["MRI"]['Spine']['COMMENTS (If Abnormal)'])

                cursor.execute(mri, mri_values)
                connection.commit()

            st.write("Data Inserted Successfully")

    def get_data(val, name):
            with st.container(border=1):
                st.write(f"<p style='text-align:center;font-weight:bold;font-size:50px;margin-bottom:-30px'>{val}</p>", unsafe_allow_html=True)
                st.write(f"<p style='text-align:center'>{name}</p>", unsafe_allow_html=True)

    with st.container(border=1):
        r1c1,r1c2,r1c3,r1c4 = st.columns(4)
        with r1c1:
            get_data(st.session_state.total_census, "Total Census")
        with r1c2:
            get_data(st.session_state.total_healthy, "Healthy")
        with r1c3:
            get_data(st.session_state.total_unhealthy, "Unhealthy")
        with r1c4:
            get_data(st.session_state.appointments, "Appointments")