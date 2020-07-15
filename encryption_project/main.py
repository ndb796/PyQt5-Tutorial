import sys
from PyQt5.QtWidgets import *

from lib import Encryptor


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        file_ext_targets = ['txt', 'py']
        self.encryptor = Encryptor(file_ext_targets)
        self.folder_name = ""

    def setup_ui(self):
        self.setGeometry(800, 200, 400, 400)

        self.folder_button = QPushButton("Folder Open")
        self.folder_button.clicked.connect(self.folder_button_clicked)

        self.label = QLabel()
        self.label.setText("암호화/복호화를 진행할 폴더를 선택하세요.")

        self.radio_encrypt = QRadioButton("암호화", self)
        self.radio_encrypt.setChecked(True)

        self.radio_decrypt = QRadioButton("복호화", self)

        self.execute_button = QPushButton("Execute")
        self.execute_button.clicked.connect(self.execute_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.folder_button)
        layout.addWidget(self.label)
        layout.addWidget(self.radio_encrypt)
        layout.addWidget(self.radio_decrypt)
        layout.addWidget(self.execute_button)

        self.setLayout(layout)

    def folder_button_clicked(self):
        self.folder_name = QFileDialog.getExistingDirectory(self, '폴더를 선택하세요.', options=QFileDialog.DontUseNativeDialog)
        self.label.setText("선택된 폴더: " + self.folder_name)

    def execute_button_clicked(self):
        if self.folder_name == "":
            self.label.setText("폴더를 선택해야 합니다.")
            return
        if self.radio_encrypt.isChecked():
            self.encryptor.generate_key()
            file_name = QFileDialog.getSaveFileName(self, '키를 저장할 경로를 선택하세요.')
            self.encryptor.crypt_root(self.folder_name, encrypting=True)
            self.encryptor.write_key(file_name[0])
        else:
            file_name = QFileDialog.getOpenFileName(self, '복호화 키의 경로를 선택하세요.')
            self.encryptor.read_key(file_name[0])
            self.encryptor.crypt_root(self.folder_name, encrypting=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
