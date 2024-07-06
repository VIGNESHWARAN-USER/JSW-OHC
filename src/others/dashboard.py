import streamlit as st
import os
import pandas as pd
import json
from datetime import datetime
from dateutil.parser import parse


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
        st.write(dataitem[0])
        if st.button("Submit"):
            st.write("Data Submitted")
            for i in dataitem:
                # st.write(str(int(i['Details']['Basic detail']['EMP NO'])))
                # insert the data into the database
                date_str = str(i['Details']['Basic detail'].get('Date'))
                if not date_str or date_str.lower() == 'null':
                    date_ = None  # will insert NULL into the database
                else:
                    date_ = parse(date_str).strftime('%Y-%m-%d')

                try:   
                    vitals = ("INSERT INTO vitals(emp_no, entry_date, year, batch, hospital, Systolic, Diastolic, PulseRate, SpO2, Temperature, RespiratoryRate, Height, Weight, BMI)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    
                    vital_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                    date_,
                                    i['Details']['Basic detail']['Year'],
                                    i['Details']['Basic detail']['Batch'],
                                    i['Details']['Basic detail']['Hospital'],
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

                    hematology = ("INSERT INTO hematology_result( emp_no, entry_date, year, batch, hospital, heamoglobin, rbc_count, wbc_count, haemotocrit, mcv, mch, mchc, platelet, rdw, neutrophil, lymphocyte, eosinophil, monocyte, basophils, esr, pbs_rbc, pbc_parasites, pbc_others) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    hematology_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                        date_,
                                        i['Details']['Basic detail']['Year'],
                                        i['Details']['Basic detail']['Batch'],
                                        i['Details']['Basic detail']['Hospital'],
                                        i["HAEMATALOGY"]['Haemoglobin']['RESULT'],
                                        i["HAEMATALOGY"]['Red Blood Cell (RBC) Count']['RESULT'],
                                        i["HAEMATALOGY"]['WBC Count (TC)']['RESULT'],
                                        i["HAEMATALOGY"]['Haemotocrit (PCV)']['RESULT'],
                                        i["HAEMATALOGY"]['MCV']['RESULT'],
                                        i["HAEMATALOGY"]['MCH']['RESULT'],
                                        i["HAEMATALOGY"]['MCHC']['RESULT'],
                                        i["HAEMATALOGY"]['Platelet Count']['RESULT'],
                                        i["HAEMATALOGY"]['RDW (CV)']['RESULT'],
                                        i["HAEMATALOGY"]['Neutrophil']['RESULT'],
                                        i["HAEMATALOGY"]['Lymphocyte']['RESULT'],
                                        i["HAEMATALOGY"]['Eosinophil']['RESULT'],
                                        i["HAEMATALOGY"]['Monocyte']['RESULT'],
                                        i["HAEMATALOGY"]['Basophils']['RESULT'],
                                        i["HAEMATALOGY"]['Erythrocyte Sedimentation Rate (ESR)']['RESULT'],
                                        i["HAEMATALOGY"]['Peripheral Blood Smear - RBC Morphology']['COMMENTS'],
                                        i["HAEMATALOGY"]['Peripheral Blood Smear - Parasites']['COMMENTS'],
                                        i["HAEMATALOGY"]['Peripheral Blood Smear - Others']['COMMENTS'])
                    cursor.execute(hematology, hematology_values) 


                    routinesugartest = ("INSERT INTO routine_sugartest"
                                        "(emp_no, entry_date, year, batch, hospital, glucosef, glucosepp, rbs, eag, hba1c) "
                                        "VALUES "
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                    routinesugartest_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                            date_,
                                            i['Details']['Basic detail']['Year'],
                                            i['Details']['Basic detail']['Batch'],
                                            i['Details']['Basic detail']['Hospital'],
                                            i['ROUTINE SUGAR TESTS']['Glucose (F)']['RESULT'],
                                            i['ROUTINE SUGAR TESTS']['Glucose (PP)']['RESULT'],
                                            i['ROUTINE SUGAR TESTS']['Random Blood sugar']['RESULT'],
                                            i['ROUTINE SUGAR TESTS']['Estimated Average Glucose']['RESULT'],
                                            i['ROUTINE SUGAR TESTS']['HbA1c']['RESULT'])
                    cursor.execute(routinesugartest, routinesugartest_values)

                            
                    renalfunctiontest = ("INSERT INTO rft_result "
                        "(emp_no, entry_date, year, batch, hospital, urea, bun, sr_creatinine, uric_acid, sodium, potassium, calcium, phosphorus, chloride, bicarbonate) "
                        "VALUES "
                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    renalfunctiontest_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                                date_,
                                                i['Details']['Basic detail']['Year'],
                                                i['Details']['Basic detail']['Batch'],
                                                i['Details']['Basic detail']['Hospital'],
                                                i["RENAL FUNCTION TEST & ELECTROLYTES"]['Urea']['RESULT'],
                                                i["RENAL FUNCTION TEST & ELECTROLYTES"]['Blood urea nitrogen (BUN)']['RESULT'],
                                                i["RENAL FUNCTION TEST & ELECTROLYTES"]['Sr.Creatinine']['RESULT'],
                                                i["RENAL FUNCTION TEST & ELECTROLYTES"]['Uric acid']['RESULT'],
                                                i["RENAL FUNCTION TEST & ELECTROLYTES"]['Sodium']['RESULT'],
                                                i["RENAL FUNCTION TEST & ELECTROLYTES"]['Potassium']['RESULT'],
                                                i["RENAL FUNCTION TEST & ELECTROLYTES"]['Calcium']['RESULT'],
                                                i["RENAL FUNCTION TEST & ELECTROLYTES"]['Phosphorus']['RESULT'],
                                                i["RENAL FUNCTION TEST & ELECTROLYTES"]['Chloride']['RESULT'],
                                                i["RENAL FUNCTION TEST & ELECTROLYTES"]['Bicarbonate']['RESULT'])
                    cursor.execute(renalfunctiontest, renalfunctiontest_values)

                    lipidprofile = ("INSERT INTO lipid_profile "
                                    "(emp_no, entry_date, year, batch, hospital, tcholesterol, triglycerides, hdl_cholesterol, vldl_cholesterol, ldl_cholesterol, chol_hdlratio, ldlhdlratio) "
                                    "VALUES "
                                    "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    lipidprofile_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                        date_,
                                        i['Details']['Basic detail']['Year'],
                                        i['Details']['Basic detail']['Batch'],
                                        i['Details']['Basic detail']['Hospital'],
                                        i["LIPID PROFILE"]['Total Cholesterol']['RESULT'],
                                        i["LIPID PROFILE"]['Triglycerides']['RESULT'],
                                        i["LIPID PROFILE"]['HDL - Cholesterol']['RESULT'],
                                        i["LIPID PROFILE"]['VLDL -Choleserol']['RESULT'],
                                        i["LIPID PROFILE"]['LDL- Cholesterol']['RESULT'],
                                        i["LIPID PROFILE"]['CHOL:HDL ratio']['RESULT'],
                                        i["LIPID PROFILE"]['LDL.CHOL/HDL.CHOL Ratio']['RESULT'])
                    cursor.execute(lipidprofile, lipidprofile_values)

                    liverfunctiontest = ("INSERT INTO liver_function "
                                        "(emp_no, entry_date, year, batch, hospital, bilirubin_total, bilirubin_direct, bilirubin_indirect, sgot_alt, sgpt_alt, alkaline_phosphatase, total_protein, albumin, globulin, alb_globratio, gammagt) "
                                        "VALUES "
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    liverfunctiontest_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                                date_,
                                                i['Details']['Basic detail']['Year'],
                                                i['Details']['Basic detail']['Batch'],
                                                i['Details']['Basic detail']['Hospital'],
                                                i["LIVER FUNCTION TEST"]['Bilirubin -Total']['RESULT'],
                                                i["LIVER FUNCTION TEST"]['Bilirubin -Direct']['RESULT'],
                                                i["LIVER FUNCTION TEST"]['Bilirubin -indirect']['RESULT'],
                                                i["LIVER FUNCTION TEST"]['SGOT /AST']['RESULT'],
                                                i["LIVER FUNCTION TEST"]['SGPT /ALT']['RESULT'],
                                                i["LIVER FUNCTION TEST"]['Alkaline phosphatase']['RESULT'],
                                                i["LIVER FUNCTION TEST"]['Total Protein']['RESULT'],
                                                i["LIVER FUNCTION TEST"]['Albumin (Serum )']['RESULT'],
                                                i["LIVER FUNCTION TEST"][' Globulin(Serum)']['RESULT'],
                                                i["LIVER FUNCTION TEST"]['Alb/Glob Ratio']['RESULT'],
                                                i["LIVER FUNCTION TEST"]['Gamma Glutamyl transferase']['RESULT'])
                    cursor.execute(liverfunctiontest, liverfunctiontest_values)

                    thyroidfunctiontest = ("INSERT INTO thyroid_function_test "
                                        "(emp_no, entry_date, year, batch, hospital, t3, t4, tsh) "
                                        "VALUES "
                                        "(%s, %s, %s, %s, %s, %s, %s, %s)")
                    
                    thyroidfunctiontest_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                                date_,
                                                i['Details']['Basic detail']['Year'],
                                                i['Details']['Basic detail']['Batch'],
                                                i['Details']['Basic detail']['Hospital'],
                                                i["THYROID FUNCTION TEST"]['T3- Triiodothyroine']['RESULT'],
                                                i["THYROID FUNCTION TEST"]['T4 - Thyroxine']['RESULT'],
                                                i["THYROID FUNCTION TEST"]['TSH- Thyroid Stimulating Hormone']['RESULT'])
                    cursor.execute(thyroidfunctiontest, thyroidfunctiontest_values)

                    autoimmunetest = ("INSERT INTO autoimmune_test "
                            "(emp_no, entry_date, year, batch, hospital, ana, adna, anticardiolipin, rheumatoid) "
                            "VALUES "
                            "(%s, %s, %s, %s, %s, %s, %s, %s, %s)")

                    autoimmunetest_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                        date_,
                                        i['Details']['Basic detail']['Year'],
                                        i['Details']['Basic detail']['Batch'],
                                        i['Details']['Basic detail']['Hospital'],
                                        i["AUTOIMMUNE TEST"]['ANA (Antinuclear Antibody)']['RESULT'],
                                        i["AUTOIMMUNE TEST"]['Anti ds DNA']['RESULT'],
                                        i["AUTOIMMUNE TEST"]['Anticardiolipin Antibodies (IgG & IgM)']['RESULT'],
                                        i["AUTOIMMUNE TEST"]['Rheumatoid factor']['RESULT'])
                    cursor.execute(autoimmunetest, autoimmunetest_values)

                    coagulationtest = ("INSERT INTO coagulation_test "
                                    "(emp_no, entry_date, year, batch, hospital, pt, ptinr, bt, ct) "
                                    "VALUES "
                                    "(%s, %s, %s, %s, %s, %s, %s, %s, %s)")

                    coagulationtest_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                        date_,
                                        i['Details']['Basic detail']['Year'],
                                        i['Details']['Basic detail']['Batch'],
                                        i['Details']['Basic detail']['Hospital'],
                                        i["COAGULATION TEST"]['Prothrombin Time (PT)']['RESULT'],
                                        i["COAGULATION TEST"]['PT INR']['RESULT'],
                                        i["COAGULATION TEST"]['Bleeding Time (BT)']['RESULT'],
                                        i["COAGULATION TEST"]['Clotting Time (CT)']['RESULT'])
                    cursor.execute(coagulationtest, coagulationtest_values)

                    enzymesandcardiacprofile = ("INSERT INTO enzymes_cardio "
                                                "(emp_no, entry_date, year, batch, hospital, acid_phosphatase, adenosine, amylase, lipase, troponin_t, troponin_i, cpk_total, cpk_mb, ecg, ecg_comments, echo, echo_comments, tmt, tmt_comments) "
                                                "VALUES "
                                                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    enzymesandcardiacprofile_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                                    date_,
                                                    i['Details']['Basic detail']['Year'],
                                                    i['Details']['Basic detail']['Batch'],
                                                    i['Details']['Basic detail']['Hospital'],
                                                    i["ENZYMES & CARDIAC Profile"]['Acid Phosphatase']['RESULT'],
                                                    i["ENZYMES & CARDIAC Profile"]['Adenosine Deaminase']['RESULT'],
                                                    i["ENZYMES & CARDIAC Profile"]['Amylase']['RESULT'],
                                                    i["ENZYMES & CARDIAC Profile"]['Lipase']['RESULT'],
                                                    i["ENZYMES & CARDIAC Profile"]['Troponin- T']['RESULT'],
                                                    i["ENZYMES & CARDIAC Profile"]['Troponin- I']['RESULT'],
                                                    i["ENZYMES & CARDIAC Profile"]['CPK - TOTAL']['RESULT'],
                                                    i["ENZYMES & CARDIAC Profile"]['CPK - MB']['RESULT'],
                                                    i["ENZYMES & CARDIAC Profile"]['ECG ']['NORMAL / ABNORMAL'],
                                                    i["ENZYMES & CARDIAC Profile"]['ECG ']['COMMENTS(If Abnormal)'],
                                                    i["ENZYMES & CARDIAC Profile"]['ECHO']['NORMAL / ABNORMAL'],
                                                    i["ENZYMES & CARDIAC Profile"]['ECHO']['COMMENTS(If Abnormal)'],
                                                    i["ENZYMES & CARDIAC Profile"]['TMT']['NORMAL / ABNORMAL'],
                                                    i["ENZYMES & CARDIAC Profile"]['TMT']['COMMENTS(If Abnormal)'])
                    cursor.execute(enzymesandcardiacprofile, enzymesandcardiacprofile_values)

                    urineroutine = ("INSERT INTO urine_routine "
                                    "(emp_no, entry_date, year, batch, hospital, colour, apperance, reaction, specific_gravity, protein_albumin, glucose, ketone, urobilinogen, bile_salts, bile_pigments, wbc_pluscells, rbc, epithelial_cell, casts, crystals, bacteria) "
                                    "VALUES "
                                    "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    urineroutine_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                        date_,
                                        i['Details']['Basic detail']['Year'],
                                        i['Details']['Basic detail']['Batch'],
                                        i['Details']['Basic detail']['Hospital'],
                                        i["URINE ROUTINE"]['Colour']['RESULT'],
                                        i["URINE ROUTINE"]['Appearance']['RESULT'],
                                        i["URINE ROUTINE"]['Reaction (pH)']['RESULT'],
                                        i["URINE ROUTINE"]['Specific gravity']['RESULT'],
                                        i["URINE ROUTINE"]['Protein/Albumin']['RESULT'],
                                        i["URINE ROUTINE"]['Glucose (Urine)']['RESULT'],
                                        i["URINE ROUTINE"]['Ketone Bodies']['RESULT'],
                                        i["URINE ROUTINE"]['Urobilinogen']['RESULT'],
                                        i["URINE ROUTINE"]['Bile Salts']['RESULT'],
                                        i["URINE ROUTINE"]['Bile Pigments']['RESULT'],
                                        i["URINE ROUTINE"]['WBC / Pus cells']['RESULT'],
                                        i["URINE ROUTINE"]['Red Blood Cells']['RESULT'],
                                        i["URINE ROUTINE"]['Epithelial celss']['RESULT'],
                                        i["URINE ROUTINE"]['Casts']['RESULT'],
                                        i["URINE ROUTINE"]['Crystals']['RESULT'],
                                        i["URINE ROUTINE"]['Bacteria']['RESULT'])
                    cursor.execute(urineroutine, urineroutine_values)

                    serology = ("INSERT INTO serology_result "
                    "(emp_no, entry_date, year, batch, hospital, hiv_screening, hiv_screening_range, hiv_screening_comment, "
                    "hbsag, hbsag_range, hbsag_comment, "
                    "hcv, hcv_range, hcv_comment, "
                    "widal, widal_range, widal_comment, "
                    "vdrl, vdrl_range, vdrl_comment, "
                    "denguens, denguens_range, denguens_comment, "
                    "dengueigg, dengueigg_range, dengueigg_comment, "
                    "dengueigm, dengueigm_range, dengueigm_comment) "
                    "VALUES "
                    "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                    serology_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                    date_,
                                    i['Details']['Basic detail']['Year'],
                                    i['Details']['Basic detail']['Batch'],
                                    i['Details']['Basic detail']['Hospital'],
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
                            "(emp_no, entry_date, year, batch, hospital, colour, appearance, occult_blood, ova, cyst, mucus, pus_cells, rbcs, others_t) "
                            "VALUES "
                            "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    motion_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                date_,
                                i['Details']['Basic detail']['Year'],
                                i['Details']['Basic detail']['Batch'],
                                i['Details']['Basic detail']['Hospital'],
                                i["MOTION"]['Colour']['RESULT'],
                                i["MOTION"]['Appearance']['RESULT'],
                                i["MOTION"]['Occult Blood']['RESULT'],
                                i["MOTION"]['Ova']['RESULT'],
                                i["MOTION"]['Cyst']['RESULT'],
                                i["MOTION"]['Mucus']['RESULT'],
                                i["MOTION"]['Pus Cells']['RESULT'],
                                i["MOTION"]['RBCs']['RESULT'],
                                i["MOTION"]['Others']['RESULT'])
                    cursor.execute(motion, motion_values)

                    routinetest = ("INSERT INTO routine_culture "
                                "(emp_no, entry_date, year, batch, hospital, urine, motion, sputum, blood) "
                                "VALUES "
                                "(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    routinetest_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                        date_,
                                        i['Details']['Basic detail']['Year'],
                                        i['Details']['Basic detail']['Batch'],
                                        i['Details']['Basic detail']['Hospital'],
                                        i["ROUTINE CULTURE & SENSITIVITY TEST"]['Urine']['RESULT'],
                                        i["ROUTINE CULTURE & SENSITIVITY TEST"]['Motion']['RESULT'],
                                        i["ROUTINE CULTURE & SENSITIVITY TEST"]['Sputum']['RESULT'],
                                        i["ROUTINE CULTURE & SENSITIVITY TEST"]['Blood']['RESULT'])
                    cursor.execute(routinetest, routinetest_values)

                    menspack = ("INSERT INTO mens_pack "
                    "( emp_no, entry_date, year, batch, hospital, psa) "
                    "VALUES "
                    "(%s, %s, %s, %s, %s, %s)")

                    menspack_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                        date_,
                                        i['Details']['Basic detail']['Year'],
                                        i['Details']['Basic detail']['Batch'],
                                        i['Details']['Basic detail']['Hospital'],
                                        i["Men's Pack"]["PSA (Prostate specific Antigen)"]['RESULT'])
                    cursor.execute(menspack, menspack_values)

                    womenspack = ("INSERT INTO womens_pack "
                                "( emp_no, entry_date, year, batch, hospital, mammogram_nm_ab, mammogram_comment,  pap_nm_ab, pap_comment) "
                                "VALUES "
                                "( %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                    womenspack_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                        date_,
                                        i['Details']['Basic detail']['Year'],
                                        i['Details']['Basic detail']['Batch'],
                                        i['Details']['Basic detail']['Hospital'],
                                        i["Women's Pack"]['Mammogram']['NORMAL / ABNORMAL'],
                                        i["Women's Pack"]['Mammogram']['COMMENTS'],
                                        i["Women's Pack"]['PAP Smear']['NORMAL / ABNORMAL'],
                                        i["Women's Pack"]['PAP Smear']['COMMENTS'])
                    cursor.execute(womenspack, womenspack_values)

                    occupationalprofile = ("INSERT INTO occupational_profile "
                    "( emp_no, entry_date, year, batch, hospital,  audiometry_nm_ab, audiometry_comment,  pft_nm_ab, pft_comment) "
                    "VALUES "
                    "( %s, %s, %s, %s, %s, %s, %s, %s, %s)")  


                    occupationalprofile_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                                date_,
                                                i['Details']['Basic detail']['Year'],
                                                i['Details']['Basic detail']['Batch'],
                                                i['Details']['Basic detail']['Hospital'],
                                                i["Occupational Profile"]['Audiometry ']['NORMAL / ABNORMAL'],
                                                i["Occupational Profile"]['Audiometry ']['COMMENTS'],
                                                i["Occupational Profile"]['PFT']['NORMAL / ABNORMAL'],
                                                i["Occupational Profile"]['PFT']['COMMENTS'])  
                    cursor.execute(occupationalprofile, occupationalprofile_values)

                    otherstest = ("INSERT INTO other_tests "
                    "( emp_no, entry_date, year, batch, hospital, pathology, pathology_comments) "
                    "VALUES "
                    "( %s, %s, %s, %s, %s, %s, %s)")

                    otherstest_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                        date_,
                                        i['Details']['Basic detail']['Year'],
                                        i['Details']['Basic detail']['Batch'],
                                        i['Details']['Basic detail']['Hospital'],
                                        i["Others TEST"]['Pathology ']['NORMAL / ABNORMAL'],
                                        i["Others TEST"]['Pathology ']['COMMENTS'])
                    cursor.execute(otherstest, otherstest_values)

                    ophthalmicreport = ("INSERT INTO ophthalmic_report "
                    "( emp_no, entry_date, year, batch, hospital, vision, vision_comments, colourvision, colourvision_comment) "
                    "VALUES "
                    "( %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                    ophthalmicreport_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                            date_,
                                            i['Details']['Basic detail']['Year'],
                                            i['Details']['Basic detail']['Batch'],
                                            i['Details']['Basic detail']['Hospital'],
                                            i["OPHTHALMIC REPORT"]['Vision']['NORMAL / ABNORMAL'],
                                            i["OPHTHALMIC REPORT"]['Vision']['COMMENTS'],
                                            i["OPHTHALMIC REPORT"]['Color Vision']['NORMAL / ABNORMAL'],
                                            i["OPHTHALMIC REPORT"]['Color Vision']['COMMENTS'])
                    cursor.execute(ophthalmicreport, ophthalmicreport_values)

                    xray = ("INSERT INTO x_ray "
                    "( emp_no, entry_date, year, batch, hospital, chest_nm_ab, chest_comment, "
                    "spine_nm_ab, spine_comment, "
                    "abdomen_nm_ab, abdomen_comment, "
                    "kub_nm_ab, kub_comment, "
                    "pelvis_nm_ab, pelvis_comment) "
                    "VALUES "
                    "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                    xray_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                date_,
                                i['Details']['Basic detail']['Year'],
                                i['Details']['Basic detail']['Batch'],
                                i['Details']['Basic detail']['Hospital'],
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
                    "( emp_no, entry_date, year, batch, hospital, abdomen, abdomen_comments, "
                    "pelvis, pelvis_comments, "
                    "neck, neck_comments, "
                    "kub, kub_comments) "
                    "VALUES "
                    "( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    
                    usg_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                date_,
                                i['Details']['Basic detail']['Year'],
                                i['Details']['Basic detail']['Batch'],
                                i['Details']['Basic detail']['Hospital'],
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
                    "( emp_no, entry_date, year, batch, hospital, brain, brain_comment, "
                    "abdomen, abdomen_comment, "
                    "pelvis, pelvis_comment, "
                    "ct_lungs, ct_lungs_comment, "
                    "spine, spine_comment) "
                    "VALUES "
                    "( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                    ct_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                date_,
                                i['Details']['Basic detail']['Year'],
                                i['Details']['Basic detail']['Batch'],
                                i['Details']['Basic detail']['Hospital'],
                                i["CT"]['Brain']['NORMAL / ABNORMAL'],
                                i["CT"]['Brain']['COMMENTS (If Abnormal)'],
                                i["CT"]['Abdomen']['NORMAL / ABNORMAL'],
                                i["CT"]['Abdomen']['COMMENTS (If Abnormal)'],
                                i["CT"]['Pelvis']['NORMAL / ABNORMAL'],
                                i["CT"]['Pelvis']['COMMENTS (If Abnormal)'],
                                i["CT"]['Lungs']['NORMAL / ABNORMAL'],
                                i["CT"]['Lungs']['COMMENTS (If Abnormal)'],
                                i["CT"]['Spine']['NORMAL / ABNORMAL'],
                                i["CT"]['Spine']['COMMENTS (If Abnormal)'])

                    cursor.execute(ct, ct_values)

                    mri = ("INSERT INTO mri "
                    "(emp_no, entry_date, year, batch, hospital, brain, brain_comments, "
                    "abdomen, abdomen_comments, "
                    "pelvis, pelvis_comments, "
                    "mri_lungs, mri_lungs_comments, "
                    "spine, spine_comments) "
                    "VALUES "
                    "( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

                    mri_values = (str(int(i['Details']['Basic detail']['EMP NO'])),
                                date_,
                                i['Details']['Basic detail']['Year'],
                                i['Details']['Basic detail']['Batch'],
                                i['Details']['Basic detail']['Hospital'],
                                i["MRI"]['Brain']['NORMAL / ABNORMAL'],
                                i["MRI"]['Brain']['COMMENTS (If Abnormal)'],
                                i["MRI"]['Abdomen']['NORMAL / ABNORMAL'],
                                i["MRI"]['Abdomen']['COMMENTS (If Abnormal)'],
                                i["MRI"]['Pelvis']['NORMAL / ABNORMAL'],
                                i["MRI"]['Pelvis']['COMMENTS (If Abnormal)'],
                                i["MRI"]['Lungs']['NORMAL / ABNORMAL'],
                                i["MRI"]['Lungs']['COMMENTS (If Abnormal)'],
                                i["MRI"]['Spine']['NORMAL / ABNORMAL'],
                                i["MRI"]['Spine']['COMMENTS (If Abnormal)'])

                    cursor.execute(mri, mri_values)
                    connection.commit()
                    st.write(str(int(i['Details']['Basic detail']['EMP NO'])),
                            i["Details"]['Basic detail']['Name'])
                except Exception as e:
                    st.write(e)
                    st.write(str(int(i['Details']['Basic detail']['EMP NO'])),
                            i["Details"]['Basic detail']['Name'])
                    

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