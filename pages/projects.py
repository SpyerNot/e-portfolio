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
    st.link_button("Github repo","https://github.com/SpyerNot/e-portfolio")
option = st.radio("Pick a project you would like to view:",["Tackling Obesity","E-portfolio"])
if option == "Tackling Obesity":
    st.link_button("Fitness app","https://designinnovationapp-4wh5oserqjkuznsnik2pwq.streamlit.app")
    st.link_button("Github Repo","https://github.com/SpyerNot/design_innovation_app")
if option == "E-portfolio":
    st.write("***You are currently viewing the project E-portfolio, this e-portfolio is written in python***")
    st.link_button("Github Repo","https://github.com/SpyerNot/e-portfolio")

