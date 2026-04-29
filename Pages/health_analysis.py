import streamlit as st
import plotly.graph_objects as go
from datetime import date

from model import predict_disease
from risk_predictor import predict_health_risk
from diet_recommender import recommend_diet
from workout_planner import recommend_workout
from database import create_health_table, save_health_data
from report import generate_report

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

st.title("🧑‍⚕️ Health Analysis")
st.markdown("### 💙 Analyze your health and get smart recommendations")

# -------------------------
# INPUT
# -------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 100, 25)
    weight = st.text_input("Weight (kg)", "60")

with col2:
    height = st.text_input("Height (cm)", "170")
    goal = st.selectbox("Health Goal", ["Weight Loss", "Weight Gain", "Stay Fit"])

# -------------------------
# VALIDATION
# -------------------------
try:
    weight = float(weight)
    height = float(height) / 100
except:
    st.error("Enter valid numbers")
    st.stop()

# -------------------------
# ANALYZE BUTTON (ONLY ONE)
# -------------------------
if st.button("🚀 Analyze Health", key="analyze_btn"):

    bmi = weight / (height ** 2)

    # Category + Score
    if bmi < 18.5:
        health_score = 60
        category = "Underweight"
    elif bmi < 25:
        health_score = 90
        category = "Normal"
    elif bmi < 30:
        health_score = 70
        category = "Overweight"
    else:
        health_score = 50
        category = "Obese"

    calories = 1800 if goal == "Weight Loss" else 2500 if goal == "Weight Gain" else 2200

    # Save session
    st.session_state["bmi"] = bmi
    st.session_state["score"] = health_score
    st.session_state["calories"] = calories
    st.session_state["goal"] = goal

    # Save DB
    save_health_data(username, str(date.today()), weight, bmi, health_score, calories)

    # -------------------------
    # DISPLAY BMI
    # -------------------------
    st.subheader("📊 Your BMI")
    st.write(round(bmi, 2))

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=bmi,
        title={'text': "BMI"},
        gauge={
            'axis': {'range': [0, 40]},
            'steps': [
                {'range': [0, 18.5], 'color': "lightblue"},
                {'range': [18.5, 25], 'color': "green"},
                {'range': [25, 30], 'color': "yellow"},
                {'range': [30, 40], 'color': "red"}
            ]
        }
    ))
    st.plotly_chart(fig)

    # Category
    st.subheader("📌 Category")
    st.write(category)

    # -------------------------
    # HEALTH SCORE
    # -------------------------
    st.subheader("⭐ Health Score")
    st.progress(health_score / 100)

    # -------------------------
    # HEALTH SCORE BREAKDOWN
    # -------------------------
    st.subheader("🧠 Health Score Breakdown")

    bmi_score = 100 - abs(bmi - 22) * 5
    bmi_score = max(min(bmi_score, 100), 0)

    activity_score = 80 if goal == "Stay Fit" else 70
    diet_score = 75
    habit_score = 70

    final_score = int(
        (bmi_score * 0.4) +
        (activity_score * 0.2) +
        (diet_score * 0.2) +
        (habit_score * 0.2)
    )

    st.write(f"Overall Score: {final_score}/100")
    st.progress(final_score / 100)

    st.write("BMI:", int(bmi_score))
    st.write("Activity:", activity_score)
    st.write("Diet:", diet_score)
    st.write("Habits:", habit_score)

    # -------------------------
    # CALORIES
    # -------------------------
    st.subheader("🔥 Calories")
    st.write(f"{calories} kcal/day")

    # -------------------------
    # RISK
    # -------------------------
    st.subheader("⚠️ Risk")
    obesity, heart, diabetes = predict_health_risk(age, bmi)
    st.write("Obesity:", obesity)
    st.write("Heart:", heart)
    st.write("Diabetes:", diabetes)

    # -------------------------
    # DIET
    # -------------------------
    st.subheader("🍎 Diet")
    diet = recommend_diet(goal, calories)
    for k, v in diet.items():
        st.write(f"{k}: {v}")

    # -------------------------
    # WORKOUT
    # -------------------------
    st.subheader("🏋️ Workout")
    workout = recommend_workout(goal)
    for d in workout:
        st.write(d)

# -------------------------
# PDF REPORT
# -------------------------
st.subheader("📄 Report")

if "bmi" in st.session_state:

    if st.button("Generate Report", key="report_btn"):

        diet = recommend_diet(
            st.session_state["goal"],
            st.session_state["calories"]
        )

        workout = recommend_workout(st.session_state["goal"])

        generate_report(
            st.session_state["bmi"],
            st.session_state["score"],
            st.session_state["calories"],
            diet,
            workout,
            st.session_state["goal"]
        )

        with open("health_report.pdf", "rb") as f:
            st.download_button("Download Report", f, "health_report.pdf")

else:
    st.info("⚠️ Run Health Analysis first.")

# -------------------------
# DISEASE PREDICTION
# -------------------------
st.header("🧬 Disease Prediction")

fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")
fatigue = st.checkbox("Fatigue")

if st.button("Predict Disease", key="disease_btn"):
    symptoms = [int(fever), int(cough), int(headache), int(fatigue)]
    st.success(predict_disease(symptoms))