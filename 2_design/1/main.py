import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("example.ui")[0]


class MyWindow(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        self.textEdit.setText("Hello World!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
