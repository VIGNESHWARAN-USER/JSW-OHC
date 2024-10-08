from pickle import FALSE
import streamlit as st
import os
import pandas as p

if "success" not in st.session_state:
    st.session_state.success = False

def Mock_Drill(connection, cursor):
    st.title("Mock Drill")
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
    # create a session state for mock drill
    if "mockdrill" not in st.session_state:
        st.session_state.mockdrill = {}

    if not isinstance(st.session_state.mockdrill, dict):
        st.session_state.mockdrill = {}

    with st.container(border=1, height=750):
        r1c1, r1c2 = st.columns(2)
        with r1c1:
            date = st.date_input("Date")
            st.session_state.mockdrill["Date"] = date.strftime("%Y-%m-%d")
        with r1c2:
            time = st.time_input("Time")
            st.session_state.mockdrill["Time"] = time.strftime("%H:%M:%S")
        r2c1,r2c2,r2c3,r2c4 = st.columns(4)
        with r2c1:
            st.session_state.mockdrill["Department"] = st.text_input("Department")
        with r2c2:
            st.session_state.mockdrill["Location"] = st.text_input("Location")
        with r2c3:
            st.session_state.mockdrill["Scenario"] = st.text_input("Scenario")
        with r2c4:
            st.session_state.mockdrill["Call Recived"] =st.time_input("Call Recived")
        st.subheader("Ambulance Timing :")
        r3c1,r3c2 = st.columns(2)
        with r3c1:
            st.session_state.mockdrill["Depature from OHC"] = st.time_input("Depature from OHC")
        with r3c2:
            st.session_state.mockdrill["Reeturn to OHC"] = st.time_input("Return to OHC")
        st.subheader("Victim Details :")
        r4c1,r4c2,r4c3,r4c4 = st.columns(4)
        with r4c1:
            st.session_state.mockdrill["EmpID"] = st.text_input("Emp ID")
            st.session_state.mockdrill["Victim Department"] = st.text_input("Victim Department")
        with r4c2:
            st.session_state.mockdrill["Victim Name"] = st.text_input("Victim Name")
            st.session_state.mockdrill["Nature of Job"] = st.text_input("Nature of Job")
        with r4c3:
            st.session_state.mockdrill["Age"] = st.number_input("Age",step=1)
            st.session_state.mockdrill["Mobile No."] = st.text_input("Mobile No.")
        with r4c4:
            st.session_state.mockdrill["Gender"] = st.text_input("Gender")
        
        st.session_state.mockdrill["Vitals"] = st.text_area("Vitals", height=1)
        st.session_state.mockdrill["Complaints"] = st.text_area("Complaints", height=1)
        st.session_state.mockdrill["Treatment"] = st.text_area("Treatment", height=1)
        st.session_state.mockdrill["Referal"] = st.text_input("Referal")

        st.subheader("Ambulance :")
        r5c1,r5c2 = st.columns(2)
        with r5c1:
            st.session_state.mockdrill["Ambulance Driver"] = st.text_input("Ambulance Driver")
        with r5c2:
            st.session_state.mockdrill["Staff Name"] = st.text_input("Staff Name")

        st.subheader("OHC :")
        r6c1,r6c2 = st.columns(2)
        with r6c1:
            st.session_state.mockdrill["OHC Doctor"] = st.text_input("OHC Doctor")
        with r6c2:
            st.session_state.mockdrill["Staff Nurse"] = st.text_input("Staff Nurse")
        
        st.subheader("OHC Observation/Action/Follow up")
        st.session_state.mockdrill["Observation"] = st.text_area("Observation")
        st.session_state.mockdrill["Action / Completion"] = st.text_area("Action / Completion")
        st.session_state.mockdrill["Responsible"] = st.text_area("Responsible")

    c1, c2 = st.columns([6,1])
    with c1:
        if st.session_state.success:
            st.success("Data Inserted") 
    with c2:
        if st.session_state.success:
            if st.button("Continue", type = "primary"):
                st.session_state.success = False
                st.rerun()
        if not st.session_state.success:
            if st.button("Submit", type="primary"):
                i = st.session_state.mockdrill
                mockdrillinsert = ("INSERT INTO mockdrill( Date, Time, Department, Location, "
                "Scenario, Call_Received, Departure_from_OHC, Return_to_OHC,"
                " Victim_name, Age, Sex, Emp_No,"
                " Victim_Department, Job_nature, Phone_No, Vitals,"
                " Complaints, Treatment, Referral, Amb_Driver,"
                " Amb_Staff_Nurse, Doctor, Staff_Nurse, Observation,"
                " Action_completion, Responsible) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)") 
            
                mockdrill_values = (i["Date"], i["Time"], i["Department"], i["Location"], 
                i["Scenario"], i["Call Recived"], i["Depature from OHC"], i["Reeturn to OHC"],
                i["Victim Name"], i["Age"], i["Gender"], i["EmpID"],
                i["Victim Department"], i["Nature of Job"], i["Mobile No."], i["Vitals"], 
                i["Complaints"], i["Treatment"], i["Referal"], i["Ambulance Driver"],
                i["Staff Name"], i["OHC Doctor"], i["Staff Nurse"], i["Observation"],
                    i["Action / Completion"], i["Responsible"])
                cursor.execute(mockdrillinsert, mockdrill_values)
                connection.commit()
                st.session_state.success = True
                st.rerun()
      