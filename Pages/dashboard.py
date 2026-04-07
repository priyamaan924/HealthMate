import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_health_data, create_health_table

if "username" not in st.session_state:
    st.session_state["username"] = "Guest"
st.title("📊 Health Dashboard")

create_health_table()

st.success("Welcome to AI Health Assistant")

data = get_health_data(st.session_state["username"])

if data:

    df = pd.DataFrame(
        data,
        columns=["Date","Weight","BMI","Health Score","Calories"]
    )

    st.subheader("📈 Latest Health Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("BMI", round(df["BMI"].iloc[-1],2))
    col2.metric("Health Score", df["Health Score"].iloc[-1])
    col3.metric("Calories", df["Calories"].iloc[-1])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("BMI Progress")

        bmi_chart = px.line(
            df,
            x="Date",
            y="BMI",
            markers=True,
            color_discrete_sequence=["green"]
        )

        st.plotly_chart(bmi_chart, use_container_width=True)

    with col2:

        st.subheader("Weight Progress")

        weight_chart = px.line(
            df,
            x="Date",
            y="Weight",
            markers=True,
            color_discrete_sequence=["blue"]
        )

        st.plotly_chart(weight_chart, use_container_width=True)

    st.subheader("Daily Calories")

    calorie_chart = px.bar(
        df,
        x="Date",
        y="Calories",
        color="Calories",
        color_continuous_scale="Blues"
    )

    st.plotly_chart(calorie_chart, use_container_width=True)

else:

    st.info("No health data available yet. Run health analysis to generate data.")