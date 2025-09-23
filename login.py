import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

def display_login():
  key = None
  def get_key():
      user_key = st.text_input("Enter password", type="password")
      print (user_key)
      return user_key
  
  if "user_key" not in st.session_state:
      st.session_state.user_key = ""  # initialize empty
      
      col1, col2, col3, col4 = st.columns(4)
      
      @st.dialog(" ")
      def vote(item):
          if item == "A":
              st.header("Login")
              username = st.text_input("Username")
              st.session_state["username"] = username
              st.session_state['use_key'] = get_key()
              key = st.session_state['use_key']
              submit_button = st.button("Submit")
              if submit_button:
                      conn = st.connection("gsheets", type=GSheetsConnection)
                      df = conn.read(
                          worksheet="Sheet1",
                          ttl="10m",
                      )
  
                      # Print results
                      for row in df.itertuples(index=False):
                          if row.Username == username and row.Password == key:
                              st.session_state.page += 1
                              st.rerun()
                          else:
                              valid = False
                              
                      if valid == False:
                         st.warning("Username or password is incorrect.")
                          
          def generate_id(length=8):
              """Generate a random alphanumeric string."""
              return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
          
          if item == "B":
              conn = st.connection("gsheets", type=GSheetsConnection)
          
              st.header("Signup")
          
              username = st.text_input("Username")
              password = st.text_input("Password", type="password")
              organization = st.text_input("Organization")
          
              if st.button("Submit"):
                  # Load current data from Sheet1
                  df = conn.read(worksheet="Sheet1", ttl=5)
          
                  # Check if username already exists
                  if username in df["Username"].values:
                      st.error("That username is already taken. Please choose another.")
                  else:
                      # Generate ID + default plan
                      user_id = generate_id()
                      plan = "User"
          
                      # Create new row
                      new_row = pd.DataFrame({
                          "Username": [username],
                          "Password": [password],
                          "ID": [user_id],
                          "Organization": [organization],
                          "Plan": [plan]
                      })
          
                      # Append row
                      updated_df = pd.concat([df, new_row], ignore_index=True)
          
                      # Save back to Google Sheets
                      conn.update(worksheet="Sheet1", data=updated_df)
          
                      st.success(f"Account created successfully! Your ID is {user_id}. You can now log in.")
  
  
      
      if "vote" not in st.session_state:
          with col2: 
              if st.button("Login"):
                  vote("A")
          with col3:
              if st.button("Signup"):
                  vote("B")
      else:
          f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
