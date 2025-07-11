import streamlit as st
import streamlit.components.v1 as components
option = st.radio("Pick a project you would like to view:",["Tackling Obesity","E-portfolio","Translator","Secret Santa"])
if option == "Tackling Obesity":
    st.link_button("Fitness app","https://designinnovationapp-4wh5oserqjkuznsnik2pwq.streamlit.app")
    st.link_button("Github Repo","https://github.com/SpyerNot/design_innovation_app")
    st.write("This is my project from the Design Innovation Challenge")
if option == "E-portfolio":
    st.write("***You are currently viewing the project E-portfolio, this e-portfolio is written in python***")
    st.link_button("Github Repo","https://github.com/SpyerNot/e-portfolio")
if option == "Translator":
    st.link_button("Translator App","https://translator-ixyqcckissjuf57apt9kec.streamlit.app/")
    st.link_button("Github repo", "https://github.com/SpyerNot/Translator")
    st.write("This is one of my hackathon project with my team to do audio to text translation")
if option == "Secret Santa":
    st.link_button("Secret Santa website", "https://secretsanta22.vercel.app/")
    st.link_button("Github repo","https://github.com/frosetrain/secretsanta")
    st.write("This is another of my hackathon project which is secret santa to promote giving gifts, I am added as the collaborator")




