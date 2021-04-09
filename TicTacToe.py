from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        # Creating UI
        self.resize(278, 377)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 211, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Set text label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(36, 233, 201, 20))
        self.label.setObjectName("label")

        self.clear()

        # Button for game restarting
        self.btn_restart = QtWidgets.QPushButton(self.centralwidget)
        self.btn_restart.setGeometry(QtCore.QRect(30, 270, 211, 51))
        self.btn_restart.setObjectName("btn_restart")
        self.btn_restart.setText('Сбросить')
        self.btn_restart.clicked.connect(self.clear)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.setWindowIcon(QIcon('tic-tac-toe.png'))
        self.setWindowTitle("Clerk's browser")

    def clear(self):
        # Make and clear field
        self.label.setText('Игра продолжается')

        self.winner = ''
        self.btn = 'X'
        self.status = [['', '', ''],
                       ['', '', ''],
                       ['', '', '']]
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        # object, coords, name, what connect
        lst = [[QtWidgets.QPushButton(self.gridLayoutWidget), (2, 1, 1, 1), ''],
               [QtWidgets.QPushButton(self.gridLayoutWidget), (2, 0, 1, 1), ''],
               [QtWidgets.QPushButton(self.gridLayoutWidget), (1, 2, 1, 1), ''],
               [QtWidgets.QPushButton(self.gridLayoutWidget), (0, 2, 1, 1), ''],
               [QtWidgets.QPushButton(self.gridLayoutWidget), (0, 0, 1, 1), ''],
               [QtWidgets.QPushButton(self.gridLayoutWidget), (0, 1, 1, 1), ''],
               [QtWidgets.QPushButton(self.gridLayoutWidget), (1, 0, 1, 1), ''],
               [QtWidgets.QPushButton(self.gridLayoutWidget), (1, 1, 1, 1), ''],
               [QtWidgets.QPushButton(self.gridLayoutWidget), (2, 2, 1, 1), '']]

        for i in lst:
            obj, coor, name = i
            obj.setText(name)
            obj.setFont(font)
            obj.coord = coor
            obj.clicked.connect(self.make_turn)
            self.gridLayout.addWidget(obj, coor[0], coor[1], coor[2], coor[3])

    def make_turn(self):
        # Function is called when symbol is placed
        if self.sender().text() == '':
            coords = self.sender().coord
            self.sender().setText(self.btn)
            self.status[coords[0]][coords[1]] = self.btn
            if self.btn == 'X':
                self.btn = 'O'
            else:
                self.btn = 'X'
            if self.winner == '':
                self.check_winner()

    def check_winner(self):
        # Check if someone won
        if ((self.status[0][0] == self.status[0][1] and self.status[0][1] == self.status[0][2] and self.status[0][
            0] == 'X') or
                (self.status[1][0] == self.status[1][1] and self.status[1][1] == self.status[1][2] and self.status[1][
                    0] == 'X') or
                (self.status[2][0] == self.status[2][1] and self.status[2][1] == self.status[2][2] and self.status[2][
                    0] == 'X') or
                (self.status[0][0] == self.status[1][0] and self.status[1][0] == self.status[2][0] and self.status[0][
                    0] == 'X') or
                (self.status[0][1] == self.status[1][1] and self.status[1][1] == self.status[2][1] and self.status[0][
                    1] == 'X') or
                (self.status[0][2] == self.status[1][2] and self.status[1][2] == self.status[2][2] and self.status[0][
                    2] == 'X') or
                (self.status[0][0] == self.status[1][1] and self.status[1][1] == self.status[2][2] and self.status[0][
                    0] == 'X') or
                (self.status[0][2] == self.status[1][1] and self.status[1][1] == self.status[2][0] and self.status[0][
                    2] == 'X')):
            self.winner = 'X'
            self.label.setText('Победил X')

        if ((self.status[0][0] == self.status[0][1] and self.status[0][1] == self.status[0][2] and self.status[0][
            0] == 'O') or
                (self.status[1][0] == self.status[1][1] and self.status[1][1] == self.status[1][2] and self.status[1][
                    0] == 'O') or
                (self.status[2][0] == self.status[2][1] and self.status[2][1] == self.status[2][2] and self.status[2][
                    0] == 'O') or
                (self.status[0][0] == self.status[1][0] and self.status[1][0] == self.status[2][0] and self.status[0][
                    0] == 'O') or
                (self.status[0][1] == self.status[1][1] and self.status[1][1] == self.status[2][1] and self.status[0][
                    1] == 'O') or
                (self.status[0][2] == self.status[1][2] and self.status[1][2] == self.status[2][2] and self.status[0][
                    2] == 'O') or
                (self.status[0][0] == self.status[1][1] and self.status[1][1] == self.status[2][2] and self.status[0][
                    0] == 'O') or
                (self.status[0][2] == self.status[1][1] and self.status[1][1] == self.status[2][0] and self.status[0][
                    2] == 'O')):
            self.winner = 'O'
            self.label.setText('Победил O')
