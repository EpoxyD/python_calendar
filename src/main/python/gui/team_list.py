''' Teams module '''
from PyQt5.QtWidgets import QBoxLayout, QGridLayout, QGroupBox, QHBoxLayout, QListWidget, QListWidgetItem, QTextBrowser, QWidget


class TeamList(QGroupBox):
    ''' TODO '''

    def __init__(self, parent):
        super().__init__()

        self.setTitle("Teams in selected competition")
        self.setLayout(QHBoxLayout())
        self.list = QListWidget()
        self.layout().addWidget(self.list)
