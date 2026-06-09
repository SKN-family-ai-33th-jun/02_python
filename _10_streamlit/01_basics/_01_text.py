import streamlit as st

# 실행 명령어
# streamlit run [파일명].py

# 제목
st.title("😁😁Hello, Streamlit")

st.header("Text", divider="rainbow")
st.subheader("sub:green[header]", divider="blue")

# text: 단순 글자
st.text("text 테스트")

# write
## - 단순 글자
## - 마크다운, 표, 리스트, 차트, 입력 타입 등에 따라 출력방식이 정해짐
st.write("write 테스트")
st.write("write **markdown** ***지원***")
st.write("`write`")

st.markdown("# markdown")

st.html("<h3 style='text-align: center; font-size:50px;'>html도 지원</h3>")

st.subheader(":red[magic]", divider="orange")
"streamlit magic"
"변수나 리터럴 값이 출력 구문내에 없어도 화면에 값을 기록"
100
lst = [10,20,30]
lst
dct = {"a":10, "b":20, "c":30}
dct

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python", line_numbers=True)

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)


# metric: 측량, 측정
# 개발할 때 metric이란, 표 만들기로서 이해하기
a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)