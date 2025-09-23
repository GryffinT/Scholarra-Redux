import streamlit as st
import pandas as pd
import random
import string
from streamlit_gsheets import GSheetsConnection

def login_window():
    # Initialize session state
    if "page" not in st.session_state:
        st.session_state.page = 0
    if "username" not in st.session_state:
        st.session_state.username = ""

    @st.experimental_singleton
    def get_conn():
        return st.connection("gsheets", type=GSheetsConnection)

    conn = get_conn()

    # The function called when a box is clicked
    def vote(item):
        if item == "A":
            # LOGIN
            st.header("Login")
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")
            valid = False

            if st.button("Submit", key="login_submit"):
                df = conn.read(worksheet="Sheet1", ttl="10m")

                for row in df.itertuples(index=False):
                    if row.Username == username and row.Password == password:
                        st.session_state.username = username
                        st.session_state.page += 1
                        st.success("Login successful!")
                        valid = True
                        st.rerun()
                        break

                if not valid:
                    st.warning("Username or password is incorrect.")

        elif item == "B":
            # SIGNUP
            st.header("Signup")
            username = st.text_input("Username", key="signup_username")
            password = st.text_input("Password", type="password", key="signup_password")
            organization = st.text_input("Organization", key="signup_org")

            if st.button("Submit", key="signup_submit"):
                df = conn.read(worksheet="Sheet1", ttl="10m")

                if username in df["Username"].values:
                    st.error("That username is already taken. Please choose another.")
                else:
                    user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                    plan = "User"

                    new_row = pd.DataFrame({
                        "Username": [username],
                        "Password": [password],
                        "ID": [user_id],
                        "Organization": [organization],
                        "Plan": [plan]
                    })

                    updated_df = pd.concat([df, new_row], ignore_index=True)
                    conn.update(worksheet="Sheet1", data=updated_df)

                    st.success(f"Account created successfully! Your ID is {user_id}. You can now log in.")

    # CSS for hover/expanding boxes
    st.markdown("""
    <style>
    .click-box {
        border: 2px solid #d3d3d3;
        background-color: #d3d3d3;
        border-radius: 12px;
        padding: 40px;
        font-size: 40px;
        font-family: 'Josefin Sans', sans-serif;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        display: inline-block;
    }
    .click-box:hover {
        transform: scale(1.05);
        background-color: #e0e0ff;
        border-color: #888;
    }
    /* Hide the real button but keep it clickable */
    .stButton > button {
        opacity: 0;
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

    # Columns for left/right layout
    col_left, col_spacer, col_right = st.columns([1, 8, 1])

    with col_left:
        st.markdown("<div class='click-box'>LOGIN</div>", unsafe_allow_html=True)
        if st.button("login_hidden"):
            vote("A")

    with col_right:
        st.markdown("<div class='click-box'>SIGNUP</div>", unsafe_allow_html=True)
        if st.button("signup_hidden"):
            vote("B")
