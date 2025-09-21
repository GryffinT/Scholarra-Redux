import streamlit as st

def format_chat(message, size):
  st.markdown(f'<h1 style="font-size:{size}px">{message}</h1>', unsafe_allow_html=True)

def display_home():
  st.markdown('<h1 style="font-size:70px">Welcome, User.</h1>', unsafe_allow_html=True)
  
  st.markdown('<h1 style="font-size:70px">Samrter study starts here</h1>', unsafe_allow_html=True)
  format_chat("Expand and feed your interests, understanding, and curiosities", 50)
  st.markdown(
    '<h1 style="font-size:70px; text-align:center;">We offer Microsoft Excel prep materials.</h1>', 
    unsafe_allow_html=True
  )



