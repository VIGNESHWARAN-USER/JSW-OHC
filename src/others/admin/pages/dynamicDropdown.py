import streamlit as st
from streamlit_option_menu import option_menu
if "temp" not in st.session_state:
    st.session_state.temp = {
        "vaccine":["Covid", "Radiesse"],
        "Employer":["JSW Cement", "JSW Steel"],
        "Contractor":["A", "B"],
        "Nature of Job": ["Height Works", "Fire Works"],
        "Department": ["OHC", "IT", "HR"],
    }
def addNewDropDown(opt):
    rc1, rc2 = st.columns(2)
    with rc1:
        col1, col2 = st.columns([6,4])
        with col1:
            st.write(opt)
            temp_opt = st.text_input("Enter the name of the option:")
        with col2:
            if st.button("Submit", type="primary"):
                st.write(temp_opt)
                if opt == 'Vaccine':
                    st.session_state.temp['vaccine'].append(temp_opt)
                elif opt == 'Employer':
                    st.session_state.temp['Employer'].append(temp_opt)
                elif opt == 'Contractor':
                    st.session_state.temp['Contractor'].append(temp_opt)
                elif opt == 'Nature of Job':
                    st.session_state.temp['Nature of Job'].append(temp_opt)
                elif opt == 'Department':
                    st.session_state.temp['Department'].append(temp_opt)
def dynamicDropdown(connection,cursor):
    st.header("Dynamic Dropdown")
    with st.container(border=1):
        st.write("Select the dropdown for the modification")
        opt = option_menu(None, ["Vaccine","Employer", "Contractor", "Nature of Job", "Deptartment"], icons=['a','a','a','a','a'], orientation='horizontal')
        st.subheader(opt)
        with st.container(border=1):
            st.write("Existing dropdown options:")
            j=1
            if opt == 'Vaccine':
                for i in st.session_state.temp["vaccine"]:
                    st.write(f'{j}. {i}')
                    j+=1
            elif opt == 'Employer':
                for i in st.session_state.temp["Employer"]:
                    st.write(f'{j}. {i}')
                    j+=1
            elif opt == 'Contractor':
                for i in st.session_state.temp["Contractor"]:
                    st.write(f'{j}. {i}')
                    j+=1
            
            elif opt == 'Nature of Job':
                for i in st.session_state.temp["Nature of Job"]:
                    st.write(f'{j}. {i}')
                    j+=1
            
            elif opt == 'Department':
                for i in st.session_state.temp["Department"]:
                    st.write(f'{j}. {i}')
                    j+=1
            if st.button("Add new dropdown option", type='primary'):
                addNewDropDown(opt)