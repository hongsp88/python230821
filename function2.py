# function2.py
# 이름 해석 규칙 : LGB

# 전역 변수
x = 1
def func(a):
    return a + x

# 호출
print(func(1))

def func2(a):
    #지역 변수
    x = 5
    return a + x

# 호출
print(func2(1))
