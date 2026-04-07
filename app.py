import streamlit as st
import plotly.graph_objects as go
from model import predict_disease

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="AI Health Assistant",
    page_icon="💙",
    layout="wide"
)

# ---------------------------------
# LOAD CUSTOM CSS
# ---------------------------------

def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

load_css()

# ---------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------

st.sidebar.title("💙 AI Health Assistant")

page = st.sidebar.radio(
    "Navigate",
    [
        "Health Analysis",
        "Disease Prediction"
    ]
)

# ---------------------------------
# HERO / LANDING SECTION
# ---------------------------------

st.title("💙 AI Health Assistant")

st.markdown("""
### Your Personal AI Health Companion

Track your health, analyze BMI, get personalized diet plans,  
predict diseases, and monitor your wellness journey.
""")

st.image(
    "https://images.unsplash.com/photo-1576091160550-2173dba999ef",
    use_container_width=True
)

st.markdown("---")

# =================================
# HEALTH ANALYSIS PAGE
# =================================

if page == "Health Analysis":

    st.header("🧑‍⚕️ Health Analysis")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=100, value=25)
        weight = st.text_input("Weight (kg)", "60")

    with col2:
        height = st.text_input("Height (cm)", "170")

        goal = st.selectbox(
            "Health Goal",
            [
                "Weight Loss",
                "Weight Gain",
                "Stay Fit"
            ]
        )

    # Convert inputs safely
    try:
        weight = float(weight)
        height = float(height) / 100
    except:
        st.error("Please enter valid numeric values.")
        st.stop()

    if st.button("Analyze Health"):

        bmi = weight / (height ** 2)

        st.subheader("Your BMI")
        st.write(round(bmi, 2))

        # BMI Gauge Chart
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
                ]
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

        # BMI Category + Health Score
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

        # Calorie Recommendation
        st.subheader("Daily Calorie Recommendation")

        if goal == "Weight Loss":
            calories = 1800
        elif goal == "Weight Gain":
            calories = 2500
        else:
            calories = 2200

        st.write(f"Recommended calories: **{calories} kcal/day**")

# =================================
# DISEASE PREDICTION PAGE
# =================================

elif page == "Disease Prediction":

    st.header("🧬 Disease Prediction")

    st.write("Select the symptoms you are experiencing:")

    col1, col2 = st.columns(2)

    with col1:
        fever = st.checkbox("Fever")
        cough = st.checkbox("Cough")

    with col2:
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

        st.subheader("Possible Condition")
        st.success(disease)
        
        page = st.sidebar.radio(
    "Navigate",
    [
        "Health Analysis",
        "Disease Prediction",
        "AI Chatbot"
    ]
)
    elif page == "AI Chatbot":
        import Pages.chatbot
        