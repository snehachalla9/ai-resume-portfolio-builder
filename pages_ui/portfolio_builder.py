import streamlit as st

def show_portfolio_builder():
    st.title("Portfolio Builder")

    name = st.text_input("Your Name")
    role = st.text_input("Your Role (e.g. AI Engineer)")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")

    if st.button("Generate Portfolio"):
        st.subheader("Portfolio Preview")
        st.write(f"### {name}")
        st.write(f"**Role:** {role}")
        st.write("**Skills:**")
        st.write(skills)
        st.write("**Projects:**")
        st.write(projects)
