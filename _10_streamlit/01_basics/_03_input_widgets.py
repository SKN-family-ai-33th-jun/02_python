import streamlit as st
# streamlit의 특성: 내부의 버튼이나 특정 기능이 활성화되면,
    # streamlit은 코드의 처음부터 다시 읽어나가기(실행) 때문에 초기값으로 돌아가는 현상이 나타나기도 한다.
    # 이에 반해 session을 유지하는 기능을 사용하면 이를 대처할 수도 있다.

st.title("😒Input Widgets😒")
st.header("Button", divider="rainbow")

# button 생성 + 입력 값 저장
clicked = st.button("Click Me")
print("clicked:", clicked)


if clicked:
    st.write("버튼이 클릭되었습니다!!")

else:
    st.write("아직 버튼을 클릭하지 않았습니다.")

st.button("Reset", type="primary")

st.subheader("Text Input", divider="rainbow")
destination = st.text_input(
    label="가고 싶은 여행지가 있으신가요?",
    placeholder="여행지를 입력하세요"
)
st.write("선택된 여행지는 ", destination,"입니다.")


txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)
st.write(f"You wrote {len(txt)} characters.")


# 라디오 버튼 (여러 개 중 한 가지만 선택)
st.subheader("Radio Buttons", divider="rainbow")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)
if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

st.header('SelectBox') # 하나만 선택하는 것.
# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ',
     'ISTP', 'ISFP', 'INFP', 'INTP',
     'ESTP', 'ESFP', 'ENFP', 'ENTP',
     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ',
     '모름'),
    index=7
)
if mbti:
    st.write(f'선택한 MBTI는 :red[{mbti}]입니다.')

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")