import streamlit as st
st.set_page_config(page_title="Home page")
st.title("Low Li Wen's e-portfolio")
st.write("Welcome to my portfolio, lets take a look at the different option")
st.page_link("home.py",label="home",icon="🏠")
st.page_link("pages/about me.py",label="About me :D",icon="😎")
st.page_link("pages/projects.py",label="My projects",icon="💻")
st.page_link("pages/achievements.py",label="My achievements",icon="🏆")
