import sys

from PyQt5.QtWidgets import QApplication
from src.gui.mainwindow import MainScreen

if __name__ == "__main__":
    WINDOW = QApplication(sys.argv)
    APP = MainScreen()
    APP.show()
    sys.exit(WINDOW.exec_())
