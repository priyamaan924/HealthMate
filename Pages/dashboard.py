import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_health_data, create_health_table, get_profile
from diet_recommender import recommend_diet
from workout_planner import recommend_workout
from database import create_habit_table, save_habit, get_habits
from groq import Groq
import os
from dotenv import load_dotenv
from datetime import date

# -------------------------
# AUTH CHECK
# -------------------------
if "username" not in st.session_state:
    st.warning("Please login first")
    st.stop()

username = st.session_state["username"]

# -------------------------
# INIT
# -------------------------
create_health_table()
create_habit_table()

# API
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# -------------------------
# UI
# -------------------------
st.title("📊 Health Dashboard")
st.success(f"Welcome {username}")

# Logout
if st.button("Logout"):
    st.session_state.clear()
    st.rerun()

# -------------------------
# DATA
# -------------------------
data = get_health_data(username)

if not data:
    st.warning("⚠️ Run health analysis first")
    st.stop()

df = pd.DataFrame(data, columns=["Date", "Weight", "BMI", "Health Score", "Calories"])

# -------------------------
# METRICS
# -------------------------
st.subheader("📈 Latest Health Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("BMI", round(df["BMI"].iloc[-1], 2))
col2.metric("Health Score", df["Health Score"].iloc[-1])
col3.metric("Calories", df["Calories"].iloc[-1])

st.divider()

# -------------------------
# CHARTS
# -------------------------
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(px.line(df, x="Date", y="BMI", markers=True), use_container_width=True)

with col2:
    st.plotly_chart(px.line(df, x="Date", y="Weight", markers=True), use_container_width=True)

st.plotly_chart(px.line(df, x="Date", y="Health Score", markers=True))
st.plotly_chart(px.bar(df, x="Date", y="Calories"))

# -------------------------
# PROFILE CHECK
# -------------------------
profile = get_profile(username)

if not profile:
    st.warning("⚠️ Please complete your profile first")
    st.stop()

goal = profile[3]
target = profile[4]

# -------------------------
# GOAL PREDICTION
# -------------------------
st.divider()
st.subheader("🎯 Goal Prediction")

current = df["Weight"].iloc[-1]

# Check profile
if not profile or target is None:
    st.warning("⚠️ Please complete your profile with target weight")
else:
    remaining = abs(current - target)

    if remaining == 0:
        st.success("🎉 You already reached your goal!")
    elif len(df) < 2:
        st.info("Add more data to predict goal timeline")
    else:
        prev = df["Weight"].iloc[-2]
        change = abs(current - prev)

        if change == 0:
            st.info("No weight change yet. Add more data for prediction")
        else:
            days = int(remaining / change)

            st.write(f"Current Weight: {current} kg")
            st.write(f"Target Weight: {target} kg")

            st.success(f"📅 Estimated time to reach goal: {days} days")

            # Extra UX improvement
            if current > target:
                st.write("🔥 You are on a weight loss journey")
            else:
                st.write("💪 You are on a weight gain journey")


# -------------------------
# GOAL PROGRESS %
# -------------------------
st.divider()
st.subheader("🎯 Goal Progress")

start_weight = df["Weight"].iloc[0]
current_weight = df["Weight"].iloc[-1]

if profile:
    target = profile[4]

    total_needed = abs(start_weight - target)
    progress_done = abs(start_weight - current_weight)

    if total_needed == 0:
        progress_percent = 100
    else:
        progress_percent = int((progress_done / total_needed) * 100)

    progress_percent = min(progress_percent, 100)

    st.progress(progress_percent / 100)
    st.write(f"Progress: {progress_percent}% complete")

else:
    st.warning("Set your profile to track goal progress")
# -------------------------
# AI DAILY PLAN
# -------------------------
st.divider()
st.subheader("🧠 AI Daily Plan")

if st.button("Generate Plan"):

    calories = df["Calories"].iloc[-1]

    diet = recommend_diet(goal, calories)
    workout = recommend_workout(goal)

    st.write("🍎 Diet Plan")
    for k, v in diet.items():
        st.write(f"{k}: {v}")

    st.write("🏋️ Workout Plan")
    for w in workout:
        st.write(w)

# -------------------------
# EXPLAIN HEALTH
# -------------------------
st.divider()
st.subheader("🧠 Explain My Health")

if st.button("Explain"):

    latest = df.iloc[-1]

    prompt = f"""
BMI: {latest['BMI']}
Health Score: {latest['Health Score']}
Goal: {goal}

Explain the user's health and give advice.
"""

    try:
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        st.info(res.choices[0].message.content)

    except Exception as e:
        st.error(e)

# -------------------------
# HABIT TRACKER
# -------------------------
st.divider()
st.subheader("💧 Habit Tracker")

today = str(date.today())

water = st.number_input("Water (L)", 0.0)
sleep = st.number_input("Sleep (hrs)", 0.0)
steps = st.number_input("Steps", 0)

if st.button("Save Habits"):
    save_habit(username, today, water, sleep, steps)
    st.success("Saved!")

habits = get_habits(username)

if habits:
    latest = habits[-1]

    st.write("Water:", latest[1])
    st.write("Sleep:", latest[2])
    st.write("Steps:", latest[3])