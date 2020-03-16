''' Central controller file '''

import generator
import parser


def print_competitions(competitions):
    print("Competitions:")
    for comp in competitions:
        print("[", comp, "]")
        for team in competitions[comp]:
            print("\t-", team)


def print_restrictions(restrictions):
    print("Restrictions")
    for team in restrictions:
        print("[", team, "]")
        for gameday, nr_tables in restrictions[team].items():
            print("\t[ %s ] = ( %s tables )" % (gameday, nr_tables))


def start():
    ''' Start the controller '''
    csv_file = "csv/teams.csv"

    rounds = {"WEEKS": 30, "ERE": 2, "EERSTE": 3}

    competitions, restrictions = parser.parse_csv(csv_file)

    generator.competition_padding(competitions, rounds)

    print_competitions(competitions)
    print_restrictions(restrictions)

    generator.generate_calendar(competitions, restrictions, rounds)

    return 0
