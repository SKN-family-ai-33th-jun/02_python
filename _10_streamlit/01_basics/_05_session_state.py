import streamlit as st
# from jedi.third_party.typeshed.stubs.docutils.docutils.nodes import description

st.title("Session State")   # session: 서버에 접속한 사용자(클라이언트) 객체
# 사용자가 접속했을 때 Session에 저장하면 그 내용이 서버에 남게 됨.

description = """
- Streamlit은 버튼 클릭 등 사용자 상호 작용이 발생하면 스크립트(코드)를
  위에서 아래로 다시 시작한다.
  
- 그래서 일반 변수에 저장된 값들이 매번 초기화된다.

- session_state를 이용하면 같은 사용자 안에서 값을 유지한다.
  (사용자 기준 == 브라우저)
"""
st.markdown(description)

# 버튼 클릭
count: int = 0 # 초기값 0

# clicked = st.button("클릭 시 count 1 증가")
# clicked # Streamlit의 Magic --> 화면 출력하는 기능이 내장되어 있음

if st.button("버튼 클릭 시 count 1 증가"):
    count += 1

st.write("클릭한 횟수:", count)


st.subheader("session_state를 이용한 count", divider="rainbow")

# session_state
# - 서버 컴퓨터 메모리 영역에 접속한 사용자별 객체

# st.session_state에 count가 없으면 수행 -> 최초 1회 접속시에만 실행
if not "count" in st.session_state:     # dict 형태로 반환됨
    st.session_state["count"] = 0

if st.button("클릭 시 count 1 증가"):
    st.session_state["count"] += 1

if st.button("클릭 시 count 1 감소"):
    st.session_state["count"] -= 1


st.write("클릭한 횟수:", st.session_state["count"])
