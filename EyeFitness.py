import streamlit as st
import pandas as pd



st.title("Eye Examination Report")

import streamlit as st
import pandas as pd

# Define the table data
data = [
    ["", "Without Correction", "", "With Correction", ""],
    ["", "Right Eye", "Left Eye", "Right Eye", "Left Eye"],
    ["Distance", "6/6", "6/6", "6/6", "6/6"],
    ["Near", "N6", "N6", "N6", "N6"]
]

# Convert to a DataFrame
table_df = pd.DataFrame(data)

# Convert the DataFrame to HTML without the index and header
table_html = table_df.to_html(index=False, header=False, border=0, escape=False)

# Display the Vision section
st.subheader("Vision")

# Apply custom styling and render the HTML table
st.write(f"""
<style>
    table {{
        margin: auto;
        border-collapse: collapse;
    }}
    td {{
        border: 1px solid black;
        padding: 8px;
        text-align: center;
    }}
</style>
{table_html}
""", unsafe_allow_html=True)


# Anterior Segment Section
st.subheader("Anterior Segment")
st.text_area("Details:", "", height=100, key="anterior_segment")

# Fundus Section
st.subheader("FUNDUS")
st.text_area("Details:", "", height=100, key="fundus")

# Colour Vision Section
st.subheader("COLOUR VISION")
st.text_area("Details:", "", height=100, key="colour_vision")

# Advice Section
st.subheader("ADVICE")
st.text_area("Details:", "", height=100, key="advice",max_chars=50)

# Ophthalmologist Name
st.subheader("NAME OF THE OPHTHALMOLOGIST")
st.text_input("Enter Name:", key="ophthalmologist_name")

# Eye Examination Result
st.subheader("EYE EXAMINATION RESULT BY OPHTHALMOLOGIST")
options = [
    "Fit",
    "Fit with newly prescribed glass",
    "Fit with existing glass",
    "Fit with an advice to change existing glass with newly prescribed glass",
    "Unfit"
]
for option in options:
    st.checkbox(option, key=f"result_{option}")