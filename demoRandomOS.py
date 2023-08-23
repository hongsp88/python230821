# demoRandomOS.py
import random
import Demo

print(random.random())
print(random.random())
print(random.uniform(2,5))
print([random.randrange(20) for i in range(10)])    # randrange : 중복 숫자 발생
print([random.randrange(20) for i in range(10)])

Demo.printf("샘플링")
print(random.sample(range(20), 10))     # sample : 중복 숫자 발생 안함
print(random.sample(range(20), 10))

from os.path import *
from os import *

path = "c:\\python310\\python.exe"

print(abspath("python.exe"))    # os.path
print(basename(path))           # os.path

if exists(path):                # os.path
    print("파일 크기: {0}".format(getsize(path)))   # os.path
else:
    print("파일 없음")


print("운영체제 이름: {0}".format(name))    # os
print("환경변수: {0}".format(environ))      # os
#system("notepad.exe")   # os

# 파일 목록
import glob
result = glob.glob("c:\\work\\*.py")
for item in result:
    print(item)