import streamlit as st

# Title for the page
st.title("Alcohol Examination Form")

# Dropdown for Alcohol breath smell
alcohol_breath_smell = st.selectbox("Alcohol breath smell", ["Present", "Absent"])

# Dropdown for Speech
speech = st.selectbox("Speech", ["Normal", "Abnormal"])

# Dropdown for Dryness of Lips
dryness_of_lips = st.selectbox("Dryness of Lips", ["Present", "Absent"])

# Text box for CNS
cns = st.text_input("CNS", placeholder="Enter CNS details")

# Dropdown for Hand tremors
hand_tremors = st.selectbox("Hand tremors", ["Negative", "Positive"])

# Range slider for Alcoholic breath analyzer study
alcohol_breath_analyzer = st.text_input("Alcoholic breath analyzer study (mg/ml)")

# Text area for Remarks
remarks = st.text_area("Remarks", placeholder="Enter any additional comments or observations")

# Button to submit the form
if st.button("Submit"):
    st.write("### Submitted Details:")
    st.write(f"- **Alcohol breath smell:** {alcohol_breath_smell}")
    st.write(f"- **Speech:** {speech}")
    st.write(f"- **Dryness of Lips:** {dryness_of_lips}")
    st.write(f"- **CNS:** {cns}")
    st.write(f"- **Hand tremors:** {hand_tremors}")
    st.write(f"- **Alcoholic breath analyzer study (mg/ml):** {alcohol_breath_analyzer}")
    st.write(f"- **Remarks:** {remarks}")
