import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="오늘 뭐 먹지?",
    page_icon="🍽️",
    layout="centered"
)

# CSS
st.markdown("""
<style>

.main {
    background-color: #f8f5f2;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #ff4b4b;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 40px;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    text-align: center;
    margin-top: 20px;
}

.food {
    font-size: 34px;
    font-weight: bold;
    color: #333;
}

.reason {
    margin-top: 15px;
    color: #666;
    font-size: 18px;
}

textarea {
    font-size: 18px !important;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
    border: none;
}

.stButton>button:hover {
    background-color: #ff2e2e;
}

</style>
""", unsafe_allow_html=True)

# 제목
st.markdown(
    '<div class="title">🍽️ 오늘 뭐 먹지?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">지금 기분이나 땡기는 음식을 자유롭게 적어보세요 😋</div>',
    unsafe_allow_html=True
)

# 메뉴 데이터
foods = {
    "매운": [
        ("마라탕", "화끈하게 스트레스 풀어보세요 🌶️"),
        ("떡볶이", "매콤달콤한 게 최고죠 🔥"),
        ("짬뽕", "얼큰한 국물로 리프레시!")
    ],

    "국물": [
        ("김치찌개", "따뜻한 국물이 위로가 돼요 🍲"),
        ("국밥", "든든하게 한 끼 먹기 좋아요"),
        ("쌀국수", "깔끔한 국물이 생각날 때!")
    ],

    "가벼운": [
        ("샐러드", "부담 없이 산뜻하게 🥗"),
        ("포케", "건강하고 맛있게!"),
        ("샌드위치", "간단하지만 든든해요")
    ],

    "기분좋은": [
        ("피자", "행복한 날엔 피자죠 🍕"),
        ("스테이크", "오늘은 조금 특별하게 ✨"),
        ("파스타", "분위기 있게 즐겨보세요")
    ]
}

# 사용자 입력
user_input = st.text_area(
    "💭 지금 기분이나 먹고 싶은 걸 적어주세요",
    placeholder="예: 피곤하고 얼큰한 국물 먹고 싶어"
)

# 추천 로직
def recommend_food(text):

    text = text.lower()

    if "매운" in text or "스트레스" in text:
        category = "매운"

    elif "국물" in text or "뜨끈" in text or "피곤" in text:
        category = "국물"

    elif "다이어트" in text or "가벼운" in text or "건강" in text:
        category = "가벼운"

    elif "행복" in text or "기분좋" in text or "특별" in text:
        category = "기분좋은"

    else:
        category = random.choice(list(foods.keys()))

    return random.choice(foods[category])

# 버튼
if st.button("추천받기 🎲"):

    if user_input.strip() == "":
        st.warning("기분이나 먹고 싶은 걸 입력해주세요!")
    else:
        food, reason = recommend_food(user_input)

        st.markdown(f"""
        <div class="card">
            <div class="food">
                🍴 {food}
            </div>

            <div class="reason">
                {reason}
            </div>
        </div>
        """, unsafe_allow_html=True)
