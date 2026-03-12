import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="코딩 성공!", page_icon="🎊")

# 2. 메인 문구
st.markdown("<h1 style='text-align: center;'>오늘 코딩 성공!</h1>", unsafe_allow_html=True)

st.write("") # 간격 조절용 빈 줄

# 3. 버튼 및 효과
if st.button('여기를 눌러 폭죽 터뜨리기!', use_container_width=True):
    st.balloons()
