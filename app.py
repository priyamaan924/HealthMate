import streamlit as st
from database import create_user_table, add_user, login_user

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="AI Health Assistant", layout="wide")

create_user_table()

# -------------------------
# LOGIN SYSTEM
# -------------------------
if "username" not in st.session_state:

    st.title("🔐 Login / Signup")

    menu = st.radio("Select", ["Login", "Signup"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # SIGNUP
    if menu == "Signup":
        if st.button("Create Account", key="signup_btn"):
            if add_user(username, password):
                st.success("Account created! Please login.")
            else:
                st.error("Username already exists")

    # LOGIN
    if menu == "Login":
        if st.button("Login", key="login_btn"):
            if login_user(username, password):
                st.session_state["username"] = username
                st.success(f"Welcome {username}")
                st.rerun()
            else:
                st.error("Invalid credentials")

    # 🔥 IMPORTANT: DO NOT REMOVE
    st.stop()

# -------------------------
# MAIN APP
# -------------------------
st.title("💙 AI Health Assistant")
st.success(f"Logged in as: {st.session_state['username']}")

# -------------------------
# NAVIGATION
# -------------------------
page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Health Analysis", "Chatbot"]
)

# LOGOUT
if st.sidebar.button("Logout", key="logout_btn"):
    st.session_state.clear()
    st.rerun()

# -------------------------
# PAGE ROUTING
# -------------------------
if page == "Dashboard":
    import pages.dashboard

elif page == "Health Analysis":
    import pages.health_analysis

elif page == "Chatbot":
    import pages.chatbot