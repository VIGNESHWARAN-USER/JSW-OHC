import streamlit as st
import os
import pandas as p
from  streamlit_option_menu import option_menu

def get_data(cursor, table_name, filters=None,inv = None):
    # Execute the first query
    if "col" not in st.session_state:
        st.session_state.col = []

    if "filter_data" not in st.session_state:
        st.session_state.filter_data = {}

    if table_name == "Investigations":
        table_name = inv
    cursor.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows from the query
    st.session_state.data = cursor.fetchall()
    st.session_state.col = cursor.description
    st.session_state.df = p.DataFrame(st.session_state.data, columns=[desc[0] for desc in st.session_state.col])
    # apply the condition in the filter and return

    if filters:
        for key,value in filters.items():
            return st.session_state.df[st.session_state.df[key] == value]
    return st.session_state.df

def Records_Filters(cursor):
    st.header("Records and Filters")
    
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

        r0c1,r0c2= st.columns([6,2])
        with r0c1:
            form_name = option_menu(
                None,
                ["Recent","General","Basic Details","Vitals","Investigations","Fitness","Medical History"],
                orientation="horizontal",
                icons=['a','a','a','a','a','a','a']
            )
        
        
            if form_name == "Investigations":
                inv_form = ["HAEMATALOGY","ROUTINE SUGAR TESTS","RENAL FUNCTION TEST & ELECTROLYTES","LIPID PROFILE","LIVER FUNCTION TEST","THYROID FUNCTION TEST","AUTOIMMUNE TEST","COAGULATION TEST","ENZYMES & CARDIAC Profile","URINE ROUTINE","SEROLOGY","MOTION","ROUTINE CULTURE & SENSITIVITY TEST","Men's Pack","Women's Pack","Occupational Profile","Others TEST","OPHTHALMIC REPORT","X-RAY","USG","CT","MRI"]

                r0c1,r0c2= st.columns([2,8])

                inv = st.selectbox(
                    "Select the type of investigation you want to view",
                    inv_form,
                )

        if form_name != "Recent" and form_name != "Investigations":
            with st.container(height=250):
                if form_name == "General":
                    r0c1,r0c2,r0c3= st.columns([2,2,4])
                    with r0c1:
                        start_date = st.date_input('Select a start date')
                        start_date_str = start_date.strftime('%Y-%m-%d')
                    with r0c2:
                        end_date = st.date_input('Select an end date')
                        end_date_str = end_date.strftime('%Y-%m-%d')
                    
                    
                
                if form_name == "Basic Details":
                    with st.form(key="Basic Details"):
                        r1c1,r1c2,r1c3,r1c4 = st.columns([2,2,2,2])
                        with r1c1:
                            vaccination = st.selectbox("Vaccination",["Yes","No"])
                        with r1c2:
                            dept = st.text_input("Department")
                        with r1c3:
                            desig = st.text_input("Designation")
                        with r1c4:
                            age = st.number_input("Age",min_value=0)
                        
                        r2c1,r2c2,r2c3,r2c4 = st.columns([2,2,2,2],vertical_alignment="bottom")
                        with r2c1:
                            gender = st.selectbox("Gender",["All","Male", "Female"])

                        with r2c2:
                            work = st.text_input("Work")
                        with r2c3:
                            blood_group = st.multiselect("Blood Group",["All","A+","A-","B+","B-","AB+","AB-","O+","O-"])
                        with r2c4:
                            if st.form_submit_button("Submit",):
                                st.session_state.filter_data = {
                                    "Department":dept,
                                    "Designation":desig,
                                    "Age":age,
                                    "Gender": gender,
                                    "Work":work,
                                    "Blood Group":blood_group,
                                    "Vaccination":vaccination
                                }
                if st.session_state.filter_data:
                    st.write(st.session_state.filter_data)

                if form_name == "Vitals":
                    st.write("Vitals")
                
                if form_name == "Fitness":
                    st.write("Fitness")
                
                if form_name == "Medical History": 
                    st.write("Medical History")
        
        form_to_table = {
            "Recent":"Employee_det",
            "General":"Employee_det",
            "Basic Details":"Employee_det",
            "Vitals":"vitals",
            "Investigations":"Employee_det",
            "Fitness":"fitness",
            "Medical History":"medicalpersonalhist"
        }
        

        st.write(get_data(cursor=cursor, table_name=form_to_table[form_name]))