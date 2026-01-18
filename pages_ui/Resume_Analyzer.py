import streamlit as st
from services.pdf_service import extract_text_from_resume
from services.ml_service import calculate_match_score

def show_resume_analyzer():
    st.title("Resume Analyzer")
    st.write("Upload a resume and analyze it using AI.")
    resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    job_desc = st.text_area("Paste Job Description")

    if st.button("Analyze Resume"):
        if resume is None:
            st.warning("Please upload a resume PDF")
        elif job_desc.strip() == "":
            st.warning("Please paste the job description")
        else:
            resume_text = extract_text_from_resume(resume)
            score = calculate_match_score(resume_text, job_desc)
            st.success(f"Match Score: {score}%")
