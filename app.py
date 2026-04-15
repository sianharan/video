import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(layout="wide")

# 2. 사용할 비디오 URL
video_url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"

# 3. 강력한 CSS: 상단 간격 확보 및 짤림 방지
st.markdown("""
    <style>
        /* [수정] 전체 컨테이너 상단 여백을 넉넉하게 (5rem) */
        .block-container { 
            padding-top: 5rem !important; 
            padding-bottom: 2rem; 
        }

        /* [수정] 타이틀 글자가 짤리지 않도록 하단 여백 추가 */
        h3 {
            margin-bottom: 1.5rem !important;
            line-height: 1.6 !important;
            padding: 10px 0;
        }

        .video-container {
            position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;
            max-width: 100%; background: black; border-radius: 12px 12px 0 0;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3); margin-bottom: 0px !important;
        }
        .video-container video { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0; }

        /* 영상과 폼 사이의 간격만 0으로 유지 */
        [data-testid="stVerticalBlock"] > div:has(div.video-container) + div { display: none !important; }
        
        /* [수정] 전체 gap을 0으로 만드는 대신, 특정 요소들만 밀착 */
        .stVerticalBlock { gap: 1rem !important; } /* 기본 간격은 조금 둡니다 */

        .consultation-form-container { 
            background-color: #f0f2f6; padding: 30px; border-radius: 0 0 15px 15px;
            margin-top: -1rem !important; /* 영상과 강제로 밀착 */
            box-shadow: 0 2px 5px rgba(0,0,0,0.1); 
        }

        .guide-text {
            font-size: 16px;
            color: #666666;
            margin-bottom: 10px;
            margin-top: 5px;
        }

        div.stButton > button {
            background-color: #FF4B4B; color: white; padding: 18px 40px;
            font-size: 24px; border-radius: 50px; border: none; font-weight: bold;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2); transition: background-color 0.3s ease, transform 0.2s ease;
        }
        div.stButton > button:hover { background-color: #E03E3E; transform: scale(1.05); }
        
        .countdown-text { 
            font-size: 80px; font-weight: bold; color: #FF4B4B; 
            text-align: center; margin-top: 20px; 
        }
    </style>
""", unsafe_allow_html=True)

# --- State Management ---
if "app_state" not in st.session_state:
    st.session_state.app_state = "start_button"

# --- UI Layout ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.session_state.app_state == "start_button":
        st.write("### 전문가 상담")
        st.write("아래 버튼을 눌러 교육 영상을 시청하고 상담을 신청하세요.")
        if st.button("상담 신청", key="start_btn"):
            st.session_state.app_state = "countdown"
            st.rerun()

    elif st.session_state.app_state == "countdown":
        st.write("<h3 style='text-align: center;'>학부모 교육을 위한 영상을 시청 후<br>상담을 신청해주세요</h3>", unsafe_allow_html=True)
        placeholder = st.empty()
        for i in range(5, 0, -1):
            placeholder.markdown(f"<div class='countdown-text'>{i}</div>", unsafe_allow_html=True)
            time.sleep(1)
        placeholder.empty()
        st.session_state.app_state = "video_and_form"
        st.rerun()

    elif st.session_state.app_state == "video_and_form":
        st.write("<h3 style='text-align: center;'>🎬 학부모 교육 영상 시청 중</h3>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="video-container">
                <video controls autoplay><source src="{video_url}" type="video/mp4"></video>
            </div>
        """, unsafe_allow_html=True)

        # 상담 양식 영역
        st.markdown('<div class="consultation-form-container">', unsafe_allow_html=True)
        st.write("### 📝 상담 요청")
        st.markdown('<div class="guide-text">상담 내용을 적어주세요</div>', unsafe_allow_html=True)
        
        user_input = st.text_area("", placeholder="", height=150, key="consult_input", label_visibility="collapsed")
        
        if st.button("상담 내용 제출", key="submit_btn"):
            if user_input:
                st.success("접수되었습니다! 전문가 수연님이 곧 연락드리겠습니다.")
                time.sleep(2.5)
                st.session_state.app_state = "start_button"
                st.rerun()
            else:
                st.warning("문의 내용을 입력해 주세요.")
        st.markdown('</div>', unsafe_allow_html=True)
