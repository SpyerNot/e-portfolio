import streamlit as st
st.title("My projects")
st.markdown("Open the popover")
popover = st.popover("Open me up!!")
tackling_obesity = popover.radio("Tacking Obesity project")
my_portfolio = popover.radio("My e-portfolio project")
if tackling_obesity:
    st.link_button("Fitness app", "https://designinnovationapp-4wh5oserqjkuznsnik2pwq.streamlit.app")
    st.link_button("Github repo","https://github.com/SpyerNot/design_innovation_app")
else:
    st.write("I wrote this e-portfolio from scratch using python so no app link is provided since your already here :D")
    st.link_button("Github repo","https://e-portfolio-8wugkwxplflpwfpwjzgirj.streamlit.app")


