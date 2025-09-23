import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import random
import string

def display_login():
    if "login_mode" not in st.session_state:
        st.session_state.login_mode = None
        st.session_state.page = 0  # Add if you use page logic

    col1, col2, col3, col4 = st.columns(4)

    with col2:
        if st.button("Login"):
            st.session_state.login_mode = "login"
    with col3:
        if st.button("Signup"):
            st.session_state.login_mode = "signup"

    if st.session_state.login_mode == "login":
        st.header("Login")
        username = st.text_input("Username", key="login_username")
        key = st.text_input("Enter password", type="password", key="login_password")
        submit_button = st.button("Submit", key="login_submit")

        if submit_button:
            conn = st.connection("gsheets", type=GSheetsConnection)
            df = conn.read(worksheet="Sheet1", ttl="10m")

            valid = False
            for row in df.itertuples(index=False):
                if row.Username == username and row.Password == key:
                    valid = True
                    st.session_state.page += 1
                    st.success("Login successful!")
                    st.session_state.login_mode = None
                    st.rerun()
                    break

            if not valid:
                st.warning("Username or password is incorrect.")

    elif st.session_state.login_mode == "signup":
        st.header("Signup")
        username = st.text_input("Username", key="signup_username")
        password = st.text_input("Password", type="password", key="signup_password")
        organization = st.text_input("Organization", key="signup_organization")
        submit_button = st.button("Submit", key="signup_submit")

        if submit_button:
            conn = st.connection("gsheets", type=GSheetsConnection)
            df = conn.read(worksheet="Sheet1", ttl="5m")

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
                st.session_state.login_mode = None
                st.rerun()
