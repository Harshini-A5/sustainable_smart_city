import streamlit as st

def summary_card_ui():
    st.subheader("📊 Summary Report")
    st.markdown("""
    - Total Citizens: 10,000  
    - Active Feedback Reports: 147  
    - Average City Health Score: 8.4 / 10  
    - Monthly Energy Usage Reduction: 12%
    """)
