# I used icons from https://www.flaticon.com/
# I used code for web browser from there:
# https://github.com/learnpyqt/15-minute-apps/blob/20b3f89f2eb1b6e74cca59432cce4477ac3c0afa/browser_tabbed/browser_tabbed.py#L230

import sys
import os
import datetime
import sqlite3
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from Calculator import *
from Notebook import *
from History import *
from TicTacToe import *


class QActionMod(QAction):
    # Modified class for simplifying making UI
    def __init__(self, icon, name, description, obj):
        super(QActionMod, self).__init__(icon, name, obj)
        self.setStatusTip(description)


class Browser(QMainWindow):
    def __init__(self):
        # UI
        super().__init__()
        self.browser = QTabWidget()
        self.add_new_tab()
        self.setCentralWidget(self.browser)

        self.menu_bar()
        self.navigation_tool_bar()

        self.url.setText('https://google.com/')
        self.browser.setTabsClosable(True)
        self.browser.setTabBarAutoHide(True)
        self.browser.tabCloseRequested.connect(self.close_current_tab)

        self.setWindowIcon(QIcon('donut.png'))
        self.setWindowTitle("Clerk's browser")

    def navigation_tool_bar(self):
        # Creating navigation tool bar with functions
        navigation_tb = QToolBar("Навигация")
        navigation_tb.setIconSize(QSize(25, 20))
        self.addToolBar(navigation_tb)

        back_btn = QActionMod(QIcon('left-arrow.png'), 'Назад', 'Перейти на предыдущую страницу', self)
        back_btn.triggered.connect(self.browser.currentWidget().back)

        frwd_btn = QActionMod(QIcon('right-arrow.png'), "Вперед", "Перейти на следующую страницу", self)
        frwd_btn.triggered.connect(self.browser.currentWidget().forward)

        reload_btn = QActionMod(QIcon('reload_arrow.png'), "Перезагрузить", "Перезагрузить страницу", self)
        reload_btn.triggered.connect(self.browser.currentWidget().reload)

        home_btn = QActionMod(QIcon('house.png'), "Стартовая страница", "Вернуться на стартовую страницу", self)
        home_btn.triggered.connect(self.navigate_home)

        self.url = QLineEdit()
        self.url.editingFinished.connect(self.navigate_to_url)

        stop_btn = QActionMod(QIcon('close.png'), "Остановка", "Остановка загрузки страницы", self)
        stop_btn.triggered.connect(self.browser.currentWidget().stop)

        new_tab_action = QActionMod(QIcon('new_tab.png'), "Новая вкладка", "Открыть новую вкладку", self)
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())

        [navigation_tb.addAction(i) for i in [back_btn, frwd_btn, reload_btn, home_btn]]

        navigation_tb.addSeparator()
        navigation_tb.addAction(new_tab_action)
        navigation_tb.addSeparator()

        navigation_tb.addWidget(self.url)
        navigation_tb.addAction(stop_btn)

    def menu_bar(self):
        # Creating menu bar with additional apps
        menu = self.menuBar().addMenu("&Apps")
        files = self.menuBar().addMenu("&Files")

        calc = QActionMod(QIcon('calc.png'), 'Калькулятор', 'Открыть калькулятор', self)
        calc.triggered.connect(self.calculator)
        menu.addAction(calc)

        note = QActionMod(QIcon('notebook.png'), 'Заметки', 'Открыть заметки', self)
        note.triggered.connect(self.notebook)
        menu.addAction(note)

        hstry = QActionMod(QIcon('history.png'), 'История', 'История посещения веб-сайтов', self)
        hstry.triggered.connect(self.history)
        menu.addAction(hstry)

        ttt = QActionMod(QIcon('tic-tac-toe.png'), 'Крестики-Нолики', 'Запустить игру крестики-нолики', self)
        ttt.triggered.connect(self.tic_tac_toe)
        menu.addAction(ttt)

    def add_new_tab(self):
        # Create new tab
        new_tab = QWebEngineView()
        new_tab.setUrl(QUrl('https://google.com/'))
        i = self.browser.addTab(new_tab, new_tab.page().title())
        self.browser.setCurrentIndex(i)
        new_tab.loadFinished.connect(lambda _: self.browser.setTabText(i, new_tab.page().title()))
        new_tab.urlChanged.connect(lambda _: self.url.setText(new_tab.page().url().toString()))
        new_tab.urlChanged.connect(
            lambda _: self.add_to_history(new_tab.page().title(), new_tab.page().url().toString()))

    def close_current_tab(self, i):
        # Close tab under cursor
        if self.browser.count() < 2:
            return
        else:
            self.browser.removeTab(i)

    def navigate_home(self):
        # Open home page in current tab
        self.browser.currentWidget().setUrl(QUrl('https://google.com/'))
        self.url.setText('https://google.com/')

    def navigate_to_url(self):
        # Open user's url
        q = QUrl(self.url.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.currentWidget().setUrl(q)

    def calculator(self):
        # Open calculator
        self.calc = Calculator()
        self.calc.show()

    def notebook(self):
        # Open notebook
        self.notes = Notebook()
        self.notes.show()

    def add_to_history(self, name, url):
        # Extending user's history
        time = datetime.datetime.now()
        con = sqlite3.connect('history.sqlite')
        cur = con.cursor()
        cur.execute(f"""
            INSERT INTO history(Name, url, Time) VALUES('{name}', '{url}', '{time}')
        """)
        con.commit()
        con.close()

    def history(self):
        # Open history app
        self.hstry = History()
        self.hstry.show()

    def tic_tac_toe(self):
        # Open tic-tac-toe
        self.ttt = TicTacToe()
        self.ttt.show()


# Run web browser
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Browser()
    ex.show()
    sys.exit(app.exec_())
