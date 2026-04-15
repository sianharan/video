import streamlit as st
import time

st.set_page_config(layout="wide")

video_url = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/720/Big_Buck_Bunny_720_10s_5MB.mp4" # 10초 길이의 비디오

# --- State Management --- (상태 관리)
# Define states (앱의 현재 단계를 정의합니다)
STATE_START_BUTTON = "start_button"
STATE_COUNTDOWN = "countdown"
STATE_VIDEO = "video"
STATE_CONSULTATION_FORM = "consultation_form"

# Initialize state if not present (앱 상태가 없으면 초기 상태로 설정합니다)
if "app_state" not in st.session_state:
    st.session_state.app_state = STATE_START_BUTTON

# --- UI Layout --- (UI 레이아웃)
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

            /* 카운트다운 텍스트 스타일 (오버레이가 아닌 일반 텍스트) */
            .countdown-text {
                font-size: 72px; /* 큰 숫자 */
                font-weight: bold;
                color: #FF4B4B; /* 빨간색으로 강조 */
                text-align: center;
                margin-top: 50px;
            }
            .countdown-message {
                font-size: 24px; /* 메시지 폰트 크기 */
                line-height: 1.4;
                text-align: center;
                margin-bottom: 30px;
                color: #555555;
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

    # --- State Logic --- (상태별 로직 처리)

    # 1. 초기 '상담하기' 버튼 표시
    if st.session_state.app_state == STATE_START_BUTTON:
        st.markdown("<br>" * 5, unsafe_allow_html=True)
        st.write("상담하기 버튼을 눌러 영상을 시청하고 상담을 요청하세요.")
        if st.button("상담하기", key="start_consultation"):
            st.session_state.app_state = STATE_COUNTDOWN # 상태를 카운트다운으로 변경
            st.rerun() # 앱을 다시 실행하여 새 상태 반영

    # 2. 카운트다운 표시
    elif st.session_state.app_state == STATE_COUNTDOWN:
        st.write("<h3 style='text-align: center;'>학부모 교육을 위한 영상을 보신 뒤 상담을 신청해주세요</h3>", unsafe_allow_html=True)
        countdown_placeholder = st.empty()
        for i in range(5, 0, -1):
            countdown_placeholder.markdown(f"<div class='countdown-text'>{i}</div>", unsafe_allow_html=True)
            time.sleep(1) # 1초씩 UI를 블록하여 카운트다운을 시각적으로 보여줍니다.
        countdown_placeholder.empty() # 카운트다운 완료 후 메시지 제거
        st.session_state.app_state = STATE_VIDEO # 상태를 비디오 재생으로 변경
        st.rerun() # 앱을 다시 실행하여 새 상태 반영

    # 3. 비디오 재생
    elif st.session_state.app_state == STATE_VIDEO:
        st.write("<h3 style='text-align: center;'>교육 영상 시청 중</h3>", unsafe_allow_html=True)
        st.video(video_url, format="video/mp4", start_time=0, loop=False, muted=True, autoplay=True, width=700)

        # 비디오 재생 시간을 시뮬레이션 (10초 동안 UI 블록) - 이 부분을 제거하여 비디오가 바로 재생되도록 합니다.
        # time.sleep(10) # 비디오가 재생되는 동안 UI를 10초간 블록합니다.
        st.session_state.app_state = STATE_CONSULTATION_FORM # 상태를 상담 양식으로 변경
        st.rerun() # 앱을 다시 실행하여 새 상태 반영

    # 4. 상담 양식 표시
    elif st.session_state.app_state == STATE_CONSULTATION_FORM:
        st.markdown('<div class="consultation-form-container">', unsafe_allow_html=True)
        st.write("### 상담 요청")
        user_input = st.text_area("문의 내용을 입력하세요.", key="consultation_input_form", height=150)
        if st.button("상담 내용 제출", key="submit_consultation_form"):
            if user_input:
                st.success("상담 내용이 접수되었습니다. 곧 연락드리겠습니다!")
                st.session_state.app_state = STATE_START_BUTTON # 초기 상태로 돌아감
                st.rerun()
            else:
                st.warning("문의 내용을 입력해주세요.")
        st.markdown('</div>', unsafe_allow_html=True)
