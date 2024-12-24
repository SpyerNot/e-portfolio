import streamlit as st
st.title("My projects")
st.markdown("Open the popover")
popover = st.popover("Open me up!!")
tackling_obesity = popover.checkbox("Tacking Obesity project")
my_portfolio = popover.checkbox("My e-portfolio project")
if tackling_obesity:
    st.link_button("Fitness app", "https://designinnovationapp-4wh5oserqjkuznsnik2pwq.streamlit.app")
    st.link_button("Github repo","https://github.com/SpyerNot/design_innovation_app")
if my_portfolio:
    st.write("I wrote this e-portfolio from scratch using python so no app link is provided since you are already here :D")
    st.link_button("Github repo","https://e-portfolio-8wugkwxplflpwfpwjzgirj.streamlit.app")
option = st.radio("Pick a project you would like to view:",["Tackling Obesity","E-portfolio"])
if option == "Tackling Obesity":
    st.html("<a href='https://designinnovationapp-4wh5oserqjkuznsnik2pwq.streamlit.app/'> Fitness App </a>")
    st.html("<a href='https://github.com/SpyerNot/design_innovation_app'>Github repo</a>")
if option == "E-portfolio":
    st.write("***You are currently viewing thr project E-portfolio, this e-portfolio is written in python***")
    st.html("<a href='https://e-portfolio-8wugkwxplflpwfpwjzgirj.streamlit.app'>Github repo</a>")

