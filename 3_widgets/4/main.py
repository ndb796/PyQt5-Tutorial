import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(800, 400, 260, 150)

        label = QLabel("이름:", self)
        label.move(20, 20)

        self.line_edit = QLineEdit("", self)
        self.line_edit.move(80, 20)
        self.line_edit.textChanged.connect(self.line_edit_changed)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

    def line_edit_changed(self):
        self.status_bar.showMessage("당신의 이름은: " + self.line_edit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
