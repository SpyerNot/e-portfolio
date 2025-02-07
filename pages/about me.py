import streamlit as st
st.html("<style>.name{font-family: 'Lucida Handwriting', cursive;}</style>")
st.html("<style>h1{font-size: 40px;}</style>")
st.html("<h1><b>About Me!</b></h1>")
col1,col2,col3 = st.columns(3)
with col1:
    st.html("<p id = 'name', align = 'left'>My name is <span class='name'>Low Li Wen </span> from Serangoon Garden Secondary School I am from Robotics CCA that likes to code. I have learnt the coding languages: Python and Javascript. The markup language HTML and the style sheet CSS. I am a student that likes to smile and laugh a lot in hopes to make other people smile :D ")
st.html("<div></div>")
st.html("<h1 align = 'right'><b>My Passion!</b></h1>")
with col3:
    st.html("<p id = 'passion'>My passion started around 8 years old, I went for different workshops for microbit, scratch, airblock drone and sphero when I was in primary school. After stepping into secondary school, my CCA was robotics to further pursue my passion in coding, in CCA we did scratch, microbit and tello drone. At upper secondary, my school offered O-Level Computing so I took this subject and started learning python coding. At the end of the year, I got top in computing. During my Sec 3 year, I signed up for multiple workshop. For example, BuildingBloCS March,June and December conference. I also took up a few competitions which include hackathon and CTF. </p>") 


