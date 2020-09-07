#!/usr/bin/python3

''' entrypoint for the application '''

from parser import csv_parse

if __name__ == '__main__':
    TEAMS = csv_parse("csv/example.csv")
    for team in TEAMS:
        print(team)
