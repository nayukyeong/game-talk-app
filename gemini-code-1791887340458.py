import datetime
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="선생님과의 점심 시간 데이트 🍱",
    page_icon="✨",
    layout="centered",
)

# 세션 상태 초기화 (페이지 간 데이터 유지를 위함)
if "step" not in st.session_state:
    st.session_state.step = 1
if "name" not in st.session_state:
    st.session_state.name = ""
if "grade" not in st.session_state:
    st.session_state.grade = 1
if "class_num" not in st.session_state:
    st.session_state.class_num = 1
if "number" not in st.session_state:
    st.session_state.number = 1
if "activity_type" not in st.session_state:
    st.session_state.activity_type = ""
if "detail_choice" not in st.session_state:
    st.session_state.detail_choice = ""
if "custom_detail" not in st.session_state:
    st.session_state.custom_detail = ""
if "day_choice" not in st.session_state:
    st.session_state.day_choice = "월요일"

# 스타일 커스텀 (CSS)
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.2rem;
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #555555;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- 1단계: 시작 및 학생 정보 입력 ---
if st.session_state.step == 1:
    st.markdown(
        '<div class="main-title">🍱 선생님과 함께하는 점심 시간!</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-title">어떤 이야기를 나누고 싶거나, 어떤 게임을 하고 싶은가요? 신청서를 작성해 주세요!</div>',
        unsafe_allow_html=True,
    )

    with st.form("student_info_form"):
        st.subheader("📝 학생 정보 입력")
        col1, col2, col3 = st.columns(3)
        with col1:
            grade = st.selectbox("학년", [1, 2, 3], index=0)
        with col2:
            class_num = st.number_input(
                "반", min_value=1, max_value=20, value=1
            )
        with col3:
            number = st.number_input(
                "번호", min_value=1, max_value=40, value=1
            )

        name = st.text_input("이름", placeholder="이름을 입력해주세요")

        submitted = st.form_submit_button(
            "다음 단계로 ➡️", use_container_width=True
        )

        if submitted:
            if not name.strip():
                st.warning("⚠️ 이름을 정확히 입력해주세요!")
            else:
                st.session_state.grade = grade
                st.session_state.class_num = int(class_num)
                st.session_state.number = int(number)
                st.session_state.name = name
                st.session_state.step = 2
                st.rerun()

# --- 2단계: 활동 유형 선택 (대화 vs 게임) ---
elif st.session_state.step == 2:
    st.markdown(
        f'<div class="main-title">반가워요, {st.session_state.name} 학생! 👋</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-title">오늘 점심 시간에 선생님과 하고 싶은 활동을 선택해 주세요.</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🗣️ 선생님과 대화하기", use_container_width=True):
            st.session_state.activity_type = "대화"
            st.session_state.step = 3
            st.rerun()

    with col2:
        if st.button("🎮 선생님과 게임하기", use_container_width=True):
            st.session_state.activity_type = "게임"
            st.session_state.step = 3
            st.rerun()

    st.markdown("---")
    if st.button("⬅️ 이전으로"):
        st.session_state.step = 1
        st.rerun()

# --- 3단계: 세부 내용 선택 (대화 주제 혹은 게임 종류) ---
elif st.session_state.step == 3:
    if st.session_state.activity_type == "대화":
        st.markdown(
            '<div class="main-title">🗣️ 어떤 이야기를 나누고 싶나요?</div>',
            unsafe_allow_html=True,
        )

        detail_options = [
            "진로 및 공부 고민 (성적, 진학 등)",
            "친구 관계 및 학교 생활 이야기",
            "요즘 빠져있는 취미/관심사 공유 (아이돌, 운동, 유튜브 등)",
            "그냥 가볍게 수다 떨고 싶어요!",
            "기타 (직접 입력)",
        ]
        selected = st.radio("주제를 선택해주세요:", detail_options)

        if selected == "기타 (직접 입력)":
            custom = st.text_input("나누고 싶은 이야기를 적어주세요:")
            st.session_state.detail_choice = (
                custom if custom else "자유 주제"
            )
        else:
            st.session_state.detail_choice = selected

    else:  # 게임인 경우
        st.markdown(
            '<div class="main-title">🎮 어떤 게임을 하고 싶나요?</div>',
            unsafe_allow_html=True,
        )

        game_options = [
            "📱 모바일 루미큐브 (두뇌 타일 게임)",
            "🏷️ 양세찬 게임 (머리에 단어 붙이고 맞추기)",
            "🕵️‍♂️ 라이어 게임 (거짓말쟁이 찾기 심리전)",
            "🐺 마피아 게임 (클래식 심리 마피아)",
            "✏️ 기타 (하고 싶은 다른 게임 추천)",
        ]
        selected = st.radio("게임을 선택해주세요:", game_options)

        if selected == "✏️ 기타 (하고 싶은 다른 게임 추천)":
            custom = st.text_input("하고 싶은 게임 이름을 적어주세요:")
            st.session_state.detail_choice = (
                custom if custom else "자유 게임"
            )
        else:
            st.session_state.detail_choice = selected

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ 이전으로"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("다음 (요일 선택) ➡️"):
            st.session_state.step = 4
            st.rerun()

# --- 4단계: 요일 및 시간 선택 ---
elif st.session_state.step == 4:
    st.markdown(
        '<div class="main-title">📅 언제 방문할 예정인가요?</div>',
        unsafe_allow_html=True,
    )

    day_options = ["월요일", "화요일", "수요일", "목요일", "금요일"]
    st.session_state.day_choice = st.selectbox(
        "방문하고 싶은 요일을 선택해주세요:", day_options
    )

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ 이전으로"):
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("🎉 신청 완료하기!", type="primary"):
            st.session_state.step = 5
            st.rerun()

# --- 5단계: 최종 결과 화면 ---
elif st.session_state.step == 5:
    st.markdown(
        '<div class="main-title">🎉 점심 시간 신청 완료!</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-title">아래 내용을 확인하고 점심 시간에 만나요!</div>',
        unsafe_allow_html=True,
    )

    # 결과 카드 디자인
    st.markdown(
        f"""
        <div style="background-color: #f0f8ff; border: 2px dashed #4682b4; border-radius: 15px; padding: 25px; text-align: center;">
            <h2 style="color: #2c3e50; margin-bottom: 15px;">🌟 점심 시간 데이트 티켓 🌟</h2>
            <hr style="border: 0.5px solid #dcdcdc;">
            <p style="font-size: 1.2rem; text-align: left; margin: 10px 0;"><b>👤 신청자:</b> {st.session_state.grade}학년 {st.session_state.class_num}반 {st.session_state.number}번 {st.session_state.name}</p>
            <p style="font-size: 1.2rem; text-align: left; margin: 10px 0;"><b>🎯 선택 활동:</b> {st.session_state.activity_type}</p>
            <p style="font-size: 1.2rem; text-align: left; margin: 10px 0;"><b>📌 세부 내용:</b> {st.session_state.detail_choice}</p>
            <p style="font-size: 1.2rem; text-align: left; margin: 10px 0;"><b>⏰ 방문 일정:</b> 매칭된 주 <b>{st.session_state.day_choice}</b> 점심 시간 급식 직후!</p>
            <hr style="border: 0.5px solid #dcdcdc;">
            <p style="color: #e74c3c; font-weight: bold; font-size: 1.1rem; margin-top: 15px;">"맛있게 밥 먹고 교실/상담실로 놀러와!" 😊</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    if st.button("🔄 처음으로 돌아가기 (새로 신청)", use_container_width=True):
        # 상태 초기화
        st.session_state.step = 1
        st.session_state.name = ""
        st.session_state.activity_type = ""
        st.session_state.detail_choice = ""
        st.rerun()