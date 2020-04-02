''' Frontend window '''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

from gui.csvmodule import CSVModule
from gui.generatemodule import GenerateModule
from gui.datamodule import DataModule

from cal_controller import parse_csv


class MainWindow(QWidget):
    ''' Create the main window '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Generator")
        self.setFixedSize(600, 300)

        self.setLayout(QGridLayout())
        self.layout().addWidget(CSVModule(self), 1, 1, 1, 2)
        self.layout().addWidget(DataModule(self, "Competitions"), 2, 1, 3, 1)
        self.layout().addWidget(DataModule(self, "Teams"), 2, 2, 3, 1)
        self.layout().addWidget(GenerateModule(self), 5, 1, 1, 2)

    @pyqtSlot()
    def update_competitions(self):
        print("update competitions")
        parse_csv(self.findChild())
