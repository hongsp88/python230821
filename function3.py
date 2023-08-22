# function3.py
# 가변 인자 처리(*는 Tuple을 의미)
import Demo

def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

# 람다 함수
g = lambda x,y:x*y
print(g(3,4))
print(g(3,6))
print((lambda x:x*x)(3))
print(globals())

# 필터링 함수 정의
def getBiggerThan20(i):
    return i > 20

Demo.printf("필터링 함수")
lst = [10,25,30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

Demo.printf("람다 함수 정의")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)

