import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QApplication, QMenuBar
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import webbrowser
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        textEdit = QTextEdit(f'ПРИЛОЖЕНИЕ ЧТОБЫ ПРИЛОЖИТЬ! \n '
                             f'\n НАЖМИТЕ "ЧИТАТЬ" ИЛИ "БАЗА ЗНАНИЙ"')
        self.setCentralWidget(textEdit)
        textEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        exitAction = QAction('&Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        QMenuBar.menubar = self.menuBar()
        QMenuBar.menubar.setNativeMenuBar(False)
        fileMenu = QMenuBar.menubar.addMenu('&Описание')
        openAct = QAction('&Открыть', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open file')
        editAct = QAction('&Редактировать', self)
        editAct.setShortcut('Ctrl+E')
        editAct.setStatusTip('Edit file')
        fileMenu.addAction(openAct)
        fileMenu.addAction(editAct)
        fileMenu.addAction(exitAction)

        fileMenu1 = QMenuBar.menubar.addMenu('&Инструкция')
        readAct = QAction('&Читать', self)
        readAct.setShortcut('Ctrl+R')
        readAct.setStatusTip('Push the button')
        readAct.triggered.connect(self.the_read_was_clicked)
        fileMenu1.addAction(readAct)
        fbAct = QAction('Обратная связь', self)
        fbAct.setShortcut('Ctrl+S')
        fbAct.setStatusTip('Leave feedback')
        fileMenu1.addAction(fbAct)
        fileMenu1.addAction(exitAction)

        fileMenu2 = QMenuBar.menubar.addMenu('&Помощь')
        helpAct = QAction("&База знаний", self)
        helpAct.setShortcut('Ctrl+H')
        helpAct.setStatusTip('Push the button')
        helpAct.triggered.connect(self.the_help_was_clicked)
        fileMenu2.addAction(helpAct)
        fileMenu2.addAction(exitAction)



        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Домашняя работа 26_4')
        self.show()

    def the_help_was_clicked(self):
        return webbrowser.open('https://realpython.com/python-menus-toolbars/')

    def the_read_was_clicked(self):
        return webbrowser.open('https://docs.python.org/3/tutorial/index.html')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
