import streamlit as st
st.set_page_config(page_title="Scholarra", layout="wide")

# Top bar
col1, col2, col3, col4 = st.columns([1,2,2,1])  


with col2:
    st.markdown("### 🏠 Home")
with col3:
    st.markdown("### 📚 Courses")
st.markdown('<h1 style="font-size:70px">Welcome, User.</h1>', unsafe_allow_html=True)
