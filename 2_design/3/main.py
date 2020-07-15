import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        label = QLabel('RED')
        label.setStyleSheet("color: red;"
                            "border-style: solid;"
                            "border-width: 2px;"
                            "border-color: #FF0000;"
                            "border-radius: 5px")

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        self.setLayout(vbox)

        self.setWindowTitle('스타일시트 예시')
        self.setGeometry(300, 300, 300, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
