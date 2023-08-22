class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    def working(self):
        print("now working..")
    def coding(self):
        print("now coding..")

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        #Person.__init__(self, name, phoneNumber)
        super().__init__(name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    def printInfo(self):
        #Person.printInfo(self)
        super().printInfo()
        print("Info(Subject: {0}, ID: {1})".format(self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "201234")
#print(p.__dict__)
#print(s.__dict__)
p.printInfo()
s.printInfo()
s.working()
s.coding()

