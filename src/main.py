import streamlit as st 
import os 
import mysql.connector
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image
import base64
import io
from others.search import Search
from others.dashboard import Dashboard
from others.newvisit import New_Visit
from others.eventsandcamps import Events_Camps
from others.recordsandfilters import Records_Filters
from others.mockdrill import Mock_Drill
from others.appointment import Appointment

icon = Image.open("./src/assets/favicon.png")

st.set_page_config(page_title="JSW", page_icon=icon, layout="wide", initial_sidebar_state="expanded")


#MainMenu, header, footer {visibility: hidden;}

st.markdown("""
<style>
    .block-container{
        padding-top:10px;
        padding-bottom:10px;
        padding-left:20px;
    }
</style>
""",unsafe_allow_html=True)
# mysql connection from env

load_dotenv()
MYSQL_HOST = os.getenv("DB_HOST")
MYSQL_USER = os.getenv("DB_USER")
MYSQL_PASSWORD = os.getenv("DB_PASSWORD")
MYSQL_DATABASE = os.getenv("DB_NAME")
MYSQL_PORT = os.getenv("DB_PORT")

# create a connection
# create a session state

if "connection" not in st.session_state:
    st.session_state.connection =  mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        port=MYSQL_PORT
    )

if st.session_state.connection.is_connected():
    # console log it
    print("Connected to MySQL Server")
else:
    print("Connection failed")

if "accessLevel" not in st.session_state:
    st.session_state.accessLevel = None

cursor = st.session_state.connection.cursor()

if "login" not in st.session_state:
    st.session_state.login = False

def Login():
    Login1, Login2 = st.columns([1,1])
    with Login1:
        
        bg = Image.open("./src/assets/login-left.png")
        buffered = io.BytesIO()
        bg.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.write("<img src='data:image/png;base64,{}' style='width: 1000px;position: absolute; margin-left:-100px;margin-top:-100px'>".format(img_str), unsafe_allow_html=True)
        logo = Image.open("./src/assets/logo.png")
        st.write("<div style='text-align: center;margin-top:530px; color: #333;'></div>", unsafe_allow_html=True)
        Login11,Login12,Login13 = st.columns([1,2,1])
        with Login12:
            st.image(logo, width=400)
    with Login2:
        l1,l2,l3 = st.columns([1,2,1])
        with l2:
            st.write("<h1 style='text-align: center;margin-top:160px; color: #333;'>Login</h1>", unsafe_allow_html=True)
            st.write("""
                    <div style='width:100px;height:20px'></div>
                    <p style='color:#333; text-align: center;font-size:20px'>Welcome to JSW OHC</p>
                    <div style='width:100px;height:50px'></div>
                """, unsafe_allow_html=True)
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            # Login with mysql server
            st.markdown("""
                <style>
                    button[kind="primary"] {
                        all: unset;
                        background-color: #22384F;
                        color: white;
                        border-radius: 5px;
                        text-align: center;
                        cursor: pointer;
                        font-size: 20px;
                        width: 95%;
                        padding: 10px ;
                    }
                    [data-testid="stHeader"]{
                        background-color: transparent;
                    }
                </style>""", unsafe_allow_html=True)
            if st.button("Login", type="primary"):
                cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
                result = cursor.fetchall()
                if result:
                    st.session_state.accessLevel =  result[0][2]
                    st.write("Login Success")
                    st.session_state.login = True
                    st.rerun()
                if username == "" or password == "":
                    st.warning("Please enter username and password")
                else:
                    st.error("Username and password are incorrect")

if __name__ == "__main__":
    # if not login show login page else show dashboard
    if not st.session_state.login:
        Login()
    else:
        if st.session_state.accessLevel == "admin":
            st.subheader("Welcome Admin")
        
        if st.session_state.accessLevel == "doctor":
            with st.sidebar:
                selected = option_menu("JSW OHC", ['Search',"Dashboard", 'New Visit', 'Events & Camps', 'Records & Filters','Mock Drills', 'Appointments'], 
                    icons=['search', 'house','gear', 'calendar', 'filter', 'shield', 'calendar-check'],
                    menu_icon="building-fill-add", 
                    default_index=1)
                
                st.divider()

                st.header(f"Login as {st.session_state.accessLevel.capitalize()}")

                st.divider()
                if st.button("Logout"):
                    st.session_state.login = False
                    st.write("Logout Success")
                    st.rerun()
            
            if selected == "Dashboard":
                Dashboard(cursor, "doctor")
            
            if selected == "New Visit":
                New_Visit(cursor)

            if selected == "Search":
                Search(cursor)

            if selected == "Events & Camps":
                Events_Camps(cursor)

            if selected == "Records & Filters":
                Records_Filters(cursor)
            
            if selected == "Mock Drills":
                Mock_Drill(cursor)
            
            if selected == "Appointments":
                Appointment(st.session_state.connection, st.session_state.accessLevel)
        
        if st.session_state.accessLevel == "nurse":
            with st.sidebar:
                selected = option_menu("JSW OHC", ['Search',"Dashboard", 'New Visit', 'Events & Camps', 'Records & Filters','Mock Drills', 'Appointments'], 
                    icons=['search', 'house','gear', 'calendar', 'filter', 'shield', 'calendar-check'],
                    menu_icon="building-fill-add", 
                    default_index=1)
                
                st.divider()

                st.header(f"Login as {st.session_state.accessLevel.capitalize()}")

                st.divider()
                if st.button("Logout"):
                    st.session_state.login = False
                    st.write("Logout Success")
                    st.rerun()
            
            if selected == "Dashboard":
                Dashboard(cursor, "nurse")
            
            if selected == "New Visit":
                New_Visit(cursor)

            if selected == "Search":
                Search(cursor)

            if selected == "Events & Camps":
                Events_Camps(cursor)

            if selected == "Records & Filters":
                Records_Filters(cursor)
            
            if selected == "Mock Drills":
                Mock_Drill(cursor)
            
            if selected == "Appointments":
                Appointment(st.session_state.connection, st.session_state.accessLevel)

