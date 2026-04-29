import streamlit as st
from database import create_user_table, add_user, login_user

if "username" not in st.session_state:
    # show login UI
    ...
    st.stop()
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
                st.success(f"Welcome {username}")
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()
# -------------------------
# MAIN APP (AFTER LOGIN)
# -------------------------

st.title("💙 AI Health Assistant")
st.success(f"Logged in as: {st.session_state['username']}")

page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Health Analysis", "Chatbot"]
)

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

if page == "Dashboard":
    import pages.dashboard
elif page == "Health Analysis":
    import pages.health_analysis
elif page == "Chatbot":
    import pages.chatbot