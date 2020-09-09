''' Generate a calendar based on a number of rounds per competition '''

from random import shuffle, randint

from team import Team




def generate_calendar(data):
    ''' Generate a complete calendar '''

    # Find the amount of weeks

    # shuffle(competition)

    # calendar = list()
    # nr_teams = len(competition)

    # for i in range(1, nr_teams):
    #     game_day = list()
    #     home = competition[:nr_teams//2]
    #     away = competition[nr_teams//2:]

    #     for j, _ in enumerate(home):
    #         if i % 2:
    #             game_day.append((home[j], away[-j]))
    #         else:
    #             game_day.append((away[-j], home[j]))

    #     calendar.append(game_day)
    #     competition.insert(1, competition.pop(-1))

    # return calendar

    # # 1 2 3 4 5 6 (16 25 34 43 52 61)
    # # 1 6 2 3 4 5 (15 23 32 46 51 64)
    # # 1 5 6 2 3 4 (14 26 35 41 53 62)
    # # 1 4 5 6 2 3 (13 24 31 42 56 65)
    # # 1 3 4 5 6 2 (12 21 36 45 54 63)


def invert_calendar(calendar):
    ''' Invert all games in a calendar '''
    for _, game_day in enumerate(calendar):
        for j, game in enumerate(game_day):
            game_day[j] = tuple(reversed(game))


def insert_free_day(calendar):
    ''' Insert a day where all teams are available '''
    free_team = Team("FREE", "FREE", "FREE")
    free_game = (free_team, free_team)
    free_day = [free_game for _ in enumerate(calendar[0])]
    calendar.insert(randint(0, len(calendar)-1), free_day)


def generate_calendars(competitions, restrictions, rounds):
    ''' Generate all calendars '''

    calendars = dict()

    nr_weeks = rounds["WEEKS"]

    for comp in competitions:
        calendars[comp] = list()

        nr_rounds = rounds[comp]

        nr_game_days = nr_rounds * (len(competitions[comp]) - 1)
        nr_free_days = nr_weeks - nr_game_days

        for i in range(0, nr_rounds):
            calendar = generate_calendar(competitions[comp], restrictions)
            if i % 2:
                invert_calendar(calendar)
            if nr_free_days:
                insert_free_day(calendar)
                nr_free_days -= 1
            calendars[comp].extend(calendar)

    return calendars
