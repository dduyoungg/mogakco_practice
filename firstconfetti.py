import streamlit as st

st.set_page_config(page_title="코딩 성공!", page_icon="🎊")

# 1. 누적 횟수 (이건 브라우저를 끄기 전까지만 유지됨)
if 'count' not in st.session_state:
    st.session_state.count = 0

st.markdown("<h1 style='text-align: center;'>오늘 코딩 성공!</h1>", unsafe_allow_html=True)
st.write(f"<p style='text-align: center;'>현재 <b>{st.session_state.count}</b>번 축하받았습니다.</p>", unsafe_allow_html=True)

# 2. 버튼 클릭 시 동작
if st.button('여기를 눌러 풍선 날리기!', use_container_width=True):
    st.session_state.count += 1
    st.balloons()
