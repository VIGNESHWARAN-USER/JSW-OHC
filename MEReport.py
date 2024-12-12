import streamlit as st
st.set_page_config(page_title="JSW", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
<style>
    .block-container{
        padding-top:10px;
        padding-bottom:10px;
        padding-left:20px;
    }
MainMenu, header, footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
st.markdown("<p style = 'fontSize: 24px; marginTop: 20px; marginLeft: 100px'><b>MEDICAL EXAMINATION REPORT (Canteen Workers)</u><p>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    r1c1, r1c2 = st.columns([4,6])
    with r1c1:
        st.write("General Examination")
        st.write("\n")
        st.write("Contagious Diseases")
        st.write("\n")
        st.write("Skin & Scalp")
        st.write("\n")
        st.write("Ears")
        st.write("\n")
        st.write("Oral Cavity")
        st.write("\n")
        st.write("Fingers")
        st.write("\n")
        st.write("Trunk")
        st.write("\n")
    with r1c2:
        st.text_input("input data", label_visibility='collapsed', key="general")
        st.text_input("input data", label_visibility='collapsed', key="contagious")
        st.text_input("input data", label_visibility='collapsed', key="skin")
        st.text_input("input data", label_visibility='collapsed', key="ears")
        st.text_input("input data", label_visibility='collapsed', key="oral")
        st.text_input("input data", label_visibility='collapsed', key="finger")
        st.text_input("input data", label_visibility='collapsed', key="trunk")
with col2:
    r1c1, r1c2 = st.columns([4,6])
    with r1c1:
        st.write("Ul/LL")
        st.write("\n")
        st.write("CVS")
        st.write("\n")
        st.write("RS")
        st.write("\n")
        st.write("Abdomen")
        st.write("\n")
        st.write("CNS")
        st.write("\n")
        st.write("Others")
        st.write("\n")
        st.write("General Hygiene")
    with r1c2:
        st.text_input("input data", label_visibility='collapsed', key="ul/ll")
        st.text_input("input data", label_visibility='collapsed', key="cvs")
        st.text_input("input data", label_visibility='collapsed', key="rs")
        st.text_input("input data", label_visibility='collapsed', key="abdomen")
        st.text_input("input data", label_visibility='collapsed', key="cns")
        st.text_input("input data", label_visibility='collapsed', key="others")
        st.text_input("input data", label_visibility='collapsed', key="hygiene")