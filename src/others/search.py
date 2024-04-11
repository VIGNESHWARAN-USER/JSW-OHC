import streamlit as st
import os
import pandas as pd
from streamlit_modal import Modal
from streamlit_option_menu import option_menu


def show_data(emp):
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
        st.title("Employee Profile")
        with st.container(border=1):
            with st.container(border=1):
                r1c1,r1c2 = st.columns([4,6])
                with r1c1:
                    st.write(f"Employee ID: {st.session_state.usr_prof['emp_no']}")
                    st.write(f"Name: {st.session_state.usr_prof['name']}")
                    st.write(f"DOB: {st.session_state.usr_prof['dob']}")
            
            with st.container(border=1):
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
                        with st.container(border=1):
                            st.title("Personal Details")
                            st.write(f"**Employee ID**: {st.session_state.usr_prof['emp_no']}")
                            st.write(f"**Name**: {st.session_state.usr_prof['name']}")
                            st.write(f"**DOB**: {st.session_state.usr_prof['dob']}")
                            st.write(f"**Age**: {st.session_state.usr_prof['age']}")
                            st.write(f"**Gender**: {st.session_state.usr_prof['gender']}")
                            st.write(f"**Height**: {st.session_state.usr_prof['height']}")
                            st.write(f"**Weight**: {st.session_state.usr_prof['weight']}")
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



                
        st.write(st.session_state.usr_prof)
        if st.button("close"):
            st.session_state.open_modal = False
            st.rerun()
