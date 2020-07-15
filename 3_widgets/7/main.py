import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(800, 200, 300, 300)

        date_edit = QDateEdit(self)
        date_edit.setDate(QDate.currentDate())
        date_edit.setMinimumDate(QDate(1900, 1, 1))
        date_edit.setMaximumDate(QDate(2100, 12, 31))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
