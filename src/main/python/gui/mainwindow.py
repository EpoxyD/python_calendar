''' Frontend window '''

from PyQt5.QtWidgets import QWidget, QGridLayout

from gui.csv_input import CSVInput
from gui.competition_list import CompetitionList
from gui.team_list import TeamList
from gui.generate_button import GenerateButton

from cal_controller import Controller


class MainWindow(QWidget):
    ''' Create the main window '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Generator")
        self.setFixedSize(600, 400)

        Controller.parentWidget = self

        self.setLayout(QGridLayout())

        self.csv_input = CSVInput(self)
        self.comp_list = CompetitionList(self)
        self.team_list = TeamList(self)
        self.gen_button = GenerateButton(self)

        self.layout().addWidget(self.csv_input, 1, 1, 1, 2)
        self.layout().addWidget(self.comp_list, 2, 1, 2, 2)
        self.layout().addWidget(self.team_list, 4, 1, 2, 2)
        self.layout().addWidget(self.gen_button, 6, 1, 1, 2)

    def update_competitions(self):
        print("update competitions")
        self.comp_list.update()
