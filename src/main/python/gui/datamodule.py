''' Teams module '''
from PyQt5.QtWidgets import QBoxLayout, QGridLayout, QGroupBox, QHBoxLayout, QListWidget, QListWidgetItem, QTextBrowser, QWidget


class DataModule(QGroupBox):
    ''' TODO '''

    def __init__(self, parent, data):
        super().__init__()

        self.setTitle("%s:" % data)
        self.setLayout(QHBoxLayout())
        self.list = QListWidget()
        self.layout().addWidget(self.list)

        # self.teams = QGroupBox("Teams:")
        # self.teams.setLayout(QHBoxLayout())
        # self.teams.list = QListWidget()
        # self.teams.layout().addWidget(self.teams.list)
        # parent.layout().addWidget(self)


# class TeamsModule(QGroupBox):
#     ''' TODO '''

#     def __init__(self, parent):
#         super().__init__()

#         self.competitions = QGroupBox("Competitions:")
#         self.competitions.setLayout(QHBoxLayout())
#         self.competitions.list = QListWidget()
#         self.competitions.layout().addWidget(self.competitions.list)

#         self.teams = QGroupBox("Teams:")
#         self.teams.setLayout(QHBoxLayout())
#         self.teams.list = QListWidget()
#         self.teams.layout().addWidget(self.teams.list)

#         layout.addWidget(self.competitions, 1, 1)
#         layout.addWidget(self.teams, 1, 2)

#         self.setLayout(layout)
#         parent.layout().addWidget(self)
