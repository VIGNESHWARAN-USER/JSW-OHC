import streamlit as st
import os
import pandas as pd

def Events_Camps(cursor):

    if "event_form" not in st.session_state:
        st.session_state.event_form = {}

    st.header("Camps")

    with st.form(key='camp_form'):
        st.subheader("Add a new camp")

        r1c1,r1c2,r1c3 = st.columns([1,1,1])
        with r1c1:
            st.session_state.event_form['camp_name'] = st.text_input("Camp Name")
        with r1c2:
            st.session_state.event_form['start_date'] = st.date_input("Start Date")
        with r1c3:
            st.session_state.event_form['end_date'] = st.date_input("End Date")

        r2c1,r2c2,r2c3,r2c4 = st.columns([6,1,1,2])
        with r2c1:
            st.session_state.event_form['camp_details'] = st.text_area("Camp Details")
        with r2c2:
            st.markdown("<style>div.stButton>button:first-child {margin-top: 15px;}</style>", unsafe_allow_html=True)
            upcoming_button = st.form_submit_button(label='Upcoming')
        with r2c3:
            st.markdown("<style>div.stButton>button:first-child {margin-top: 5px; margin-left: 0px;}</style>", unsafe_allow_html=True)
            live_button = st.form_submit_button(label='Live')

    if upcoming_button:
        # Handle upcoming button click here
        st.write(st.session_state.event_form)

    if live_button:
        # Handle live button click here
        pass