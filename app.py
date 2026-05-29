import streamlit as st
import random

st.title("🍽️ 오늘 뭐 먹지?")

menus = {
    "한식": [
        ("김치찌개", "얼큰하고 든든해요."),
        ("비빔밥", "건강하게 한 끼 가능!"),
        ("삼겹살", "스트레스 해소엔 고기죠.")
    ],
    "중식": [
        ("짜장면", "실패 없는 국민 메뉴."),
        ("짬뽕", "매콤한 국물이 최고."),
        ("탕수육", "같이 먹기 좋은 메뉴.")
    ],
    "양식": [
        ("파스타", "분위기 있게 먹기 좋아요."),
        ("피자", "여럿이 먹기 최고."),
        ("스테이크", "특별한 날 추천!")
    ]
}

category = st.selectbox(
    "먹고 싶은 종류를 선택하세요",
    list(menus.keys())
)

if st.button("추천받기 🎲"):
    menu, reason = random.choice(menus[category])

    st.subheader(f"🍴 {menu}")
    st.write(reason)
