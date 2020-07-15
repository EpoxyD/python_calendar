''' Frontend window '''

from pathlib import Path
from shutil import copyfile
import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QGroupBox, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QLineEdit, QPushButton


class CSVInput(QGroupBox):
    ''' Create a box for inputting CSV file '''

    def __init__(self):
        super().__init__()
        self.setTitle("Teams CSV file")

        self.csv_text = QLineEdit()
        self.csv_text.setEnabled(True)
        self.csv_text.setAcceptDrops(True)
        self.csv_button = QPushButton("Browse ...")
        self.csv_button.clicked.connect(self.search_csv_file)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.csv_text, stretch=3)
        self.layout().addWidget(self.csv_button, stretch=1)

    def search_csv_file(self):
        ''' Browse computer for the csv file '''
        filename, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select CSV file",
            filter="Excel csv File (*.csv)",
            options=QFileDialog.Options())
        if filename:
            self.csv_text.setText(filename)


class GenerateCalendar(QPushButton):
    ''' Add the generate Button '''

    def __init__(self):
        super().__init__()
        self.button = QPushButton("Generate calendar!")
        self.button.clicked.connect(self.generate_calendar)
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.button)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def generate_calendar(self):
        print("Generate Calendar!")


class DownloadExample(QPushButton):
    ''' Download an example file '''

    def __init__(self):
        super().__init__()
        self.button = QPushButton("Download an example CSV file")
        self.button.clicked.connect(self.download_csv_file)
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.button)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def download_csv_file(self):
        example_file_path = "/home/sahnalys09/Documents/Github/python_calendar/csv/example.csv"
        downloads_path = str(Path.home()) + '/Downloads/example.csv'
        copyfile(example_file_path, downloads_path)
        popup = QMessageBox(QMessageBox.Information, "Download Status", "Example file copied to " + downloads_path)
        popup.addButton(QMessageBox.Ok)
        popup.exec()


class MainWindow(QWidget):
    ''' Create the main window '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Generator")
        self.setFixedWidth(800)
        self.setLayout(QVBoxLayout())

        self.layout().addWidget(CSVInput())
        self.layout().addWidget(GenerateCalendar())
        self.layout().addWidget(DownloadExample())


class AppContext(ApplicationContext):
    ''' Starting point for the GUI '''

    def __init__(self):
        super().__init__()
        app_window = QMainWindow()
        app_window.setCentralWidget(MainWindow())
        app_window.show()
        sys.exit(self.app.exec_())
