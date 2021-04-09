import sys

from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class History(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Make app for manipulating with browser's history data base
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('history.sqlite')
        db.open()

        view = QTableView(self)

        model = QSqlTableModel(self, db)
        model.setTable('history')
        model.select()

        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)

        self.setGeometry(300, 100, 650, 450)
        self.setWindowTitle("Clerk's notebook")
        self.setWindowIcon(QtGui.QIcon('history.png'))
