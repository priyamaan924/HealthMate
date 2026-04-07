import streamlit as st
import plotly.graph_objects as go
from datetime import date

from model import predict_disease
from risk_predictor import predict_health_risk
from diet_recommender import recommend_diet
from workout_planner import recommend_workout
from database import create_health_table, save_health_data

# Create database table
create_health_table()

st.title("🧑‍⚕️ Health Analysis")

st.write("Enter your health details")

# -------------------------
# INPUT SECTION
# -------------------------

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    weight = st.text_input("Weight (kg)", "60")

with col2:
    height = st.text_input("Height (cm)", "170")
    goal = st.selectbox(
        "Health Goal",
        ["Weight Loss", "Weight Gain", "Stay Fit"]
    )

# Convert safely
try:
    weight = float(weight)
    height = float(height) / 100
except:
    st.error("Please enter valid numeric values.")
    st.stop()

# -------------------------
# BMI ANALYSIS
# -------------------------

if st.button("Analyze Health", key="analyze_button"):
    

    bmi = weight / (height ** 2)

    st.subheader("Your BMI")
    st.write(round(bmi, 2))

    # health score
    if bmi < 18.5:
        health_score = 60
    elif bmi < 25:
        health_score = 90
    elif bmi < 30:
        health_score = 70
    else:
        health_score = 50

    # calories
    if goal == "Weight Loss":
        calories = 1800
    elif goal == "Weight Gain":
        calories = 2500
    else:
        calories = 2200

    # -----------------------
    # SAVE DATA TO DATABASE
    # -----------------------

    today = date.today()

    username = "default_user"

    save_health_data(
        username,
        str(today),
        weight,
        bmi,
        health_score,
        calories
    )

    # BMI Gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=bmi,
        title={'text': "BMI Level"},
        gauge={
            'axis': {'range': [0, 40]},
            'steps': [
                {'range': [0, 18.5], 'color': "lightblue"},
                {'range': [18.5, 25], 'color': "green"},
                {'range': [25, 30], 'color': "yellow"},
                {'range': [30, 40], 'color': "red"}
            ],
        }
    ))

    st.plotly_chart(fig)

    # BMI Category
    if bmi < 18.5:
        st.warning("Underweight")
        health_score = 60
    elif bmi < 25:
        st.success("Normal weight")
        health_score = 90
    elif bmi < 30:
        st.warning("Overweight")
        health_score = 70
    else:
        st.error("Obese")
        health_score = 50

    # Health Score
    st.subheader("Health Score")
    st.progress(health_score / 100)

    # -------------------------
    # CALORIE RECOMMENDATION
    # -------------------------

    st.subheader("Daily Calorie Recommendation")

    if goal == "Weight Loss":
        calories = 1800
    elif goal == "Weight Gain":
        calories = 2500
    else:
        calories = 2200

    st.write(f"{calories} kcal/day")

    # HEALTH RISK PREDICTION

    st.subheader("Health Risk Prediction")

    obesity_risk, heart_risk, diabetes_risk = predict_health_risk(age, bmi)

    st.write("Obesity Risk:", obesity_risk)
    st.write("Heart Disease Risk:", heart_risk)
    st.write("Diabetes Risk:", diabetes_risk)

    # DIET PLAN

    st.subheader("Personalized Diet Plan")

    diet = recommend_diet(goal, calories)

    for meal, food in diet.items():
        st.write(f"{meal}: {food}")

    # WORKOUT PLAN

    st.subheader("Weekly Workout Plan")

    workout_plan = recommend_workout(goal)

    for day in workout_plan:
        st.write(day)

    # SAVE DATA

    today = date.today()

    username = "default_user"

    save_health_data(
        username,
        str(today),
        weight,
        bmi,
        health_score,
        calories
    )

# DISEASE PREDICTION

st.header("🧬 Disease Prediction")

fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")
fatigue = st.checkbox("Fatigue")

if st.button("Predict Disease"):

    symptoms = [
        int(fever),
        int(cough),
        int(headache),
        int(fatigue)
    ]

    disease = predict_disease(symptoms)

    st.subheader("Possible Disease")
    st.success(disease)