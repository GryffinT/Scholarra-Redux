import Main_classification
import classification_data
import streamlit as st
import os
import base64
from Main_classification import render_sidebar
from Main_generative import output

images_dir = os.path.join(os.path.dirname(__file__), "media")
logo = [
    os.path.join(images_dir, "long-exposure-pier.jpg"),
    os.path.join(images_dir, "LaurentLogo.png")
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

def display_ai():
    # -------------------------
    # Sidebar (persistent)
    # -------------------------
    render_sidebar(
        Main_classification.training_text,
        Main_classification.training_pclass,
        Main_classification.training_sclass,
        Main_classification.accuracies
    )
    
    # -------------------------
    # Chat panel
    # -------------------------
    with open(logo[0], "rb") as image_file:
            bg_encoded = base64.b64encode(image_file.read()).decode()
        
    with open(logo[1], "rb") as image_file:
        fg_encoded = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        /* Background ai-banner */
        .ai-banner-wrapper {{
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
        .ai-banner-foreground {{
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
        .ai-banner-foreground img {{
            width: 600px;   /* change foreground size independently */
            height: auto;   /* keep aspect ratio */
            margin-bottom: 10px;
        }}
    
        /* Foreground text */
        .ai-banner-foreground p {{
            font-size: 50px;
            color: white;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.6);
            margin: 0;
        }}
        </style>
    
        <div class="ai-banner-wrapper">
            <div class="ai-banner-foreground">
                <img src="data:image/png;base64,{fg_encoded}">
                <p>Logistic Regression Transformer, Floating Point 16 precision </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.title("")
    contain(("Hello, User.", 50, 1),
            ("What's on today's agenda?", 25, 1)
           )
    st.write("")
    st.warning("Laurent is still in training, this is just a mockup prototype we whipped up for display purposes!", icon="⚠️")
    st.title("")
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask Laurent anything."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    
        with st.chat_message("assistant"):
            classifications = Main_classification.pipeline.predict(prompt)
            generation = output(prompt)
            response = f"The classifications are: {classifications}, and my answer is {generation}"
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
