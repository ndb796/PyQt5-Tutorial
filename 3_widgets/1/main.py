import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        btn = QPushButton("종료", self)
        btn.move(20, 20)
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QCoreApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
