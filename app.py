import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(layout="wide")

# 2. 사용할 비디오 URL (10초짜리 MP4, 짤림 방지 로직 적용)
video_url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"

# 3. 사용자 지정 CSS: 영상 비율 유지, 예쁜 버튼, 중앙 정렬 등
st.markdown("""
    <style>
        /* [핵심] 짤림 방지 및 16:9 비율 유지 (검은 배경 처리) */
        .video-container {
            position: relative;
            padding-bottom: 56.25%; /* 16:9 비율 (9 / 16 = 0.5625) */
            height: 0;
            overflow: hidden;
            max-width: 100%; /* 너비는 꽉 차게 */
            background: black; /* 배경 검은색 (비는 공간 처리) */
            margin-bottom: 30px; /* 아래 양식과의 간격 */
            border-radius: 12px; /* 모서리 둥글게 */
            box-shadow: 0 4px 10px rgba(0,0,0,0.3); /* 그림자 효과 */
        }

        /* 컨테이너 안의 실제 비디오 스타일 */
        .video-container iframe,
        .video-container video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 0;
        }

        /* [요청 2] 예쁘고 직관적인 "상담 신청" 버튼 스타일 */
        div.stButton > button {
            background-color: #FF4B4B; /* 빨간색 (강조) */
            color: white;
            padding: 18px 40px; /* 크기 키우기 */
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 24px; /* 글씨 크기 키우기 */
            margin: 10px 2px;
            cursor: pointer;
            border-radius: 50px; /* 둥근 모서리 (타원형) */
            border: none;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2); /* 입체감 */
            transition: background-color 0.3s ease, transform 0.2s ease; /* 애니메이션 효과 */
        }
        div.stButton > button:hover {
            background-color: #E03E3E; /* 호버 시 약간 어둡게 */
            transform: scale(1.05); /* 약간 키우기 효과 */
        }

        /* 나머지 UI 요소 스타일 유지 */
        .countdown-text { font-size: 80px; font-weight: bold; color: #FF4B4B; text-align: center; margin-top: 40px; }
        .consultation-form-container { background-color: #f0f2f6; padding: 30px; border-radius: 15px; margin-top: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# --- State Management ---
STATE_START_BUTTON = "start_button"
STATE_COUNTDOWN = "countdown"
STATE_VIDEO_AND_FORM = "video_and_form" # 로직 통합 상태

if "app_state" not in st.session_state:
    st.session_state.app_state = STATE_START_BUTTON

# --- UI Layout ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # 1단계: 초기 화면
    if st.session_state.app_state == STATE_START_BUTTON:
        # [요청 1] "학습 안내" -> "전문가 상담" 문구 수정
        st.write("### 전문가 상담")
        st.write("아래 버튼을 눌러 교육 영상을 시청하고 상담을 신청하세요.")
        
        # [요청 2] 버튼 이름 변경 및 예쁜 스타일 적용 완료
        if st.button("상담 신청", key="start_btn"):
            st.session_state.app_state = STATE_COUNTDOWN
            st.rerun()

    # 2단계: 카운트다운
    elif st.session_state.app_state == STATE_COUNTDOWN:
        st.write("<h3 style='text-align: center;'>영상을 짤림 없이 보실 수 있도록 준비 중입니다</h3>", unsafe_allow_html=True)
        placeholder = st.empty()
        for i in range(5, 0, -1):
            placeholder.markdown(f"<div class='countdown-text'>{i}</div>", unsafe_allow_html=True)
            time.sleep(1)
        placeholder.empty()
        st.session_state.app_state = STATE_VIDEO_AND_FORM
        st.rerun()

    # 3단계: 비디오 + 상담 양식 (동시에 표시, 짤림 방지 적용!)
    elif st.session_state.app_state == STATE_VIDEO_AND_FORM:
        st.write("<h3 style='text-align: center;'>🎬 학부모 교육 영상 시청 중</h3>", unsafe_allow_html=True)
        
        # 🌟 핵심: CSS 컨테이너로 영상을 감싸서 비율 유지 및 짤림 방지 🌟
        st.markdown(f"""
            <div class="video-container">
                <video controls autoplay>
                    <source src="{video_url}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
        """, unsafe_allow_html=True)

        # 영상 아래에 상담 양식 배치 (스타일 유지)
        st.markdown('<div class="consultation-form-container">', unsafe_allow_html=True)
        st.write("### 📝 상담 요청")
        st.write("영상을 시청하신 후, 궁금한 점이나 상담 내용을 아래에 입력해 주세요.")
        user_input = st.text_area("문의 내용 (예: 전학 절차, 교육공학 적용 등)", height=150, key="consult_input")
        if st.button("상담 내용 제출", key="submit_btn"):
            if user_input:
                st.success("접수되었습니다! 전문가 수연님이 곧 연락드리겠습니다.")
                time.sleep(2.5) # 메시지 볼 시간 부여
                st.session_state.app_state = STATE_START_BUTTON
                st.rerun()
            else:
                st.warning("문의 내용을 입력해 주세요.")
        st.markdown('</div>', unsafe_allow_html=True)
