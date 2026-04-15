import streamlit as st
import time

st.set_page_config(layout="wide")
st.title("간단한 비디오 플레이어 앱")

st.write("### 샘플 비디오")

video_url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"

# 재생 버튼을 클릭하면 카운트다운 후 영상이 재생됩니다.
if st.button("영상 재생 시작"):
    countdown_placeholder = st.empty()
    for i in range(5, 0, -1):
        countdown_placeholder.markdown(f"<h1 style='text-align: center; color: red;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(1) # 1초 지연
    countdown_placeholder.empty() # 카운트다운 텍스트 제거
    st.video(video_url, format="video/mp4", start_time=0)
else:
    st.write("재생 버튼을 눌러주세요.")

# 파일 업로드 기능 추가 (옵션)
# st.write("### 또는 비디오 파일 업로드")
# uploaded_file = st.file_uploader("비디오 파일 선택", type=["mp4", "mov", "avi"])
# if uploaded_file is not None:
#    st.video(uploaded_file, format=uploaded_file.type)
