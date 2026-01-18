import streamlit as st
from services.pdf_service import generate_resume_pdf
template = st.session_state.get("selected_template","Modern")
st.info(f"Selected Template: {template}")

def show_build_resume():
    st.title("Build My Resume")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    linkedin = st.text_input("LinkedIn")
    github = st.text_input("GitHub")
    about = st.text_area("About You")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")

    if st.button("Generate Resume"):
        data = {
            "name": name,
            "email": email,
            "linkedin": linkedin,
            "github": github,
            "about": about,
            "skills": skills,
            "projects": projects
        }

        pdf = generate_resume_pdf(data,template)
        st.download_button(
            label="Download Resume PDF",
            data=pdf,
            file_name="resume.pdf",
            mime="application/pdf"
        )
