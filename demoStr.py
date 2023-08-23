# demoStr.py
#print(dir(str))
import Demo

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p", 7))

Demo.printf("upper")
result = strA.upper()
print(result)

Demo.printf("swith")
print(strA.startswith("py"))    # py 로 시작하니?
print(strA.endswith("py"))      # py 로 끝나니?
print(strA.endswith("ful"))     # ful 로 끝나니?

Demo.printf("alnum")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

Demo.printf("strip")
data = "<<< spam and ham >>>"
result = data.strip("<> ")
print(data)
print(result)

Demo.printf("replace")
result2 = result.replace("spam", "spam egg")
print(result2)

Demo.printf("split")
lst = result2.split()
print(lst)
print(":)".join(lst))
