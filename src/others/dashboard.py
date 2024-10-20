from requests import session
import streamlit as st
import os
import pandas as pd
import json
from datetime import datetime
from dateutil.parser import parse
from  streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
def Dashboard(connection,cursor,accessLevel):
    if 'optFilter' not in st.session_state:
        st.session_state.optFilter = "Healthy"
    r0c1, r0c2 = st.columns([3,7])
    with r0c1:
        st.write('\n')
        st.write('\n')
        st.subheader("Nurse > Dashboard")
    with r0c2:
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
        st.dataframe(pd.DataFrame(dataitem))
        if st.button("Submit"):
            st.write("Submitting Basic Details")
            for i in dataitem:
                # st.write(str(i['Details']['Basic detail']['EMP NO']))
                # insert the data into the database
                date_str = str(i['Details']['Basic detail'].get('Date'))
                if date_str or date_str.lower() == 'null':
                    date_ = None  # will insert NULL into the database
                else:
                    date_ = parse(date_str).strftime('%Y-%m-%D')

                try:
                    vitals = (
                        "UPDATE vitals "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, "
                        "Systolic = %s, Diastolic = %s, PulseRate = %s, SpO2 = %s, "
                        "Temperature = %s, RespiratoryRate = %s, Height = %s, Weight = %s, BMI = %s "
                        "WHERE emp_no = %s"
                    )
                    
                    vital_values = (
                        date_,
                        i['Details']['Basic detail']['Year'],
                        i['Details']['Basic detail']['Batch'],
                        i['Details']['Basic detail']['Hospital'],
                        i['General Test']['Vitals']['Systolic BP'],
                        i['General Test']['Vitals']['Diastolic BP'],
                        i['General Test']['Vitals']['Pulse Rate'],
                        None if i['General Test']['Vitals']['sp O2'] == 'null' else i['General Test']['Vitals']['sp O2'],
                        None if i['General Test']['Vitals']['Temperature'] == 'null' else i['General Test']['Vitals']['Temperature'],
                        i['General Test']['Vitals']['Respiratory Rate'],
                        i['General Test']['Vitals']['Height'],
                        i['General Test']['Vitals']['weight'],
                        None if i['General Test']['Vitals']['BMI'] == 'null' else i['General Test']['Vitals']['BMI'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )
                    
                    cursor.execute(vitals, vital_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
    
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Hematology Result Details")
            for i in dataitem:
                try:
                    hematology = (
                        "UPDATE hematology_result "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, heamoglobin = %s, rbc_count = %s, "
                        "wbc_count = %s, haemotocrit = %s, mcv = %s, mch = %s, mchc = %s, platelet = %s, rdw = %s, "
                        "neutrophil = %s, lymphocyte = %s, eosinophil = %s, monocyte = %s, basophils = %s, esr = %s, "
                        "pbs_rbc = %s, pbc_parasites = %s, pbc_others = %s "
                        "WHERE emp_no = %s"
                    )
                    
                    hematology_values = (
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
                        i["HAEMATALOGY"]['Peripheral Blood Smear - Others']['COMMENTS'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )
                    
                    cursor.execute(hematology, hematology_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                    
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Routine Sugar Test Details")
            for i in dataitem:
                try:
                    routinesugartest = (
                        "UPDATE routine_sugartest "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, glucosef = %s, glucosepp = %s, "
                        "rbs = %s, eag = %s, hba1c = %s "
                        "WHERE emp_no = %s"
                    )
                    
                    routinesugartest_values = (
                        date_,
                        i['Details']['Basic detail']['Year'],
                        i['Details']['Basic detail']['Batch'],
                        i['Details']['Basic detail']['Hospital'],
                        i['ROUTINE SUGAR TESTS']['Glucose (F)']['RESULT'],
                        i['ROUTINE SUGAR TESTS']['Glucose (PP)']['RESULT'],
                        i['ROUTINE SUGAR TESTS']['Random Blood sugar']['RESULT'],
                        i['ROUTINE SUGAR TESTS']['Estimated Average Glucose']['RESULT'],
                        i['ROUTINE SUGAR TESTS']['HbA1c']['RESULT'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )
                    
                    cursor.execute(routinesugartest, routinesugartest_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                    
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting RFT Result Details")
            for i in dataitem:
                try:
                    renalfunctiontest = (
                        "UPDATE rft_result "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, urea = %s, bun = %s, sr_creatinine = %s, "
                        "uric_acid = %s, sodium = %s, potassium = %s, calcium = %s, phosphorus = %s, chloride = %s, bicarbonate = %s "
                        "WHERE emp_no = %s"
                    )
                    
                    renalfunctiontest_values = (
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
                        i["RENAL FUNCTION TEST & ELECTROLYTES"]['Bicarbonate']['RESULT'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )
                    
                    cursor.execute(renalfunctiontest, renalfunctiontest_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                    
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Lipid Profile Details")
            for i in dataitem:
                try:
                    lipidprofile = (
                        "UPDATE lipid_profile "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, tcholesterol = %s, triglycerides = %s, "
                        "hdl_cholesterol = %s, vldl_cholesterol = %s, ldl_cholesterol = %s, chol_hdlratio = %s, ldlhdlratio = %s "
                        "WHERE emp_no = %s"
                    )
                    
                    lipidprofile_values = (
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
                        i["LIPID PROFILE"]['LDL.CHOL/HDL.CHOL Ratio']['RESULT'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )
                    
                    cursor.execute(lipidprofile, lipidprofile_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                    
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Liver Function Details")
            for i in dataitem:
                try:
                    liverfunctiontest = (
                        "UPDATE liver_function "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, bilirubin_total = %s, bilirubin_direct = %s, "
                        "bilirubin_indirect = %s, sgot_alt = %s, sgpt_alt = %s, alkaline_phosphatase = %s, total_protein = %s, "
                        "albumin = %s, globulin = %s, alb_globratio = %s, gammagt = %s "
                        "WHERE emp_no = %s"
                    )
                    
                    liverfunctiontest_values = (
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
                        i["LIVER FUNCTION TEST"]['Gamma Glutamyl transferase']['RESULT'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )
                    
                    cursor.execute(liverfunctiontest, liverfunctiontest_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])

                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Thyroid Function Details")
            for i in dataitem:
                try:
                    thyroidfunctiontest = (
                        "UPDATE thyroid_function_test "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, t3 = %s, t4 = %s, tsh = %s "
                        "WHERE emp_no = %s"
                    )
                    
                    thyroidfunctiontest_values = (
                        date_,
                        i['Details']['Basic detail']['Year'],
                        i['Details']['Basic detail']['Batch'],
                        i['Details']['Basic detail']['Hospital'],
                        i["THYROID FUNCTION TEST"]['T3- Triiodothyroine']['RESULT'],
                        i["THYROID FUNCTION TEST"]['T4 - Thyroxine']['RESULT'],
                        i["THYROID FUNCTION TEST"]['TSH- Thyroid Stimulating Hormone']['RESULT'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )
                    
                    cursor.execute(thyroidfunctiontest, thyroidfunctiontest_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])

                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Autiimmune Test Details")
            for i in dataitem:
                try:
                    autoimmunetest = (
                        "UPDATE autoimmune_test "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, ana = %s, adna = %s, "
                        "anticardiolipin = %s, rheumatoid = %s "
                        "WHERE emp_no = %s"
                    )

                    autoimmunetest_values = (
                        date_,
                        i['Details']['Basic detail']['Year'],
                        i['Details']['Basic detail']['Batch'],
                        i['Details']['Basic detail']['Hospital'],
                        i["AUTOIMMUNE TEST"]['ANA (Antinuclear Antibody)']['RESULT'],
                        i["AUTOIMMUNE TEST"]['Anti ds DNA']['RESULT'],
                        i["AUTOIMMUNE TEST"]['Anticardiolipin Antibodies (IgG & IgM)']['RESULT'],
                        i["AUTOIMMUNE TEST"]['Rheumatoid factor']['RESULT'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )

                    cursor.execute(autoimmunetest, autoimmunetest_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])

                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Coagulation Test Details")
            for i in dataitem:
                try:
                    coagulationtest = (
                        "UPDATE coagulation_test "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, pt = %s, ptinr = %s, "
                        "bt = %s, ct = %s "
                        "WHERE emp_no = %s"
                    )

                    coagulationtest_values = (
                        date_,
                        i['Details']['Basic detail']['Year'],
                        i['Details']['Basic detail']['Batch'],
                        i['Details']['Basic detail']['Hospital'],
                        i["COAGULATION TEST"]['Prothrombin Time (PT)']['RESULT'],
                        i["COAGULATION TEST"]['PT INR']['RESULT'],
                        i["COAGULATION TEST"]['Bleeding Time (BT)']['RESULT'],
                        i["COAGULATION TEST"]['Clotting Time (CT)']['RESULT'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )

                    cursor.execute(coagulationtest, coagulationtest_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])

                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Enzymes and Cardiac Details")
            for i in dataitem:
                try:
                    enzymesandcardiacprofile = (
                        "UPDATE enzymes_cardio "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, "
                        "acid_phosphatase = %s, adenosine = %s, amylase = %s, lipase = %s, "
                        "troponin_t = %s, troponin_i = %s, cpk_total = %s, cpk_mb = %s, "
                        "ecg = %s, ecg_comments = %s, echo = %s, echo_comments = %s, "
                        "tmt = %s, tmt_comments = %s "
                        "WHERE emp_no = %s"
                    )
                    
                    enzymesandcardiacprofile_values = (
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
                        i["ENZYMES & CARDIAC Profile"]['TMT']['COMMENTS(If Abnormal)'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )
                    
                    cursor.execute(enzymesandcardiacprofile, enzymesandcardiacprofile_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                    
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Urine Routine Details")
            for i in dataitem:
                try:
                    urineroutine = (
                        "UPDATE urine_routine "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, "
                        "colour = %s, apperance = %s, reaction = %s, specific_gravity = %s, "
                        "protein_albumin = %s, glucose = %s, ketone = %s, urobilinogen = %s, "
                        "bile_salts = %s, bile_pigments = %s, wbc_pluscells = %s, rbc = %s, "
                        "epithelial_cell = %s, casts = %s, crystals = %s, bacteria = %s "
                        "WHERE emp_no = %s"
                    )
                    
                    urineroutine_values = (
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
                        i["URINE ROUTINE"]['Bacteria']['RESULT'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )
                    
                    cursor.execute(urineroutine, urineroutine_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                    
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Serology Result Details")
            for i in dataitem:
                try:
                    serology = (
                        "UPDATE serology_result "
                        "SET entry_date = %s, year = %s, batch = %s, hospital = %s, "
                        "hiv_screening = %s, hiv_screening_range = %s, hiv_screening_comment = %s, "
                        "hbsag = %s, hbsag_range = %s, hbsag_comment = %s, "
                        "hcv = %s, hcv_range = %s, hcv_comment = %s, "
                        "widal = %s, widal_range = %s, widal_comment = %s, "
                        "vdrl = %s, vdrl_range = %s, vdrl_comment = %s, "
                        "denguens = %s, denguens_range = %s, denguens_comment = %s, "
                        "dengueigg = %s, dengueigg_range = %s, dengueigg_comment = %s, "
                        "dengueigm = %s, dengueigm_range = %s, dengueigm_comment = %s "
                        "WHERE emp_no = %s"
                    )
                    
                    serology_values = (
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
                        i["SEROLOGY"]['Dengue IgM']['Comment'],
                        str(i['Details']['Basic detail']['EMP NO'])
                    )
                    
                    cursor.execute(serology, serology_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                    
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Submitting Motion Details")
            for i in dataitem:
                try:
                    motion = ("UPDATE motion SET "
                            "entry_date = %s, year = %s, batch = %s, hospital = %s, "
                            "colour = %s, appearance = %s, occult_blood = %s, "
                            "ova = %s, cyst = %s, mucus = %s, pus_cells = %s, "
                            "rbcs = %s, others_t = %s "
                            "WHERE emp_no = %s")
                    motion_values = (
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
                        i["MOTION"]['Others']['RESULT'],
                        str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                    )
                    cursor.execute(motion, motion_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

                st.write("Updating Routine Culture Details")
                for i in dataitem:
                    try:
                        routinetest = ("UPDATE routine_culture SET "
                                    "entry_date = %s, year = %s, batch = %s, hospital = %s, "
                                    "urine = %s, motion = %s, sputum = %s, blood = %s "
                                    "WHERE emp_no = %s")
                        routinetest_values = (
                            date_,
                            i['Details']['Basic detail']['Year'],
                            i['Details']['Basic detail']['Batch'],
                            i['Details']['Basic detail']['Hospital'],
                            i["ROUTINE CULTURE & SENSITIVITY TEST"]['Urine']['RESULT'],
                            i["ROUTINE CULTURE & SENSITIVITY TEST"]['Motion']['RESULT'],
                            i["ROUTINE CULTURE & SENSITIVITY TEST"]['Sputum']['RESULT'],
                            i["ROUTINE CULTURE & SENSITIVITY TEST"]['Blood']['RESULT'],
                            str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                        )
                        cursor.execute(routinetest, routinetest_values)
                        connection.commit()
                        print(i['Details']['Basic detail']['EMP NO'])
                    except Exception as e:
                        st.write(e)
                        st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                                i["Details"]['Basic detail']['Name'])

                st.write("Updating Men's Pack Details")
                for i in dataitem:
                    try:
                        menspack = ("UPDATE mens_pack SET "
                                    "entry_date = %s, year = %s, batch = %s, hospital = %s, psa = %s "
                                    "WHERE emp_no = %s")
                        menspack_values = (
                            date_,
                            i['Details']['Basic detail']['Year'],
                            i['Details']['Basic detail']['Batch'],
                            i['Details']['Basic detail']['Hospital'],
                            i["Men's Pack"]["PSA (Prostate specific Antigen)"]['RESULT'],
                            str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                        )
                        cursor.execute(menspack, menspack_values)
                        connection.commit()
                        print(i['Details']['Basic detail']['EMP NO'])
                    except Exception as e:
                        st.write(e)
                        st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                                i["Details"]['Basic detail']['Name'])

            st.write("Updating Women's Pack Details")
            for i in dataitem:
                try:
                    womenspack = ("UPDATE womens_pack SET "
                                "entry_date = %s, year = %s, batch = %s, hospital = %s, "
                                "mammogram_nm_ab = %s, mammogram_comment = %s, "
                                "pap_nm_ab = %s, pap_comment = %s "
                                "WHERE emp_no = %s")

                    womenspack_values = (
                        date_,
                        i['Details']['Basic detail']['Year'],
                        i['Details']['Basic detail']['Batch'],
                        i['Details']['Basic detail']['Hospital'],
                        i["Women's Pack"]['Mammogram']['NORMAL / ABNORMAL'],
                        i["Women's Pack"]['Mammogram']['COMMENTS'],
                        i["Women's Pack"]['PAP Smear']['NORMAL / ABNORMAL'],
                        i["Women's Pack"]['PAP Smear']['COMMENTS'],
                        str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                    )
                    cursor.execute(womenspack, womenspack_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Updating Occupational Profile Details")
            for i in dataitem:
                try:
                    occupationalprofile = ("UPDATE occupational_profile SET "
                                        "entry_date = %s, year = %s, batch = %s, hospital = %s, "
                                        "audiometry_nm_ab = %s, audiometry_comment = %s, "
                                        "pft_nm_ab = %s, pft_comment = %s "
                                        "WHERE emp_no = %s")

                    occupationalprofile_values = (
                        date_,
                        i['Details']['Basic detail']['Year'],
                        i['Details']['Basic detail']['Batch'],
                        i['Details']['Basic detail']['Hospital'],
                        i["Occupational Profile"]['Audiometry ']['NORMAL / ABNORMAL'],
                        i["Occupational Profile"]['Audiometry ']['COMMENTS'],
                        i["Occupational Profile"]['PFT']['NORMAL / ABNORMAL'],
                        i["Occupational Profile"]['PFT']['COMMENTS'],
                        str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                    )
                    cursor.execute(occupationalprofile, occupationalprofile_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Updating Other Tests Details")
            for i in dataitem:
                try:
                    otherstest = ("UPDATE other_tests SET "
                                "entry_date = %s, year = %s, batch = %s, hospital = %s, "
                                "pathology = %s, pathology_comments = %s "
                                "WHERE emp_no = %s")

                    otherstest_values = (
                        date_,
                        i['Details']['Basic detail']['Year'],
                        i['Details']['Basic detail']['Batch'],
                        i['Details']['Basic detail']['Hospital'],
                        i["Others TEST"]['Pathology ']['NORMAL / ABNORMAL'],
                        i["Others TEST"]['Pathology ']['COMMENTS'],
                        str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                    )
                    cursor.execute(otherstest, otherstest_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Updating Ophthalmic Report Details")
            for i in dataitem:
                try:
                    ophthalmicreport = ("UPDATE ophthalmic_report SET "
                                        "entry_date = %s, year = %s, batch = %s, hospital = %s, "
                                        "vision = %s, vision_comments = %s, colourvision = %s, colourvision_comment = %s "
                                        "WHERE emp_no = %s")

                    ophthalmicreport_values = (
                        date_,
                        i['Details']['Basic detail']['Year'],
                        i['Details']['Basic detail']['Batch'],
                        i['Details']['Basic detail']['Hospital'],
                        i["OPHTHALMIC REPORT"]['Vision']['NORMAL / ABNORMAL'],
                        i["OPHTHALMIC REPORT"]['Vision']['COMMENTS'],
                        i["OPHTHALMIC REPORT"]['Color Vision']['NORMAL / ABNORMAL'],
                        i["OPHTHALMIC REPORT"]['Color Vision']['COMMENTS'],
                        str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                    )
                    cursor.execute(ophthalmicreport, ophthalmicreport_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Updating X-Ray Details")
            for i in dataitem:
                try:
                    xray = ("UPDATE x_ray SET "
                            "entry_date = %s, year = %s, batch = %s, hospital = %s, "
                            "chest_nm_ab = %s, chest_comment = %s, "
                            "spine_nm_ab = %s, spine_comment = %s, "
                            "abdomen_nm_ab = %s, abdomen_comment = %s, "
                            "kub_nm_ab = %s, kub_comment = %s, "
                            "pelvis_nm_ab = %s, pelvis_comment = %s "
                            "WHERE emp_no = %s")

                    xray_values = (
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
                        i["X-RAY"]['Pelvis']['COMMENTS (If Abnormal)'],
                        str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                    )

                    cursor.execute(xray, xray_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Updating USG Details")
            for i in dataitem:
                try:
                    usg = ("UPDATE usg SET "
                        "entry_date = %s, year = %s, batch = %s, hospital = %s, "
                        "abdomen = %s, abdomen_comments = %s, "
                        "pelvis = %s, pelvis_comments = %s, "
                        "neck = %s, neck_comments = %s, "
                        "kub = %s, kub_comments = %s "
                        "WHERE emp_no = %s")

                    usg_values = (
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
                        i["USG "]['KUB']['COMMENTS (If Abnormal)'],
                        str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                    )

                    cursor.execute(usg, usg_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Updating CT Report Details")
            for i in dataitem:
                try:
                    ct = ("UPDATE ct_report SET "
                        "entry_date = %s, year = %s, batch = %s, hospital = %s, "
                        "brain = %s, brain_comment = %s, "
                        "abdomen = %s, abdomen_comment = %s, "
                        "pelvis = %s, pelvis_comment = %s, "
                        "ct_lungs = %s, ct_lungs_comment = %s, "
                        "spine = %s, spine_comment = %s "
                        "WHERE emp_no = %s")

                    ct_values = (
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
                        i["CT"]['Spine']['COMMENTS (If Abnormal)'],
                        str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                    )

                    cursor.execute(ct, ct_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

            st.write("Updating MRI Details")
            for i in dataitem:
                try:
                    mri = ("UPDATE mri SET "
                        "entry_date = %s, year = %s, batch = %s, hospital = %s, "
                        "brain = %s, brain_comments = %s, "
                        "abdomen = %s, abdomen_comments = %s, "
                        "pelvis = %s, pelvis_comments = %s, "
                        "mri_lungs = %s, mri_lungs_comments = %s, "
                        "spine = %s, spine_comments = %s "
                        "WHERE emp_no = %s")

                    mri_values = (
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
                        i["MRI"]['Spine']['COMMENTS (If Abnormal)'],
                        str(i['Details']['Basic detail']['EMP NO'])  # Emp No for WHERE clause
                    )

                    cursor.execute(mri, mri_values)
                    connection.commit()
                    print(i['Details']['Basic detail']['EMP NO'])
                except Exception as e:
                    st.write(e)
                    st.write("Error:", str(i['Details']['Basic detail']['EMP NO']),
                            i["Details"]['Basic detail']['Name'])

                    

            st.write("Data Inserted Successfully")

    r2c1, r2c2 = st.columns([3,7])
    with r2c1:
        with st.container(border=1, height = 700):
            st.session_state.optFilter = option_menu("Filter", options=["Healthy", "Unhealthy"], icons=['a','a'])
    with r2c2:
        with st.container(border=1, height=700):
            rc1, rc2 = st.columns([2,8])
            with rc1:
                st.subheader('Dashboard')
            with rc2:
                opt = option_menu(None, ["Total Footfalls", "Employee", "Contractor"],orientation='horizontal',icons=['a','a','a'])
            r1c1, r1c2, r1c3, r1c4 = st.columns(4)
            with r1c1:
                cursor.execute(f"SELECT count(PatientID) FROM basicdetails WHERE status = 'Healthy' and DATE(EntryDateTime) = CURDATE();")
                footfalls = cursor.fetchall()
                cursor.execute(f"SELECT count(appoint_ID) FROM appointments WHERE appoint_date = CURDATE();")
                appoint = cursor.fetchall()
                with st.container(border=True):
                    st.markdown(
                       f"""
                        <div style=  height: 100px; display: flex; align-items: center; justify-content: center;">
                            <div style="text-align: center;">
                                <h2 style="margin-left: 24px; margin-top: -15px;">{footfalls[0][0]}</h2>
                                <p style=" font-weight: bold;">Total Footfalls</p>
                            </div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
            with r1c2:
                with st.container(border=True):
                    st.markdown(
                        """
                        <div style=  height: 100px; display: flex; align-items: center; justify-content: center;">
                            <div style="text-align: center;">
                                <h2 style="margin-left: 24px; margin-top: -15px;">10</h2>
                                <p style=" font-weight: bold;">Healthy Entry</p>
                            </div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
            with r1c3:
                with st.container(border=True):
                    st.markdown(
                        """
                        <div style=  height: 100px; display: flex; align-items: center; justify-content: center;">
                            <div style="text-align: center;">
                                <h2 style="margin-left: 24px; margin-top: -15px;">10</h2>
                                <p style=" font-weight: bold;">Unhealthy Entry</p>
                            </div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
            with r1c4:
                with st.container(border=True):
                    st.markdown(
                        f"""
                        <div style=  height: 100px; display: flex; align-items: center; justify-content: center;">
                            <div style="text-align: center;">
                                <h2 style="margin-left: 24px; margin-top: -15px;">{appoint[0][0]}</h2>
                                <p style=" font-weight: bold;">Appointments</p>
                            </div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
            with st.container(border=1, height=500):
                if st.session_state.optFilter == "Healthy":
                    st.write("*Healthy Entry*")
                    visitreason = []
                    count = []                    
                    cursor.execute("SELECT DISTINCT vistreason FROM basicdetails where status = 'Healthy';")
                    result = cursor.fetchall()
                    for row in result:
                        visitreason.append(row[0])                  
                    for reason in visitreason:
                        cursor.execute("SELECT COUNT(PatientID) FROM basicdetails WHERE status = 'Healthy' AND vistreason = %s AND DATE(entrydatetime) = CURDATE();", (reason,))
                        count.append(cursor.fetchone()[0])  
                    fig, ax = plt.subplots(figsize=(10, 4), facecolor='none')
                    colors = ['#0C3D8C', '#C6256A', '#7C0C0C', '#7CAEFF', '#705314']  
                    bars = ax.bar(visitreason, count, color=colors)
                    ax.set_xlabel('')
                    ax.set_ylabel('Count', fontsize=12, color='black')
                    ax.set_xticks(range(len(visitreason)))
                    ax.set_xticklabels(visitreason, rotation=45, ha="right", color='black')
                    ax.grid(True, linestyle='--', alpha=0.6)
                    ax.set_facecolor('none')  
                    for spine in ax.spines.values():
                        spine.set_visible(False)
                    ax.legend(bars, visitreason, loc='lower center', bbox_to_anchor=(0.5, -0.2), fancybox=True, shadow=True, ncol=3)
                    plt.tight_layout()
                    
                    st.pyplot(fig)
                if st.session_state.optFilter == "Unhealthy":
                    st.write("*Unhealthy Entry*")

