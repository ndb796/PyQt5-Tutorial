import sys
from PyQt5.QtWidgets import *
from customer_util import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.column_count = CUSTOMER_NUM
        self.setup_ui()
        self.data_refresh()

    def data_refresh(self):
        self.customers = get_customers_from_db()
        self.set_table_widget_data()

    def setup_ui(self):
        self.setGeometry(800, 200, 300, 300)

        self.table_widget = QTableWidget()
        self.table_widget.cellClicked.connect(self.table_cell_clicked)

        self.customer_add_button = QPushButton("고객 정보 추가")
        self.customer_add_button.clicked.connect(self.customer_add_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.customer_add_button)

        self.setLayout(layout)

    def table_cell_clicked(self, row, col):
        customer_id = self.customers[row][0]
        name = self.customers[row][1]
        result = QMessageBox.question(self, '삭제 메시지', f"{name} 고객을 삭제하시겠습니까?",
                                            QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if result == QMessageBox.Yes:
            delete_customer_from_db(customer_id)
            self.data_refresh()

    def customer_add_button_clicked(self):
        dialog = CustomerAddDialog()
        result = dialog.exec_()

        if result:
            insert_customer_to_db(dialog.name, dialog.age, dialog.job)
            self.data_refresh()

    def set_table_widget_data(self):
        self.table_widget.setRowCount(0);
        self.table_widget.setRowCount(len(self.customers))
        self.table_widget.setColumnCount(self.column_count)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        column_headers = ['번호', '이름', '나이', '직업']
        self.table_widget.setHorizontalHeaderLabels(column_headers)

        for i in range(len(self.customers)):
            for j in range(self.column_count):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(self.customers[i][j])))

        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
