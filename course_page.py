
import streamlit as st

def display_course():
    
    # Unique key to detect click
    if "box_clicked" not in st.session_state:
        st.session_state.box_clicked = False
    
    # Inject CSS + JS
    st.markdown(
        """
        <style>
        .expand-box {
            display: inline-block;
            background-color: #f0f0f0;
            border: 2px solid #ccc;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .expand-box:hover {
            transform: scale(1.1);
            background-color: #e0e0ff;
            border-color: #888;
        }
        </style>
    
        <script>
        function sendClick() {
            const streamlitEvent = new Event("streamlit:custom_click");
            window.parent.document.dispatchEvent(streamlitEvent);
        }
        </script>
    
        <div class="expand-box" onclick="sendClick()">
            🚀 Hover & Click Me
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Listen for the JS event and set a flag
    clicked = st.session_state.box_clicked
    st.markdown(
        """
        <script>
        const doc = window.parent.document;
        doc.addEventListener("streamlit:custom_click", function() {
            fetch("/_stcore/streamlit_set_value", {
                method: "POST",
                body: JSON.stringify({key: "box_clicked", value: true}),
                headers: {"Content-Type": "application/json"}
            });
        });
        </script>
        """,
        unsafe_allow_html=True,
    )
    
    # Check if it was clicked
    if st.session_state.box_clicked:
        st.success("✅ You clicked the expanding box!")
        st.session_state.box_clicked = False  # reset after click
