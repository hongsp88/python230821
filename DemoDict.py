# DemoDict.py
import Demo

colors = {"apple":"red", "banana":"yellow"}
print(len(colors))
colors["kiwi"] = "green"
print(colors["apple"])

for item in colors.items():
    print(item)

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print("kim" in phone)
print("kang" not in phone)
p = phone
p["kang"] = "1234"
print(p)
print(phone)
print(id(phone), id(p))
print(phone["kim"])

Demo.printf("깊은 복사")
import copy

device = {"아이폰":5, "아이패드":10}
device2 = copy.deepcopy(device)
device2["맥북"] = 20
print(device)
print(device2)

