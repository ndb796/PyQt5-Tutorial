import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(800, 200, 260, 300)

        combo_box = QComboBox(self)
        combo_box.addItem('학부생')
        combo_box.addItem('대학원생')
        combo_box.addItem('직장인')
        combo_box.move(50, 50)

        combo_box.activated[str].connect(self.combo_box_clicked)

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

    def combo_box_clicked(self, text):
        self.status_bar.showMessage(text + "을 선택하셨습니다.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
