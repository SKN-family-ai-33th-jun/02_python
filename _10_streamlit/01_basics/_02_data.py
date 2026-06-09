import streamlit as st
import pandas as pd

# pandas란?
# - 데이터 분석과 조작을 위해 설계된 파이썬 라이브러리
# - 특히 구조화된 데이터(표 형식) 처리에 특화
# - DataFrame이라는 구조를 중심으로 빠르고 직관적인 데이터 처리 및 분석을 지원

st.title("👍 Data 👍")

st.header("Pandas `DataFrame`")

student_df = pd.DataFrame({
    "Name":["홍길동", "이순신", "신사임당"],
    "Age": [20,30,40],
    "Score":[90,88,76]
})

st.dataframe(student_df)

st.subheader("DataFrame + csv", divider=True)
sample_df = pd.read_csv("../data/annual-enterprise-survey-2023.csv")
st.dataframe(sample_df)


st.subheader("DataFrame 강조 기능", divider="rainbow")

data = {
    "Product" : ["A","B","C","D"],
    "Sales" : [500,300,400,600],
    "Growth(%)" : [10,-5,15,7]
}
df = pd.DataFrame(data)

# 시각적 강조
st.dataframe(
    df.style
    .highlight_max(subset=["Sales"], color="lightgreen")
    .highlight_min(subset=["Growth(%)"], color="pink")
)

# 열 설정을 추가한 DataFrame 표시
st.dataframe(df, column_config={
    "Sales": st.column_config.NumberColumn("Total Sales", format="%d units"),
    "Growth (%)": st.column_config.NumberColumn("Growth Percentage", format="%.1f%%")
}, width="stretch")