# demoFile.py
import Demo

path = "c:\\work\\demo2.txt"

f = open(path, "wt", encoding="utf-8")
f.write("데이터1번\n데이터2번\n데이터3번")
f.close()

# Read
f = open(path, "rt", encoding="utf-8")
result = f.read()
print(result)

Demo.printf("readline()")
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")

Demo.printf("readlines()")
f.seek(0)
lst = f.readlines()
for item in lst:
    print(item, end="")

f.close()