import sys
from PyQt5.QtWidgets import *


# Callback 함수
def clicked_slot():
    print('Clicked!')


app = QApplication(sys.argv)

# Button 위젯
btn = QPushButton("Push me!")
btn.clicked.connect(clicked_slot)
btn.show()

# GUI 프로그램 동작 시작
print("이벤트 루프가 시작됩니다...")
app.exec_()
print("이벤트 루프를 종료됩니다...")
