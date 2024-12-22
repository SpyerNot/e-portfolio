import streamlit as st
st.title("My achievements")
col1, col2, col3=st.columns(3)
with col1:
    st.image("cert/es2022.jpg",caption="Edusave Scholarship Sec 1")
with col2:
    st.image("cert/emb22023.jpg")
    st.caption("Edusave Merit Bursary Sec 2")
with col3:
    st.image("cert/alpchange2023.jpg")
    st.caption("Applied Learning Programme Changemaker award Sec 2")
