import streamlit as st

def enquiry_form():
    with st.form("enquiry_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Your Message or Query")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thanks! We'll get back to you shortly.")

