# web1.py

from bs4 import BeautifulSoup
import Demo

# page loading
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
# object for search
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify()) # 전체 출력

Demo.printf("문서에서 <p> 검색")
print(soup.find_all("p"))

Demo.printf("문서에서 첫번째 <p> 검색")
print(soup.find("p"))

Demo.printf("조건이 있는 경우 : <p class='outer-text'>")
# class는 python 키워드와 충돌남. ->  class_ 로 사용
print(soup.find_all("p", class_="outer-text"))

Demo.printf("특정 속성을 지정할 때: attrs(attributes)")
print(soup.find_all("p", attrs={"class":"outer-text"}))

Demo.printf("특정 id만 지정")
print(soup.find_all(id="first"))

# ///////////////////////////////////////////////
Demo.printf("태그 내부의 컨텐츠를 출력: .text, .get_text()")
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)