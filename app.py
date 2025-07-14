import streamlit as st

st.set_page_config(page_title="CareConnect", page_icon="💖", layout="wide")

# ✅ Either show emoji with markdown
st.markdown("## 💖 Welcome to CareConnect 💖")

# ✅ OR load image from URL
# st.image("https://upload.wikimedia.org/wikipedia/commons/5/5e/Charity_icon.svg", width=100)

st.sidebar.title("Navigation")
menu = st.sidebar.radio("Navigate", ["Home", "Donate"])

if menu == "Home":
    st.header("Home")
    st.write("Welcome to our charity platform.")

elif menu == "Donate":
    st.header("Donate")
    st.write("Support a cause you care about.")

