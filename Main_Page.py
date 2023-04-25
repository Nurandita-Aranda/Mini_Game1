import streamlit as st
import base64

st.markdown("<h1 style='text-align: center; color: raisin black;'>Alchemist Diary</h1>", unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: 120%;
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
add_bg_from_local('Resource/image/Night_sky.png')
