''' Teams module '''
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QListWidget


class CompetitionList(QGroupBox):
    '''
        A Dialog which lists all competitions in the provided CSV file,
        and has boxes for entering how many round should be generated
        for each of these competitions.
    '''

    def __init__(self, parent):
        super().__init__()

        self.setTitle("Competitions")
        self.setLayout(QHBoxLayout())
        self.list = QListWidget()
        self.layout().addWidget(self.list)
