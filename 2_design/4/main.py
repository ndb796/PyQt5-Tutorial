import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QWidget {
                background: beige;
            }
            QPushButton {
                background-color: white;
            }
            QPushButton#confirm_button {
                background-color: red;
            }
        """)

        default_widget = DefaultWidget()
        self.setCentralWidget(default_widget)


class DefaultWidget(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel('Do you like chicken?')
        confirm_button = QPushButton('Yes')
        confirm_button.setObjectName("confirm_button")
        cancel_button = QPushButton('No')
        
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(confirm_button)
        layout.addWidget(cancel_button)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
