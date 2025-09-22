import streamlit as st
import os
import base64
import uuid
import json
from course_page import display_course

images_dir = os.path.join(os.path.dirname(__file__), "media")
logo = [
    os.path.join(images_dir, "excel_logo.png"),
    os.path.join(images_dir, "splotchlogo.png"),
    os.path.join(images_dir, "Library.jpg")
]

def contain(*messages):
    # Start the div with styles
    html_content = '<div style="border:2px solid #e6e6e6; background-color:#FFFFFF; padding:10px; border-radius:10px;">'
    
    # Add each message to the div
    for msg, size, align in messages:
        alignment = ["center", "left", "right"]
        html_content += f'<p style="text-align:{alignment[align]}; font-size:{size}px;">{msg}</p>'
    
    # Close the div
    html_content += '</div>'
    
    # Render everything at once
    st.markdown(html_content, unsafe_allow_html=True)



#def contain(*messages):
#    container = st.container(border=True)
#    with container:
#        for msg, size, align in messages:
#            format_chat(msg, size, align)


def graphic(image_index, size):
    image_path = logo[image_index]
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f'<p style="text-align:center;">'
        f'<img src="data:image/png;base64,{encoded}" width={size}>'
        f'</p>',
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

def display_course():
    st.success("✅ display_course() triggered!")


import streamlit as st
import base64

def display_course():
    st.success("✅ display_course() has been triggered!")

import streamlit as st
import base64

def display_course():
    st.success("✅ display_course() has been triggered!")

def embed(message, size, centering, extra=None):
    align = {0: "left", 1: "center", 2: "right"}.get(centering, "left")

    image_html = ""
    if extra is not None and 0 <= extra < len(logo):
        image_path = logo[extra]
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        image_html = f'<img src="data:image/png;base64,{encoded}" width="200" style="display:block; margin:20px auto;">'

    key = f"button_{message}"

    # CSS to style the Streamlit button like the box
    st.markdown(f'''
    <style>
    div.stButton > button#{key} {{
        all: unset;
        display: block;
        width: 100%;
        cursor: pointer;
        border-radius: 10px;
        border: 2px solid #d3d3d3;
        background-color: #d3d3d3;
        padding: 20px;
        box-sizing: border-box;
        transition: all 0.3s ease;
        text-align: {align};
    }}
    div.stButton > button#{key}:hover {{
        transform: scale(1.02);
        background-color: #e0e0ff;
        border-color: #888;
    }}
    div.stButton > button#{key} h1 {{
        font-size: {size}px;
        font-family: 'Josefin Sans', sans-serif;
        margin: 0;
    }}
    </style>
    ''', unsafe_allow_html=True)

    # Streamlit button that **looks like your box** and triggers Python
    if st.button(label=f'<h1>{message}</h1>{image_html}', key=key, unsafe_allow_html=True):
        display_course()
    
def display_home():
    
    with open(logo[2], "rb") as image_file:
        bg_encoded = base64.b64encode(image_file.read()).decode()
    
    with open(logo[1], "rb") as image_file:
        fg_encoded = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        /* Background banner */
        .banner-wrapper {{
            position: relative;
            width: 100%;
            height: 600px; /* background height */
            background-image: url("data:image/png;base64,{bg_encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            overflow: hidden;
        }}
    
        /* Foreground content */
        .banner-foreground {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 400px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 2;
        }}
    
        /* Foreground logo (adjust size here) */
        .banner-foreground img {{
            width: 600px;   /* change foreground size independently */
            height: auto;   /* keep aspect ratio */
            margin-bottom: 10px;
        }}
    
        /* Foreground text */
        .banner-foreground p {{
            font-size: 25px;
            font-weight: 700;
            color: white;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.6);
            margin: 0;
        }}
        </style>
    
        <div class="banner-wrapper">
            <div class="banner-foreground">
                <img src="data:image/png;base64,{fg_encoded}">
                <p>Smarter study starts here.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    pad(2)
    format_chat("Expand and feed your interests, understanding, and curiosities", 50, 1)
    format_chat("Through Scholarra you can take courses and learn with Laurent", 25, 1)
    pad(2)
    embed("Excel, with Scholarra! Earn your Excel certiifcation today!", 30, 1, extra=0)
    pad(2)
    format_chat("New to Scholarra.", 50, 0)
    tab1, tab2, tab3 = st.tabs(["A site redux", "Meet Laurent", "Excel, with Scholarra"])

    st.markdown("""
        <style>
            div[data-testid="stTabs"] button {
                font-size: 50px;
                padding: 4px 100px;  /* vertical = 4px, horizontal = 100px */
                font-weight: 600;
            }
        </style>
    """, unsafe_allow_html=True)

    
    with tab1:
        contain(
            ("A site redux!", 40, 1),
            ("We did an entire site-wide redux to improve UI experience and backend work!", 25, 1)
        )
    with tab2:
        contain(
            ("Meet Laurent", 40, 0),
            ("The newest member to the Scholarra team! Laurent.FP16, a Logistic Regression Transformer with Float Point 16 precision, can be found on the chat tab!", 25, 0)
        )
    with tab3:
        contain(
            ("Excel, with Scholarra!", 40, 2),
            ("Starting now, 9/23/2025, users can access the Excel prep course free of cost!", 25, 2)
        )











