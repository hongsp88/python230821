# DemoForm2.py
# DemoForm2.ui + DemoForm2.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import requests # 웹서버 통신
from bs4 import BeautifulSoup

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# Form Class 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def firstClick(self):

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

        self.label.setText("당근 마켓 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")

# 직접 모듈 실행 유무
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
