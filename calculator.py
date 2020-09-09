import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def click_add(self):
        result = int(self.first.text()) + int(self.second.text())
        self.lbl.setNum(result)
        self.lbl.adjustSize()

    def click_sub(self):
        result = int(self.first.text()) - int(self.second.text())
        self.lbl.setNum(result)
        self.lbl.adjustSize()

    def click_mul(self):
        result = int(self.first.text()) * int(self.second.text())
        self.lbl.setNum(result)
        self.lbl.adjustSize()

    def click_div(self):
        result = int(self.first.text()) / int(self.second.text())
        self.lbl.setNum(result)
        self.lbl.adjustSize()

    def initUI(self):
        add_btn = QPushButton(self)
        add_btn.setText("+")
        add_btn.clicked.connect(self.click_add)

        sub_btn = QPushButton(self)
        sub_btn.setText("-")
        sub_btn.clicked.connect(self.click_sub)

        mul_btn = QPushButton(self)
        mul_btn.setText("x")
        mul_btn.clicked.connect(self.click_mul)

        div_btn = QPushButton(self)
        div_btn.setText("/")
        div_btn.clicked.connect(self.click_div)

        self.first = QLineEdit(self)
        self.first.move(10,20)
        self.first.setText('')

        self.second = QLineEdit(self)
        self.second.move(10,60)
        self.second.setText('')

        self.lbl = QLabel(self)
        self.lbl.setText('result here')

        grid = QGridLayout()
        grid.addWidget(QLabel('Num :'), 0, 0)
        grid.addWidget(QLabel('Cal :'), 1, 0)
        grid.addWidget(QLabel('Result :'), 2, 0)

        grid.addWidget(add_btn, 1, 1)
        grid.addWidget(sub_btn, 1, 2)
        grid.addWidget(mul_btn, 1, 3)
        grid.addWidget(div_btn, 1, 4)

        grid.addWidget(self.lbl, 2, 1)

        self.setLayout(grid)
        self.setWindowTitle('calculator')
        self.setGeometry(300, 300, 700, 700)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
