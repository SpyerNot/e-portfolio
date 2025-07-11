import streamlit as st
from PIL import Image 
Image.MAX_IMAGE_PIXELS = 1000000000 
st.title("My Achievements")
col1, col2, col3=st.columns(3)
with col1:
    st.image("cert/es2022.jpg",caption="Edusave Scholarship 2022 (Sec 1)")
with col2:
    st.image("cert/emb12023.jpg",caption="Edusave Certificate of Academic Achievement 2023 (Sec 2)")
with col3:
    st.image("cert/emb22023.jpg",caption="Edusave Merit Bursary 2023 (Sec 2)")
col4,col5,col6=st.columns(3)
with col4:
    st.image("cert/eagles2023.jpg",caption="Edusave Award for Achievement, Good Leadership and Service 2023 (Sec 2)")
with col5:
    st.image("cert/alpchange2023.jpg",caption="Applied Learning Programme Changemaker Award 2023 (Sec 2)")
with col6:
    st.image("cert/alpchange2024.jpg",caption="Applied Learning Programme Changemaker Award 2024 (Sec 3)")
col7,col8,col9=st.columns(3)
with col7:
    st.image("cert/alpinnov2024.jpg",caption="Applied Learning Programme Innovation Award 2024 (Sec 3)")
with col8:
    st.image("cert/alpstellar2024.jpg",caption="Applied Learning Programme Stellar Award 2024 (Sec 3)")
with col9:
    st.image("cert/dic2024.jpg",caption="S1 Design Innovation Challenge 2024 2nd prize (Sec 3)",width=160)
col10,col11,col12=st.columns(3)
with col10:
    st.image("cert/marchconf.png",caption="BuildingBloCS Participation March Conference Hackathon 2024 (Sec3)")
with col11:
    st.image("cert/marchhack.png",caption="BuildingBloCS March Conference Hackathon 2024, First Place (Sec 3)")
with col12:
    st.image("cert/juneconf.png",caption="BuildingBloCS June Conference 2024 (Sec 3)")
col13,col14,col15=st.columns(3)
with col13:
    st.image("cert/junehack.png",caption="BuildingBloCS June Conference Hackathon 2024 (Sec 3)")
with col14:
    st.image("cert/decconf.png",caption="BuildingBloCS December Conference 2024 (Sec 3)")
with col15:
    st.image("cert/dechack.png",caption="BuildingBloCS December Conference Hackathon 2024 (Sec 3) ")
col16,col17,col18=st.columns(3)
with col16:
    st.image("cert/top2024.jpg",caption="Top in Computing 2024 (Sec 3)")
with col17:
    st.image("cert/ybnctf2024.jpg",caption="Yes But No Capture the Flag 2024 (Sec 3)")
with col18:
    st.image("cert/nypcyber2025.png",caption="NYP course taster workshop for Cybersecurity and Digtial Forensics (Sec 4)")
col19,col20,col21=st.columns(3)
with col19:
    st.image("cert/nypsoft2025.png",caption="NYP course taster workshop for Information Technology (Sec 4)")
with col20:
    st.image("cert/IDE2024.png",caption="IDE Series Competition (Sec 3)")
with col21:
    st.image("cert/marchhack2025.png",caption="BuildingBloCS March Conference Hackathon 2025 (Sec 4)")
col22,col23,col24=st.columns(3)
with col22:
    st.image("cert/juneconf2025.png",caption="BuildingBloCS June Conference 2025 (Sec 4)")
with col23:
    st.image("cert/junehack2025.png",caption="BuildingBloCS June Conference Hackathon 2025 (Sec 4)")
with col24:
    st.image("cert/YCEP2025.png",caption="YCEP Bootcamp 2025 participation certificate at NYP (Sec 4)")
col25,col26,col27=st.columns(3)
with col25:
    st.image("cert/YCEP2025indiv.png",captions="YCEP Finals 2025 Individual Category (Sec 4)")
with col26:
    st.image("cert/Low Li Wen_Certificate_of_Excellence_Group.png",caption="YCEP Finals 2025 6th Place for Group Category (Sec 4)")
