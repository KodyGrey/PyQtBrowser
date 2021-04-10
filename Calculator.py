import sys
import math

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Calculator(QMainWindow):
    def __init__(self):
        # Creating UI
        super().__init__()
        self.resize(371, 565)

        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 342, 481))
        self.layoutWidget.setObjectName("layoutWidget")

        # Creating number panel
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QLCDNumber(self.layoutWidget)
        self.table.setObjectName("table")
        self.verticalLayout.addWidget(self.table)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)

        # Creating buttons on grid layout
        # object, coords, name, what connect
        lst = [[QtWidgets.QPushButton(self.layoutWidget), (2, 1, 1, 1), '8', self.nums],
               [QtWidgets.QPushButton(self.layoutWidget), (0, 0, 1, 1), '1', self.nums],
               [QtWidgets.QPushButton(self.layoutWidget), (2, 2, 1, 1), '9', self.nums],
               [QtWidgets.QPushButton(self.layoutWidget), (0, 2, 1, 1), '3', self.nums],
               [QtWidgets.QPushButton(self.layoutWidget), (1, 0, 1, 1), '4', self.nums],
               [QtWidgets.QPushButton(self.layoutWidget), (1, 1, 1, 1), '5', self.nums],
               [QtWidgets.QPushButton(self.layoutWidget), (2, 0, 1, 1), '7', self.nums],
               [QtWidgets.QPushButton(self.layoutWidget), (1, 2, 1, 1), '6', self.nums],
               [QtWidgets.QPushButton(self.layoutWidget), (0, 1, 1, 1), '2', self.nums],
               [QtWidgets.QPushButton(self.layoutWidget), (0, 3, 1, 1), '+', self.operations],
               [QtWidgets.QPushButton(self.layoutWidget), (1, 3, 1, 1), '-', self.operations],
               [QtWidgets.QPushButton(self.layoutWidget), (3, 3, 1, 1), '/', self.operations],
               [QtWidgets.QPushButton(self.layoutWidget), (2, 3, 1, 1), '*', self.operations],
               [QtWidgets.QPushButton(self.layoutWidget), (4, 0, 1, 1), '^', self.operations],
               [QtWidgets.QPushButton(self.layoutWidget), (3, 2, 1, 1), '=', self.equal],
               [QtWidgets.QPushButton(self.layoutWidget), (3, 0, 1, 1), '0', self.num0],
               [QtWidgets.QPushButton(self.layoutWidget), (4, 1, 1, 1), '√', self.sq_root],
               [QtWidgets.QPushButton(self.layoutWidget), (4, 2, 1, 1), "!", self.factorial],
               [QtWidgets.QPushButton(self.layoutWidget), (4, 3, 1, 1), 'С', self.clear],
               [QtWidgets.QPushButton(self.layoutWidget), (3, 1, 1, 1), '.', self.dot]]

        for i in lst:
            obj, coor, name, con = i
            obj.setMinimumSize(QtCore.QSize(80, 80))
            obj.setMaximumSize(QtCore.QSize(80, 80))
            obj.setText(name)
            obj.setFont(font)
            obj.clicked.connect(con)
            self.gridLayout.addWidget(obj, coor[0], coor[1], coor[2], coor[3])

        self.verticalLayout.addLayout(self.gridLayout)

        self.text = '0'
        self.can_input = True
        self.first_num = '0'
        self.second_num = '0'
        self.operation = ''
        self.setWindowIcon(QtGui.QIcon('calc.png'))
        self.setWindowTitle("Clerk's calculator")

    def make_operation(self):
        # Make arithmetic operation
        try:
            ans = str(
                eval(f'{self.first_num} {self.operation} {self.second_num}'))
            if len(ans) > 5:
                ans = ans[:5]
            self.text = ans
            return ans
        except ArithmeticError:
            return 'Error'

    def clear(self):
        # Clear calculator menu
        self.text = '0'
        self.operation = ''
        self.can_input = True
        self.table.display(self.text)

    def num0(self):
        # Operation for number 0
        if not self.can_input:
            self.text = '0'
            self.table.display(self.text)
            self.can_input = True
        if self.text != '0':
            self.text += '0'
            self.table.display(self.text)

    def nums(self):
        # Put number into workspace
        num = self.sender().text()
        if not self.can_input:
            self.text = num
            self.table.display(self.text)
            self.can_input = True
        if self.text != '0':
            self.text += num
            self.table.display(self.text)
        else:
            self.text = num
            self.table.display(self.text)

    def dot(self):
        # Put dot into workspace
        if not self.can_input:
            self.text = '0.'
            self.table.display(self.text)
            self.can_input = True
        else:
            self.text += '.'
            self.table.display(self.text)

    def operations(self):
        # Put arithmetical operation into workspace
        if self.sender().text() == '-' and (
                self.text == '0' or self.text == '0.0'):
            self.text = '-'
            self.table.display(self.text)
        else:
            self.first_num = self.text
            self.operation = self.sender().text()
            if self.operation == '^':
                self.operation = '**'

            self.text = '0'
            self.can_input = True
            self.table.display(self.text)

    def factorial(self):
        # Make factorial operation
        self.text = str(math.factorial(int(self.text))) if '.' not in self.text \
            else 'Error'
        if len(self.text) > 5:
            self.text = self.text[:5]
        self.table.display(self.text)

    def sq_root(self):
        # Make square root operation
        try:
            self.text = str(math.sqrt(float(self.text)))
            if len(self.text) > 5:
                self.text = self.text[:5]
            self.table.display(self.text)
        except ValueError:
            self.text = 'Error'
            self.table.display(self.text)

    def equal(self):
        # Get result of arithmetical operation
        try:
            self.second_num = self.text
            self.table.display(self.make_operation())
            self.can_input = False
        except Exception as ex:
            pass

# Hello Alexey Levushkin
