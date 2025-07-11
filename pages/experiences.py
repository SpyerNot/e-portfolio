import streamlit as st
from streamlit_timeline import timeline
st.title("My Experiences")
st.set_page_config(page_title="Test Basic Timelines", layout="wide")
with open('timeline.json','r') as f:
    data = f.read()
timeline(data,height=600)
