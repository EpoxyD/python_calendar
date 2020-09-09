#!/usr/bin/python3

''' entrypoint for the application '''

from parser import csv_parse
from generator import generate_calendar

if __name__ == '__main__':
    DATA = csv_parse("csv/example.csv")
    CALENDAR = generate_calendar(DATA)
