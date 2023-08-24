# web2.py
import Demo

import requests # 웹서버 통신
from bs4 import BeautifulSoup

url = "https://www.daangn.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

f = open("C:\\work\\daangn.txt", "a+", encoding="utf-8")

posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})

    title = titleElem.text.replace("\n", "").strip()
    price = priceElem.text.replace("\n", "").strip()
    addr = addrElem.text.replace("\n", "").strip()
    print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}\n")

f.close()
