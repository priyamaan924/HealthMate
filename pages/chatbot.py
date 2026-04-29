import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from database import get_health_data, get_profile

# -------------------------
# AUTH CHECK
# -------------------------
if "username" not in st.session_state:
    st.warning("Please login first")
    st.stop()

username = st.session_state["username"]   # ✅ FIXED

# -------------------------
# LOAD API
# -------------------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ API key not found.")
    st.stop()

client = Groq(api_key=api_key)

# -------------------------
# UI
# -------------------------
st.title("🤖 AI Health Coach")
st.markdown("💡 Your personalized AI health assistant")

# -------------------------
# SESSION STATE (CHAT HISTORY)
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# DISPLAY CHAT HISTORY
# -------------------------
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# -------------------------
# FETCH USER DATA (PERSONALIZATION)
# -------------------------
data = get_health_data(username)
profile = get_profile(username)

if data:
    latest = data[-1]
    bmi = latest[2]
    health_score = latest[3]
    calories = latest[4]
else:
    bmi = "unknown"
    health_score = "unknown"
    calories = "unknown"

goal = profile[3] if profile else "unknown"

# -------------------------
# CONTEXT BUILDER (SMART)
# -------------------------
context = f"""
User Profile:
Goal: {goal}

Latest Health Data:
BMI: {bmi}
Health Score: {health_score}
Daily Calories: {calories}

Instructions:
- Give simple, actionable advice
- Be motivational
- Avoid medical diagnosis
"""

# -------------------------
# USER INPUT
# -------------------------
user_input = st.chat_input("Ask your health question...")

if user_input:

    # Show user message
    st.chat_message("user").write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        # -------------------------
        # INCLUDE CHAT MEMORY (🔥 UNIQUE)
        # -------------------------
        messages = [
            {
                "role": "system",
                "content": f"You are a personal AI health coach.\n{context}"
            }
        ]

        # Add last 5 messages for memory
        messages.extend(st.session_state.messages[-5:])

        # Add current user input
        messages.append({
            "role": "user",
            "content": user_input
        })

        # -------------------------
        # GROQ CALL
        # -------------------------
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        reply = response.choices[0].message.content

        # Show response
        st.chat_message("assistant").write(reply)

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# -------------------------
# 🔥 WEEKLY AI COACH FEATURE
# -------------------------
st.divider()
st.subheader("🧠 Weekly AI Coach")

if st.button("Get Weekly Advice", key="weekly_btn"):

    if data and len(data) >= 2:
        latest = data[-1]
        prev = data[-2]

        prompt = f"""
User Goal: {goal}
Current BMI: {latest[2]}
Weight Change: {latest[1] - prev[1]}

Give short weekly coaching advice.
"""

        try:
            res = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            st.success(res.choices[0].message.content)

        except Exception as e:
            st.error(e)

    else:
        st.info("Add more health data for weekly insights")

# -------------------------
# CLEAR CHAT (UX FEATURE)
# -------------------------
if st.button("🧹 Clear Chat", key="clear_btn"):
    st.session_state.messages = []
    st.rerun()