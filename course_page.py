import streamlit as st
import os
import base64
import streamlit_pdf

images_dir = os.path.join(os.path.dirname(__file__), "media")
medias = [
    os.path.join(images_dir, "excel_medias.png"),
    os.path.join(images_dir, "scholarracourselogo.png"),
    os.path.join(images_dir, "courseimage.jpg"),
    os.path.join(images_dir, "Syllabus TTS.mp3"),
    os.path.join(images_dir, "mo-200-microsoft-excel-2019-skills-measured (2).pdf")
    
]

def navigation_buttons(id1,id2):
    if "prog" not in st.session_state:
        st.session_state.prog = 1
    # CSS styling for buttons
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #FFFFFF;
            color: black;
            border: 2px solid #e6e6e6;
            border-radius: 5px;
            padding: 8px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    # Three columns: left button, spacer, right button
    col1, col2, col3 = st.columns([1, 8, 1])

    # Back button (left)
    with col1:
        if st.button("Back", key=id1):
            st.session_state.prog -= 1

    # Spacer column col2 does nothing (just stretches space)

    # Next button (right)
    with col3:
        if st.button("Next", key=id2):
            st.session_state.prog += 1

    # Display current value centered
    st.markdown(f"<h3 style='text-align:center;'>Current prog: {st.session_state.prog}</h3>", unsafe_allow_html=True)

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

def display_course():
    if "prog" not in st.session_state:
        st.session_state.prog = 1
    if st.session_state.page == 2:
        
        with open(medias[2], "rb") as image_file:
            bg_encoded = base64.b64encode(image_file.read()).decode()
        
        with open(medias[1], "rb") as image_file:
            fg_encoded = base64.b64encode(image_file.read()).decode()
        
        st.markdown(
            f"""
            <style>
            /* Background banner */
            .course-banner-wrapper {{
                position: relative;
                width: 100%;
                height: 600px;
                background-image: url("data:image/png;base64,{bg_encoded}");
                background-size: cover;
                background-position: center bottom;
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

            /* Foreground medias */
            .course-banner-foreground img {{
                width: 600px;
                height: auto;
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

            <div class="course-banner-wrapper" id="courseBanner">
                <div class="course-banner-foreground">
                    <img src="data:image/png;base64,{fg_encoded}">
                    <p>Smarter study starts here.</p>
                </div>
            </div>

            <script>
            window.addEventListener('scroll', function() {{
                var banner = document.getElementById('courseBanner');
                var scrollTop = window.pageYOffset;
                var yPos = -(scrollTop * 0.3); // adjust speed here
                banner.style.backgroundPosition = 'center ' + yPos + 'px';
            }});
            </script>
            """,
            unsafe_allow_html=True
        )
    
    tab1, tab2 = st.tabs(["Excel", "Intro to ML"])
    
    with tab1:
        contain(
            ("MO-200 Excel", 40, 0),
            ("Welcome! We're so glad you've chosen to enroll in our excel prep program! Feel free to look through the course syllabus. Once done scroll down and click next.", 25, 0)
        )
        st.audio(medias[3])
        st.pdf(medias[4])
        navigation_buttons(1,2)

        
    with tab2:
        st.header("Intro to ML")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
