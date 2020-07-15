import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("클래스로 정의한 화면")
        button = QPushButton("Push me!", self)
        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        QMessageBox.information(self, "Information", "You clicked me!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
