import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout, QInputDialog, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot


class MainScreen(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Generator")
        self.setWindowIcon(QIcon(QPixmap("src/img/pool.ico")))

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(FileSelector(self))

    @pyqtSlot()
    def search_csv_file(self):
        pass


class FileSelector(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        csv_label = QLabel("CSV file path:")
        csv_line_edit = QLineEdit()
        csv_line_edit.setDisabled(True)
        csv_button = QPushButton("Search")
        csv_button.clicked.connect(self.search_csv_file)

        self.layout.addWidget(csv_label)
        self.layout.addWidget(csv_line_edit)
        self.layout.addWidget(csv_button)

    @pyqtSlot()
    def search_csv_file(self):
        options = QFileDialog.Options()
        filename = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select CSV file",
            filter="Excel Comma Seperated Value (*.csv)",
            options=options)
        if filename:
            print(filename)


if __name__ == "__main__":
    window = QApplication(sys.argv)
    app = MainScreen()
    app.show()
    sys.exit(window.exec_())
