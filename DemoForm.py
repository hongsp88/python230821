# DemoForm.py
# DemoForm.ui + DemoForm.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

# Form Class 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 폼 데모")

    def resizeEvent(self, QResizeEvent):
        clientSize = self.window().size()

        self.label.move(10, 0)
        self.tableWidget.move(10, 80)
        self.tableWidget.resize(clientSize.width() - 20, clientSize.height() - 90)

# 직접 모듈 실행 유무
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
