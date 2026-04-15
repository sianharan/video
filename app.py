import streamlit as st
import time

st.set_page_config(layout="wide")

video_url = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/720/Big_Buck_Bunny_720_10s_5MB.mp4" # New 10-second video

# 콘텐츠를 중앙에 배치하기 위해 컬럼 사용 (대략 절반 너비)
col1, col2, col3 = st.columns([1, 2, 1])

with col2: # 모든 콘텐츠를 중앙 컬럼에 배치
    # 버튼에 대한 사용자 지정 CSS 추가
    st.markdown("""
        <style>
            /* Streamlit 메인 콘텐츠 영역을 중앙으로 정렬 */
            .main > div {
                justify-content: center;
                align-items: center;
                display: flex;
                flex-direction: column;
            }
            .block-container {
                padding-top: 2rem; /* 상단 패딩 */
                padding-bottom: 2rem; /* 하단 패딩 */
                max-width: 900px; /* 중앙 콘텐츠 최대 너비 */
            }

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

            /* 카운트다운 팝업 스타일 */
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
                z-index: 1000; /* 다른 요소 위에 표시 */
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
                font-family: 'Roboto', sans-serif; /* 더 세련된 폰트 */
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

            /* 비디오 및 상담 양식 컨테이너 스타일 */
            .video-consultation-container {
                background-color: #f0f2f6; /* 밝은 회색 배경 */
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                margin-top: 30px; /* 버튼과 간격 */
            }
            .stVideo {
                border-radius: 10px; /* 비디오 모서리 둥글게 */
                overflow: hidden; /* 모서리 둥글게 적용 */
            }
        </style>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    if "show_consultation_flow" not in st.session_state:
        st.session_state.show_consultation_flow = False

    if st.button("상담하기", key="start_consultation"):
        st.session_state.show_consultation_flow = True
        # 버튼 클릭 후 즉시 카운트다운을 시작하여 화면이 전환되는 것처럼 보이게 함

    if st.session_state.show_consultation_flow:
        # 카운트다운 로직 (팝업 형태로 구현)
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
        countdown_placeholder.empty() # 카운트다운 텍스트 제거

        # 비디오 및 상담 영역 (팝업처럼 보이도록 스타일링)
        st.markdown('<div class="video-consultation-container">', unsafe_allow_html=True)
        st.video(video_url, format="video/mp4", start_time=0, loop=False, muted=False, width=700) # width for central column
        st.write("### 상담 요청")
        user_input = st.text_area("문의 내용을 입력하세요.", key="consultation_input")
        if st.button("상담 내용 제출", key="submit_consultation"):
            if user_input:
                st.success("상담 내용이 접수되었습니다. 곧 연락드리겠습니다!")
                st.session_state.show_consultation_flow = False # 제출 후 상태 초기화 또는 다른 페이지로 리다이렉트
            else:
                st.warning("문의 내용을 입력해주세요.")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.write("상담하기 버튼을 눌러 영상을 시작하고 상담을 요청하세요.")
