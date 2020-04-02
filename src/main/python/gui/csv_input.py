''' CSV module '''

from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QLineEdit, QPushButton, QGroupBox
from PyQt5.QtCore import pyqtSlot


class CSVInput(QGroupBox):
    ''' Create the CSV file module '''

    def __init__(self, parent):
        super().__init__()

        self.setTitle("CSV file:")

        csv_layout = QHBoxLayout()

        self.csv_text = QLineEdit()
        self.csv_text.setDisabled(True)
        self.csv_button = QPushButton("Search")
        self.csv_button.clicked.connect(self.search_csv_file)

        csv_layout.addWidget(self.csv_text, stretch=3)
        csv_layout.addWidget(self.csv_button, stretch=1)

        self.setLayout(csv_layout)

        parent.layout().addWidget(self)

    @pyqtSlot()
    def search_csv_file(self):
        ''' Select CSV file using native searchbox '''
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select CSV file",
            filter="Excel csv File (*.csv)",
            options=options)
        if filename:
            self.csv_text.setText(filename)
