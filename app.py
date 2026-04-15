import streamlit as st
import time

st.set_page_config(layout="wide")
st.title("간단한 비디오 플레이어 앱")

video_url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"

# 콘텐츠를 중앙에 배치하기 위해 컬럼 사용 (대략 절반 너비)
col1, col2, col3 = st.columns([1, 2, 1])

with col2: # 모든 콘텐츠를 중앙 컬럼에 배치
    st.write("### 샘플 비디오")

    if st.button("상담하기"):
        # 카운트다운 로직
        countdown_placeholder = st.empty()
        for i in range(5, 0, -1):
            countdown_html = f"""
            <div style="
                width: 200px;
                height: 200px;
                background-color: rgba(0, 0, 0, 0.7);
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 10px;
                margin: auto; /* 박스를 중앙에 배치 */
            ">
                <h1 style='color: white; font-size: 80px; margin: 0;'>{i}</h1>
            </div>
            """
            countdown_placeholder.markdown(countdown_html, unsafe_allow_html=True)
            time.sleep(1)
        countdown_placeholder.empty() # 카운트다운 텍스트 제거

        # 카운트다운 후 비디오 재생 (16:9 비율, 폭 700px)
        st.video(video_url, format="video/mp4", start_time=0) # 16:9 비율 유지 (700 * 9 / 16 ≈ 394)
    else:
        st.write("상담하기 버튼을 눌러 영상을 시작하세요.")

# 파일 업로드 기능 추가 (옵션)
# st.write("### 또는 비디오 파일 업로드")
# uploaded_file = st.file_uploader("비디오 파일 선택", type=["mp4", "mov", "avi"])
# if uploaded_file is not None:
#    st.video(uploaded_file, format=uploaded_file.type)
