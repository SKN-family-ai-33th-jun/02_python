# str (문자형, 문자열, String)
# "", '', """ """, ''' ''' 감싸서 표현

print("--- 홑 따옴표, 쌍 따옴표 ---")
s1 = "Hello"
s2 = "World"

# s3 = "abc' X
s3 = "'abc'"

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

# 삼중 따옴표
print("""
삼중 따옴표는
입력된 형식 그대로 문자열(str)로 변환
""")
print("""앞/뒤 엔터 없이 작성하려면
따옴표와 문자열을 딱 붙여서 작성

""")

# str 연산

# 1. 문자열 + 문자열 = 이어쓰기
print('--- 문자열 더하기 연산 ---')
a = "apple"
b = "banana"
print(a + ', ' + b) # apple, banana

# 2. 문자열 * 양의 정수 = 양의 정수 크기 만큼 반복
print('★' * 30)

# 빼기, 나누기 연산은 불가
# print('a' - 'b')
print("\n\n")


# len(객체): 파이썬 객체 길이 반환
# 파이썬 객체: str, list, tuple, dict, set 등
print('--- len() ---')
text = "오늘 점심은 뭘 먹죠?"
print(text, len(text),"글자")

# --- str 메서드 (str api) --- ## api: Application Programming Interface
# (참고) 함수, 메서드 == 기능(실행 후 결과 반환)

# str.replace(old, new)
# - str 내에서 old에 해당하는 문자를 new로 치환

print("--- str.replace() ---")
today = "2026-06-01"

print(today, today.replace("-", "_"))


# str.strip([str])
# - 문자열 좌우 [str] 제거
# - [str] 생략 시 공백 제거
# //////## 문자열에서 공백을 지워주는 기능
# - 코드 작성법에서 []는 생략 가능 --> []를 써도 되고 []를 쓰지 않아도 됨.
print('--- str.strip() ---')
some = "                    하하하        "
print('[' + some + ']')
print('[' + some.strip() + ']')


# 대소문자 관련  str 메서드
print("--- 대소문자 관련  str 메서드 ---")
origin_str = 'hELLO wORLD!'

print(origin_str.upper())         # HELLO WORLD!
print(origin_str.lower())         # hello world!
print(origin_str.capitalize())    # Hello world!
print(origin_str.swapcase())      # Hello World!
print(origin_str.title())         # Hello World!


# 문자열 포맷팅

# 1. % 포맷팅
print("--- % 포맷팅 ---")
x = 10
print("x is %d" %x)    # x is 10

# 2. str.format()
# .format() 메서드는 {}칸에 값을 기입한다. () []는 X
print("--- str.format() ---")
x = 10
y = 1.23
print("{} + {} = {}".format(x, y, x + y))

# 3. f-string (python 3.6)
print("--- f-string() ---")
print(f"{x} + {y} = {x + y}")