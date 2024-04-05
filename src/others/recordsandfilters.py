import streamlit as st
import os
import pandas as p


def Records_Filters(cursor):
    st.header("Records and Filters")
    with st.container(border=1):
        st.title("Container")