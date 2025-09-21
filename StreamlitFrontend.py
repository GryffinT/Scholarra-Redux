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

#    selected = option_menu(
#        menu_title=None,
#        options=["Home", "Courses", "Search", "Profile"],
#        icons=["house", "book", "search", "person"],
#        orientation="horizontal",
#    )
#    
#    if selected == "Home":
#        display_home()
#    elif selected == "Browse Courses":
#    elif selected == "Search":
#    elif selected == "Profile":

import streamlit as st

st.markdown("""
    <style>
        div[data-testid="stTabs"] button {
            font-size: 200px;
            padding: 60px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# Define tabs
tab1, tab2, tab3 = st.tabs(["Home", "Courses", "Profile"])

with tab1:
    display_home()

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
