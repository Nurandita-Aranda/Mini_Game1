import streamlit as st
import base64
import time

st.markdown("<h1 style='text-align: center; color: raisin black;'>Alchemist Diary</h1>", unsafe_allow_html=True)


#Musik
html_string = """
            <audio controls autoplay>
              <source src="Resource/BGM/Riverdel.mp3">
            </audio>
            """

sound = st.empty()
sound.markdown(html_string, unsafe_allow_html=True)
time.sleep(30)
sound.empty()


#Background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: 100%;
        background-position: top;
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
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('Resource/image/Night_sky.jpg')
