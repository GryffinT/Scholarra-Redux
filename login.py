import streamlit as st
import pandas as pd
import random
import string
from streamlit_gsheets import GSheetsConnection


def login_window():
    if "page" not in st.session_state:
        st.session_state.page = 0
    if "username" not in st.session_state:
        st.session_state.username = ""

    col1, col2, col3, col4 = st.columns(4)

    @st.dialog(" ")
    def vote(item):
        conn = st.connection("gsheets", type=GSheetsConnection)

        if item == "A":
            # LOGIN
            st.header("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Submit"):
                df = conn.read(worksheet="Sheet1", ttl="10m")
                valid = False

                for row in df.itertuples(index=False):
                    if row.Username == username and row.Password == password:
                        st.session_state.username = username
                        st.session_state.page += 1
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        valid = False

                if not valid:
                    st.warning("Username or password is incorrect.")

        elif item == "B":
            # SIGNUP
            st.header("Signup")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            organization = st.text_input("Organization")

            if st.button("Submit"):
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
    st.markdown("""
    <style>
    .big-box-button > button {
        width: 100%;
        padding: 60px 0;  /* height of box */
        font-size: 40px;
        border-radius: 12px;
        border: 2px solid #d3d3d3;
        background-color: #d3d3d3;
        cursor: pointer;
        transition: all 0.3s ease;
        font-family: 'Josefin Sans', sans-serif;
    }
    .big-box-button > button:hover {
        transform: scale(1.03);
        background-color: #e0e0ff;
        border-color: #888;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Columns for layout
    col_left, col_spacer, col_right = st.columns([1,8,1])
    
    with col_left:
        if st.button("LOGIN", key="login_btn", help="Click to login"):
            vote("A")
    
    with col_right:
        if st.button("SIGNUP", key="signup_btn", help="Click to signup"):
            vote("B")
