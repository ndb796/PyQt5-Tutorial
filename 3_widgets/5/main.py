import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(800, 200, 260, 300)

        self.radio1 = QRadioButton("학부생", self)
        self.radio1.move(20, 20)
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.radio_button_clicked)

        self.radio2 = QRadioButton("대학원생", self)
        self.radio2.move(20, 40)
        self.radio2.clicked.connect(self.radio_button_clicked)

        self.radio3 = QRadioButton("직장인", self)
        self.radio3.move(20, 60)
        self.radio3.clicked.connect(self.radio_button_clicked)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

    def radio_button_clicked(self):
        msg = ""
        if self.radio1.isChecked():
            msg = "학부생"
        elif self.radio2.isChecked():
            msg = "대학원생"
        else:
            msg = "직장인"
        self.status_bar.showMessage(msg + "을 선택하셨습니다.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
