import streamlit as st
st.title("My achievements")
col1, col2, col3=st.columns(3)
with col1:
    st.image("cert/es2022.jpg",caption="Edusave Scholarship Sec 1")
with col2:
    st.image("cert/emb12023.jpg",caption="Edusave Certificate of Academic Achievement Sec 2")
with col3:
    st.image("cert/emb22023.jpg",caption="Edusave Merit Bursary Sec 2")
col4,col5,col6=st.columns(3)
with col4:
    st.image("cert/alpchange2023.jpg",caption="Applied Learning Programme Changemaker Award Sec 2")
with col5:
    st.image("cert/alpchange2024.jpg",caption="Applied Learning Programme Changemaker Award Sec 3")
with col6:
    st.image("cert/alpstellar2024.jpg",caption="Applied Learning Programme Stellar Award Sec 3")
