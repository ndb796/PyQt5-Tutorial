import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(800, 400, 260, 150)

        self.label = QLabel("", self)
        self.label.move(100, 20)
        self.label.resize(140, 20)

        btn1 = QPushButton("Click", self)
        btn1.move(20, 60)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton("Clear", self)
        btn2.move(140, 60)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        self.label.setText("Clicked!")

    def btn2_clicked(self):
        self.label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
