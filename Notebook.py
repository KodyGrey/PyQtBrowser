from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Notebook(QMainWindow):
    def __init__(self):
        super().__init__()
        # Creating UI
        self.resize(800, 600)
        self.setWindowIcon(QtGui.QIcon('notebook.png'))
        self.setWindowTitle("Clerk's notebook")
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        lst = [[QtWidgets.QLabel(self.centralwidget), QtCore.QRect(16, 10, 141, 31), 'label', 'Имя Файла:'],
               [QtWidgets.QPushButton(self.centralwidget), QtCore.QRect(120, 530, 161, 41), "pushButton",
                "Загрузить"],
               [QtWidgets.QPushButton(self.centralwidget), QtCore.QRect(490, 530, 161, 41), 'pushButton_2',
                'Сохранить']]
        for i in lst:
            obj, geom, name, txt = i[0], i[1], i[2], i[3]
            obj.setGeometry(geom)
            obj.setText(txt)
            if txt == 'Загрузить':
                obj.clicked.connect(self.load_file)
            elif txt == 'Сохранить':
                obj.clicked.connect(self.save_file)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 10, 621, 31))
        self.lineEdit.setText('notes.txt')

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 60, 781, 461))
        self.textBrowser.setReadOnly(False)

    def load_file(self):
        # Put text from file into field
        try:
            with open('Notes/' + self.lineEdit.text(), 'r', encoding='utf8') as f:
                self.textBrowser.setText(f.read())
        except FileNotFoundError:
            self.textBrowser.setText('''В директории нет такого файла, для создания файла
             нажмите кнопку сохранить после редактирования''')

    def save_file(self):
        # Save text into file
        text = self.textBrowser.toPlainText()
        with open('Notes/' + self.lineEdit.text(), 'w', encoding='utf8') as f:
            f.write(text)
