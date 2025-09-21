from streamlit_option_menu import option_menu
import streamlit as st

st.set_page_config(layout="wide")

selected = option_menu(
    menu_title=None,
    options=["Home", "Courses", "Search", "Profile"],
    icons=["house", "book", "search", "person"],
    orientation="horizontal",
)

if selected == "Home":
    st.title("🏠 Welcome to Home")
elif selected == "Courses":
    st.title("📚 Browse Courses")
elif selected == "Search":
    st.title("🔍 Search Tool")
elif selected == "Profile":
    st.title("👤 Your Profile")
