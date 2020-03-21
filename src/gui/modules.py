''' csv module in main window '''

from PyQt5.QtWidgets import QFileDialog, QGridLayout, QGroupBox, QHBoxLayout, QLineEdit, QPushButton, QSpacerItem, QTextEdit, QWidget
from PyQt5.QtCore import pyqtSlot


class CSVSelectModule(QGroupBox):
    ''' Create the CSV file module '''

    def __init__(self, parent):
        super().__init__()

        self.setTitle("CSV file:")

        csv_layout = QHBoxLayout()

        self.csv_line_edit = QLineEdit()
        self.csv_line_edit.setDisabled(True)
        self.csv_button = QPushButton("Search")
        self.csv_button.clicked.connect(self.search_csv_file)

        csv_layout.addWidget(self.csv_line_edit, stretch=3)
        csv_layout.addWidget(self.csv_button, stretch=1)

        self.setLayout(csv_layout)

        parent.layout.addWidget(self)

    @pyqtSlot()
    def search_csv_file(self):
        ''' Select CSV file using native searchbox '''
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select CSV file",
            filter="Excel Comma Seperated Value (*.csv)",
            options=options)
        if filename:
            self.csv_line_edit.setText(filename)
            print(filename)


class TeamsModule(QGroupBox):
    ''' Create the CSV file module '''

    def __init__(self, parent):
        super().__init__()

        self.setTitle("Teams in csv file:")

        layout = QGridLayout()
        self.team_textbox = QTextEdit()
        self.team_textbox.setDisabled(True)
        layout.addWidget(self.team_textbox)

        self.setLayout(layout)
        parent.layout.addWidget(self)


class GenerateModule(QPushButton):
    ''' Add the generate Button '''

    def __init__(self, parent):
        super().__init__()

        self.setText("Generate!")
        parent.layout.addWidget(self)
