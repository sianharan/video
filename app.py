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
                width: 250px; /* Adjust width */
                height: 150px; /* Adjust height for both elements */
                background-color: rgba(0, 0, 0, 0.7);
                display: flex;
                flex-direction: column; /* Stack number and text vertically */
                justify-content: center;
                align-items: center;
                border-radius: 10px;
                margin: auto; /* Center the box */
                text-align: center; /* Center align text */
                padding: 10px; /* Add some padding */
            ">
                <h1 style='color: white; font-size: 48px; margin-bottom: 10px;'>{i}</h1>
                <p style='color: white; font-size: 16px; margin: 0;'>학부모 교육용 영상을 보신 뒤 상담을 신청하세요</p>
            </div>
            """
            countdown_placeholder.markdown(countdown_html, unsafe_allow_html=True)
            time.sleep(1)
        countdown_placeholder.empty() # 카운트다운 텍스트 제거

        # 카운트다운 후 비디오 재생 및 상담 영역 노출
        st.video(video_url)

        st.write("### 상담 요청")
        user_input = st.text_area("문의 내용을 입력하세요.", key="consultation_input")
        if st.button("상담 내용 제출", key="submit_consultation"):
            if user_input:
                st.success("상담 내용이 접수되었습니다. 곧 연락드리겠습니다!")
            else:
                st.warning("문의 내용을 입력해주세요.")

    else:
        st.write("상담하기 버튼을 눌러 영상을 시작하고 상담을 요청하세요.")

# 파일 업로드 기능 추가 (옵션)
# st.write("### 또는 비디오 파일 업로드")
# uploaded_file = st.file_uploader("비디오 파일 선택", type=["mp4", "mov", "avi"])
# if uploaded_file is not None:
#    st.video(uploaded_file, format=uploaded_file.type)
