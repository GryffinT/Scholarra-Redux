import streamlit as st
import os

images_dir = os.path.join(os.path.dirname(__file__), "media")
logo = [
    os.path.join(images_dir, "excel_logo.png")
]

def graphic(image):
    st.markdown(
        f'<p style="text-align:center;"><img src="{logo[image]}" width="200"></p>',
        unsafe_allow_html=True
    )

def pad(amount):
    for i in range(amount):
        st.title("")

def format_chat(message, size, centering):

    if centering == 1:
        st.markdown(f"""
            <h1 style="font-size:{size}px; text-align:center; font-family:'Josefin Sans', sans-serif;">
                {message}
            </h1>
        """, unsafe_allow_html=True)
    elif centering == 0:
        st.markdown(f"""
            <h1 style="font-size:{size}px; font-family:'Josefin Sans', sans-serif;">
                {message}
            </h1>
        """, unsafe_allow_html=True)
    elif centering == 2:
        st.markdown(f"""
            <h1 style="font-size:{size}px; text-align:right; font-family:'Josefin Sans', sans-serif;">
                {message}
            </h1>
        """, unsafe_allow_html=True)

def display_home():
    format_chat("Welcome, User.", 70, 0)
    pad(3)
    format_chat("Smarter study starts here.", 50, 1)
    format_chat("Expand and feed your interests, understanding, and curiosities", 50, 1)
    with st.container():
        format_chat("We offer Microsoft Excel prep materials.", 70, 1)
    graphic(0)
    format_chat("New to Scholarra.", 50, 0)
    tab1, tab2, tab3 = st.tabs(["A site redux", "Meet Laurent", "Excel, with Scholarra"])
    
    with tab1:
        format_chat("A site redux!", 40, 0)
        format_chat("We did an entire site-wide redux to improve UI experience and backend work!", 25, 0)
    with tab2:
        format_chat("Meet Laurent", 40, 1)
        format_chat("The newest member to the Scholarra team! Laurent.FP16, a Logistic Regression Transformer with Float Point 16 precision, can be found on the chat tab!", 25, 1)
    with tab3:
        format_chat("Excel, with Scholarra!", 40, 2)
        format_chat("We're pleased to announce that starting now, 9/23/2025, users can access the Excel prep course through the course tab, free of cost!", 25, 2)



