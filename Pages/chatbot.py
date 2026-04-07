import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🤖 AI Health Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input
user_input = st.chat_input("Ask your health question...")

if user_input:

    st.chat_message("user").write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI health assistant. Give safe and general health advice."
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
)

        reply = response.choices[0].message.content

        st.chat_message("assistant").write(reply)

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })

    except Exception as e:
        st.error(f"Error: {e}")