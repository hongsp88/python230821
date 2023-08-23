# db1.py
import sqlite3
import Demo

# memory에 저장하는 방법
#con = sqlite3.connect(":memory:")
# 파일에 저장
con = sqlite3.connect("c:\\work\\sample.db")
cur = con.cursor()  # cursor 객체에서 구문실행

cur.execute("create table if not exists PhoneBook " +
    "(id integer primary key autoincrement, name text, phoneNum text);")

cur.execute("insert into PhoneBook (name, phoneNum) values ('hong', '010-111');")

# 입력
name = "전우치"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);", (name, phoneNumber))

# 다중 레코드 입력
datalist = (("박문수","010-123"), ("김길동","010-456"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);", datalist)

# 출력
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

con.commit()
con.close()