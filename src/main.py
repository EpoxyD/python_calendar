import csv
import random
import os

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

    def dump(self):
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


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


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
    result = list()
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

        result.append(day_1)
        result.insert(len(result)//2, day_2)
        teamlist.insert(1, teamlist.pop(-1))
    return result

    # 1 2 3 4 5 6 (16 25 34 43 52 61)
    # 1 6 2 3 4 5 (15 23 32 46 51 64)
    # 1 5 6 2 3 4 (14 26 35 41 53 62)
    # 1 4 5 6 2 3 (13 24 31 42 56 65)
    # 1 3 4 5 6 2 (12 21 36 45 54 63)


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
    global check_constraints
    for week in range(1, len(cal)):
        for game in cal[week]:
            day = game[0].getDay()
            club = game[0].getClub()
            if game[0].getName() != 'FREE' and game[1].getName() != 'FREE':
                constraints_list[day][club]['games'] += 1

        for d, day in constraints_list.items():
            for k, club in day.items():
                if club['games'] > club['total']:
                    # print("ISSUE WEEK {:2}: {:20} on {:10}".format(week, k, d))
                    ret = True
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

    for i in range(0, nr_weeks):
        print(
            "|--- WEEK {:2} - {:6} -------------------------------------------------------------|".format(i+1, rank))
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

    if not 'MAANDAG' in constraints_list:
        constraints_list['MAANDAG'] = dict()
    constraints_list['MAANDAG']['FREE'] = dict()
    constraints_list['MAANDAG']['FREE']['games'] = 0
    constraints_list['MAANDAG']['FREE']['total'] = 1000


def remove_old_output(file):
    if os.path.exists(file):
        os.remove(file)

    with open('new_calendar.csv', 'w', newline='') as file:
        fieldnames = ['week', 'day', 'comp', 'team1', 'team2', 'location']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


def generate_output(cal):
    with open('new_calendar.csv', 'a', newline='') as file:
        fieldnames = ['week', 'day', 'comp', 'team1', 'team2', 'location']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for i in range(len(cal)):
            for game in cal[i]:
                writer.writerow({
                    'week': str(i+1),
                    'day': game[0].getDay(),
                    'comp': game[0].getRank(),
                    'team1': game[0].getName(),
                    'team2': game[1].getName(),
                    'location': game[0].getClub()
                })


def add_eindronde(cal):
    nr_weeks = len(cal) // 2
    mock_team = Team('FREE', 'FREE', cal[0][0][0].getRank(), 1000, 'MAANDAG')
    mock_game = [mock_team for game in cal[0][0]]
    mock_week = [mock_game for week in cal[0]]
    for week in range(nr_weeks):
        cal.append(mock_week)


if __name__ == "__main__":
    csvfile = input("What is the name of your csv file? ")
    if ".csv" not in csvfile:
        csvfile = csvfile + ".csv"

    # Get all teams from csv file
    teamlist = get_teamlist(csvfile)

    # Populate Constraints list
    populate_constraints_list(teamlist)

    # Get list per ranking
    teamlist_1 = get_teamlist_competition(teamlist, "ERE")
    teamlist_2 = get_teamlist_competition(teamlist, "EERSTE")

    # Remove full teamlist from memory
    del teamlist

    attempts = 0
    not_done_yet = True
    max_tries = 250000
    printProgressBar(attempts, max_tries, prefix='Progress:', suffix='')
    while(not_done_yet):
        attempts += 1

        # Randomnize teamlist
        random.shuffle(teamlist_1)
        random.shuffle(teamlist_2)

        # Create Calendar
        calendar_1 = generate_calendar(teamlist_1)
        calendar_2 = generate_calendar(teamlist_2)

        add_eindronde(calendar_2)

        # Make the calendars equal in length
        fix_calendar_length(calendar_1, calendar_2)

        # Merge Two Calendars
        calendar = merge_calendars(calendar_1, calendar_2)

        not_done_yet = check_constraints(calendar)

        printProgressBar(attempts, max_tries, prefix='Progress:', suffix='')

        if attempts == max_tries:
            print("Failed to find suitable calendar within 250.000 tries.")
            print("Are the constraints too strict?")
            raise SystemExit

    printProgressBar(max_tries, max_tries, prefix='Progress:', suffix='')

    print_header()
    print_matchweeks(calendar_1)
    print_matchweeks(calendar_2)

    remove_old_output('output.csv')

    generate_output(calendar_1)
    generate_output(calendar_2)

    print("NR OF ATTEMPTS = {}".format(attempts))
    input()
