import streamlit as st
def Events_Camps(cursor):

    if "event_form" not in st.session_state:
        st.session_state.event_form = {}

    st.header("Camps")
    st.subheader("Add a new camp")
    with st.container(border=1, height=400):
        r1c1,r1c2,r1c3 = st.columns([1,1,1])
        with r1c1:
            st.session_state.event_form['camp_name'] = st.text_input("Camp Name")
        with r1c2:
            st.session_state.event_form['start_date'] = st.date_input("Start Date")
        with r1c3:
            st.session_state.event_form['end_date'] = st.date_input("End Date")

        r2c1,r2c2,r2c3,r2c4 = st.columns([6,2,1,2])
        with r2c1:
            st.session_state.event_form['camp_details'] = st.text_area("Camp Details")
        with r2c2:
            update = st.selectbox("Select", options=["Previous","Live", "Upcoming" ])
        with r2c3:
            st.write("\n")
            st.write('\n')
            if st.button("Submit"):
                cursor.execute("""
                    INSERT INTO camps (CampName, StartDate, EndDate, Details, UpdateAs) 
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    st.session_state.event_form['camp_name'], 
                    st.session_state.event_form['start_date'], 
                    st.session_state.event_form['end_date'], 
                    st.session_state.event_form['camp_details'], 
                    update
                ))
                cursor._connection.commit()
                print("Submitted")
            