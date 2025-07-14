

import streamlit as st
from components.cause_card import display_causes
from components.contact_form import enquiry_form
from utils.helper import load_causes

# Use emoji instead of image path to avoid file errors
st.set_page_config(page_title="CareConnect - Charity Platform", page_icon="💖", layout="wide")

st.markdown("## 💖 Welcome to CareConnect 💖")

menu = st.sidebar.radio("Navigate", ["Home", "Causes", "Donate", "Enquire", "Impact Stories"])

if menu == "Home":
    st.title("Welcome to CareConnect")
    st.markdown("Give a hand, change a life.")
    display_causes(load_causes("data/sample_causes.json"), limit=3)

elif menu == "Causes":
    st.header("Support a Cause")
    display_causes(load_causes("data/sample_causes.json"))

elif menu == "Donate":
    st.header("Donate Now")
    st.info("Select a cause and enter your details to donate.")

elif menu == "Enquire":
    st.header("Get Involved or Enquire")
    enquiry_form()

elif menu == "Impact Stories":
    st.header("Real Stories That Matter")
    st.markdown("These are stories from those you’ve helped. ❤️")
