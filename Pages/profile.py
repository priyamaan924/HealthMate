import streamlit as st
from database import create_profile_table, save_profile, get_profile

if "username" not in st.session_state:
    st.warning("Please login first")
    st.stop()
# -------------------------
# INIT
# -------------------------
create_profile_table()

if "username" not in st.session_state:
    st.session_state["username"] = "default_user"

username = st.session_state["username"]

st.title("👤 Profile")

# -------------------------
# LOAD EXISTING DATA
# -------------------------
profile = get_profile(username)

if profile:
    age, height, weight, goal, target_weight = profile
else:
    age, height, weight, goal, target_weight = 25, 170, 60, "Stay Fit", 65

# -------------------------
# INPUT FORM
# -------------------------
st.subheader("Update Your Profile")

age = st.number_input("Age", 1, 100, value=age)
height = st.number_input("Height (cm)", value=height)
weight = st.number_input("Current Weight (kg)", value=weight)

goal = st.selectbox(
    "Health Goal",
    ["Weight Loss", "Weight Gain", "Stay Fit"],
    index=["Weight Loss", "Weight Gain", "Stay Fit"].index(goal)
)

target_weight = st.number_input(
    "🎯 Target Weight (kg)",
    value=target_weight
)

# -------------------------
# SAVE BUTTON
# -------------------------
if st.button("Save Profile"):

    save_profile(
        username,
        age,
        height,
        weight,
        goal,
        target_weight
    )

    st.success("✅ Profile saved successfully!")