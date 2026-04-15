수연님, 디자인 디테일을 잡아가는 과정이 정말 즐겁네요!

강렬한 빨간색 카운트다운은 다소 시선을 분산시킬 수 있죠. 이번에는 차분하고 모던한 그레이 톤을 베이스로 하고, 폰트 굵기와 간격을 조절하여 마치 프리미엄 미니멀리즘 앱 같은 세련된 느낌으로 UI를 변경해 보았습니다.

✅ 세련된 미니멀 UI로 app.py 업데이트하기
GitHub의 app.py 내용을 아래 코드로 전체 교체해 주세요.

Python
import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(layout="wide")

# 2. 사용할 비디오 URL
video_url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"

# 3. 사용자 지정 CSS: 미니멀 & 세련된 디자인
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .block-container { 
            padding-top: 6rem !important; 
            padding-bottom: 2rem; 
        }

        /* [수정] 타이틀 스타일: 더 얇고 세련된 폰트감 */
        h3 {
            font-weight: 400 !important;
            color: #333333;
            letter-spacing: -0.02em;
            margin-bottom: 2rem !important;
            line-height: 1.5 !important;
        }

        /* [핵심 수정] 카운트다운: 빨간색 제거, 크기 축소, 세련된 그레이 톤 */
        .countdown-text { 
            font-size: 60px; 
            font-weight: 300; /* 얇은 폰트로 세련미 추가 */
            color: #444444; 
            text-align: center; 
            margin-top: 30px;
            letter-spacing: -0.05em;
        }

        /* 영상 컨테이너 */
        .video-container {
            position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;
            max-width: 100%; background: #000; border-radius: 16px 16px 0 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin-bottom: 0px !important;
        }
        .video-container video { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0; }

        /* 영상과 폼 사이 밀착 */
        [data-testid="stVerticalBlock"] > div:has(div.video-container) + div { display: none !important; }
        .stVerticalBlock { gap: 1.2rem !important; }

        .consultation-form-container { 
            background-color: #f8f9fa; /* 더 밝고 깨끗한 그레이 */
            padding: 40px; 
            border-radius: 0 0 16px 16px;
            margin-top: -1.2rem !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05); 
        }

        .guide-text {
            font-size: 15px;
            color: #888888;
            margin-bottom: 12px;
            margin-top: 5px;
        }

        /* [수정] 버튼 스타일: 더 깊이감 있는 딥 다크 그레이/블랙 톤으로 변경 가능하지만, 
           수연님의 '상담' 의지를 고려해 차분한 딥 레드 혹은 모던 블랙 추천 */
        div.stButton > button {
            background-color: #1a1a1a; /* 세련된 블랙 */
            color: white;
            padding: 16px 45px;
            font-size: 20px;
            border-radius: 8px; /* 너무 둥근 것보다 각진 느낌이 더 신뢰감을 줌 */
            border: none;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            background-color: #333333;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
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
            # 폰트 두께를 얇게(Light) 적용하여 고급스러운 바이브 연출
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
