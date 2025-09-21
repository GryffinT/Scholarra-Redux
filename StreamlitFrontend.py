from streamlit_option_menu import option_menu
import streamlit as st
from home_page import display_home
from home_page import pad
import os
from home_page import embed

images_dir = os.path.join(os.path.dirname(__file__), "media")
logo = [
    os.path.join(images_dir, "excel_logo.png")
]

st.set_page_config(layout="wide")

selected = option_menu(
    menu_title=None,
    options=["Home", "Courses", "Search", "Profile"],
    icons=["house", "book", "search", "person"],
    orientation="horizontal",
)

if selected == "Home":
    display_home()
    st.image(logo[0])
elif selected == "Courses":
    st.title("📚 Browse Courses")
elif selected == "Search":
    st.title("🔍 Search Tool")
elif selected == "Profile":
    st.title("👤 Your Profile")
