import random

import parser as pa
import printer as pr
import generator as gn
import objects.Team as Team

constraints_list = {
    "MAANDAG": {
        "FREE": {
            "games": 0,
            "total": 1000
        }
    },
    "WOENSDAG": {
        "FREE": {
            "games": 0,
            "total": 1000
        }
    }
}
issues = dict()


# def generate_calendar(teamlist):
#     result = list()
#     tll = len(teamlist)
#     for i in range(1, tll):
#         day_1 = list()
#         day_2 = list()
#         home = teamlist[:tll//2]
#         away = teamlist[tll//2:]
#         for j in range(len(home)):
#             if i % 2 == 0:
#                 day_1.append((home[j], away[-j]))
#                 day_2.append((away[-j], home[j]))
#             else:
#                 day_1.append((away[-j], home[j]))
#                 day_2.append((home[j], away[-j]))

#         result.append(day_1)
#         result.insert(len(result)//2, day_2)
#         teamlist.insert(1, teamlist.pop(-1))
#     return result

#     # 1 2 3 4 5 6 (16 25 34 43 52 61)
#     # 1 6 2 3 4 5 (15 23 32 46 51 64)
#     # 1 5 6 2 3 4 (14 26 35 41 53 62)
#     # 1 4 5 6 2 3 (13 24 31 42 56 65)
#     # 1 3 4 5 6 2 (12 21 36 45 54 63)


def merge_calendars(cal_1, cal_2):
    res = list()
    for i in range(0, len(cal_1)):
        res.append(cal_1[i] + cal_2[i])
    return res


def fix_calendar_length(cal_1, cal_2):
    mix = 0
    while(len(cal_1) != len(cal_2)):
        len_1 = len(cal_1)
        len_2 = len(cal_2)
        if len_1 > len_2:
            mock_game = [Team("FREE", "FREE", team.getRank(), 1000)
                         for team in cal_2[0][0]]
            mock_week = [mock_game for _ in cal_2[0]]
            if mix % 2:
                cal_2.append(mock_week)
            else:
                cal_2.insert(len_2//2, mock_week)

        if len_1 < len_2:
            mock_game = [Team("FREE", "FREE", team.getRank(), 1000)
                         for team in cal_1[0][0]]
            mock_week = [mock_game for _ in cal_1[0]]
            if mix % 2:
                cal_1.append(mock_week)
            else:
                cal_1.insert(len_2//2, mock_week)

        mix = mix + 1
    return


def check_constraints(cal):
    ret = False
    global constraints_list
    for week in range(1, len(cal)):
        for game in cal[week]:
            day = game[0].getDay()
            club = game[0].getClub()
            if game[0].getName() != 'FREE' and game[1].getName() != 'FREE':
                constraints_list[day][club]['games'] += 1

        for d, day in constraints_list.items():
            for c, club in day.items():
                if club['games'] > club['total']:
                    # print("ISSUE WEEK {:2}: {:20} on {:10}".format(week, k, d))
                    if not c in issues:
                        issues[c] = dict()
                    if not d in issues[c]:
                        issues[c][d] = 0
                    issues[c][d] = issues[c][d] + 1
                    ret = True
                club['games'] = 0

    return ret


def populate_constraints_list(teamlist):
    for team in teamlist:
        day = team.getDay()
        club = team.getClub()

        if not day in constraints_list:
            constraints_list[day] = dict()

        if not club in constraints_list[day]:
            constraints_list[day][club] = dict()

        constraints_list[day][club]['games'] = 0
        constraints_list[day][club]['total'] = int(team.getGames())


def add_eindronde(cal):
    nr_weeks = len(cal) // 2
    mock_team = Team('FREE', 'FREE', cal[0][0][0].getRank(), 1000, 'MAANDAG')
    mock_game = [mock_team for game in cal[0][0]]
    mock_week = [mock_game for week in cal[0]]
    for _ in range(nr_weeks):
        cal.append(mock_week)


if __name__ == "__main__":
    CSVFILE = input("What is the name of your csv file? ")
    if ".csv" not in CSVFILE:
        CSVFILE = CSVFILE + ".csv"

    # Get all teams from csv file
    TEAMLIST = pa.get_teamlist(CSVFILE)

    # Populate Constraints list
    populate_constraints_list(TEAMLIST)

    # Get list per ranking
    TEAMLIST_1 = pa.get_teamlist_competition(TEAMLIST, "ERE")
    TEAMLIST_2 = pa.get_teamlist_competition(TEAMLIST, "EERSTE")

    # Remove full teamlist from memory
    del TEAMLIST

    ATTEMPTS = 0
    NOT_DONE_YET = True
    MAX_TRIES = 250000
    pr.print_progress_bar(ATTEMPTS, MAX_TRIES, prefix='Progress:', suffix='')
    while(NOT_DONE_YET):
        ATTEMPTS += 1

        # Randomnize teamlist
        random.shuffle(TEAMLIST_1)
        random.shuffle(TEAMLIST_2)

        # Create Calendar
        CALENDAR_1 = gn.generate_calendar(TEAMLIST_1)
        CALENDAR_2 = gn.generate_calendar(TEAMLIST_2)

        add_eindronde(CALENDAR_2)

        # Make the calendars equal in length
        fix_calendar_length(CALENDAR_1, CALENDAR_2)

        # Merge Two Calendars
        CALENDAR = merge_calendars(CALENDAR_1, CALENDAR_2)

        NOT_DONE_YET = check_constraints(CALENDAR)

        pr.print_progress_bar(ATTEMPTS, MAX_TRIES, prefix='Progress:', suffix='')

        if ATTEMPTS == MAX_TRIES:
            print("Failed to find suitable calendar within 250.000 tries.")
            print("Are the constraints too strict?")
            pr.print_issues(issues)
            raise SystemExit

    pr.print_progress_bar(MAX_TRIES, MAX_TRIES, prefix='Progress:', suffix='')

    pr.print_header()
    pr.print_matchweeks(CALENDAR_1)
    pr.print_matchweeks(CALENDAR_2)

    pa.remove_old_output('output.csv')

    pa.generate_output(CALENDAR_1)
    pa.generate_output(CALENDAR_2)

    print("NR OF ATTEMPTS = {}".format(ATTEMPTS))
    input()
