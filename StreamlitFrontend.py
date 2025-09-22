from streamlit_option_menu import option_menu
import streamlit as st
from home_page import display_home
from home_page import pad
import os
from home_page import embed
from home_page import contain
from course_page import display_course
from streamlit_autorefresh import st_autorefresh

if "prog" not in st.session_state:
    st.session_state.prog = 1
if "page" not in st.session_state:
    st.session_state.page = 1

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

st.markdown("""
    <style>
        div[data-testid="stTabs"] button {
            font-size: 50px;
            padding: 4px 100px;  /* vertical = 4px, horizontal = 100px */
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)



# Define tabs
tab1, tab2, tab3 = st.tabs(["Home", "Courses", "Profile"])

st.session_state.page = 0

with tab1:
    st.session_state.page = 1
    if st.session_state.page == 1:
        display_home()
        st_autorefresh(interval=840000, key="1_auto_refresh")

with tab2:
    st.session_state.page = 2
    if st.session_state.page == 2:
        display_course()
        st_autorefresh(interval=840000, key="2_auto_refresh")

with tab3:
    st.session_state.page = 3
    if st.session_state.page == 3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
        st_autorefresh(interval=840000, key="3_auto_refresh")
