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


# ------------------------------------------------------
# 문자열 인덱싱/슬라이싱
# - 파이썬 문자열(str)은 text sequence 형태를 갖는다.
# abcd --> a가 1번 째, b가 2번 째, ...
# --> 여기서 순서를 가리키는 용어를 Index라고 함 (base index == 0) --> 마지막 index == str 길이 -1
# 결론: 순서가 있는 데이터 구조.

print("--- 문자열 indexing ---")
x = "Monday"
print("x의 길이:", len(x)) # 길이 6, Last Index: 5
print(x[0]) # [] == 배열, [0] == str 배열 중 0번 째 index

print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[5])

# 역 인덱스: str을 거꾸로 탐색
# + 인덱스와 - 인덱스 모두 항상 0번은 첫 번째 글자이고, -의 경우 글자 맨 뒤로 이동하여 1번부터 시작함.
print(x[0])
print(x[-5])
print(x[-4])
print(x[-3])
print(x[-2])
print(x[-1])

print(x[-1], x[-2], x[-3], x[-4], x[-5], x[-6])

# str 슬라이싱: 문자열 일부를 잘라서 가져오는 방법
# 작성법:      str[start:stop:step]
# - start: 시작 인덱스
# - stop: 종료 인덱스 (미포함)
# - step: 건너 뛸 개수 (생략 시 기본값 1)
print("--- str slicing ---")

text = "hello world"
print("text:", text)
print("len(text):", len(text)) # 11

print("text[0:5:1]", text[0:5:1]) #hello
print("text[0:5]", text[0:5]) #hello
print("text[:5]", text[:5]) #hello

print("text[6:11]", text[6:11]) #world
print("text[6:len(text)]", text[6:len(text)]) #world
print("text[6:]", text[6:]) #world, 6 시작, 끝까지

print("text[:]", text[:]) #hello world, 0 시작, 끝까지 --> 아무것도 자르지 않겠다는 것을 의미.


print("text[0:11:2]", text[0:11:2]) #0, 2, 4, 8, 10
print("text[::2]", text[::2]) #0, 2, 4, 8, 10
print("text[::-1]", text[::-1]) #0, 2, 4, 8, 10 --> 순서를 반대로 바꿈.

#***************************************************************
#***************************************************************
#          indexing 숫자 계산 중요 for project!!!!!!!!!!!
#***************************************************************
#***************************************************************


# 문자열 불변 타입 (immutable)
# - 변수: 값을 저장할 수 있는 메모리 상의 공간
# - str은 한 번 메모리에 값이 저장되면 수정할 수 없다.
print("--- 문자열 불변 타입 ---")
s = 'python'
print("s:", s)
print("변경 전 s:", id(s)) # id: 메모리 주소
s = s+ ' hello' # 문자열을 추가할 때 해당 메모리 내용을 동적으로 수정하는 것이 아닌 새로운 메모리 공간을 할당하여 적용.
print("s:", s)
print("변경 후 s:", id(s)) # id: 메모리 주소


# in 연산자(멤버쉽 검사 연산자)
# - 특정 값이 포함되어 있는지 검사 --> 결과: bool(True or false)
print("--- in 연산자 ---")
txt = "김밥, 라면, 어묵, 떡볶이"
print("라면" in txt) # True
print("돈까스" in txt) # False