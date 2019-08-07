''' PoolCalendar Generator '''

import csv
import random
import os

CONSTRAINTS_LIST = dict()


class Team:
    ''' Object containing all the team data '''

    #pylint: disable-msg=too-many-arguments
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
        ''' dump the Team data '''
        print("[{0}, {1}, {2}, {3}, {4}]".format(
            self.name,
            self.club,
            self.rank,
            self.games,
            self.day
        ))

    def get_club(self):
        ''' get Team Club '''
        return self.club

    def get_name(self):
        ''' get Team Name '''
        return self.name

    def get_rank(self):
        ''' get Team Rank '''
        return self.rank

    def get_games(self):
        ''' get Team Games '''
        return self.games

    def get_day(self):
        ''' get Team Day '''
        return self.day


# Print iterations progress
#pylint: disable-msg=too-many-arguments
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    '''
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : barline fill character (Str)
    '''
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filled_length = int(length * iteration // total)
    barline = fill * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s%% %s' % (prefix, barline, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def get_teamlist(csv_file):
    '''
    @brief: return all teams in the defined csv file
    @params:
        csv_file: a csv file with headers containing all participating teams
    '''
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
    '''
    @brief: return a subset of all teams containing only those with the specified rank
    @params:
        all_teams   a list of all teams accross competitions
        rank        the competition we want a subset of
    '''

    result = list()
    for team in all_teams:
        if team.rank == rank:
            result.append(team)
    if len(result) % 2:
        result.append(Team("FREE", "FREE", rank, 1000))
    return result


def generate_calendar(teamlist):
    '''
    @brief: Generate a calendar for a particular rank
    @params:
        teamlist    list of the teams in the competition
    '''
    result = list()
    tll = len(teamlist)
    for i in range(1, tll):
        day_1 = list()
        day_2 = list()
        home = teamlist[:tll//2]
        away = teamlist[tll//2:]
        for j in enumerate(home):
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


def merge_calendars(cal_1, cal_2):
    '''
    @brief: Merge 2 calenders into 1
    @params:
        cal_1   generated calendar 1
        cal_2   generated calendar 2
    '''
    res = list()
    for i in enumerate(cal_1):
        res.append(cal_1[i]+cal_2[i])
    return res


def fix_teamlist_lengths(tl1, tl2):
    '''
    @brief: Fix teamlist length in case of uneven teams
    @params:
        tl1   Teamlist 1
        tl2   Teamlist 2
    '''
    if len(tl1) > len(tl2):
        padding_team = Team("FREE", "FREE", tl2[0][0][0].get_rank(), 1000)
        nr_games = len(tl2[0])
        padding = [[padding_team, padding_team] for _ in range(nr_games)]
        tl2.append(padding)
        tl2.append(padding)
    if len(tl1) < len(tl2):
        padding_team = Team("FREE", "FREE", tl1[0][0][0].get_rank(), 1000)
        nr_games = len(tl1[0])
        padding = [[padding_team, padding_team] for _ in range(nr_games)]
        tl1.append(padding)
        tl1.append(padding)


def check_constraints(cal):
    '''
    @brief: Check if the calender provided fits with the criteria
    @params:
        cal   The generated calendar
    '''
    ret = False
    for week in range(1, len(cal)):
        for game in cal[week]:
            day = game[0].get_day()
            club = game[0].get_club()
            if game[1].get_name() != 'FREE':
                CONSTRAINTS_LIST[day][club]['games'] += 1

        for _, day in CONSTRAINTS_LIST.items():
            for _, club in day.items():
                if club['games'] > club['total']:
                    ret = True
                club['games'] = 0

    return ret


def print_header():
    '''
    @brief: Print a header. Looks cool.
    '''
    print(r'''
         _____               _    _____        _                   _
        |  __ \             | |  / ____|      | |                 | |
        | |__) |___    ___  | | | |      __ _ | |  ___  _ __    __| |  __ _  _ __
        |  ___// _ \  / _ \ | | | |     / _` || | / _ \| '_ \  / _` | / _` || '__|
        | |   | (_) || (_) || | | |____| (_| || ||  __/| | | || (_| || (_| || |
        |_|    \___/  \___/ |_|  \_____|\__,_||_| \___||_| |_| \__,_| \__,_||_|

                By Evert B.
    ''')


def print_matchweeks(cal):
    '''
    @brief: Dump all the generated matchweeks
    '''
    nr_weeks = len(cal)
    rank = cal[0][0][0].get_rank()

    for i in range(0, nr_weeks):
        print('''
        |--- WEEK {:2} - {:6} -------------------------------------------------------------|
        '''.format(i+1, rank))
        for day in cal[i]:
            print("| {:10} | {:20} VS {:20} @ {:20} |".format(
                day[0].get_day(),
                day[0].get_name(),
                day[1].get_name(),
                day[0].get_club()
            ))
        print('''
        |----------------------------------------------------------------------------------|
        ''')
        print()
    print()


def populate_constraints_list(teamlist):
    '''
    @brief: Generate a global CONSTRAINTS_LIST which can be used to check the constraints against.
    @params:
        teamlist    all teams which have an impact in the league for constaints
    '''
    for team in teamlist:
        day = team.get_day()
        club = team.get_club()

        if not day in CONSTRAINTS_LIST:
            CONSTRAINTS_LIST[day] = dict()

        if not club in CONSTRAINTS_LIST[day]:
            CONSTRAINTS_LIST[day][club] = dict()

        CONSTRAINTS_LIST[day][club]['games'] = 0
        CONSTRAINTS_LIST[day][club]['total'] = int(team.get_games())

    if 'MAANDAG' not in CONSTRAINTS_LIST:
        CONSTRAINTS_LIST['MAANDAG'] = dict()
    CONSTRAINTS_LIST['MAANDAG']['FREE'] = dict()
    CONSTRAINTS_LIST['MAANDAG']['FREE']['games'] = 0
    CONSTRAINTS_LIST['MAANDAG']['FREE']['total'] = 1000


def remove_old_output(file):
    ''' Remove old output file if it exists '''
    if os.path.exists(file):
        os.remove(file)

    with open('new_CALENDAR.csv', 'w', newline='') as outputfile:
        fieldnames = ['week', 'day', 'comp', 'team1', 'team2', 'location']
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        writer.writeheader()


def generate_output(cal):
    ''' Generate a CSV output file with the generated calendar '''
    with open('new_CALENDAR.csv', 'a', newline='') as file:
        fieldnames = ['week', 'day', 'comp', 'team1', 'team2', 'location']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for i in enumerate(cal):
            for game in cal[i]:
                writer.writerow({
                    'week': str(i+1),
                    'day': game[0].get_day(),
                    'comp': game[0].get_rank(),
                    'team1': game[0].get_name(),
                    'team2': game[1].get_name(),
                    'location': game[0].get_club()
                })


if __name__ == "__main__":
    # Get all teams from csv file
    TEAMLIST = get_teamlist("teams.csv")

    # Populate Constraints list
    populate_constraints_list(TEAMLIST)

    # Get list per ranking
    TEAMLIST_1 = get_teamlist_competition(TEAMLIST, "ERE")
    TEAMLIST_2 = get_teamlist_competition(TEAMLIST, "EERSTE")

    # Remove full teamlist from memory
    del TEAMLIST

    ATTEMPTS = 0
    NOT_DONE = True
    MAX_TRIES = 250000
    print_progress_bar(ATTEMPTS, MAX_TRIES, prefix='Progress:', suffix='')
    while NOT_DONE:
        ATTEMPTS += 1

        # Randomnize teamlist
        random.shuffle(TEAMLIST_1)
        random.shuffle(TEAMLIST_2)

        # Create CALENDAR
        CALENDAR_1 = generate_calendar(TEAMLIST_1)
        CALENDAR_2 = generate_calendar(TEAMLIST_2)

        # Make the CALENDARs equal in length
        fix_teamlist_lengths(CALENDAR_1, CALENDAR_2)

        # Merge Two CALENDARs
        CALENDAR = merge_calendars(CALENDAR_1, CALENDAR_2)

        NOT_DONE = check_constraints(CALENDAR)

        print_progress_bar(ATTEMPTS, MAX_TRIES, prefix='Progress:', suffix='')

        if ATTEMPTS == MAX_TRIES:
            print("Failed to find suitable CALENDAR within 250.000 tries.")
            print("Are the constraints too strict?")
            raise SystemExit

    print_progress_bar(MAX_TRIES, MAX_TRIES, prefix='Progress:', suffix='')

    print_header()
    print_matchweeks(CALENDAR_1)
    print_matchweeks(CALENDAR_2)

    remove_old_output('output.csv')

    generate_output(CALENDAR_1)
    generate_output(CALENDAR_2)

    print("NR OF ATTEMPTS = {}".format(ATTEMPTS))
    input()
