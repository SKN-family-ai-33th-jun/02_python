# number(숫자형)
# - 정수
# - 실수
# - 복소수



# type(변수명 | 값) 함수: 변수 또는 값의 타입을 확인하는 내장 함수

# 정수 (int) integer
n = 123
print(n, type(n))

price = 1000000000 # 정수 자릿수 구분
print(price, type(price))

# 정수(int) 최대값
import sys
print(sys.maxsize)

# 2진법, 8진법, 16진법
a = 0b100 # 4

b = 0o23 # 19

c = 0xFF #


# 실수 (float)
m = 123.456
print(m, type(m))

f2 = -99999.99999

# 소수점 아래 16자리까지 표현 가능
f3 = 1.098765432123456789009876543


# 복소수 (complex) j
c = 2j
print(c, type(c))

d= 3+4j
print(d, type(d))


# ----------------------------
# 산술 연산 (+, -, *, /, //, %, **) 에스터비스크, 슬래쉬, 몫, 모듈로, 거듭제곱
print(1+2)
print(1-2)
print(1*2)
print(1/2) # 나누어 떨어질 때 까지의 몫
print(1//2) # 정수 영역에서의 몫
print(1%2) # 정수 영역에서의 나머지

print(3**2)
print(2**63) # int 양의 최대값

