import streamlit as st
from app.services.granite_llm import ask_granite

def chat_assistant_ui():
    st.subheader("💬 Chat Assistant")
    user_input = st.text_input("Ask something:")
    if user_input:
        response = ask_granite(user_input)
        st.write("🧠 Response:", response)
