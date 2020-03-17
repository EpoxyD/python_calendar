''' Central controller file '''

from parser import parse_csv, parse_output
from generator import generate_padding, generate_calendars


def start():
    ''' Start the controller '''
    csv_file = "csv/teams.csv"

    rounds = {"WEEKS": 30, "ERE": 2, "EERSTE": 3}

    competitions, restrictions = parse_csv(csv_file)

    generate_padding(competitions, rounds)

    calendars = generate_calendars(competitions, restrictions, rounds)

    parse_output(calendars)

    return 0
