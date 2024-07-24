import streamlit as st
import os
import pandas as pd
from streamlit_modal import Modal
from streamlit_option_menu import option_menu



def show_data(emp):
    # MARK: Show Data
    for i in range(len(emp)):
        with st.container(border=1):
            r1c1,r1c2,r1c3,r1c4 = st.columns([4,6,2,0.2])
            with r1c1:
                st.html(f"""
                        <style>
                            button[kind="primary"]{{
                                all: unset;
                                background-color: #22384F;
                                color: white;
                                border-radius: 5px;
                                text-align: center;
                                cursor: pointer;
                                font-size: 20px;
                                width: 95%;
                                padding: 10px ;
                            }}
                            .cnt{{
                                width: 100%;
                                margin-left:20px;
                                display: flex;
                            }}
                            .cnt h2{{
                                text-align: center;
                                color: #333;
                                margin-left: 20px;
                            }}
                            .cnt img{{
                                width: 50px;
                                height: 50px;
                                border-radius: 50px;
                                margin-top: 15px;
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
                            <h2>{emp[i]["emp_no"]}</h3>
                            <div>
                                <h5>{emp[i]["name"]}</h4>
                            </div>

                        </div>
                    """)
            with r1c3:
                st.html("""
                    <div style="width:100px;height:3px"></div>
                        """)
                if st.button("View",key=i,type="primary"):
                    st.session_state.open_modal = True
                    st.session_state.usr_prof = emp[i]
                    st.rerun()

def set_data(emp):
    st.session_state.data = emp.to_dict('records')

def Search(cursor):
    modal = Modal(
        "Employee Profile",
        key="modal",
    )
    if "usr_prof" not in st.session_state:
        st.session_state.usr_prof = {}
    if "search" not in st.session_state:
        st.session_state.search = False
    if "searchinp" not in st.session_state:
        st.session_state.searchinp = ""

    if "data" not in st.session_state:
        st.session_state.data = {}
    if "open_modal" not in st.session_state:
        st.session_state.open_modal = False

    if st.session_state.open_modal == False:
        st.title("Search")
        search1, search2,search3 = st.columns([7,1,3])
        with search1:
            st.session_state.searchinp = st.text_input("search",placeholder="Search by Patient ID")
        with search2:
            st.write("<div><br></div>", unsafe_allow_html=True)
            st.session_state.search = st.button("Search", type="primary")

        if st.session_state.search:
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
        with st.container(border=1):
            with st.container(border=1):
                r1c1,r1c2 = st.columns([4,6])
                cursor.execute(f"SELECT * FROM vitals WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                vitals = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                cursor.execute(f"SELECT * FROM consultation WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                consultation = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                
                cursor.execute(f"SELECT * FROM x_ray WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                xray = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                cursor.execute(f"SELECT * FROM womens_pack WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                womens = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                

                with r1c1:
                    st.write(f"Employee ID: {st.session_state.usr_prof['emp_no']}")
                    st.write(f"Name: {st.session_state.usr_prof['name']}")
                    st.write(f"DOB: {st.session_state.usr_prof['dob']}")
            
            with st.container(border=1,height=700):
                r0r1,r0r2 = st.columns([6,4])
                with r0r1:
                    menu = option_menu(
                        None,
                        ["Basic Details","Medical Details","Other Details"],
                        key="menu",
                        orientation="horizontal",
                        icons=['a','b','c']
                    )
                if menu == "Basic Details":
                    r0c1,r0c2 = st.columns([5,6])
                    with r0c1:
                        # MARK: Personal Details
                        with st.container(border=1):
                            st.title("Personal Details")
                            st.write(f"**Employee ID**: {st.session_state.usr_prof['emp_no']}")
                            st.write(f"**Name**: {st.session_state.usr_prof['name']}")
                            st.write(f"**DOB**: {st.session_state.usr_prof['dob']}")
                            st.write(f"**Age**: {st.session_state.usr_prof['age']}")
                            st.write(f"**Gender**: {st.session_state.usr_prof['gender']}")
                            st.write("**Identification Mark**:")
                            st.markdown(f" * {st.session_state.usr_prof['identification_mark']}")
                    with r0c2:
                        with st.container(border=1):
                            st.title("Contact Details")
                            st.write(f"**Email**: {st.session_state.usr_prof['personal_mail']}")
                            st.write(f"**Office Email**: {st.session_state.usr_prof['office_mail']}")
                            st.write(f"**Emergency Contact Person**: {st.session_state.usr_prof['emg_con_person']}")
                            st.write(f"**Emergency Contact Relation**: {st.session_state.usr_prof['emg_con_relation']}")
                            st.write(f"**Emergency Contact Number**: {st.session_state.usr_prof['emg_con_number']}")
                            st.write(f"**Emergency Contact Email**: {st.session_state.usr_prof['emg_con_mail']}")
                            st.write(f"**Address**: {st.session_state.usr_prof['address']}")
                            st.write(f"**Personal Phone No.**: {st.session_state.usr_prof['personal_phone_no']}")
                            st.write(f"**Office Phone No.**: {st.session_state.usr_prof['office_phone_no']}")
                if menu == "Medical Details":
                    r0c1,r0c2 = st.columns([4,7])
                    if not vitals.empty:
                        with r0c1:
                            with st.container(border=1, height=300):
                                # MARK: Vitals
                                st.title("Vitals")
                                r01c1,r02c2 = st.columns([4,6])
                                with r01c1:
                                    st.write(f"**Systolic**: {vitals['Systolic'][0]}")
                                    st.write(f"**Diastolic**: {vitals['Diastolic'][0]}")
                                    st.write(f"**Pulse**: {vitals['PulseRate'][0]}")
                                    st.write(f"**SpO2**: {vitals['SpO2'][0]}")
                                with r02c2:
                                    st.write(f"**Temperature**: {vitals['Temperature'][0]} °F")
                                    st.write(f"**Weight**: {vitals['Weight'][0]} kg")
                                    st.write(f"**Height**: {vitals['Height'][0]} cm")
                                    st.write(f"**BMI**: {(float(vitals['Weight'][0]) / (float(vitals['Height'][0])/100)**2):.2f}")
                    else:
                        with r0c1:
                            st.warning("No records found")
                    with r0c2:
                        with st.container(border=1,height=580): # type: ignore
                            # MARK: Investigation
                            st.subheader("Investigations")
                            inve = st.selectbox("Select Investigation",["Hematology","RST","RFT","LFT","Thyroid","Autoimmune","Coagulation","CT","Enzymes","Lipid","Mens","Motion","MRI","Occupational","Ophthalmic","Other","Routine","Serology","Urine","USG"])
                            if inve == "Hematology":
                                cursor.execute(f"SELECT * FROM hematology_result WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                hematology = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                st.subheader("Hematology")
                                r2c0,r2c1 = st.columns([4,6])
                                if not hematology.empty:
                                    # MARK: Hematology
                                    with r2c0:
                                        st.write("**Hemoglobin**: ",hematology['heamoglobin'][0])
                                        st.write("**RBC**: ",hematology['rbc_count'][0])
                                        st.write("**WBC**: ",hematology['wbc_count'][0])
                                        st.write("**Haemotocrit**: ",hematology['haemotocrit'][0])
                                        st.write("**MCV**: ",hematology['mcv'][0])
                                        st.write("**MCH**: ",hematology['mch'][0])
                                        st.write("**Eosinophil**: ",hematology['eosinophil'][0])
                                        st.write("**Basophils**: ",hematology['basophils'][0])
                                        st.write("**PBS_RBC**: ",hematology['pbs_rbc'][0])
                                    with r2c1:
                                        st.write("**MCHC**: ",hematology['mchc'][0])
                                        st.write("**RDW**: ",hematology['rdw'][0])
                                        st.write("**Platelet Count**: ",hematology['platelet'][0])
                                        st.write("**RDW**: ",hematology['rdw'][0])
                                        st.write("**Neutrophil**: ",hematology['neutrophil'][0])
                                        st.write("**Lymphocyte**: ",hematology['lymphocyte'][0])
                                        st.write("**Monocyte**: ",hematology['monocyte'][0])
                                        st.write("**ESR**: ",hematology['esr'][0])
                                else:
                                    st.warning("No records found")

                            if inve == "RST":
                                # MARK: RST
                                cursor.execute(f"SELECT * FROM routine_sugartest WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                st.subheader("Routine Sugar Test")
                                sugar = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                if not sugar.empty:
                                    r2c0,r2c1 = st.columns([4,6])
                                    with r2c0:
                                        st.write("**Fasting Glucose**: ",sugar['glucosef'][0])
                                        st.write("**Post Prandial Glucose**: ",sugar['glucosepp'][0])
                                        st.write("**Random Blood Sugar**: ",sugar['rbs'][0])
                                        st.write("**EAG**: ",sugar['eag'][0])
                                        st.write("**HbA1c**: ",sugar['hba1c'][0])
                                else:
                                    st.warning("No records found")
                            if inve == "RFT":
                                # MARK: RFT
                                st.subheader("Renal Function Test")
                                cursor.execute(f"SELECT * FROM rft_result WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                rft = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                if not rft.empty:
                                    r2c0,r2c1 = st.columns([4,6])
                                    with r2c0:
                                        st.write("**Urea**: ",rft['urea'][0])
                                        st.write("**BUN**: ",rft['bun'][0])
                                        st.write("**Serum Creatinine**: ",rft['sr_creatinine'][0])
                                        st.write("**Uric Acid**: ",rft['uric_acid'][0])
                                        st.write("**Sodium**: ",rft['sodium'][0])
                                        st.write("**Potassium**: ",rft['potassium'][0])
                                    with r2c1:
                                        st.write("**Calcium**: ",rft['calcium'][0])
                                        st.write("**Phosphorus**: ",rft['phosphorus'][0])
                                        st.write("**Chloride**: ",rft['chloride'][0])
                                        st.write("**Bicarbonate**: ",rft['bicarbonate'][0])
                                else:
                                    st.warning("No records found")
                            if inve == "LFT":
                                # MARK: LFT
                                cursor.execute(f"SELECT * FROM liver_function WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                liver = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                st.subheader("Liver Function Test")
                                if not liver.empty:
                                    r2c0,r2c1 = st.columns([4,6])
                                    with r2c0:
                                        st.write("**Total Bilirubin**: ",liver['bilirubin_total'][0])
                                        st.write("**Direct Bilirubin**: ",liver['bilirubin_direct'][0])
                                        st.write("**Indirect Bilirubin**: ",liver['bilirubin_indirect'][0])
                                        st.write("**SGOT/ALT**: ",liver['sgot_alt'][0])
                                        st.write("**Alkaline Phosphatase**: ",liver['alkaline_phosphatase'][0])
                                        st.write("**Total Protein**: ",liver['total_protein'][0])
                                    with r2c1:
                                        st.write("**Globulin**: ",liver['globulin'][0])
                                        st.write("**Alb/Glob Ratio**: ",liver['alb_globratio'][0])
                                        st.write("**Gamma GT**: ",liver['gammagt'][0])
                                        st.write("**SGPT/ALT**: ",liver['sgpt_alt'][0])
                                        st.write("**Albumin**: ",liver['albumin'][0])
                                else:
                                    st.warning("No records found")

                            if inve == "Thyroid":
                                # MARK: Thyroid
                                thyroid = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                cursor.execute(f"SELECT * FROM autoimmune_test WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                st.subheader("Thyroid Function Test")
                                if thyroid.empty:
                                    st.warning("No records found")
                            if inve == "Autoimmune":
                                # MARK: Autoimmune
                                autoimmune = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                cursor.execute(f"SELECT * FROM coagulation_test WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")

                                st.subheader("Autoimmune Test")
                                if autoimmune.empty:
                                    st.warning("No records found")
                            if inve == "Coagulation":
                                # MARK: Coagulation
                                cursor.execute(f"SELECT * FROM thyroid_function_test WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                coagulation = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                st.subheader("Coagulation Test")
                                if coagulation.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**T3**: ",coagulation['t3'][0])
                                        st.write("**T4**: ",coagulation['t4'][0])
                                        st.write("**TSH**: ",coagulation['tsh'][0])
                                    with r0c2:
                                        st.write("**TSH NM AB**: ",coagulation['tsh_nm_ab'][0])

                                st.json(coagulation.to_dict('records'))
                            if inve == "CT":
                                # MARK: CT
                                cursor.execute(f"SELECT * FROM ct_report WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                ct = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                if ct.empty:
                                    st.warning("No records found")
                                st.json(ct.to_dict('records'))
                            if inve == "Enzymes":
                                # MARK: Enzymes
                                cursor.execute(f"SELECT * FROM enzymes_cardio WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                enzymes = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                st.subheader("Enzymes")
                                if enzymes.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**Acid Phosphatase**: ",enzymes['acid_phosphatase'][0])
                                        st.write("**Adenosine**: ",enzymes['adenosine'][0])
                                        st.write("**Amylase**: ",enzymes['amylase'][0])
                                        st.write("**Lipase**: ",enzymes['lipase'][0])
                                        st.write("**Troponin T**: ",enzymes['troponin_t'][0])
                                        st.write("**Troponin I**: ",enzymes['troponin_i'][0])
                                    with r0c2:
                                        st.write("**CPK Total**: ",enzymes['cpk_total'][0])
                                        st.write("**CPK MB**: ",enzymes['cpk_mb'][0])
                                        st.write("**ECG**: ",enzymes['ecg'][0])
                                        st.write("**ECHO**: ",enzymes['echo'][0])
                                        st.write("**TMT**: ",enzymes['tmt'][0])

                            if inve == "Lipid":
                                # MARK: Lipid
                                cursor.execute(f"SELECT * FROM lipid_profile WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                lipid = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                                st.subheader("Lipid Profile")
                                if lipid.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**Total Cholesterol**: ",lipid['tcholesterol'][0])
                                        st.write("**Triglycerides**: ",lipid['triglycerides'][0])
                                        st.write("**HDL Cholesterol**: ",lipid['hdl_cholesterol'][0])
                                        st.write("**VLDL Cholesterol**: ",lipid['vldl_cholesterol'][0])
                                    with r0c2:
                                        st.write("**LDL/HDL Ratio**: ",lipid['ldlhdlratio'][0])
                                        st.write("**Chol/HDL Ratio**: ",lipid['chol_hdlratio'][0])
                                        st.write("**LDL Cholesterol**: ",lipid['ldl_cholesterol'][0])
                            if inve == "Mens":
                                # MARK: Mens
                                cursor.execute(f"SELECT * FROM mens_pack WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                mens = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                st.subheader("Mens Pack")
                                if mens.empty:
                                    st.warning("No records found")
                                else:
                                    st.write("**PSA**: ",mens['psa'][0])

                
                            if inve == "Motion":
                                # MARK: Motion
                                cursor.execute(f"SELECT * FROM motion WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                motion = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                st.subheader("Motion")
                                if motion.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**Colour**: ",motion['colour'][0])
                                        st.write("**Appearance**: ",motion['appearance'][0])
                                        st.write("**Occult Blood**: ",motion['occult_blood'][0])                                   

                            if inve == "MRI":
                                # MARK: MRI
                                cursor.execute(f"SELECT * FROM mri WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                mri = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                st.subheader("MRI")
                                if mri.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**Brain**: ",mri['brain'][0])
                                        st.write("**Abdomen**: ",mri['abdomen'][0])
                                        st.write("**Pelvis**: ",mri['pelvis'][0])
                                    with r0c2:
                                        st.write("**MRI Lungs**: ",mri['mri_lungs'][0])
                                        st.write("**Spine**: ",mri['spine'][0])

                           

                            if inve == "Occupational":
                                # MARK: Occupational
                                cursor.execute(f"SELECT * FROM occupational_profile WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                occupational = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                st.subheader("Occupational")

                                if occupational.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**Audiometry NM AB**: ",occupational['audiometry_nm_ab'][0])
                                        st.write("**Audiometry Comment**: ",occupational['audiometry_comment'][0])
                                    with r0c2:
                                        st.write("**PFT NM AB**: ",occupational['pft_nm_ab'][0])
                                        st.write("**PFT Comment**: ",occupational['pft_comment'][0])


                            if inve == "Ophthalmic":
                                # MARK: Ophthalmic
                                cursor.execute(f"SELECT * FROM ophthalmic_report WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                ophthalmic = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])


                                st.subheader("Ophthalmic")

                                if ophthalmic.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**Vision**: ",ophthalmic['vision'][0])
                                        st.write("**Vision Comments**: ",ophthalmic['vision_comments'][0])
                                    with r0c2:
                                        st.write("**Colour Vision**: ",ophthalmic['colourvision'][0])
                                        st.write("**Colour Vision Comment**: ",ophthalmic['colourvision_comment'][0])

                            if inve == "Other":
                                # MARK: Other
                                cursor.execute(f"SELECT * FROM other_tests WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                other = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                st.subheader("Other Tests")
                                if other.empty:
                                    st.warning("No records found")

                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**Pathology**: ",other['pathology'][0])
                                        st.write("**Pathology Comments**: ",other['pathology_comments'][0])

                            if inve == "Routine":
                                # MARK: Routine
                                cursor.execute(f"SELECT * FROM routine_culture WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                routine = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                st.subheader("Routine")
                                if routine.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**Urine**: ",routine['urine'][0])
                                        st.write("**Motion**: ",routine['motion'][0])
                                    with r0c2:
                                        st.write("**Blood**: ",routine['blood'][0])
                                        st.write("**Sputum**: ",routine['sputum'][0])

                            if inve == "Serology":
                                # MARK: Serology
                                cursor.execute(f"SELECT * FROM serology_result WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                serology = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
                

                                st.subheader("Serology")
                                if serology.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**HIV Screening**: ",serology['hiv_screening'][0])
                                        st.write("**HIV Screening Comment**: ",serology['hiv_screening_comment'][0])
                                        st.write("**HBsAg**: ",serology['hbsag'][0])
                                        st.write("**HBsAg Comment**: ",serology['hbsag_comment'][0])
                                        st.write("**HCV**: ",serology['hcv'][0])
                                        st.write("**HCV Comment**: ",serology['hcv_comment'][0])
                                        st.write("**Widal**: ",serology['widal'][0])
                                        st.write("**Widal Comment**: ",serology['widal_comment'][0])
                                    with r0c2:
                                        st.write("**VDRL**: ",serology['vdrl'][0])
                                        st.write("**VDRL Comment**: ",serology['vdrl_comment'][0])
                                        st.write("**Dengue NS1**: ",serology['denguens'][0])
                                        st.write("**Dengue NS1 Comment**: ",serology['denguens_comment'][0])
                                        st.write("**Dengue IgG**: ",serology['dengueigg'][0])
                                        st.write("**Dengue IgG Comment**: ",serology['dengueigg_comment'][0])
                                        st.write("**Dengue IgM**: ",serology['dengueigm'][0])
                                        st.write("**Dengue IgM Comment**: ",serology['dengueigm_comment'][0])
                                    

                            if inve == "Urine":
                                # MARK: Urine
                                cursor.execute(f"SELECT * FROM urine_routine WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                urine = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                st.subheader("Urine")

                                if urine.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**Colour**: ",urine['colour'][0])
                                        st.write("**Appearance**: ",urine['apperance'][0])
                                        st.write("**Reaction**: ",urine['reaction'][0])
                                        st.write("**Specific Gravity**: ",urine['specific_gravity'][0])
                                        st.write("**Protein Albumin**: ",urine['protein_albumin'][0])
                                        st.write("**Glucose**: ",urine['glucose'][0])
                                        st.write("**Ketone**: ",urine['ketone'][0])
                                        st.write("**Urobilinogen**: ",urine['urobilinogen'][0])
                                        st.write("**Bile Salts**: ",urine['bile_salts'][0])
                                        st.write("**Bile Pigments**: ",urine['bile_pigments'][0])
                                    with r0c2:
                                        st.write("**WBC Plus Cells**: ",urine['wbc_pluscells'][0])
                                        st.write("**RBC**: ",urine['rbc'][0])
                                        st.write("**Epithelial Cell**: ",urine['epithelial_cell'][0])
                                        st.write("**Casts**: ",urine['casts'][0])
                                        st.write("**Crystals**: ",urine['crystals'][0])
                                        st.write("**Bacteria**: ",urine['bacteria'][0])

                            if inve == "USG":
                                # MARK: USG
                                cursor.execute(f"SELECT * FROM usg WHERE emp_no = '{st.session_state.usr_prof['emp_no']}'")
                                usg = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                                st.subheader("USG")
                                if usg.empty:
                                    st.warning("No records found")
                                else:
                                    r0c1,r0c2 = st.columns([4,6])
                                    with r0c1:
                                        st.write("**Liver**: ",usg['liver'][0])
                                        st.write("**Gall Bladder**: ",usg['gall_bladder'][0])
                                        st.write("**Pancreas**: ",usg['pancreas'][0])
                                        st.write("**Kidney**: ",usg['kidney'][0])
                                        st.write("**Spleen**: ",usg['spleen'][0])
                                        st.write("**Prostate**: ",usg['prostate'][0])
                                        st.write("**Uterus**: ",usg['uterus'][0])
                                        st.write("**Ovaries**: ",usg['ovaries'][0])
                                    with r0c2:
                                        st.write("**Bladder**: ",usg['bladder'][0])
                                        st.write("**Prostate**: ",usg['prostate'][0])
                                        st.write("**Uterus**: ",usg['uterus'][0])
                                        st.write("**Ovaries**: ",usg['ovaries'][0])
                                        st.write("**Bladder**: ",usg['bladder'][0])
                                        st.write("**Prostate**: ",usg['prostate'][0])
                                        st.write("**Uterus**: ",usg['uterus'][0])
                                        st.write("**Ovaries**: ",usg['ovaries'][0])


        if st.button("close"):
            st.session_state.open_modal = False
            st.rerun()
