import streamlit as st
def show_resume_templates():
    st.title("Resume Templates")

    st.write("Choose a resume template style")

    template = st.radio(
        "Select Template",
        ["Modern", "Classical", "Minimal"]
    )
    st.session_state.selected_template=template
    st.subheader("Preview")
    if template == "Modern":
        st.write("🟦 Modern Resume Layout")
    elif template == "Classical":
        st.write("📄 Classical Resume Layout")
    else:
        st.write("⬜ Minimal Resume Layout")
