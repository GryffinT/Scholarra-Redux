import streamlit as st
import os
import base64

images_dir = os.path.join(os.path.dirname(__file__), "media")
logo = [
    os.path.join(images_dir, "excel_logo.png"),
    os.path.join(images_dir, "splotchlogo.png"),
    os.path.join(images_dir, "courseimage.jpg")
    
]


def display_course():
    if st.session_state.page == 2:
        
        with open(logo[2], "rb") as image_file:
            bg_encoded = base64.b64encode(image_file.read()).decode()
        
        with open(logo[1], "rb") as image_file:
            fg_encoded = base64.b64encode(image_file.read()).decode()
        
        st.markdown(
            f"""
            <style>
            /* Background banner */
            .course-banner-wrapper {{
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
            .course-banner-foreground {{
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
            .course-banner-foreground img {{
                width: 600px;   /* change foreground size independently */
                height: auto;   /* keep aspect ratio */
                margin-bottom: 10px;
            }}
        
            /* Foreground text */
            .course-banner-foreground p {{
                font-size: 25px;
                font-weight: 700;
                color: white;
                text-shadow: 2px 2px 5px rgba(0,0,0,0.6);
                margin: 0;
            }}
            </style>
        
            <div class="course-banner-wrapper">
                <div class="course-banner-foreground">
                    <img src="data:image/png;base64,{fg_encoded}">
                    <p>Smarter study starts here.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
