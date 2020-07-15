# To do 1: 클래스 분리 및 모듈화 필요.
# To do 2: DB 관련 예외 처리 필요.

import sqlite3
from PyQt5.QtWidgets import *

db_path = './customer.db'
CUSTOMER_NUM = 4


def get_customers_from_db():
    customers = []

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('SELECT * FROM CUSTOMER;')
    for row in cur:
        customers.append(row)
    con.close()

    return customers


def delete_customer_from_db(customer_id):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("DELETE FROM CUSTOMER WHERE id = ?;", (customer_id,))
    con.commit()
    con.close()


def insert_customer_to_db(name, age, job):
    customer = (name, age, job)

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO CUSTOMER (name, age, job) VALUES (?, ?, ?);", customer)
    con.commit()
    con.close()


class CustomerAddDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

        self.name = None
        self.age = None
        self.job = None

    def setupUi(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("고객 정보 추가")

        label1 = QLabel("이름: ")
        label2 = QLabel("나이: ")
        label3 = QLabel("직업: ")

        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit3 = QLineEdit()

        self.add_button = QPushButton("등록")
        self.add_button.clicked.connect(self.add_button_clicked)

        self.close_button = QPushButton("취소")
        self.close_button.clicked.connect(self.close_button_clicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.line_edit1, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.line_edit2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.line_edit3, 2, 1)
        layout.addWidget(self.add_button, 3, 0)
        layout.addWidget(self.close_button, 3, 1)

        self.setLayout(layout)

    def add_button_clicked(self):
        self.name = self.line_edit1.text()
        self.age = self.line_edit2.text()
        self.job = self.line_edit3.text()
        self.accept()

    def close_button_clicked(self):
        self.reject()
