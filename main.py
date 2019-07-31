import csv
import random

constraints_list = dict()

class Team:
    ''' Object containing all the team data '''

    def __init__(self,
                 c=None,
                 n=None,
                 r="EERSTE",
                 t=2,
                 d1="MAANDAG"):
        self.club = c
        self.name = n
        self.rank = r
        self.games = int(t)
        self.day = d1

    def print(self):
        print("[{0}, {1}, {2}, {3}, {4}]".format(
            self.name,
            self.club,
            self.rank,
            self.games,
            self.day
        ))

    def getClub(self):
        return self.club

    def getName(self):
        return self.name

    def getRank(self):
        return self.rank

    def getGames(self):
        return self.games

    def getDay(self):
        return self.day


def get_teamlist(csv_file):
    result = list()
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for entry in reader:
            result.append(Team(
                entry['club'],
                entry['name'],
                entry['rank'],
                entry['games'],
                entry['day'],
            ))
    return result


def get_teamlist_competition(all_teams, rank):
    ''' return a subset of all teams containing only those with the specified rank '''

    result = list()
    for team in all_teams:
        if team.rank == rank:
            result.append(team)
    if len(result) % 2:
        result.append(Team("FREE", "FREE", rank, 1000))
    return result


def generate_calendar(teamlist):
    res = list()

    team_1 = teamlist.pop(0)

    for i in range(0, len(teamlist)):
        day = list()
        day.append((team_1, teamlist[0]))
        for i in range(1, len(teamlist), 2):
            day.append((teamlist[i], teamlist[i+1]))
        teamlist.append(teamlist.pop(0))  # rotate teams
        res.append(day)
    teamlist.append(team_1)

    for team in teamlist:
        team.print()
    print()

    return res


def merge_calendars(cal_1,cal_2):
    res = list()
    for i in range(0,len(cal_1)):
        res.append(cal_1[i]+cal_2[i])
    return res


def fix_teamlist_lengths(tl1,tl2):
    if len(tl1) > len(tl2):
        padding_team = Team("FREE","FREE",tl2[0][0][0].getRank(),1000)
        nr_games = len(tl2[0])
        padding = [[padding_team,padding_team] for _ in range(nr_games)]
        tl2.append(padding)
        tl2.append(padding)
    if len(tl1) < len(tl2):
        padding_team = Team("FREE","FREE",tl1[0][0][0].getRank(),1000)
        nr_games = len(tl1[0])
        padding = [[padding_team,padding_team] for _ in range(nr_games)]
        tl1.append(padding)
        tl1.append(padding)
    return


def check_constraints(cal):
    ret = False
    global check_constraints
    for week in range(1,len(cal)):
        for game in cal[week]:
            day = game[0].getDay()
            club = game[0].getClub()
            if game[1].getName() != 'FREE':
                constraints_list[day][club]['games'] += 1

        for d,day in constraints_list.items():
            for k,club in day.items():
                if club['games'] > club['total']:
                    # print("DAY {:1}: ISSUE WITH: {:8},{:16} | GAMES: {:1}, TOTAL: {:1}".format(week,d,k,club['games'],club['total']))
                    ret =  True
                club['games'] = 0

    return ret


def print_header():
    print('''
         _____               _    _____        _                   _
        |  __ \             | |  / ____|      | |                 | |
        | |__) |___    ___  | | | |      __ _ | |  ___  _ __    __| |  __ _  _ __
        |  ___// _ \  / _ \ | | | |     / _` || | / _ \| '_ \  / _` | / _` || '__|
        | |   | (_) || (_) || | | |____| (_| || ||  __/| | | || (_| || (_| || |
        |_|    \___/  \___/ |_|  \_____|\__,_||_| \___||_| |_| \__,_| \__,_||_|

                By Evert B.
    ''')


def print_matchweeks(cal):
    nr_weeks = len(cal)
    rank = cal[0][0][0].getRank()

    for i in range(0,nr_weeks):
        print("|--- WEEK {:2} - {:6} -------------------------------------------------------------|".format(i+1,rank))
        for day in cal[i]:
            print("| {:10} | {:20} VS {:20} @ {:20} |".format(
                day[0].getDay(),
                day[0].getName(),
                day[1].getName(),
                day[0].getClub()
            ))
        print("|----------------------------------------------------------------------------------|".format(i))
        print()
    print()


    for speelweek in calendar:
        for value in speelweek:
            print("({:20},{:20},{:8})".format(value[0].getName(),value[1].getName(), value[0].getRank()))
        print()


def populate_constraints_list(teamlist):
    for team in teamlist:
        day  = team.getDay()
        club = team.getClub()

        if not day in constraints_list:
            constraints_list[day] = dict()

        if not club in constraints_list[day]:
            constraints_list[day][club] = dict()

        constraints_list[day][club]['games'] = 0
        constraints_list[day][club]['total'] = int(team.getGames())

    if not 'MAANDAG' in constraints_list:
        constraints_list['MAANDAG'] = dict()
    constraints_list['MAANDAG']['FREE'] = dict()
    constraints_list['MAANDAG']['FREE']['games'] = 0
    constraints_list['MAANDAG']['FREE']['total'] = 1000


if __name__ == "__main__":
    # Get all teams from csv file
    teamlist = get_teamlist("copy.csv")

    # Populate Constraints list
    populate_constraints_list(teamlist)

    # Get list per ranking
    teamlist_1 = get_teamlist_competition(teamlist, "ERE")
    teamlist_2 = get_teamlist_competition(teamlist, "EERSTE")

    # Remove full teamlist from memory
    del teamlist

    attempts = 0
    not_done_yet = True
    while(not_done_yet):
        attempts += 1

        if attempts > 3:
            break

        # Randomnize teamlist
        random.shuffle(teamlist_1)
        random.shuffle(teamlist_2)

        # Create Calendar
        calendar_1 = generate_calendar(teamlist_1)
        calendar_2 = generate_calendar(teamlist_2)

        # Make the calendars equal in length
        fix_teamlist_lengths(calendar_1,calendar_2)

        # Merge Two Calendars
        calendar = merge_calendars(calendar_1,calendar_2)

        not_done_yet = True #check_constraints(calendar)

    print_header()
    print_matchweeks(calendar_1)
    print_matchweeks(calendar_2)

    print("NR OF ATTEMPTS = {}".format(attempts))



# 1 2 3 4 5 6 (16 25 34 43 52 61)
# 1 6 2 3 4 5 (15 23 32 46 51 64)
# 1 5 6 2 3 4 (14 26 35 41 53 62)
# 1 4 5 6 2 3 (13 24 31 42 56 65)
# 1 3 4 5 6 2 (12 21 36 45 54 63)
