''' Central controller file '''

from cal_parser import parse_csv, parse_output
from cal_generator import generate_padding, generate_calendars


class Controller:
    """ Singleton Controller """
    instance = None

    def __init__(self):
        if Controller.instance:
            raise Exception("This class is a Controller!")
        Controller.instance = self
        self.competitions = None
        self.restrictions = None

    @staticmethod
    def get():
        """ Retrieve the singleton instance """
        return Controller.instance if Controller.instance else Controller()

    def parse_csv_file(self, filename):
        """ Parse input file """
        print(f"Parsing {filename}")
        self.competitions, self.restrictions = parse_csv(filename)

def start():
    ''' Start the controller '''
    csv_file = "csv/teams.csv"

    rounds = {"WEEKS": 30, "ERE": 2, "EERSTE": 3}

    competitions, restrictions = parse_csv(csv_file)

    generate_padding(competitions, rounds)

    calendars = generate_calendars(competitions, restrictions, rounds)

    parse_output(calendars)

    return 0
