import streamlit as st
from streamlit_option_menu import option_menu
# ✅ CORRECT
from chat_assistant import chat_assistant_ui
from feedback_form import feedback_form_ui
from eco_tips import eco_tips_ui
from summary_card import summary_card_ui


selected = option_menu(
    menu_title=None,
    options=["Dashboard", "Chat Assistant", "Eco Tips", "Feedback Form"],
    icons=["bar-chart", "robot", "leaf", "pencil-square"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Dashboard":
    summary_card_ui()
elif selected == "Chat Assistant":
    chat_assistant_ui()
elif selected == "Eco Tips":
    eco_tips_ui()
elif selected == "Feedback Form":
    feedback_form_ui()
