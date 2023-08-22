# class1.py
# 1) 클래스 형식을 정의

class Person:
    def __init__(self, name = ""):
        self.name = "default name" if name == "" else name
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p2 = Person("TEST")

p1.print()
p2.print()
p2.name = "전우치"
p2.print()

# 런타임
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

# 인스턴스에 추가
p1.age = 30
print(p1.age)
#print(p2.age)
#print(Person.age)