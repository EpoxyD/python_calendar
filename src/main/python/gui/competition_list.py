''' Teams module '''
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QListWidget, QListWidgetItem

from cal_controller import Controller


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

    def update(self):
        print("update competitions")
        controller = Controller.get()

        if not controller.competitions:
            return

        for comp in controller.competitions.keys():
            self.list.addItem(comp)
