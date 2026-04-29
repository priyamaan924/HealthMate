import streamlit as st
from database import create_user_table, add_user, login_user

st.set_page_config(page_title="AI Health Assistant", layout="wide")

create_user_table()

# LOGIN
if "username" not in st.session_state:

    st.title("🔐 Login / Signup")

    menu = st.radio("Select", ["Login", "Signup"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if menu == "Signup":
        if st.button("Create Account"):
            if add_user(username, password):
                st.success("Account created! Please login.")
            else:
                st.error("Username already exists")

    if menu == "Login":
        if st.button("Login"):
            if login_user(username, password):
                st.session_state["username"] = username
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()

# MAIN APP
st.title("💙 AI Health Assistant")
st.success(f"Logged in as: {st.session_state['username']}")

st.sidebar.info("Use sidebar to navigate pages 👉")

# LOGOUT
if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()