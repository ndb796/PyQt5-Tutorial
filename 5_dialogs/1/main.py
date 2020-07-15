import sys
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(800, 200, 300, 300)

        self.file_button = QPushButton("File Open")
        self.file_button.clicked.connect(self.file_button_clicked)

        self.folder_button = QPushButton("Folder Open")
        self.folder_button.clicked.connect(self.folder_button_clicked)

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.file_button)
        layout.addWidget(self.folder_button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def file_button_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, "파일을 선택하세요.")
        self.label.setText(file_name[0])

    def folder_button_clicked(self):
        file_name = QFileDialog.getExistingDirectory(self, '폴더를 선택하세요.', options=QFileDialog.DontUseNativeDialog)
        self.label.setText(file_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
