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
    st.markdown("<p style = 'fontSize: 21px; marginTop: 30px; marginLeft: 120px'><b><u>TEMPORARY MEDICAL FITNESS CERTIFICATE</u></b><p>", unsafe_allow_html=True)
with r1c3:
    st.image('./src/assets/logo.png' ,width=150)
    st.write("Date: ")
st.markdown("""
<p>I Dr ______________ Factory medical officer, JSW steel Ltd Salem works,<br/>certify that Mr ______________ S/O____________________ BOD/AGE _________________ married/unmarried from ________________ Dept, Narute of work _________________ contract is physically <b>fit / unfit</b> for the job.</p><br/>
<p><b>This F.C valid for Three Months only from the date of issue</b></p>
<p>BP &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</p>
<p>PR &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</p>
<p>RR &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</p>
<p>SPO2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</p>
<p>TEM &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</p>
<p>WEIGHT &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</p>
<p><b>H/O ANY MEDICAL & SURGICAL &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p><b>H/O FEVER,COLD,COUGH &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p><b>H/O TRAVEL &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p><b>COVID VACCINATION &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p><b>EGG ATTACHED &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p><b>RANDOM BLOOD SUGAR &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p><b>AADHAR CARD NUMBER &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p><b>MOBILE NUMBER &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p><b>BLOOD GROUP REPORT &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p><b>COVID 19 REPORT ATTACHED &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p><b><span>EYE CHECK UP REPORT<br/>(CRANE, OPR, DVR)</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<div style = 'display: flex;'>
<p><b>OHC STAFF SIGNATURE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
<p style = 'marginLeft: 200px'><b>INDIVIDUAL SIGNATURE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></p>
</div>
""", unsafe_allow_html=True)