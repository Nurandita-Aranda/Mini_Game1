import streamlit as st

st.markdown("<h1 style='text-align: center; color: raisin black;'>Alchemist Diary</h1>", unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("Resource/style/bacground1.css")
