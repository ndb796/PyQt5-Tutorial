import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(800, 400, 300, 150)

        self.status_bar = QStatusBar(self)
        self.status_bar.showMessage("현재 프로그램이 시작되었습니다.")
        self.setStatusBar(self.status_bar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
