import streamlit as st
from database import create_user_table, add_user, login_user
st.set_page_config(page_title="Login")
# Create table
create_user_table()

st.title("🔐 Login / Signup")

st.info("Please login to access the app")

menu = st.radio("Select", ["Login", "Signup"])

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# -------------------------
# SIGNUP
# -------------------------
if menu == "Signup":
    if st.button("Create Account"):
        if username and password:
            if add_user(username, password):
                st.success("Account created! Now login.")
            else:
                st.error("Username already exists")
        else:
            st.warning("Enter username & password")

# -------------------------
# LOGIN
# -------------------------
if menu == "Login":
    if st.button("Login"):
        if username and password:
            if login_user(username, password):
                st.session_state["username"] = username
                st.success(f"Welcome {username}")

                # Redirect to main app
                st.switch_page("app.py")

            else:
                st.error("Invalid credentials")
        else:
            st.warning("Enter username & password")