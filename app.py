import streamlit as st
import time

# 1. %%writefile 문구는 반드시 삭제 (이미 하셨을 거예요!)
# 2. 필수 라이브러리 임포트
st.set_page_config(layout="wide")

video_url = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/720/Big_Buck_Bunny_720_10s_5MB.mp4"

# --- State Management ---
STATE_START_BUTTON = "start_button"
STATE_COUNTDOWN = "countdown"
STATE_VIDEO_AND_FORM = "video_and_form" # 두 단계를 하나로 합침

if "app_state" not in st.session_state:
    st.session_state.app_state = STATE_START_BUTTON

# --- UI Layout --- (수연님의 기존 스타일 유지)
st.markdown("""
    <style>
        .countdown-text { font-size: 72px; font-weight: bold; color: #FF4B4B; text-align: center; }
        .consultation-form-container { background-color: #f0f2f6; padding: 30px; border-radius: 15px; margin-top: 30px; }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # 1. 초기 화면
    if st.session_state.app_state == STATE_START_BUTTON:
        st.write("상담하기 버튼을 눌러 영상을 시청하고 상담을 요청하세요.")
        if st.button("상담하기"):
            st.session_state.app_state = STATE_COUNTDOWN
            st.rerun()

    # 2. 카운트다운
    elif st.session_state.app_state == STATE_COUNTDOWN:
        st.write("<h3 style='text-align: center;'>영상을 보신 뒤 상담을 신청해주세요</h3>", unsafe_allow_html=True)
        placeholder = st.empty()
        for i in range(5, 0, -1):
            placeholder.markdown(f"<div class='countdown-text'>{i}</div>", unsafe_allow_html=True)
            time.sleep(1)
        placeholder.empty()
        st.session_state.app_state = STATE_VIDEO_AND_FORM # 다음 단계로 이동
        st.rerun()

    # 3. 비디오 + 상담 양식 (동시에 표시!)
    elif st.session_state.app_state == STATE_VIDEO_AND_FORM:
        st.write("<h3 style='text-align: center;'>교육 영상 시청</h3>", unsafe_allow_html=True)
        
        # 에러 났던 width 제거하고 출력
        st.video(video_url, format="video/mp4", autoplay=True) 

        # 영상 바로 아래에 상담 양식 배치
        st.markdown('<div class="consultation-form-container">', unsafe_allow_html=True)
        st.write("### 상담 요청")
        user_input = st.text_area("영상을 보신 후 문의 내용을 입력하세요.", height=150)
        if st.button("상담 내용 제출"):
            if user_input:
                st.success("접수되었습니다. 곧 연락드리겠습니다!")
                time.sleep(2)
                st.session_state.app_state = STATE_START_BUTTON
                st.rerun()
            else:
                st.warning("내용을 입력해주세요.")
        st.markdown('</div>', unsafe_allow_html=True)
