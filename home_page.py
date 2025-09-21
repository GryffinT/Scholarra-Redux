import streamlit as st
import os


def format_chat(message, size, centering):
    mid = "center"
    if centered == True:
        st.markdown(f"""
            <h1 style="font-size:{size}px; text-align:{centering}; font-family:'Josefin Sans', sans-serif;">
                {message}
            </h1>
        """, unsafe_allow_html=True)
def display_home():
    images_dir = os.path.join(os.path.dirname(__file__), "media")
    logo = [
    os.path.join(images_dir, "excel_logo.png"),
    ]
    format_chat("Welcome, User.", 70)
    st.title("")
    st.title("")
    st.title("")
    format_chat("Smarter study starts here.", 50, mid)
    format_chat("Expand and feed your interests, understanding, and curiosities", 50, mid)
    format_chat("We offer Microsoft Excel prep materials.", 70, mid)
    
    st.markdown(
    f'<p style="text-align:center;"><img src="{logo[0]}" width="200"></p>',
    unsafe_allow_html=True)




