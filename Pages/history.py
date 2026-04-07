import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_health_data

st.title("📜 Health History")

username = "default_user"

data = get_health_data(username)

if data:

    df = pd.DataFrame(
        data,
        columns=["Date", "Weight", "BMI", "Health Score", "Calories"]
    )

    st.subheader("Your Past Health Records")

    st.dataframe(df)

else:
    st.info("No history available yet. Run health analysis first.")
    
    import plotly.express as px

st.subheader("BMI Progress")

chart = px.line(
    df,
    x="Date",
    y="BMI",
    markers=True
)

st.plotly_chart(chart, use_container_width=True)