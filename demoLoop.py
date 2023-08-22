# demoLoop.py
import Demo

value = 5
while value > 0:
    print(value)
    value -= 1

Demo.printf("for in")
lst = [100, "사과", 3.14]
for item in lst:
    print(item, type(item))

Demo.printf("break 구문")
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5:
        break
    print("item:{0}".format(item))

Demo.printf("continue 구문")
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item % 2 == 0:
        continue
    print("item:{0}".format(item))

Demo.printf("range() 함수")
print(list(range(10)))
print(list(range(2000,2004)))
print(list(range(1,32)))
for i in range(5):
    print("item:%d" % i)

Demo.printf("리스트 내장")
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])
tp = ("apple", "kiwi", "orange")
print([len(i) for i in tp])
fruits = {100:"apple", 200:"kiwi"}
print([v.upper() for v in fruits.values()])

