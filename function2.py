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

# 기본값이 있는 함수
def times(a = 10, b = 20):
    return a * b
print(times())
print(times(5))
print(times(5, 6))

# 키워드 인자 방식
def connectURI(server, port):
    strURL = "https://" + server + ":" + port
    return strURL
print(connectURI("multicampus.com", "80"))
print(connectURI(port = "80", server = "multicampus.com"))
