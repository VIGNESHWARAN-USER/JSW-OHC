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
            inv_form = ["HAEMATALOGY","ROUTINE SUGAR TESTS","RENAL FUNCTION TEST & ELECTROLYTES","LIPID PROFILE","LIVER FUNCTION TEST","THYROID FUNCTION TEST","AUTOIMMUNE TEST","COAGULATION TEST","ENZYMES & CARDIAC Profile","URINE ROUTINE","SEROLOGY","MOTION","ROUTINE CULTURE & SENSITIVITY TEST","Men's Pack","Women's Pack","Occupational Profile","Others TEST","OPHTHALMIC REPORT","X-RAY","USG","CT","MRI"]

            r0c1,r0c2= st.columns([2,8])

            inv = st.selectbox(
                "Select the type of investigation you want to view",
                inv_form,
            )
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
                        if fdata["Age"] != "0":
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
                    st.write("Fitness")
                
                if form_name == "Medical History": 
                    st.write("Medical History")
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
                
        