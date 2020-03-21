''' Frontend window '''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

from src.main.python.gui.modules import CSVSelectModule, GenerateModule, TeamsModule


class MainWindow(QWidget):
    ''' Create the main window '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Generator")
        self.setWindowIcon(QIcon(QPixmap("src/img/pool.ico")))
        self.setFixedSize(600, 300)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(CSVSelectModule(self), stretch=1)
        self.layout.addWidget(TeamsModule(self), stretch=3)
        self.layout.addWidget(GenerateModule(self), stretch=1)
