import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(800, 200, 260, 300)

        self.input_button = QPushButton("Push Me!")
        self.input_button.clicked.connect(self.input_button_clicked)

        self.age_label = QLabel()
        self.name_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.input_button)
        layout.addWidget(self.age_label)
        layout.addWidget(self.name_label)

        self.setLayout(layout)

    def input_button_clicked(self):
        text, flag = QInputDialog.getInt(self, "나이", "나이를 입력하세요.")
        if flag:
            self.age_label.setText("나이: " + str(text))
        text, flag = QInputDialog.getText(self, "이름", "이름을 입력하세요.")
        if flag:
            self.name_label.setText("이름: " + str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
