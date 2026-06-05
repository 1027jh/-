import streamlit as st
import google.generativeai as genai

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="오늘 뭐 먹지?",
    page_icon="🍚",
    layout="centered"
)

st.title("🍽️ 오늘 뭐 먹지?")
st.caption("기분과 날씨에 따라 메뉴를 추천해주는 AI 챗봇")

# -----------------------------
# API KEY 불러오기
# -----------------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("❌ API 키를 불러오지 못했어요.")
    st.stop()

# -----------------------------
# 모델 설정
# -----------------------------
try:
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
except Exception as e:
    st.error(f"❌ 모델 생성 오류: {e}")
    st.stop()

# -----------------------------
# 채팅 기록 유지
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕! 오늘 기분이나 날씨를 말해주면 음식 메뉴를 추천해줄게 😋"
        }
    ]

# 기존 메시지 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# 사용자 입력
# -----------------------------
user_input = st.chat_input("예: 비 오는 날 우울해...")

if user_input:
    # 사용자 메시지 저장
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # 프롬프트 생성
    prompt = f"""
    너는 음식 추천 전문 AI야.

    사용자의 기분과 날씨를 분석해서:
    1. 어울리는 음식 3개 추천
    2. 이유 설명
    3. 말투는 친근하고 귀엽게

    사용자 입력:
    {user_input}
    """

    # AI 응답
    try:
        response = model.generate_content(prompt)
        bot_reply = response.text

    except Exception as e:
        bot_reply = f"❌ 오류가 발생했어요: {e}"

    # 응답 저장
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    # 응답 출력
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
