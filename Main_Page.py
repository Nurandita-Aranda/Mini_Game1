import streamlit as st

st.markdown("<h1 style='text-align: center; color: raisin black;'>Alchemist Diary</h1>", unsafe_allow_html=True)



#Background
content: "";
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: Resource/image/Night_sky.png
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
