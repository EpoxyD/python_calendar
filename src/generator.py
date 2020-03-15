import logging
import parser
import printer
import random

from objects.team import Team


logger = printer.get_logger()


def generate_calendar(teamlist):
    if len(teamlist) % 2:
        teamlist.append(Team("FREE", "FREE", "MAANDAG"))
    print("Team length =", len(teamlist))
    random.shuffle(teamlist)
    result = dict()
    tll = len(teamlist)
    for i in range(1, tll):
        day_1 = list()
        day_2 = list()
        home = teamlist[:tll//2]
        away = teamlist[tll//2:]
        for j in range(len(home)):
            if i % 2 == 0:
                day_1.append((home[j], away[-j]))
                day_2.append((away[-j], home[j]))
            else:
                day_1.append((away[-j], home[j]))
                day_2.append((home[j], away[-j]))

        result["%s" % i] = day_1
        result["%s" % (i + tll//2)] = day_2
        teamlist.insert(1, teamlist.pop(-1))
    return result

    # 1 2 3 4 5 6 (16 25 34 43 52 61)
    # 1 6 2 3 4 5 (15 23 32 46 51 64)
    # 1 5 6 2 3 4 (14 26 35 41 53 62)
    # 1 4 5 6 2 3 (13 24 31 42 56 65)
    # 1 3 4 5 6 2 (12 21 36 45 54 63)


if __name__ == "__main__":
    logger.info("Parsing arguments")
    csv_files, nr_rounds = parser.get_arguments()

    print(csv_files)
    logger.info("Parsing teams")
    competitions, constraints = parser.parse_competitions(csv_files)
    del csv_files

    calendars = dict()
    for competition, teams in competitions.items():
        logger.info("Generating calendar for %s" % competition)
        calendar = generate_calendar(teams)
        calendars[competition] = calendar
    del calendar, competition, teams

    print('debug')
