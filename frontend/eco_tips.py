"""import streamlit as st
import requests

st.header("🌿 Eco Tips Generator")

# Input keyword for generating tips
topic = st.text_input("Enter a topic (e.g., plastic, solar, water):")

if topic:
    with st.spinner("Generating eco tips..."):
        try:
            response = requests.get("http://127.0.0.1:8000/eco-tips/", params={"topic": topic})
            if response.status_code == 200:
                tip = response.json().get("tip", "No tip available.")
                st.success("Here's your eco tip:")
                st.write(tip)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Failed to fetch eco tip: {str(e)}")

st.caption("Eco Tips powered by IBM Granite LLM 🌱")"""

# frontend/eco_tips.py

import streamlit as st

def eco_tips_ui():
    st.header("🌿 Eco Tips")
    tips = [
        "Turn off lights when not in use.",
        "Use public transport to reduce emissions.",
        "Recycle and reuse materials.",
        "Plant more trees.",
        "Save water by fixing leaks.",
    ]
    
    for tip in tips:
        st.write("✅", tip)

