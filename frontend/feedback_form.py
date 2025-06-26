"""import streamlit as st
import requests

def feedback_form():
    st.header("📝 Citizen Feedback Form")
    st.markdown("Please share your concerns or suggestions for improving your city.")

    name = st.text_input("Your Name")
    category = st.selectbox("Category", ["Water", "Electricity", "Transport", "Waste Management", "Other"])
    message = st.text_area("Your Message")

    if st.button("Submit Feedback"):
        if not name or not message:
            st.warning("Please fill in all required fields.")
        else:
            try:
                with st.spinner("Submitting..."):
                    response = requests.post(
                        "http://127.0.0.1:8000/submit-feedback",
                        json={
                            "name": name,
                            "category": category,
                            "message": message
                        }
                    )
                    if response.status_code == 200:
                        st.success("✅ Feedback submitted successfully!")
                    else:
                        st.error("❌ Error: " + response.text)
            except Exception as e:
                st.error(f"Exception occurred: {e}")"""

# frontend/feedback_form.py

import streamlit as st

def feedback_form_ui():
    st.header("📋 Feedback Form")
    name = st.text_input("Your Name")
    feedback = st.text_area("Your Feedback")
    
    if st.button("Submit"):
        st.success(f"Thanks {name}, your feedback has been recorded!")

