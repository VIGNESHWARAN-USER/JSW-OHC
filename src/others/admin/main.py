import streamlit as st 
from others.admin.pages.dashboard import dashboard
from others.admin.pages.addDoctor import addDoctor
from others.admin.pages.addNurse import addNurse
from others.admin.pages.addReferenceRange import addReferenceRange
from streamlit_option_menu import option_menu

def Admin():
    st.title("Admin Page")
    with st.sidebar:
        form = option_menu(
            "JSW-OHC Admin",
            ["Dashboard", "Add Doctor", "Add Nurse", "Add Reference Range"],
            menu_icon='a',
            icons=['a', 'b', 'c', 'd']
        )

    if form == "Dashboard":
        dashboard()
    elif form == "Add Doctor":
        addDoctor()
    elif form == "Add Nurse":
        addNurse()
    elif form == "Add Reference Range":
        addReferenceRange()