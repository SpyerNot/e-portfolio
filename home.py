import streamlit as st
st.set_page_config(page_title="Home page")
st.title("Low Li Wen's e-portfolio")
st.write("Lets look at the different options in my e-portfolio")
st.page_link("home.py",label="Home",icon="🏠")
st.page_link("pages/about me.py",label="About me :D",icon="😎")
st.page_link("pages/projects.py",label="My projects",icon="💼")
st.page_link("pages/achievements.py",label="Achievements",icon="🏆")
st.divider()
cybersec = "https://docs.google.com/document/d/1PaYX0i1-vBfCUTf_upenT20NChQDB5nj/edit?usp=sharing&ouid=104159583048794347910&rtpof=true&sd=true"
ict="https://docs.google.com/document/d/1PenPIkocIHWqWuSZoc0WKQHKJDJXGnZ2/edit?usp=sharing&ouid=104159583048794347910&rtpof=true&sd=true"
clw="https://docs.google.com/document/d/1P_lwAi3vWpR7oyutGNJnFxixdEStPJld/edit?usp=sharing&ouid=104159583048794347910&rtpof=true&sd=true"
col1,col2,col3=st.columns(3)
with col1:
    st.markdown(
        f'<iframe src="{cybersec}&rm=minimal" width="800" height="600"></iframe>',
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        f'<iframe src="{ict}&rm=minimal" width="800" height="600"></iframe>',
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        f'<iframe src="{clw}&rm=minimal" width="800" height="600"></iframe>',
        unsafe_allow_html=True,
    )
st.write("If you got any queries, contact me at lowliwen2409@gmail.com")
