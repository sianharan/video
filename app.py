import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(layout="wide")

# 2. 사용할 비디오 URL (10초짜리 MP4, 짤림 방지 로직 적용)
video_url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"

# 3. 사용자 지정 CSS
st.markdown("""
    <style>
        .video-container {
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
            overflow: hidden;
            max-width: 100%;
            background: black;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .video-container iframe, .video-container video {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%; border: 0;
        }
        .video-container + div {
            display: none !important;
            height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        div.stButton > button {
            background-color: #FF4B4B;
            color: white;
            padding: 18px 40px;
            font-size: 24px;
            border-radius: 50px;
            border: none;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        div.stButton > button:hover {
            background-color: #E03E3E;
            transform: scale(1.05);
        }
        .countdown-text { font-size: 80px; font-weight: bold; color: #FF4B4B; text-align: center; margin-top: 40px; }
        .consultation-form-container { 
            background-color: #f0f2f6; 
            padding: 30px; 
            border-radius: 15px; 
            margin-top: 0px !important; 
            box-shadow: 0 2px 5px rgba(0,0,0,0.1); 
        }
    </style>
""", unsafe_allow_html=True)

# --- State Management ---
STATE_START_BUTTON = "start_button"
STATE_COUNTDOWN = "countdown"
STATE_VIDEO_AND_FORM = "video_and_form"

if "app_state" not in st.session_state:
    st.session_state.app_state = STATE_START_BUTTON

# --- UI Layout ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.session_state.app_state == STATE_START_BUTTON:
        st.write("### 전문가 상담")
        st.write("아래 버튼을 눌러 교육 영상을 시청하고 상담을 신청하세요.")
        if st.button("상담 신청", key="start_btn"):
            st.session_state.app_state = STATE_COUNTDOWN
            st.rerun()

    elif st.session_state.app_state == STATE_COUNTDOWN:
        st.write("<h3 style='text-align: center;'>학부모 교육을 위한 영상을 시청 후 상담을 신청해주세요</h3>", unsafe_allow_html=True)
        placeholder = st.empty()
        for i in range(5, 0, -1):
            placeholder.markdown(f"<div class='countdown-text'>{i}</div>", unsafe_allow_html=True)
            time.sleep(1)
        placeholder.empty()
        st.session_state.app_state = STATE_VIDEO_AND_FORM
        st.rerun()

    elif st.session_state.app_state == STATE_VIDEO_AND_FORM:
        st.write("<h3 style='text-align: center;'>🎬 학부모 교육 영상 시청 중</h3>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class="video-container">
                <video controls autoplay>
                    <source src="{video_url}" type="video/mp4">
                </video>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="consultation-form-container">', unsafe_allow_html=True)
        st.write("### 📝 상담 요청")
        
        # [요청 반영] 안내 문구 삭제 및 placeholder(예시 문구) 빈칸 처리
        user_input = st.text_area("", placeholder="", height=150, key="consult_input")
        
        if st.button("상담 내용 제출", key="submit_btn"):
            if user_input:
                st.success("접수되었습니다! 연락드리겠습니다.")
                time.sleep(2.5)
                st.session_state.app_state = STATE_START_BUTTON
                st.rerun()
            else:
                st.warning("문의 내용을 입력해 주세요.")
        st.markdown('</div>', unsafe_allow_html=True)
