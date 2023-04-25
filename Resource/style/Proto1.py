import streamlit as st
height=720


st.title("Easy Chemistry")

# Sidebar
add_tombol_1= st.sidebar.button ("sign in")
add_tombol_2= st.sidebar.button ("sign up")
with st.sidebar:
    st.button("Help")
    st.button("About Us")
    


#tab
tab1, tab2, tab3, tab4 = st.tabs(["Materi","Mini Game", "Quiz", "Kalkulator"])
with tab1:
   st.header("Gaia Library")
   st.subheader("Apa yang mau kamu pelajari hari ini?")
   tab_1, tab_2, tab_3, tab_4, tab_5 = st.tabs(["Kimia Dasar","Analisis Jenis", "Titrimetri", "Kimia Organik", "Analisis Fisik"])
   with tab_1:
        st.caption('Pilih materi yang kamu mau')
        tombol1 = st.button("Tabel Periodik")
        if tombol1:
            st.image("https://lh3.googleusercontent.com/a8x3WJ8kZDyrjR-C3I-XWAp4u9HdYHKFz7zXL5uK3uOjLh6d1OClItacf7OQj9AiZ6YV40CcncUNlnHOuIZmicSgoxFati1SfNzeOzvR6wesSUhMduXAVhES8Y9OD6_kLfoWhot2bqgxL3X-EryeubaaQ0Q5d9t3IHfojruyUqpQPjdhjGGlFJKD66koTJdSNCl-i8_D0tPhhqJn5WBrJRKS4m_bxfcvaTd2_ERyf8rXCt3Ncu_3OAXMzf1_QggvGdF9cVHTrJ2mdC7a4WA73M4dt75FUBwvHk1FDLN-mh8reOZpMKk2oesdsFW5ByK82xlIrFft8s764xfiEbhwAJCnLhVjEfn87OnEZmjxvGy5kXCbE3LC09PXEp_ieWUqhsyuTSad9RmsC_Jop6zrXj0TqEs3OD1Kt-PyKR2Wn28DkG9PCNsQumhB9WJc37dXwvDRYVM2D2AVui-6uEd8hmF7eGFm9t6KchG0gX884KD-HqyBL-fbDDHy_vZJVein_rq92fxxPJZPyJDdYk1Gur9JWFIjFLBvo059jeG8QCXAmUL2I0skt7iTm3ACFFjikMLo2f9yvS9ep2Ri_L2CdDckE2cl3ibf6YTMJSsxxLDz39vv5yWRiOb9itt6nCE57Ezo9scfcfhHF-Oy55fgT-YrgEEsWWLf5n6rdQIud7eqAMcPsAaWYjEfQBGz2tXbcRMirFvF0k9o4ISr2crLaxFbqFNt5dOScrxnb8MomizQpd-Q_0QYCEWgTkKxPrKFcwipEKGIyOLfjCPQf6by38S0hpRhTweWwujB88UtO25KC3ukSHDzl2LJo_PW-m0wFIm_hQFIZcfaYUzeFC1qFongwmFzHvjRT23R7JZrcYVGoWOJCYorTmKrBdVmil9Jt9y4s-F9LjE99Ani6NjmpaPdbGYNAlUYpLy4Igs7KSvK1ttGbQ=w740-h416-no?authuser=0")
            tombol_11 = st.button('golongan 1')
            tombol_12 = st.button('golongan 2')
            tombol_13 = st.button('golongan 3')
            tombol_14 = st.button('golongan 4')
            tombol_15 = st.button('golongan 5')
            tombol_16 = st.button('golongan 6')
            tombol_17 = st.button('golongan 7')
            tombol_18 = st.button('golongan 8')
   
   with tab_2:
        st.caption('Pilih materi yang kamu mau')
        tombol1 = st.button("Identifikasi zat dengan cara kering")
        tombol2 = st.button("Pembuatan Larutan")
        tombol3 = st.button("Identifikasi kation golongan I-V")
        tombol4 = st.button("Identifikasi Anion")
   with tab_3:
        st.caption('Pilih materi yang kamu mau')
        tombol1 = st.button("Pemilihan Indikator")
        tombol2 = st.button("Titrasi asam basa")
        tombol3 = st.button("Titrasi Redoks")
   with tab_4:
        st.caption('Pilih materi yang kamu mau')
        tombol1 = st.button("Pendahuluan")
        tombol2 = st.button("Alkana & Sikloalkana")
        tombol3 = st.button("Alkena & Siklodiena")
        tombol4 = st.button("Alkuna")
        tombol5 = st.button("Stereokimia")
        tombol6 = st.button("Senyawa Aromatik")
   with tab_5:
        st.caption('Pilih materi yang kamu mau')


        
with tab2:
    st.header("Alchemist Diary")
    st.subheader("Mari berpetualang di kerajaan kimia")

with tab3:
   st.header("Chimeía Grandprix")
   st.subheader("Siap mengetes kemampuanmu dan menjadi yang terbaik?")
   st.caption("pilih level mu")
   tombol_1= st.button ("easy")
   if tombol_1:
        option= st.selectbox(
            "pilih salah satu",
            ("kimia dasar","analisis jenis","kimia organik"))
            
   tombol_2= st.button ("medium")
   if tombol_2:
        option= st.selectbox(
            "pilih salah satu",
            ("kimia dasar","analisis jenis","kimia organik"))
            
   tombol_3= st.button("hard")
   if tombol_3:
        option= st.selectbox(
            "pilih salah satu",
            ("kimia dasar","analisis jenis","kimia organik"))
    
with tab4:
   st.header("CHEMISCULATOR")
   st.subheader("Kalkulator buat kamu yang suka kimia")
   st.caption("Apa yang mau kamu hitung hari ini?")
   tombol_1 = st.button("Molaritas")
   tombol_2 = st.button("% Kadar")
   if tombol_2:
       option = st.selectbox(
           "Pilih salah satu",
           ("% Kadar (v/v)","% Kadar (b/v)","% Kadar (b/b)"))
   tombol_3 = st.button("BM atau AR")

#Coba-coba background
content: "";
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://lh3.googleusercontent.com/tH4S7FiLIhjyIniFg7qZd0XjSuEpR96guv_J9t-ZpdkfF8roKG40u--ycdwToGsBE9BeLN-jjjbfxcsZLH3dYGk8iyXrHfkq9sLACMwPfC5kERONPQltqd6TVUg8vQzVhhM5qMsYstQgZ9GCxaj7qrjyRelzoA6mFIkbFpgajasX2WrfT5mCgTRccPQW0kBqBjAT-6bcgiyPUlva8sbh0UiKeal4zFCp09v8cbQl5qwGO-8ubE_fYrLrAca8V-7oCHhD9IGN9xokqjzHhCzMc9zue5XeRjvOSqgv9kCEn76ZuFAvc9QVWISrvvAV0mdPOve5RnT1fWKnc_tXW6A79LPSkHbbgfjVT0OmnvTphEnuqrT1_E-nS-OwCK5vTiA0Qz4MAwaEtHaTHY7B1E8zTFWLfZHcKjCRAcBssMu4q7k6Bf-Wd-J5kn4efe-39K5EAvE6K9SNdk4R9sHS9JHnVsCpDZHrmuft0wC845u_zaJQfC5ZJlajreGHGe9cCGnpp_1aPgWcpyKbIUmTJPG35x7Q85bHAwltTzGBijUKEG8iI8xum9N19NwXU4Q7FvtHzDS8fbCJJNbYQUVzvY2duM_aV_wZy8pMMnAYs9JsO5gLQ1yRtfhvRSsUEbSI7aTne7dtONeYnZgXhCy8EJhvhnvWNxfP78JpqVriKxoIHDDywKmbxszH2snwMI3a7OMc5QDHULVnt6zHZ2BFd_eWedCPzhKqNdU3-sT72u2NuElPv-OzXHlWXFrsfTJXN1IiwBK7icfrXiL73emCnRgjKdhgOZX3x81YInDlP9SFVsbAehBkIgv6rnUijgIsA1CPXYlGfkNzweaxYfF70Ztb4bA8cqIHAOXZEqpjbeNsRNI-hERRzJJrBWtTA6d9QrfS479qOY6nQ9mRuWzOAY-VDS3k_qWOMwqvhHmVqTlNI5muLp4yig=w1422-h780-s-no?authuser=0");
background-size: 180%;
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
