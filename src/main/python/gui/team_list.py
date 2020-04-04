''' Teams module '''
from PyQt5.QtWidgets import QHBoxLayout, QListWidget, QGroupBox


class TeamList(QGroupBox):
    ''' TODO '''

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.setTitle("Teams in selected competition")
        self.setLayout(QHBoxLayout())
        self.list = QListWidget()
        self.layout().addWidget(self.list)
