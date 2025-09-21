import streamlit as st
import os

def format_chat(message, size):
    st.markdown(f'<h1 style="font-size:{size}px">{message}</h1>', unsafe_allow_html=True)

def display_home():
    images_dir = os.path.join(os.path.dirname(__file__), "media")
    logo = [
    os.path.join(images_dir, "excel_logo.png"),
    ]
    st.markdown('<h1 style="font-size:70px; text-align:center;">Welcome, User.</h1>', unsafe_allow_html=True)
    st.empty
    st.markdown('<h1 style="font-size:70px; text-align:center;">Smarter study starts here</h1>', unsafe_allow_html=True)
    format_chat("Expand and feed your interests, understanding, and curiosities", 50)
    st.markdown('<h1 style="font-size:70px; text-align:center;">We offer Microsoft Excel prep materials.</h1>', unsafe_allow_html=True)
    
    st.markdown(
    f'<p style="text-align:center;"><img src="{logo[0]}" width="200"></p>',
    unsafe_allow_html=True)




