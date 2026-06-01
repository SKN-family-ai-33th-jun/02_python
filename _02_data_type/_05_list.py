# sequence type (시퀀스 자료형)
## - str, list, tuple
## - 저장된 값의 순서가 유지
## - 인덱싱과 슬라이싱이 가능
## - 순회(iterable) 가능



# list
## - 여러 값(literal)을 묶어서 관리 (컨테이너 자료형)
## - 동적으로 list 크기가, 배열 크기가 변할 수 있다. (수정 가능)

print("--- list ---")
lst = [1, 2, 3, 4, 5]
print("lst:", lst)
print("len(lst):", len(lst))
print("lst[0]:", lst[0])
print("lst[1]:", lst[1])
print("lst[4]:", lst[4])

# list 저장 요소 추가/삭제
## - 'list'는 동적으로 크기 변경이 가능한 mutable 자료형이다!
## - mutable: list, set, dict                   --> 수정 가능
## - immutable: int, float, bool, str, tuple    --> 수정 불가 -> 버리고 다시 만듬

print("--- list mutable check ---")
print("lst:", lst)
print("추가 전 id:", id(lst))
lst_id_before = id(lst)

# list.append(값): list 끝에 값 추가                                   # append: 끝에 더하다.
lst.append(999)
print("lst:", lst)
print("append 후 lst id:", id(lst))

print("append 전후 같은 list인가?", lst_id_before == id(lst))


# list.insert(index, 값)
## - 특정 index에 값을 삽입하는 메서드 (선택된 index 바로 뒤, ex) 1을 선택하면 2번 인덱스에 값을 기입)
## - 지정된 index부터 뒤에 있는 모든 list 값의 index가 1씩 증가 (1씩 밀려남)
print("--- list.insert() ---")
lst_id_before = id(lst)
lst.insert(1, 1.5489659846)
lst.insert(0, 0)
print("insert 후 lst:", lst)
print("insert 후 id 비교", lst_id_before == id(lst))


# 'list' 수정
# list[인덱스] = 값
## --> 특정 인덱스 값을 변경 (변수에 값 대입해서 변경하는 것과 일맥상통)
## 'list'는 변수를 여러 개 묶어 놓은 것
print("\n\n\n--- list update() ---")
lst[0] = -10
print("lst:", lst)

# 특정 인덱스 값 제거
# list.pop(index): 해당 인덱스 값이 제거
# 제거된 index 뒤 요소들을 한 칸씩 당김
print("--- list remove ---")
lst.pop(2)
print("lst:", lst)
print("lst_id_before:", lst_id_before)
print("id(lst):", id(lst))


# 2차원 list              0차원: 변수, 1차원: list, 2차원: 표              *변수는 값을 하나 저장함.

# 1차원 'list': '변수'가 늘어났다.       [] 빈 칸은 0번을 참조함.
# 2차원 'list': '변수'가 늘어나있는 그 형태가 늘어났다.       [] 빈 칸은 0번을 참조함.
print("\n\n")
students = [
    ["홍길동", 30],
    ["이순신", 80],
    ["세종대왕", 100]
]

print("students:", students)
print("students:", students[0])
print("students:", students[0][0])

print("len(students):", len(students)) # 3
print("len(students[0]):", len(students[0])) #2
print("len(students[0][0]):", len(students[0][0])) #3 (홍길동)


# str.split(구분자)     구분자를 기준으로 나눈다.
## - str을 구분자를 기준으로 나눠서 list 형태로 반환.

data = "홍길동, 20, 서울시, 서초구" # csv(Comma Seperated Value)
data_ = data.split(",")
print("data_:", data_, type(data_))

name = data_[0]
age = data_[1]
addr1 = data_[2]
addr2 = data_[3]
print("\n",name, age, addr1, addr2)


# list 슬라이싱 (str 슬라이싱과 방법 동일)
print("--- list slicing ---")
texts = ["hello", "안녕", "곤니찌와", "hi"]

# ['hello', '안녕']
print(texts[0:2:1])

# ['안녕', '곤니찌와']
print(texts[1:3:1])

#['hello', '곤니찌와']
print(texts[0:3:2])
print(texts[0::2])

#['곤니찌와', 'hi']
print(texts[2:4:1])


# slicing을 이용한 list 값 변경
print("\n\n")
print(texts[:2])
texts[:2] = ["aaa", "bbb"]
print("texts[:2]:", texts[:2])
print(texts)
texts[1:3:1] = ["$$$", "&&&"]
print(texts)

# list끼리 더하기(+) 연산
print("--- list 더하기 연산 ---")
a = [10, 20]
b = [30, 40]
a= a + b
print("a:", a)

b= b + a
print("b:", b)


# list 순회(순차 접근, 순차 반복)
## - iterable 특징을 가지는 자료형만 가능           iterable: 반복될 수 있는
print("--- list 순회 ---")
lst = ['a', 'b', 'c']

# list 요소 순회
for v in lst:       # lst 인덱스 수만큼 다시 회귀하며, 마지막 인덱스 이후에도 다시 돌아가서 확인함. 확인 후 없는 것을 보았을 때 그제서야 멈춤.
    print(v)

# list 인덱스, 요소 순회
for index,v in enumerate(lst):
    print(f"{index}: {v}")