from streamlit_option_menu import option_menu
import streamlit as st
from home_page import display_home
from home_page import pad
import os
from home_page import embed

st.set_page_config(layout="wide")

selected = option_menu(
    menu_title=None,
    options=["Home", "Courses", "Search", "Profile"],
    icons=["house", "book", "search", "person"],
    orientation="horizontal",
)

if selected == "Home":
    display_home()
elif selected == "Courses":
    st.title("📚 Browse Courses")
elif selected == "Search":
    st.title("🔍 Search Tool")
elif selected == "Profile":
    st.title("👤 Your Profile")
