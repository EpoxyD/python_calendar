import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from gui.mainwindow import MainWindow

if __name__ == '__main__':
    APP_CTX = ApplicationContext()       # 1. Instantiate ApplicationContext
    WINDOW = QMainWindow()
    WINDOW.setCentralWidget(MainWindow())
    WINDOW.show()
    EXIT_CODE = APP_CTX.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(EXIT_CODE)
