import streamlit as st
from database import create_profile_table, save_profile, get_profile

st.title("User Profile")

create_profile_table()

username = "default_user"
profile = get_profile(username)

if profile:
    age, height, weight, goal = profile
else:
    age, height, weight, goal = 25, 170, 60, "Stay Fit"

age = st.number_input("Age", value=age)
height = st.number_input("Height (cm)", value=height)
weight = st.number_input("Weight (kg)", value=weight)

goal = st.selectbox(
    "Health Goal",
    ["Weight Loss","Weight Gain","Stay Fit"],
    index=["Weight Loss","Weight Gain","Stay Fit"].index(goal)
)

if st.button("Save Profile"):

    save_profile(
    username,
    age,
    height,
    weight,
    goal
)

    st.success("Profile updated successfully!")