import streamlit as st
import os
import base64

images_dir = os.path.join(os.path.dirname(__file__), "media")
logo = [
    os.path.join(images_dir, "excel_logo.png"),
    os.path.join(images_dir, "Scholarra Splotch Logo.png")
]

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

def embed(message, size, centering, extra=None):
    align = {0: "left", 1: "center", 2: "right"}.get(centering, "left")

    image_html = ""
    if extra is not None and 0 <= extra < len(logo):
        image_path = logo[extra]
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        image_html = f'<img src="data:image/png;base64,{encoded}" width="200" style="display:block; margin:20px auto;">'

    with st.container():
        st.markdown(f"""
            <div style="
                border: 2px solid #d3d3d3;
                background-color: #d3d3d3;
                padding: 20px;
                border-radius: 10px;
            ">
                <h1 style="font-size:{size}px; text-align:{align}; font-family:'Josefin Sans', sans-serif;">
                    {message}
                </h1>
                {image_html}
            </div>
        """, unsafe_allow_html=True)



def display_home():
    graphic(1, 300)
    format_chat("Smarter study starts here.", 25, 1)
    pad(2)
    format_chat("Expand and feed your interests, understanding, and curiosities", 50, 1)
    format_chat("Through Scholarra you can take courses and learn with Laurent", 25, 1)
    pad(2)
    embed("We offer Microsoft Excel prep materials.", 50, 1, 0)
    pad(2)
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



