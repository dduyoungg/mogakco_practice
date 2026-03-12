import streamlit as st

# 1. 페이지 설정 (브라우저 탭에 뜨는 이름)
st.set_page_config(page_title="오늘 코딩 성공!", page_icon="🎉")

# 2. 화면에 크게 제목 띄우기 (HTML의 <h1> 역할)
st.markdown("""
    <style>
    .main-title {
        color: #2e7d32;
        font-size: 4rem;
        font-weight: bold;
        text-align: center;
        margin-top: 20%;
    }
    .sub-title {
        color: #4caf50;
        font-size: 1.5rem;
        text-align: center;
    }
    .stApp {
        background-color: #e8f5e9;
    }
    </style>
    <div class="main-title">🎉 오늘 코딩 성공!</div>
    <div class="sub-title">수영님의 브라우저 생성을 축하합니다.</div>
    """, unsafe_allow_html=True)

# 3. Streamlit만의 특별한 축하 효과 (풍선이 펑펑 터집니다!)
st.balloons()
