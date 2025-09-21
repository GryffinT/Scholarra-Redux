import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title=None,
    options=["Home", "Courses", "Search", "Profile"],
    icons=["house", "book", "search", "person"],
    orientation="horizontal",
)

st.write(f"You selected: {selected}")

