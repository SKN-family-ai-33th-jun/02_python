"""
# 모듈이란?
- .py 파일을 의미
- 프로그램 내 코드 재사용성을 높이기 위해 (모듈 단위)로 코드를 관리
- 모듈에 작성된 변수, 함수, 클래스 등은 외부에서 import해 사용할 수 있음
- 단,    _, __로 시작하는 이름은 '내부용(private)'을 의미함. 사용할 수는 있으나 내부용이라는 "관례"가 있음
    -> 외부에서 import해서 사용하는 것을 지양.
- import *: 모듈 내 모든 변수, 함수, 클래스 등을 가져오기
            단,    _, __로 시작하는 변수, 함수, 클래스는 자동으로 제외됨.
"""

# 파이썬 내장 모듈 math 가져오기
import math

print("math.pi:", math.pi)

# dir(모듈명) 내장 함수: 해당 모듈의 사용 가능한 속성/함수 등을 나열
print("dir(math):", dir(math))

# dir() 내장 함수: 현재 모듈(_02_module.py)의 사용 가능한 속성/함수 등을 나열
print("dir():", dir())

# 모듈명 확인 (__name__)
## - import 한 모듈에 대해서는 모듈명 반환
## - 현재 모듈 실행 시에는 "__main__" 반환
print("__name__:", __name__)
print("math.__name__:", math.__name__)


""" 사용자 정의 모듈 가져오기 """
# import skn.my_math

""" 파이썬 패키지로 모듈 가져오기 """
# skn 폴더 == 패키지
# from skn import my_math as m # skn 패키지 내에서 my_math 모듈 가져오기
#
# print("skn.my_math.pi:", m.pi)
# print(m.get_circle_area(10))
# print("my_math.__z:", m.__z) # private 변수 가져오기 (권장 x)


''' import * 이용해서 모두 가져오기 '''
# from skn.my_math import *
# print("pi:", pi)
# print("x:", x)
# print("get_circle_area(10):", get_circle_area(10))

# # import * 로 가져올 시 private 변수(-,__)는 가져오지 않는다.
# # print("__z:", __z) # import *를 하였기 때문에 _, __로 시작되는 것은 import되지 않았음


""" import 모듈 별칭 처리 """
# import 모듈명/ import 패키지명.모듈명: 지정된 모듈 가져오기
## -> 사용법: 모듈명.변수명 / 패키지명.모듈명.변수명

# from 패키지명 import 모듈명: 지정된 패키지에서 모듈 가져오기
## -> 사용법: 모듈명.변수명

# import 모듈명 as 별칭 | from 패키지명 import 모듈명 as 별칭     # as: alias (별칭)
## -> 사용법: 별칭.변수명
from skn import my_math as mm
print("pi:", mm.pi)
print("x:", mm.x)
print("get_circle_area(10):", mm.get_circle_area(10))

#####
#####
# 실제 개발에서는 <import*>로 변수명만 사용하는 것보다
# <import 모듈명 as 별칭>을 통한 "모듈명.변수" 형태로 사용하는 것이 충돌을 방지하고 관리가 용이하다.
#####
#####

# __name__: 현재 모듈의 이름을 반환
print("__name__:", __name__)

# 현재 모듈을 import해서 사용하는 경우 하위 코드를 실행하지 마시오
if __name__ == "__main__":
    pass # 아무것도 하지말고 넘겨라



# 파이썬 파일이 자기 위치에서 실행되면 __name__은 main이 되고,
# 다른 파일에서 호출되는 경우 (모듈 import 등)에는 그 파일의 __name__이 해당 모듈 이름이 된다.