import streamlit as st

st.title("Alchemist Dairy")



#Background
content: "";
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: "Resource/image/Night_sky.png"
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://lh3.googleusercontent.com/21QuzfIwLY0Cz7dhez3Sw2IsTpChIzbCfdb4gTK4jIwk5U5K9L7KE_8g2p0btLBlKj5UMhsKFsLOBKkDphTf1l9uwTUMeKVDMV5dStHZasi_8S5X7w2HK1tBBvLFNMlHQdlJORWJwbt2W1-5toa7-bT9UK65Ue6GANgXP-TQqpRQr0_qJb4UbLriwuLi3rNX8igWXigfsmJZUTTrIhxDjOJupeqHZWLIZZnsw_eoZe_7WY_yYGFdadDBllr0Z4DygJLlxP5m22jgG7JtSXIDqV8j7aeFix9wwq8K4NnmISm8zSAjyzQdiLtNN2Ev9NoITWZ5oL-u--oBBUkI6xvYH7GWhrtEOhmbhJSPbVKVVpaVcgjn79ZqVdJE4GH2z3gE6Vps_Co7ExyHmMvkztJXqt5JF_hnJU7USkc_UaYC4fXr_tWsIHaUC-zn39bwXQMxn5Di_n8CpUQHMNSnVy7L8hFu4GcNDqVDE_nsTMU7fEM-cTyPUWmtsMGQADyeVtt07DP3beLwtDn-QZSSJJQ01Faaq1226WKSDhWHS-rRrjzq2azkf3XLDJUshUzFl4NFg-1RI2gnT8iKAKLUPgXVyGhkqTGEx3CVa9AnBur8lvwHb2Dl55jgv5Zuko4C5oENvs7Yk6bSHnVy2y_ezr_61IJ7Ln0SbbTYPz5TemHAnGzRWnKiOGLKZuu8r88UhrOpZ0zkQ8u6pxeIG_Rfkz1vOdXjZoc3y8jJ4SosUNhftyxP4smhMF3aHW_awrcGbyKtW4VhRH1RmJhvv_NYStRw-Z4MPheBmPnqquqrZnT4M1DeG7IiH3RKyewPB7J_s0ldDvzswq5VJwE59Ls9yPXjU40PT1RY1XEZxwPfvfFeDRI2Y57Lt0Pr1HvRKcH6hiL_oVfi14r3I4d-JAnyLiee9maLb5pkVwxsxoAiRbHnInpURwmPKw=w533-h780-s-no?authuser=0");
background-position: center; 
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
