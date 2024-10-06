from cProfile import label
import streamlit as st
import os
import pandas as pd
from  streamlit_option_menu import option_menu

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()
def get_data(cursor, table_name, filters=None,inv = None):
    # Execute the first query
    if "col" not in st.session_state:
        st.session_state.col = []
    if "filtered_data" not in st.session_state:
        st.session_state.filtered_data = pd.DataFrame()
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame()
    if "proceed" not in st.session_state:
        st.session_state.proceed = False
    if table_name == "Investigations":
        table_name = inv
    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows from the query
    st.session_state.data = cursor.fetchall()
    st.session_state.col = cursor.description
    st.session_state.df = pd.DataFrame(st.session_state.data, columns=[desc[0] for desc in st.session_state.col])
    st.session_state.filtered_data = st.session_state.df
    # apply the condition in the filter and return

    if filters:
        print(filters.items())
        for key,value in filters.items():
            return st.session_state.df[st.session_state.df[key] == value]
    return st.session_state.df


def Records_Filters(cursor):
    st.header("Records and Filters")
    
    # form_to_table = {
    #         "Recent":"Employee_det",
    #         "General":"Employee_det",
    #         "Basic Details":"Employee_det",
    #         "Vitals":"vitals",
    #         "Investigations":"Employee_det",
    #         "Fitness":"fitness",
    #         "Medical History":"medicalpersonalhist"
    #     }
    
    if "data" not in st.session_state:
        st.session_state.data = get_data(cursor=cursor,table_name="Employee_det")

    if "col_name" not in st.session_state:
        st.session_state.col_name = cursor.column_names
        
        
    if "filter_data" not in st.session_state:
        st.session_state.filter_data = {}



    with st.container(border=1):
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
                    width: 65%;
                    padding: 0px ;
                    margin-left:-10px
                }
            </style>
            """,unsafe_allow_html=True)
        if "form_data" not in st.session_state:
            st.session_state.form_data = {} 
            st.rerun()

        
        form_name = option_menu(
            None,
            ["All Details","Select Purpose","Personal & Emp Details","Vitals","Investigations","Fitness","Medical History"],
            orientation="horizontal",
            icons=['a','a','a','a','a','a', 'a']
        )
    
    
        if form_name == "Investigations":
            global inv, paropt, fromval, toval
            rc1, rc2 = st.columns([4,6])
            with rc1:
                rrc1, rrc2 = st.columns([4,6])
                with rrc1:
                    st.write("Select Test:")
                    st.write("\n")
                    st.write("Select Parameter:")
                with rrc2:
                    inv_form = ["SELECT TEST","HAEMATALOGY","ROUTINE SUGAR TESTS","RENAL FUNCTION TEST & ELECTROLYTES","LIPID PROFILE","LIVER FUNCTION TEST","THYROID FUNCTION TEST","AUTOIMMUNE TEST","COAGULATION TEST","ENZYMES & CARDIAC Profile","URINE ROUTINE","SEROLOGY","MOTION","ROUTINE CULTURE & SENSITIVITY TEST","Men's Pack","Women's Pack","Occupational Profile","Others TEST","OPHTHALMIC REPORT","X-RAY","USG","CT","MRI"]
                    inv = st.selectbox(
                    "Select the type of investigation you want to view",
                    inv_form,
                    label_visibility='collapsed')
                    if inv == "HAEMATALOGY":
                        hematology = [ "SELECT PARAMETER",
                                "Haemoglobin", "Red Blood Cell (RBC) Count", "WBC Count (TC)", "Haemotocrit (PCV)", "MCV", 
                                "MCH", "MCHC", "Platelet Count", "RDW (CV)", "Neutrophil", "Lymphocyte", "Eosinophil", 
                                "Monocyte", "Basophils", "Erythrocyte Sedimentation Rate (ESR)", "Peripheral Blood Smear - RBC Morphology", 
                                "Peripheral Blood Smear - Parasites", "Peripheral Blood Smear - Others"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= hematology, label_visibility='collapsed')
                    if inv == "ROUTINE SUGAR TESTS":
                        rst = [ "SELECT PARAMETER",
                                "Glucose (F)", "Glucose (PP)", "Random Blood sugar", "Estimated Average Glucose", "HbA1c"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= rst, label_visibility='collapsed')
                    if inv == "RENAL FUNCTION TEST & ELECTROLYTES":
                        rfte = [ "SELECT PARAMETER",
                                "Urea", "Blood urea nitrogen (BUN)", "Sr.Creatinine", "e GFR", "Uric acid", 
                                "Sodium", "Potassium", "Calcium", "Phosphorus", "Chloride", "Bicarbonate"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= rfte, label_visibility='collapsed')
                    if inv == "LIPID PROFILE":
                        lp = [ "SELECT PARAMETER",
                                "Total Cholesterol", "Triglycerides", "HDL - Cholesterol", "VLDL -Cholesterol", "LDL - Cholesterol", 
                                "CHOL:HDL ratio", "LDL:CHOL/HDL:CHOL Ratio"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= lp, label_visibility='collapsed')
                    if inv == "LIVER FUNCTION TEST":
                        lft = [ "SELECT PARAMETER",
                                "Bilirubin - Total", "Bilirubin - Direct", "Bilirubin - Indirect", "SGOT / AST", "SGPT / ALT", 
                                "Alkaline phosphatase", "Total Protein", "Albumin (Serum)", "Globulin (Serum)", "Alb/Glob Ratio", 
                                "Gamma Glutamyl Transferase"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= lft, label_visibility='collapsed')
                    if inv == "THYROID FUNCTION TEST":
                        tft = [ "SELECT PARAMETER",
                                "T3 - Triiodothyronine", "T4 - Thyroxine", "TSH - Thyroid Stimulating Hormone"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= tft, label_visibility='collapsed')
                    if inv == "AUTOIMMUNE TEST":
                        at = [ "SELECT PARAMETER",
                                "ANA (Antinuclear Antibody)", "Anti ds DNA", "Anticardiolipin Antibodies (IgG & IgM)", "Rheumatoid Factor"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= at, label_visibility='collapsed')
                    if inv == "COAGULATION TEST":
                        ct = [ "SELECT PARAMETER",
                                "Prothrombin Time (PT)", "PT INR", "Bleeding Time (BT)", "Clotting Time (CT)"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= ct, label_visibility='collapsed')
                    if inv == "ENZYMES & CARDIAC Profile":
                        ecp = [ "SELECT PARAMETER",
                                "Acid Phosphatase", "Adenosine Deaminase", "Amylase", "Lipase", "Troponin-T", "Troponin-I", 
                                "CPK - TOTAL", "CPK - MB", "ECG", "ECHO", "TMT"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= ecp, label_visibility='collapsed')
                    if inv == "URINE ROUTINE":
                        ur = [ "SELECT PARAMETER",
                                "Colour", "Appearance", "Reaction (pH)", "Specific Gravity", "Protein/Albumin", 
                                "Glucose (Urine)", "Ketone Bodies", "Urobilinogen", "Bile Salts", "Bile Pigments", 
                                "WBC / Pus Cells", "Red Blood Cells", "Epithelial Cells", "Casts", "Crystals", "Bacteria"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= ur, label_visibility='collapsed')
                    if inv == "SEROLOGY":
                        serology = [ "SELECT PARAMETER",
                                "Screening For HIV I & II", "HBsAg", "HCV", "WIDAL", "VDRL", "Dengue NS1Ag", "Dengue IgG", "Dengue IgM"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= serology, label_visibility='collapsed')
                    if inv == "MOTION":
                        motion = [ "SELECT PARAMETER",
                                "Colour", "Appearance", "Occult Blood", "Ova", "Cyst", "Mucus", "Pus Cells", "RBCs", "Others"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= motion, label_visibility='collapsed')
                    if inv == "ROUTINE CULTURE & SENSITIVITY TEST":
                        mens = [ "SELECT PARAMETER",
                                "PSA (Prostate Specific Antigen)"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= mens, label_visibility='collapsed')
                    if inv == "Men's Pack":
                        womens = [ "SELECT PARAMETER",
                                "Mammogram", "PAP Smear"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= womens, label_visibility='collapsed')
                    if inv == "Women's Pack":
                        rcst = [ "SELECT PARAMETER",
                                "Urine", "Motion", "Sputum", "Blood"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= rcst, label_visibility='collapsed')
                    if inv == "Occupational Profile":
                        ocp = [ "SELECT PARAMETER",
                                "Bone Densitometry", "Dental", "Pathology"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= ocp, label_visibility='collapsed')
                    if inv == "Others TEST":
                        ot = [ "SELECT PARAMETER",
                                "Bone Densitometry", "Dental", "Pathology"
                            ]
                        paropt = st.selectbox("Select Parameter:", options= ot, label_visibility='collapsed')
                    if inv == "OPHTHALMIC REPORT":
                        or1 = [ "SELECT PARAMETER",
                            "Vision", "Color Vision", "Cataract/Glaucoma"
                        ]
                        paropt = st.selectbox("Select Parameter:", options= or1, label_visibility='collapsed')
                    if inv == "X-RAY":
                        xray = [ "SELECT PARAMETER",
                            "Chest", "Spine", "Abdomen", "KUB", "Pelvis"
                        ]
                        paropt = st.selectbox("Select Parameter:", options= xray, label_visibility='collapsed')
                    if inv == "USG":
                        usg = [ "SELECT PARAMETER",
                            "Abdomen", "Pelvis", "Neck", "KUB"
                        ]
                        paropt = st.selectbox("Select Parameter:", options= usg, label_visibility='collapsed')
                    if inv == "CT":
                        ct = [ "SELECT PARAMETER",
                            "Brain", "Abdomen", "Pelvis", "Lungs", "Spine"
                        ]
                        paropt = st.selectbox("Select Parameter:", options= ct, label_visibility='collapsed')
                    if inv == "MRI":
                        mri = [ "SELECT PARAMETER",
                            "Brain", "Abdomen", "Pelvis", "Lungs", "Spine"
                        ]
                        paropt = st.selectbox("Select Parameter:", options= mri, label_visibility='collapsed')
            with rc2:
                rrc1, rrc2, rrc3 = st.columns([2,4,4])    
                with rrc1:
                    st.write("Range:")
                with rrc2:
                    fromval = st.number_input("From", label_visibility='collapsed')
                with rrc3:
                    toval = st.number_input("To", label_visibility='collapsed')
                r1c1, r1c2 = st.columns(2)
                with r1c1:
                    st.write("Reference Range: 11 - 15 (g/dl)")
                with r1c2:
                    if st.button("Submit"):
                        st.session_state.proceed = True
                        st.rerun()
            if inv == "HAEMATALOGY":
                cursor.execute(f"Select * from hematology_result")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Haemoglobin":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["heamoglobin"] = pd.to_numeric(filteredhem["heamoglobin"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["heamoglobin"] >= fromval) & (filteredhem["heamoglobin"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Red Blood Cell (RBC) Count":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["rbc_count"] = pd.to_numeric(filteredhem["rbc_count"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["rbc_count"] >= fromval) & (filteredhem["rbc_count"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt ==  "WBC Count (TC)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["wbc_count"] = pd.to_numeric(filteredhem["wbc_count"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["wbc_count"] >= fromval) & (filteredhem["wbc_count"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Haemotocrit (PCV)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["haemotocrit"] = pd.to_numeric(filteredhem["haemotocrit"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["haemotocrit"] >= fromval) & (filteredhem["haemotocrit"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "MCV":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["mcv"] = pd.to_numeric(filteredhem["mcv"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["mcv"] >= fromval) & (filteredhem["mcv"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "MCH":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["mch"] = pd.to_numeric(filteredhem["mch"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["mch"] >= fromval) & (filteredhem["mch"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False 
                if paropt == "MCHC":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["mchc"] = pd.to_numeric(filteredhem["mchc"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["mchc"] >= fromval) & (filteredhem["mchc"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Platelet Count":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["platelet"] = pd.to_numeric(filteredhem["platelet"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["platelet"] >= fromval) & (filteredhem["platelet"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "RDW (CV)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["rdw"] = pd.to_numeric(filteredhem["rdw"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["rdw"] >= fromval) & (filteredhem["rdw"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Neutrophil":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["neutrophil"] = pd.to_numeric(filteredhem["neutrophil"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["neutrophil"] >= fromval) & (filteredhem["neutrophil"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Lymphocyte":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["lymphocyte"] = pd.to_numeric(filteredhem["lymphocyte"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["lymphocyte"] >= fromval) & (filteredhem["lymphocyte"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Eosinophil":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["eosinophil"] = pd.to_numeric(filteredhem["eosinophil"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["eosinophil"] >= fromval) & (filteredhem["eosinophil"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False 
                if paropt == "Monocyte": 
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["monocyte"] = pd.to_numeric(filteredhem["monocyte"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["monocyte"] >= fromval) & (filteredhem["monocyte"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Basophils":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["basophils"] = pd.to_numeric(filteredhem["basophils"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["basophils"] >= fromval) & (filteredhem["basophils"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Erythrocyte Sedimentation Rate (ESR)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["esr"] = pd.to_numeric(filteredhem["esr"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["esr"] >= fromval) & (filteredhem["esr"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Peripheral Blood Smear - RBC Morphology":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pbs_rbc"] = pd.to_numeric(filteredhem["pbs_rbc"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pbs_rbc"] >= fromval) & (filteredhem["pbs_rbc"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Peripheral Blood Smear - Parasites":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pbc_parasites"] = pd.to_numeric(filteredhem["pbc_parasites"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pbc_parasites"] >= fromval) & (filteredhem["pbc_parasites"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Peripheral Blood Smear - Others":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pbc_others"] = pd.to_numeric(filteredhem["pbc_others"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pbc_others"] >= fromval) & (filteredhem["pbc_others"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "ROUTINE SUGAR TESTS":
                cursor.execute(f"Select * from routine_sugartest")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Glucose (F)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["glucosef"] = pd.to_numeric(filteredhem["glucosef"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["glucosef"] >= fromval) & (filteredhem["glucosef"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Glucose (PP)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["glucosepp"] = pd.to_numeric(filteredhem["glucosepp"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["glucosepp"] >= fromval) & (filteredhem["glucosepp"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Random Blood sugar":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["rbs"] = pd.to_numeric(filteredhem["rbs"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["rbs"] >= fromval) & (filteredhem["rbs"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Estimated Average Glucose":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["eag"] = pd.to_numeric(filteredhem["eag"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["eag"] >= fromval) & (filteredhem["eag"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "HbA1c":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["hba1c"] = pd.to_numeric(filteredhem["hba1c"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["hba1c"] >= fromval) & (filteredhem["hba1c"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "RENAL FUNCTION TEST & ELECTROLYTES":
                cursor.execute(f"Select * from rft_result")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Urea":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["urea"] = pd.to_numeric(filteredhem["urea"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["urea"] >= fromval) & (filteredhem["urea"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Blood urea nitrogen (BUN)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["bun"] = pd.to_numeric(filteredhem["bun"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["bun"] >= fromval) & (filteredhem["bun"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Sr.Creatinine":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["sr_creatinine"] = pd.to_numeric(filteredhem["sr_creatinine"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["sr_creatinine"] >= fromval) & (filteredhem["sr_creatinine"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Uric acid":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["uric_acid"] = pd.to_numeric(filteredhem["uric_acid"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["uric_acid"] >= fromval) & (filteredhem["uric_acid"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False 
                if paropt == "Sodium":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["sodium"] = pd.to_numeric(filteredhem["sodium"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["sodium"] >= fromval) & (filteredhem["sodium"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Potassium":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["potassium"] = pd.to_numeric(filteredhem["potassium"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["potassium"] >= fromval) & (filteredhem["potassium"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Calcium":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["calcium"] = pd.to_numeric(filteredhem["calcium"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["calcium"] >= fromval) & (filteredhem["calcium"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Phosphorus":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["phosphorus"] = pd.to_numeric(filteredhem["phosphorus"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["phosphorus"] >= fromval) & (filteredhem["phosphorus"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Chloride":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["chloride"] = pd.to_numeric(filteredhem["chloride"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["chloride"] >= fromval) & (filteredhem["chloride"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Bicarbonate":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["bicarbonate"] = pd.to_numeric(filteredhem["bicarbonate"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["bicarbonate"] >= fromval) & (filteredhem["bicarbonate"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "LIPID PROFILE":
                cursor.execute(f"Select * from lipid_profile")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Total Cholesterol":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["tcholesterol"] = pd.to_numeric(filteredhem["tcholesterol"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["tcholesterol"] >= fromval) & (filteredhem["tcholesterol"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Triglycerides":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["triglycerides"] = pd.to_numeric(filteredhem["triglycerides"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["triglycerides"] >= fromval) & (filteredhem["triglycerides"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "HDL - Cholesterol":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["hdl_cholesterol"] = pd.to_numeric(filteredhem["hdl_cholesterol"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["hdl_cholesterol"] >= fromval) & (filteredhem["hdl_cholesterol"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "VLDL -Cholesterol":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["vldl_cholesterol"] = pd.to_numeric(filteredhem["vldl_cholesterol"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["vldl_cholesterol"] >= fromval) & (filteredhem["vldl_cholesterol"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "LDL - Cholesterol":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["ldl_cholesterol"] = pd.to_numeric(filteredhem["ldl_cholesterol"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["ldl_cholesterol"] >= fromval) & (filteredhem["ldl_cholesterol"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False 
                if paropt == "CHOL:HDL ratio":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["chol_hdlratio"] = pd.to_numeric(filteredhem["chol_hdlratio"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["chol_hdlratio"] >= fromval) & (filteredhem["chol_hdlratio"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "LDL:CHOL/HDL:CHOL Ratio":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["ldlhdlratio"] = pd.to_numeric(filteredhem["ldlhdlratio"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["ldlhdlratio"] >= fromval) & (filteredhem["ldlhdlratio"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "LIVER FUNCTION TEST":
                cursor.execute(f"Select * from rft_result")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Bilirubin - Total":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["bilirubin_total"] = pd.to_numeric(filteredhem["bilirubin_total"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["bilirubin_total"] >= fromval) & (filteredhem["bilirubin_total"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Bilirubin - Direct":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["bilirubin_direct"] = pd.to_numeric(filteredhem["bilirubin_direct"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["bilirubin_direct"] >= fromval) & (filteredhem["bilirubin_direct"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Bilirubin - Indirect":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["bilirubin_indirect"] = pd.to_numeric(filteredhem["bilirubin_indirect"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["bilirubin_indirect"] >= fromval) & (filteredhem["bilirubin_indirect"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "SGOT / AST":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["sgot_alt"] = pd.to_numeric(filteredhem["sgot_alt"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["sgot_alt"] >= fromval) & (filteredhem["sgot_alt"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "SGPT / ALT":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["sgpt_alt"] = pd.to_numeric(filteredhem["sgpt_alt"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["sgpt_alt"] >= fromval) & (filteredhem["sgpt_alt"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Alkaline phosphatase":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["alkaline_phosphatase"] = pd.to_numeric(filteredhem["alkaline_phosphatase"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["alkaline_phosphatase"] >= fromval) & (filteredhem["alkaline_phosphatase"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Total Protein":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["total_protein"] = pd.to_numeric(filteredhem["total_protein"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["total_protein"] >= fromval) & (filteredhem["total_protein"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Albumin (Serum)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["albumin"] = pd.to_numeric(filteredhem["albumin"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["albumin"] >= fromval) & (filteredhem["albumin"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Globulin (Serum)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["globulin"] = pd.to_numeric(filteredhem["globulin"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["globulin"] >= fromval) & (filteredhem["globulin"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Alb/Glob Ratio":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["alb_globratio"] = pd.to_numeric(filteredhem["alb_globratio"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["alb_globratio"] >= fromval) & (filteredhem["alb_globratio"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Gamma Glutamyl Transferase":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["gammagt"] = pd.to_numeric(filteredhem["gammagt"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["gammagt"] >= fromval) & (filteredhem["gammagt"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "THYROID FUNCTION TEST":
                cursor.execute(f"Select * from thyroid_function_test")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "T3 - Triiodothyronine":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["t3"] = pd.to_numeric(filteredhem["t3"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["t3"] >= fromval) & (filteredhem["t3"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "T4 - Thyroxine":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["t4"] = pd.to_numeric(filteredhem["t4"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["t4"] >= fromval) & (filteredhem["t4"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "TSH - Thyroid Stimulating Hormone":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["tsh"] = pd.to_numeric(filteredhem["tsh"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["tsh"] >= fromval) & (filteredhem["tsh"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "AUTOIMMUNE TEST":
                cursor.execute(f"Select * from autoimmune_test")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "ANA (Antinuclear Antibody)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["ana"] = pd.to_numeric(filteredhem["ana"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["ana"] >= fromval) & (filteredhem["ana"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Anti ds DNA":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["adna"] = pd.to_numeric(filteredhem["adna"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["adna"] >= fromval) & (filteredhem["adna"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Anticardiolipin Antibodies (IgG & IgM)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["anticardiolipin"] = pd.to_numeric(filteredhem["anticardiolipin"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["anticardiolipin"] >= fromval) & (filteredhem["anticardiolipin"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Rheumatoid Factor":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["rheumatoid"] = pd.to_numeric(filteredhem["rheumatoid"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["rheumatoid"] >= fromval) & (filteredhem["rheumatoid"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "COAGULATION TEST":
                cursor.execute(f"Select * from coagulation_test")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Prothrombin Time (PT)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pt"] = pd.to_numeric(filteredhem["pt"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pt"] >= fromval) & (filteredhem["pt"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "PT INR":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["ptinr"] = pd.to_numeric(filteredhem["ptinr"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["ptinr"] >= fromval) & (filteredhem["ptinr"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Bleeding Time (BT)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["bt"] = pd.to_numeric(filteredhem["bt"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["bt"] >= fromval) & (filteredhem["bt"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Clotting Time (CT)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["ct"] = pd.to_numeric(filteredhem["ct"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["ct"] >= fromval) & (filteredhem["ct"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "ENZYMES & CARDIAC Profile":
                cursor.execute(f"Select * from rft_result")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Acid Phosphatase":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["acid_phosphatase"] = pd.to_numeric(filteredhem["acid_phosphatase"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["acid_phosphatase"] >= fromval) & (filteredhem["acid_phosphatase"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Adenosine Deaminase":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["adenosine"] = pd.to_numeric(filteredhem["adenosine"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["adenosine"] >= fromval) & (filteredhem["adenosine"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Amylase":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["amylase"] = pd.to_numeric(filteredhem["amylase"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["amylase"] >= fromval) & (filteredhem["amylase"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Lipase":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["lipase"] = pd.to_numeric(filteredhem["lipase"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["lipase"] >= fromval) & (filteredhem["lipase"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Troponin-T":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["troponin_t"] = pd.to_numeric(filteredhem["troponin_t"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["troponin_t"] >= fromval) & (filteredhem["troponin_t"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Troponin-I":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["troponin_i"] = pd.to_numeric(filteredhem["troponin_i"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["troponin_i"] >= fromval) & (filteredhem["troponin_i"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "CPK - TOTAL":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["cpk_total"] = pd.to_numeric(filteredhem["cpk_total"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["cpk_total"] >= fromval) & (filteredhem["cpk_total"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "CPK - MB":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["cpk_mb"] = pd.to_numeric(filteredhem["cpk_mb"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["cpk_mb"] >= fromval) & (filteredhem["cpk_mb"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "ECG":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["ecg"] = pd.to_numeric(filteredhem["ecg"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["ecg"] >= fromval) & (filteredhem["ecg"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "ECHO":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["echo"] = pd.to_numeric(filteredhem["echo"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["echo"] >= fromval) & (filteredhem["echo"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "TMT":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["tmt"] = pd.to_numeric(filteredhem["tmt"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["tmt"] >= fromval) & (filteredhem["tmt"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "URINE ROUTINE":
                cursor.execute(f"Select * from urine_routine")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Colour":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["colour"] = pd.to_numeric(filteredhem["colour"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["colour"] >= fromval) & (filteredhem["colour"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Appearance":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["appearance"] = pd.to_numeric(filteredhem["appearance"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["appearance"] >= fromval) & (filteredhem["appearance"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Reaction (pH)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["reaction"] = pd.to_numeric(filteredhem["reaction"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["reaction"] >= fromval) & (filteredhem["reaction"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Specific Gravity":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["specific_gravity"] = pd.to_numeric(filteredhem["specific_gravity"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["specific_gravity"] >= fromval) & (filteredhem["specific_gravity"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Protein/Albumin":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["protein_albumin"] = pd.to_numeric(filteredhem["protein_albumin"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["protein_albumin"] >= fromval) & (filteredhem["protein_albumin"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Glucose (Urine)":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["glucose"] = pd.to_numeric(filteredhem["glucose"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["glucose"] >= fromval) & (filteredhem["glucose"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Ketone Bodies":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["ketone"] = pd.to_numeric(filteredhem["ketone"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["ketone"] >= fromval) & (filteredhem["ketone"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Urobilinogen":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["urobilinogen"] = pd.to_numeric(filteredhem["urobilinogen"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["urobilinogen"] >= fromval) & (filteredhem["urobilinogen"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Bile Salts":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["bile_salts"] = pd.to_numeric(filteredhem["bile_salts"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["bile_salts"] >= fromval) & (filteredhem["bile_salts"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Bile Pigments":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["bile_pigments"] = pd.to_numeric(filteredhem["bile_pigments"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["bile_pigments"] >= fromval) & (filteredhem["bile_pigments"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "WBC / Pus Cells":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["wbc_pluscells"] = pd.to_numeric(filteredhem["wbc_pluscells"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["wbc_pluscells"] >= fromval) & (filteredhem["wbc_pluscells"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Red Blood Cells":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["rbc"] = pd.to_numeric(filteredhem["rbc"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["rbc"] >= fromval) & (filteredhem["rbc"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Epithelial Cells":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["epithelial_cell"] = pd.to_numeric(filteredhem["epithelial_cell"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["epithelial_cell"] >= fromval) & (filteredhem["epithelial_cell"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Casts":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["casts"] = pd.to_numeric(filteredhem["casts"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["casts"] >= fromval) & (filteredhem["casts"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Crystals":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["crystals"] = pd.to_numeric(filteredhem["crystals"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["crystals"] >= fromval) & (filteredhem["crystals"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Bacteria":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["bacteria"] = pd.to_numeric(filteredhem["bacteria"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["bacteria"] >= fromval) & (filteredhem["bacteria"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "SEROLOGY":
                cursor.execute(f"Select * from serology_result")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Screening For HIV I & II":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["hiv_screening"] = pd.to_numeric(filteredhem["hiv_screening"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["hiv_screening"] >= fromval) & (filteredhem["hiv_screening"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "HBsAg":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["hbsag"] = pd.to_numeric(filteredhem["hbsag"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["hbsag"] >= fromval) & (filteredhem["hbsag"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "HCV":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["hvc"] = pd.to_numeric(filteredhem["hvc"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["hvc"] >= fromval) & (filteredhem["hvc"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "WIDAL":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["widal"] = pd.to_numeric(filteredhem["widal"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["widal"] >= fromval) & (filteredhem["widal"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "VDRL":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["vdrl"] = pd.to_numeric(filteredhem["vdrl"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["vdrl"] >= fromval) & (filteredhem["vdrl"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Dengue NS1Ag":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["denguens"] = pd.to_numeric(filteredhem["denguens"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["denguens"] >= fromval) & (filteredhem["denguens"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Dengue IgG":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["dengueigg"] = pd.to_numeric(filteredhem["dengueigg"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["dengueigg"] >= fromval) & (filteredhem["dengueigg"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Dengue IgM":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["dengueigm"] = pd.to_numeric(filteredhem["dengueigm"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["dengueigm"] >= fromval) & (filteredhem["dengueigm"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "MOTION":
                cursor.execute(f"Select * from motion")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Colour":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["colour"] = pd.to_numeric(filteredhem["colour"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["colour"] >= fromval) & (filteredhem["colour"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Appearance":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["appearance"] = pd.to_numeric(filteredhem["appearance"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["appearance"] >= fromval) & (filteredhem["appearance"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Occult Blood":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["occult_blood"] = pd.to_numeric(filteredhem["occult_blood"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["occult_blood"] >= fromval) & (filteredhem["occult_blood"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Ova":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["ova"] = pd.to_numeric(filteredhem["ova"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["ova"] >= fromval) & (filteredhem["ova"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Cyst":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["cyst"] = pd.to_numeric(filteredhem["cyst"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["cyst"] >= fromval) & (filteredhem["cyst"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Mucus":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["mucus"] = pd.to_numeric(filteredhem["mucus"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["mucus"] >= fromval) & (filteredhem["mucus"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Pus Cells":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pus_cells"] = pd.to_numeric(filteredhem["pus_cells"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pus_cells"] >= fromval) & (filteredhem["pus_cells"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "RBCs":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["rbcs"] = pd.to_numeric(filteredhem["rbcs"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["rbcs"] >= fromval) & (filteredhem["rbcs"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Others":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["others_t"] = pd.to_numeric(filteredhem["others_t"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["others_t"] >= fromval) & (filteredhem["others_t"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "ROUTINE CULTURE & SENSITIVITY TEST":
                cursor.execute(f"Select * from routine_culture")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "PSA (Prostate Specific Antigen)":
                    st.warning("Parameter Not Found")
            if inv == "Men's Pack":
                cursor.execute(f"Select * from mens_pack")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Mammogram":
                    st.warning("No Parameter Found")
                if paropt == "PAP Smear":
                    st.warning("No Parameter Found")
            if inv == "Women's Pack":
                cursor.execute(f"Select * from womens_pack")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Urine":
                    st.warning("No Parameter Found")
                if paropt == "Motion":
                    st.warning("No Parameter Found")
                if paropt == "Sputum":
                    st.warning("No Parameter Found")
                if paropt == "Blood":
                    st.warning("No Parameter Found")
            if inv == "Occupational Profile":
                cursor.execute(f"Select * from occupational_profile")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Bone Densitometry":
                    st.warning("Parameter Not Found")
                if paropt == "Dental":
                    st.warning("Parameter Not Found")
                if paropt ==  "Pathology":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pathology"] = pd.to_numeric(filteredhem["pathology"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pathology"] >= fromval) & (filteredhem["pathology"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "Others TEST":
                cursor.execute(f"Select * from other_tests")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Bone Densitometry":
                    st.warning("Parameter Not Found")
                if paropt == "Dental":
                    st.warning("Parameter Not Found")
                if paropt ==  "Pathology":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pathology"] = pd.to_numeric(filteredhem["pathology"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pathology"] >= fromval) & (filteredhem["pathology"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "OPHTHALMIC REPORT":
                cursor.execute(f"Select * from rft_result")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Vision":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["vision"] = pd.to_numeric(filteredhem["vision"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["vision"] >= fromval) & (filteredhem["vision"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Color Vision":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["colorvision"] = pd.to_numeric(filteredhem["colorvision"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["colorvision"] >= fromval) & (filteredhem["colorvision"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Cataract/Glaucoma":
                    st.warning("No Parameter Found")
            if inv == "X-RAY":
                cursor.execute(f"Select * from x_ray")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Chest":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["chest"] = pd.to_numeric(filteredhem["chest"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["chest"] >= fromval) & (filteredhem["chest"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Spine":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["spine"] = pd.to_numeric(filteredhem["spine"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["spine"] >= fromval) & (filteredhem["spine"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "KUB":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["kub"] = pd.to_numeric(filteredhem["kub"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["kub"] >= fromval) & (filteredhem["kub"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Abdomen":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["abdomen"] = pd.to_numeric(filteredhem["abdomen"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["abdomen"] >= fromval) & (filteredhem["abdomen"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Pelvis":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pelvis"] = pd.to_numeric(filteredhem["pelvis"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pelvis"] >= fromval) & (filteredhem["pelvis"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "USG":
                cursor.execute(f"Select * from rft_result")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Neck":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["neck"] = pd.to_numeric(filteredhem["neck"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["neck"] >= fromval) & (filteredhem["neck"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "KUB":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["kub"] = pd.to_numeric(filteredhem["kub"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["kub"] >= fromval) & (filteredhem["kub"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Abdomen":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["abdomen"] = pd.to_numeric(filteredhem["abdomen"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["abdomen"] >= fromval) & (filteredhem["abdomen"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Pelvis":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pelvis"] = pd.to_numeric(filteredhem["pelvis"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pelvis"] >= fromval) & (filteredhem["pelvis"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "CT":
                cursor.execute(f"Select * from  ct_report")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Brain":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["brain"] = pd.to_numeric(filteredhem["brain"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["brain"] >= fromval) & (filteredhem["brain"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Abdomen":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["abdomen"] = pd.to_numeric(filteredhem["abdomen"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["abdomen"] >= fromval) & (filteredhem["abdomen"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Pelvis":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pelvis"] = pd.to_numeric(filteredhem["pelvis"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pelvis"] >= fromval) & (filteredhem["pelvis"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Lungs":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["lungs"] = pd.to_numeric(filteredhem["lungs"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["lungs"] >= fromval) & (filteredhem["lungs"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Spine":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["spine"] = pd.to_numeric(filteredhem["spine"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["spine"] >= fromval) & (filteredhem["spine"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
            if inv == "MRI":
                cursor.execute(f"Select * from mri")
                hematology_res = cursor.fetchall()
                hemcol = cursor.description
                hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                filteredhem = hemdf
                if paropt == "Brain":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["brain"] = pd.to_numeric(filteredhem["brain"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["brain"] >= fromval) & (filteredhem["brain"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Abdomen":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["abdomen"] = pd.to_numeric(filteredhem["abdomen"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["abdomen"] >= fromval) & (filteredhem["abdomen"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Pelvis":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["pelvis"] = pd.to_numeric(filteredhem["pelvis"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["pelvis"] >= fromval) & (filteredhem["pelvis"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Lungs":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["lungs"] = pd.to_numeric(filteredhem["lungs"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["lungs"] >= fromval) & (filteredhem["lungs"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
                if paropt == "Spine":
                    if(st.session_state.proceed == True):
                        # Ensure the "heamoglobin" column is numeric
                        filteredhem["spine"] = pd.to_numeric(filteredhem["spine"], errors='coerce')

                        # Now apply the range filtering
                        filteredhem = filteredhem[(filteredhem["spine"] >= fromval) & (filteredhem["spine"] <= toval)]
                        st.write(f"**Count({len(filteredhem)})**")
                        st.dataframe(filteredhem)
                        st.session_state.proceed = False
        if form_name == "All Details":
            st.write(f"**Count({st.session_state.df.emp_no.count()})**")
            st.dataframe(st.session_state.df)

        if form_name != "Recent" and form_name != "Investigations":
            with st.container():
                if form_name == "Personal & Emp Details":
                    with st.form(key="Basic Details"):
                        r1c1, r1c2, r1c3, r1c4 = st.columns([2, 2, 2, 2])
                        with r1c1:
                            age = st.number_input("Age", min_value=0)
                        with r1c2:
                            blood_group = st.multiselect("Blood Group", ["All", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
                        with r1c3:
                            desig = st.text_input("Designation")
                        with r1c4:
                            noc = st.text_input("Name of the Contractor")

                        r2c1, r2c2, r2c3, r2c4 = st.columns([2, 2, 2, 2])
                        with r2c1:
                            gender = st.selectbox("Gender", ["All", "Male", "Female"])
                        with r2c2:
                            work = st.text_input("Nature of Job")
                        with r2c3:
                            dept = st.text_input("Department:")
                        with r2c4:
                            if st.form_submit_button("Submit"):
                                # Create a dictionary to store filter data
                                st.session_state.filter_data = {
                                    "Department": dept,
                                    "Designation": desig,
                                    "Age": age,
                                    "Gender": gender,
                                    "Work": work,
                                    "Blood Group": blood_group,
                                    "Name of Contractor": noc
                                }

                    # Retrieve and filter the data
                    if "filter_data" in st.session_state:
                        fdata = st.session_state.filter_data  # Access the dictionary directly
                        filter_data = st.session_state.filtered_data
                        # Apply filters based on the form inputs
                        if fdata["Department"]:
                            filter_data = filter_data.loc[filter_data["department"].str.contains(fdata["Department"], case=False)]
                        if fdata["Designation"]:
                            filter_data = filter_data.loc[filter_data["designation"].str.contains(fdata["Designation"], case=False)]
                        if fdata["Gender"] != "All":
                            filter_data = filter_data.loc[filter_data["gender"] == fdata["Gender"]]
                        if fdata["Blood Group"] and fdata["Blood Group"] != ["All"]:
                            filter_data = filter_data.loc[filter_data["blood_group"].isin(fdata["Blood Group"])]
                        if fdata["Name of Contractor"]:
                            filter_data = filter_data.loc[filter_data["contractor"].str.contains(fdata["Name of Contractor"], case=False)]
                        if fdata["Age"] != 0:
                            filter_data = filter_data.loc[filter_data["age"] == fdata["Age"]]
                        # Display the filtered data
                        st.write(f"**Filtered Count: {len(filter_data)}**")
                        st.dataframe(filter_data)
                    
                if form_name == "Vitals":
                    with st.form(key="Vitals"):
                        st.write("Vitals")
                        r1c1, r1c2, r1c3, r1c4 = st.columns([2, 2, 2, 2])
                        with r1c1:
                            height = st.number_input("Height")
                        with r1c2:
                            weight = st.number_input("Weight")
                        with r1c3:
                            systolic = st.number_input("Systolic")
                        with r1c4:
                            diastolic = st.number_input("Diastolic")

                        r2c1, r2c2, r2c3, r2c4 = st.columns([2, 2, 2, 2], vertical_alignment="bottom")
                        with r2c1:
                            pulse = st.number_input("Pulse")
                        with r2c2:
                            temp = st.number_input("Temperature")
                        with r2c3:
                            resp = st.number_input("Respiration")
                        with r2c4:
                            bmi = st.multiselect("BMI", ["Thin", "Under Weight", "Normal", "Over Weight", "Obese"])
                        
                        if st.form_submit_button("Submit"):
                            st.session_state.filter_data = {
                                "Height": str(height),
                                "Weight": str(weight),
                                "Systolic": str(systolic),
                                "Diastolic": str(diastolic),
                                "Pulse": str(pulse),
                                "Temperature": str(temp),
                                "Respiration": str(resp),
                                "BMI": bmi
                            }

                    # Retrieve and filter the data
                    if "filter_data" in st.session_state:
                        cursor.execute(f"SELECT * FROM vitals")
                        # Fetch all rows from the query
                        vitals = cursor.fetchall()
                        vitalcol = cursor.description
                        vitaldf = pd.DataFrame(vitals, columns=[desc[0] for desc in vitalcol])
                        filtered_data = vitaldf
                        fdata = st.session_state.filter_data  # Access the dictionary directly
                        filter_data = filtered_data

                        # Apply filters using startswith for tolerance with floats and integers
                        if fdata["Height"] != "0.0":
                            filter_data = filter_data.loc[filter_data["Height"].astype(str).str.startswith(fdata["Height"].split('.')[0])]
                        if fdata["Weight"] != "0.0":
                            filter_data = filter_data.loc[filter_data["Weight"].astype(str).str.startswith(fdata["Weight"].split('.')[0])]
                        if fdata["Systolic"] != "0.0":
                            filter_data = filter_data.loc[filter_data["Systolic"].astype(str).str.startswith(fdata["Systolic"].split('.')[0])]
                        if fdata["Diastolic"] != "0.0":
                            filter_data = filter_data.loc[filter_data["Diastolic"].astype(str).str.startswith(fdata["Diastolic"].split('.')[0])]
                        if fdata["Pulse"] != "0.0":
                            filter_data = filter_data.loc[filter_data["PulseRate"].astype(str).str.startswith(fdata["Pulse"].split('.')[0])]
                        if fdata["Temperature"] != "0.0":
                            filter_data = filter_data.loc[filter_data["Temperature"].astype(str).str.startswith(fdata["Temperature"].split('.')[0])]
                        if fdata["Respiration"] != "0.0":
                            filter_data = filter_data.loc[filter_data["RespiratoryRate"].astype(str).str.startswith(fdata["Respiration"].split('.')[0])]
                        if fdata["BMI"]:
                            filter_data = filter_data.loc[filter_data["BMI"] == fdata["BMI"]]

                        # Display the filtered data
                        st.write(f"**Filtered Count: {len(filter_data)}**")
                        st.dataframe(filter_data)
                    
                if form_name == "Fitness":
                    cursor.execute("Select * from fitness")
                    hematology_res = cursor.fetchall()
                    hemcol = cursor.description
                    hemdf = pd.DataFrame(hematology_res, columns=[desc[0] for desc in hemcol])
                    filteredhem = hemdf
                    # Create a filter for the "status" column
                    r1c1, r1c2 = st.columns(2)
                    with r1c1:
                        r2c1, r2c2 = st.columns([4,6])
                        with r2c1:
                            st.write("Select Multiple:")
                        with r2c2:
                            selected_status = st.multiselect(
                                "select", 
                                ["Fit to Join", "Unfit", "Conditional Fit"], 
                                label_visibility='collapsed'
                            )
                    with r1c2:
                        if st.button("Submit"):
                            # Apply filter if any status is selected
                            if selected_status:
                                filteredhem = hemdf[hemdf['Status'].isin(selected_status)]
                            else:
                                filteredhem = hemdf  # No filter applied if nothing is selected

                    # Display the filtered dataframe
                    st.dataframe(filteredhem)

                
                if form_name == "Medical History": 
                    st.warning("Empty Dataset")

                if form_name == 'Select Purpose':
                    with st.form(key = "purpose"):
                        col1, col2 = st.columns(2)
                        with col1:
                            pov = st.text_input("Purpose of visit:")
                            hosName = st.text_input("Hospital Name:")
                            SelFor = st.text_input("Select Forms:")
                        with col2:
                            opt = option_menu(None,options=["Employee", "Contractor", "Visitor"], orientation="horizontal", icons = ['a', 'a', 'a'])
                            rc2, rc3 = st.columns(2)
                            with rc2:
                                datefrom = st.date_input("From")
                                batch = st.text_input("Batch")
                            with rc3:
                                dateto = st.date_input("To:")
                                year = st.text_input("Year")
                        if st.form_submit_button("Submit",):
                                st.session_state.filter_data = {
                                    "Purpose":pov,
                                    "hosName":hosName,
                                    "Forms":SelFor,
                                    "Type":opt,
                                    "from":datefrom,
                                    "to":dateto,
                                    "Year":year
                                }
                
        