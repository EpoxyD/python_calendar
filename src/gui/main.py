''' Frontend window '''

import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QGroupBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot


class MainScreen(QWidget):
    ''' Create the main window '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Generator")
        self.setWindowIcon(QIcon(QPixmap("src/img/pool.ico")))
        self.setMinimumWidth(600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(FileSelector(self))


class FileSelector(QWidget):
    ''' Create the CSV file module '''

    def __init__(self, parent):
        super().__init__()

        csv_layout = QHBoxLayout()

        # self.csv_label = QLabel("CSV file path:")
        self.csv_line_edit = QLineEdit()
        self.csv_line_edit.setDisabled(True)
        self.csv_button = QPushButton("Search")
        self.csv_button.clicked.connect(self.search_csv_file)

        # self.layout.addWidget(self.csv_label, stretch=1)
        csv_layout.addWidget(self.csv_line_edit, stretch=3)
        csv_layout.addWidget(self.csv_button, stretch=1)

        self.csv_box = QGroupBox("CSV file:")
        self.csv_box.setLayout(csv_layout)

        parent.layout.addWidget(self.csv_box)

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


if __name__ == "__main__":
    WINDOW = QApplication(sys.argv)
    APP = MainScreen()
    APP.show()
    sys.exit(WINDOW.exec_())
