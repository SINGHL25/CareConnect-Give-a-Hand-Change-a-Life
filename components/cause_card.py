import streamlit as st

def display_causes(causes, limit=None):
    count = 0
    for cause in causes:
        if limit and count >= limit:
            break

        st.markdown("---")
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(cause["image"], use_column_width=True)
        with cols[1]:
            st.subheader(cause["title"])
            st.write(cause["description"])
            st.caption(f"Category: {cause['category']}")
            if st.button(f"Donate to '{cause['title']}'", key=cause["title"]):
                st.success("Redirecting to donation page... (to be implemented)")

        count += 1

