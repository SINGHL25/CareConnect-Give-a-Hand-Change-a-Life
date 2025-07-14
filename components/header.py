import streamlit as st

def show_header(title="CareConnect", subtitle="Give a hand, change a life"):
    st.markdown(f"""
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <h2 style="color:#4B0082;">{title}</h2>
            <h4 style="color:#666;">{subtitle}</h4>
        </div>
        <hr>
    """, unsafe_allow_html=True)

