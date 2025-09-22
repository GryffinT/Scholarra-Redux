import Main_classification
import classification_data
import streamlit as st
from Main_classification import render_sidebar
from Main_generative import output

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
    
    st.markdown('<h1 style="font-size:70px">Welcome, User.</h1>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size:30px">What\'s on today\'s agenda?</h1>', unsafe_allow_html=True)
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
            contain((prompt), 40, 1)
    
        with st.chat_message("assistant"):
            classifications = Main_classification.pipeline.predict(prompt)
            generation = output(prompt)
            response = f"The classifications are: {classifications}, and my answer is {generation}"
            contain((response, 40, 1))
        st.session_state.messages.append({"role": "assistant", "content": response})
