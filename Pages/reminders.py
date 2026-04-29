import streamlit as st
import streamlit as st
import datetime

if "username" not in st.session_state:
    st.warning("Please login first")
    st.stop()
st.title("Health Reminders")

st.write("Set your daily health reminders")

# Water reminder
water_time = st.time_input("Water Reminder Time")

# Exercise reminder
exercise_time = st.time_input("Exercise Reminder Time")

# Medicine reminder
medicine_time = st.time_input("Medicine Reminder Time")

if st.button("Save Reminders"):

    st.success("Reminders saved successfully!")

# Show current time
current_time = datetime.datetime.now().time()

# Reminder alerts
if current_time.hour == water_time.hour and current_time.minute == water_time.minute:
    st.warning("💧 Time to drink water!")

if current_time.hour == exercise_time.hour and current_time.minute == exercise_time.minute:
    st.warning("🏃 Time to exercise!")

if current_time.hour == medicine_time.hour and current_time.minute == medicine_time.minute:
    st.warning("💊 Time to take medicine!")