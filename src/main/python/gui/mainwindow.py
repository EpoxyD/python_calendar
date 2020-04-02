''' Frontend window '''

from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtCore import pyqtSlot

from gui.csv_input import CSVInput
from gui.competition_list import CompetitionList
from gui.team_list import TeamList
from gui.generate_button import GenerateButton


class MainWindow(QWidget):
    ''' Create the main window '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Generator")
        self.setFixedSize(600, 400)

        self.setLayout(QGridLayout())
        self.layout().addWidget(CSVInput(self), 1, 1, 1, 2)
        self.layout().addWidget(CompetitionList(self), 2, 1, 2, 2)
        self.layout().addWidget(TeamList(self), 4, 1, 2, 2)
        self.layout().addWidget(GenerateButton(self), 6, 1, 1, 2)

    @pyqtSlot()
    def update_competitions(self):
        ''' Generate competitions in the datamodule '''
        print("update competitions")
