import streamlit as st
st.set_page_config(page_title="AI RESUME AND PORTFOLIO BUILDER")
from home import show_home
from resume_analyzer import show_resume_analyzer
from resume_templates import show_resume_templates
from build_resume import show_build_resume
from portfoilo_builder import   show_portfolio_builder
from myaccount import my_account
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False
if not st.session_state.logged_in:
    st.title("AI RESUME")
    email=st.text_input("Email")
    password=st.text_input("password")
    if st.button("Login"):
        if(email=="sneha@gmail.com" and password=="sneha"):
            st.session_state.logged_in=True
            st.success("Login suceesfully")
            st.rerun()
        else:
            st.error("Invalid email or password")
    #st.title("AI RESUME AND PORTFOLIO")
else:
    menu=st.sidebar.radio(
        "Navigation",
        ["Home","Resume Analyzer","Resume Templates","Build My Resume","Portfolio Builder","My Account"])
    if menu == "Home":
        show_home()
 
    elif menu=="Resume Analyzer":
        show_resume_analyzer()
    elif menu=="Resume Templates":
        show_resume_templates()
    elif menu=="Build My Resume":
        show_build_resume()
    elif menu=="Portfolio Builder":
        show_portfolio_builder()
    elif menu=="My Account":
        my_account()
        st.stop()
