import streamlit as st
st.markdown("""
<style>
    .block-container{
        border: black 2px solid;
        padding-top:10px;
        padding-bottom:10px;
        padding-left:25px;
        padding-right:25px;
    }
MainMenu, header, footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
r1c2, r1c3 = st.columns([8,2])
with r1c2:
    st.markdown("<p style = 'fontSize: 17px; marginTop: 30px; marginLeft: 120px'><b><u> RENEWAL FITNESS FOR HEIGHT/ CONFINED  SPACE WORK</u></b><p>", unsafe_allow_html=True)
with r1c3:
    st.image('./src/assets/logo.png' ,width=150)
    st.markdown("<b>Date: </b>", unsafe_allow_html=True)
    st.markdown("<b>EMP/CONT: </b>", unsafe_allow_html=True)
r2c1, r2c2, r2c3 = st.columns([4,4,2])
with r2c1:
    st.markdown("<b>NAME: </b>", unsafe_allow_html=True)
    st.markdown("<b>NATURE OF WORK: </b>", unsafe_allow_html=True)
with r2c2:
    st.markdown("<b>AGE: </b>", unsafe_allow_html=True)
with r2c3:
    st.markdown("<b>DEPT: </b>", unsafe_allow_html=True)
r3c1, r3c2 = st.columns([4,6])
with r3c1:
    st.markdown("<b>BP: </b>", unsafe_allow_html=True)
    st.markdown("<b>PR: </b>", unsafe_allow_html=True)
    st.markdown("<b>RR: </b>", unsafe_allow_html=True)
    st.markdown("<b>SPO2: </b>", unsafe_allow_html=True)
    st.markdown("<b>TEMP: </b>", unsafe_allow_html=True)
    st.markdown("<b>HEIGHT WORK FITNESS&nbsp;&nbsp;-----> </b>", unsafe_allow_html=True)
    st.markdown("<b><span>CONFINED SPACE WORK <br>FITNESS</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-----> </b>", unsafe_allow_html=True)
    st.markdown("<br/>",unsafe_allow_html=True)
    st.markdown("<b style = 'border: 2px solid black; padding: 10px;'>AADHAAR NO: xxxx xxxx xxxx</b>", unsafe_allow_html=True)
    st.markdown("<br/>",unsafe_allow_html=True)
    st.markdown("<b>H/O SURGICAL / MEDICAL: </b>", unsafe_allow_html=True)
    st.markdown("<b>H/O FEVER, COLD, COUGH: </b>", unsafe_allow_html=True)
    st.markdown("<b>H/O TRAVEL: </b>", unsafe_allow_html=True)
    st.markdown("<b>COVID VACCINATION: </b>", unsafe_allow_html=True)
    st.markdown("<b>INDIVIDUAL SIGNATURE: </b>", unsafe_allow_html=True)
    st.markdown("<b>OHC STAFF SIGNATURE: </b>", unsafe_allow_html=True)
with r3c2:
    st.markdown("<b>TREMORS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-----> </b>", unsafe_allow_html=True)
    st.markdown("<b>ROBERG TEST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-----> </b>", unsafe_allow_html=True)
    st.markdown("<b>TRENDELEN BERG TEST&nbsp;&nbsp;-----> </b>", unsafe_allow_html=True)
r4c1, r4c2 = st.columns(2)
with r4c2:
    st.markdown("<br/>",unsafe_allow_html=True)
    st.markdown("<br/>",unsafe_allow_html=True)
    st.markdown("<br/>",unsafe_allow_html=True)
    st.markdown("<b>DOCTOR SIGNATURE WITH SEAL</b>", unsafe_allow_html=True)