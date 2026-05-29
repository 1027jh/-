import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="오늘 뭐 먹지?",
    page_icon="🍽️",
    layout="centered"
)

# CSS 꾸미기
st.markdown("""
<style>
body {
    background-color: #f8f5f2;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #ff4b4b;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    text-align: center;
    margin-top: 20px;
}

.food-name {
    font-size: 32px;
    font-weight: bold;
    color: #333;
}

.reason {
    color: #666;
    margin-top: 10px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="main-title">🍽️ 오늘 뭐 먹지?</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">오늘 기분에 맞는 메뉴를 추천해드릴게요 😋</div>',
    unsafe_allow_html=True
)

# 데이터
menus = {
    "행복해 😊": [
        {
            "name": "피자",
            "reason": "좋은 날엔 맛있는 거 크게 먹어야죠!",
            "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591"
        },
        {
            "name": "삼겹살",
            "reason": "행복한 날엔 고기가 최고예요.",
            "image": "https://images.unsplash.com/photo-1544025162-d76694265947"
        }
    ],

    "우울해 😢": [
        {
            "name": "마라탕",
            "reason": "스트레스는 매운맛으로 날려버리기!",
            "image": "https://images.unsplash.com/photo-1512058564366-18510be2db19"
        },
        {
            "name": "떡볶이",
            "reason": "매콤달콤한 음식이 기분을 올려줘요.",
            "image": "https://images.unsplash.com/photo-1603133872878-684f208fb84b"
        }
    ],

    "피곤해 😴": [
        {
            "name": "국밥",
            "reason": "든든하게 에너지 충전!",
            "image": "https://images.unsplash.com/photo-1550547660-d9450f859349"
        },
        {
            "name": "김치찌개",
            "reason": "따뜻한 국물이 피로를 녹여줘요.",
            "image": "https://images.unsplash.com/photo-1490645935967-10de6ba17061"
        }
    ]
}

# 기분 선택
mood = st.selectbox(
    "💭 오늘 기분은 어떤가요?",
    list(menus.keys())
)

# 버튼
if st.button("메뉴 추천받기 🎲"):

    selected = random.choice(menus[mood])

    # 이미지
    st.image(selected["image"], use_container_width=True)

    # 카드 UI
    st.markdown(f"""
    <div class="card">
        <div class="food-name">
            🍴 {selected['name']}
        </div>

        <div class="reason">
            {selected['reason']}
        </div>
    </div>
    """, unsafe_allow_html=True)
