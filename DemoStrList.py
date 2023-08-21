# DemoStrList.py
import Demo

strA = "python is very powerful"
strB = "파이썬은 강력해"
strC = """파이썬을
오늘부터
학습합니다."""

print(strA)
print(len(strB))
print(strC)

result = "py" + "thon"
print(result)

Demo.printf("슬라이싱(인덱싱)")
print(strA[0])
print(strA[0:6])
print(strA[:6])
print(strA[-3:])

Demo.printf("List 형식")
lst = [1,2,3,4,5]
print(len(lst))
print(lst[0])
lst.append(10)
lst.insert(1, 20)
print(lst)

colors = ["red", "blue", "green"]
colors += ["red"]
colors += "red"
print(colors)
colors.remove("red")
print(colors)

Demo.printf("디버깅")
for item in colors:
    print(item)

Demo.printf("Tuple")
tp = (10,20,30)
print(len(tp))
print(tp)
print("id:%s, name:%s" % ("kim","김유신"))

#함수 정의
def times(a,b):
    return a+b,a*b

Demo.printf("함수 호출")
print(times(5,6))

args = (3,4)
print(times(*args))

Demo.printf("형식 변환")
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b)
print(c)

Demo.printf("Set")
a = {1,2,3,3}
b = {3,4,4,5}
print(len(a))
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b), b.difference(a))

