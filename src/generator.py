import logging
import parser
import printer
import random


logger = printer.get_logger()


def generate_calendar(teamlist):
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

if __name__ == "__main__":
    logger.info("Parsing arguments")
    csv_files = parser.get_arguments()

    logger.info("Parsing teams")
    competitions, constraints = parser.parse_competitions(csv_files)

    for competitions, teams in competitions.items():
        random.shuffle(teams)
        calendar = generate_calendar(teams)

        for week, games in calendar.items():
            print(week)
            for teams in games:
                teams[0].dump()
                teams[1].dump()
