import streamlit as st

st.set_page_config(page_title="코딩 성공!", page_icon="🎊")

# 1. 누적 횟수를 저장할 '세션 상태' 초기화
if 'count' not in st.session_state:
    st.session_state.count = 0

st.markdown("<h1 style='text-align: center;'>오늘 코딩 성공!</h1>", unsafe_allow_html=True)

# 2. 누적 횟수 표시
st.write(f"<p style='text-align: center; font-size: 1.5rem;'>현재 총 <b>{st.session_state.count}</b>번 축하받았습니다!</p>", unsafe_allow_html=True)

if st.button('여기를 눌러 풍선 날기!', use_container_width=True):
    st.session_state.count += 1  # 클릭할 때마다 1씩 증가
    st.balloons()
    st.rerun() # 화면을 다시 그려서 숫자를 업데이트
