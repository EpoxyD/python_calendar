''' Frontend window '''

import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QGroupBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

from gui.modules import CSVSelectModule, GenerateModule, TeamsModule


class MainScreen(QWidget):
    ''' Create the main window '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Generator")
        self.setWindowIcon(QIcon(QPixmap("src/img/pool.ico")))
        self.setFixedSize(600,300)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(CSVSelectModule(self), stretch=1)
        self.layout.addWidget(TeamsModule(self), stretch=3)
        self.layout.addWidget(GenerateModule(self),stretch=1)


if __name__ == "__main__":
    WINDOW = QApplication(sys.argv)
    APP = MainScreen()
    APP.show()
    sys.exit(WINDOW.exec_())
