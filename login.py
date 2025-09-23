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

    with col2: 
        if st.markdown(
            """<style>
            div.stButton > button:first-child {
                padding: 48px 128px;
                font-size: 100px;
                border-radius: 8px;
            }
            </style>""",
            unsafe_allow_html=True,
        ):
            pass
        if st.button("Login", key="login_btn"):
            vote("A")
    
    with col3:
        if st.button("Signup", key="signup_btn"):
            vote("B")

