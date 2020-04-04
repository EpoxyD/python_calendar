''' Generate Module '''

from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot


class GenerateButton(QWidget):
    ''' Add the generate Button '''

    def __init__(self, parent):
        super().__init__()

        self.button = QPushButton("Generate!")
        # self.button.clicked.connect(self.update_competitions)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.button)

        self.setContentsMargins(0, 0, 0, 0)

        parent.layout().addWidget(self)
