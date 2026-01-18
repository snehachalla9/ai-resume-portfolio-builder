import streamlit as st
def my_account():
    st.title("My Account")
    if "user_profile" not in st.session_state:
        st.session_state.user_profile = {
            "name": "",
            "email": st.session_state.get("user_email", ""),
            "role": "",
            "skills": ""
        }

    profile = st.session_state.user_profile

    st.subheader("Profile Details")

    profile["name"] = st.text_input("Full Name", profile["name"])
    profile["email"] = st.text_input("Email", profile["email"], disabled=True)
    profile["role"] = st.text_input("Role", profile["role"])
    profile["skills"] = st.text_area("Skills", profile["skills"])

    if st.button("Update Profile"):
        st.session_state.user_profile = profile
        st.success("Profile updated successfully ✅")
    st.divider()
    if st.button("🚪 Logout", type="primary"):
        st.session_state.clear()
        st.rerun()
