''' Central controller file '''

import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

from gui.mainwindow import MainWindow

from cal_parser import parse_csv, parse_output
from cal_generator import generate_padding, generate_calendars

CALENDAR_CONTEXT = {}


def start():
    ''' Start the controller '''
    csv_file = "csv/teams.csv"

    rounds = {"WEEKS": 30, "ERE": 2, "EERSTE": 3}

    competitions, restrictions = parse_csv(csv_file)

    generate_padding(competitions, rounds)

    calendars = generate_calendars(competitions, restrictions, rounds)

    parse_output(calendars)

    return 0

def parse_input_file(csv_file):
    ''' parse input file '''
    competitions, restrictions = parse_csv(csv_file)

    if not competitions:
        print("competition error")
    if not restrictions:
        print("restriction error")

    CALENDAR_CONTEXT["competitions"] = competitions
    CALENDAR_CONTEXT["restrictions"] = restrictions

    return competitions, restrictions


def run():
    ''' run the application '''
    app_ctx = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = QMainWindow()
    window.setCentralWidget(MainWindow())
    window.show()
    EXIT_CODE = app_ctx.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(EXIT_CODE)
