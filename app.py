%%writefile app.py
import streamlit as st
import time

st.set_page_config(layout="wide")

# Reverting to the previous video URL as requested by the user
video_url = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/720/Big_Buck_Bunny_720_10s_5MB.mp4"

# 콘텐츠를 중앙에 배치하기 위해 컬럼 사용 (대략 절반 너비)
col1, col2, col3 = st.columns([1, 2, 1])

with col2: # 모든 콘텐츠를 중앙 컬럼에 배치
    # 사용자 지정 CSS 추가
    st.markdown("""
        <style>
            /* Streamlit 메인 콘텐츠 영역 조정 */
            .main > div {
                /* 기본 플로우를 위해 수직 중앙 정렬 제거 */
            }
            .block-container {
                padding-top: 2rem; /* 상단 패딩 */
                padding-bottom: 2rem; /* 하단 패딩 */
                max-width: 900px; /* 중앙 콘텐츠 최대 너비 */
            }

            /* 상담하기 버튼 스타일 */
            div.stButton > button:first-child {
                background-color: #4CAF50; /* 초록색 */
                color: white;
                padding: 15px 30px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 20px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 12px;
                border: none;
                font-weight: bold;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
                transition: background-color 0.3s ease;
            }
            div.stButton > button:first-child:hover {
                background-color: #45a049;
            }

            /* 카운트다운 팝업 스타일 (비디오 팝업 위에 뜸) */
            .countdown-overlay {
                position: fixed; /* 고정 위치 */
                top: 0;
                left: 0;
                width: 100vw; /* 전체 너비 */
                height: 100vh; /* 전체 높이 */
                background-color: rgba(0, 0, 0, 0.8); /* 어두운 배경 */
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 1000; /* 가장 위에 표시 */
            }
            .countdown-box {
                width: 300px; /* 조정된 너비 */
                height: 200px; /* 조정된 높이 */
                background-color: rgba(40, 40, 40, 0.9); /* 어두운 회색 배경 */
                border-radius: 15px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.4);
                color: white;
                font-family: 'Roboto', sans-serif;
            }
            .countdown-number {
                font-size: 72px; /* 큰 숫자 */
                font-weight: bold;
                margin-bottom: 15px;
            }
            .countdown-message {
                font-size: 18px; /* 메시지 폰트 크기 */
                line-height: 1.4;
            }

            /* 상담 양식 컨테이너 스타일 (비디오 종료 후 표시) */
            .consultation-form-container {
                background-color: #f0f2f6; /* 밝은 회색 배경 */
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                margin-top: 50px; /* 상단에서 간격 */
                max-width: 900px;
                width: 100%;
            }
        </style>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    # State initialization
    if "show_start_button" not in st.session_state:
        st.session_state.show_start_button = True
    if "show_video_and_form" not in st.session_state:
        st.session_state.show_video_and_form = False

    # 1. Show initial "상담하기" button
    if st.session_state.show_start_button:
        st.markdown("<br>" * 5, unsafe_allow_html=True) # Add some initial vertical space
        st.write("상담하기 버튼을 눌러 영상을 시청하고 상담을 요청하세요.")
        if st.button("상담하기", key="start_consultation"):
            st.session_state.show_start_button = False
            st.session_state.show_video_and_form = True
            st.rerun() # Rerun to immediately show the video and form

    # 2. Show Video and Consultation Form
    if st.session_state.show_video_and_form:
        # Display video first, so the countdown can overlay it
        st.video(video_url, format="video/mp4", start_time=0, loop=False, muted=True, autoplay=True, width=700)

        # Countdown layer - this will appear on top of the video due to CSS
        countdown_placeholder = st.empty()
        for i in range(5, 0, -1):
            countdown_html = f"""
            <div class="countdown-overlay">
                <div class="countdown-box">
                    <div class="countdown-number">{i}</div>
                    <div class="countdown-message">학부모 교육용 영상을 보신 뒤 상담을 신청하세요</div>
                </div>
            </div>
            """
            countdown_placeholder.markdown(countdown_html, unsafe_allow_html=True)
            time.sleep(1)
        countdown_placeholder.empty() # Remove countdown layer

        # Consultation Form
        st.markdown('<div class="consultation-form-container">', unsafe_allow_html=True)
        st.write("### 상담 요청")
        user_input = st.text_area("문의 내용을 입력하세요.", key="consultation_input_form", height=150)
        if st.button("상담 내용 제출", key="submit_consultation_form"):
            if user_input:
                st.success("상담 내용이 접수되었습니다. 곧 연락드리겠습니다!")
                st.session_state.show_video_and_form = False # Hide video and form
                st.session_state.show_start_button = True # Go back to the initial state
                st.rerun()
            else:
                st.warning("문의 내용을 입력해주세요.")
        st.markdown('</div>', unsafe_allow_html=True)
