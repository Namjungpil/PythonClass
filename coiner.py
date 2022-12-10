# Qt Designer 사용하기
# 윈도우 앱에서 동작하는 가상화폐 가격 조회 프로그램 만들기


import sys                             # 윈도우 시스템 접근
from PyQt5.QtWidgets import *          # PyQt5 모듈 읽어 오기
from PyQt5 import uic                  # Designer 로 만든 창을 사용하기   
import pykorbit
from PyQt5.QtCore import *

tickers = ["BTC", "ETC", "XRP", "ADA"]
form_class = uic.loadUiType("mywindow3.ui")[0]   # Designer 로 만든 창을 사용하기   

class MyWindow(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)            # 버튼을 클릭하면 btn_click 함수 실행

    def btn_clicked(self) :
        for i, ticker in enumerate(tickers) :
            #print(ticker)
            #price = pykorbit.get_current_price(ticker)
            #print(price)

            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)

            price = pykorbit.get_current_price(ticker)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))

app = QApplication(sys.argv)           # 윈도우 창 띄우기
window = MyWindow()
window.show()

app.exec_()                            # 윈도우 창을 계속 유지 시켜주는 코드
