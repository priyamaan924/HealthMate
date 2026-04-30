import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_health_data

# -------------------------
# AUTH CHECK
# -------------------------
if "username" not in st.session_state:
    st.warning("Please login first")
    st.stop()

st.title("📜 Health History")

# ✅ use logged-in user
username = st.session_state["username"]

data = get_health_data(username)

# -------------------------
# IF DATA EXISTS
# -------------------------
if data:

    df = pd.DataFrame(
        data,
        columns=["Date", "Weight", "BMI", "Health Score", "Calories"]
    )

    st.subheader("Your Past Health Records")
    st.dataframe(df)

    # -------------------------
    # BMI CHART
    # -------------------------
    st.subheader("📊 BMI Progress")

    chart = px.line(
        df,
        x="Date",
        y="BMI",
        markers=True
    )

    st.plotly_chart(chart, use_container_width=True)

# -------------------------
# NO DATA
# -------------------------
else:
    st.info("No history available yet. Run health analysis first.")