import csv
import random


class Team:
    ''' Object containing all the team data '''

    def __init__(self,
                 c=None,
                 n=None,
                 r="EERSTE",
                 t=2,
                 d1="Maandag",
                 d2=None):
        self.club = c
        self.name = n
        self.rank = r
        self.tables = int(t)
        self.day = d1

    def print(self):
        print("[{0}, {1}, {2}, {3}, {4}]".format(
            self.name,
            self.club,
            self.rank,
            self.tables,
            self.day
        ))

    def getClub(self):
        return self.club

    def getName(self):
        return self.name

    def getRank(self):
        return self.rank

    def getTables(self):
        return self.tables

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
                entry['tables'],
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

    for _ in range(0, len(teamlist)):
        day = list()
        day.append((team_1, teamlist[0]))
        for i in range(1, len(teamlist), 2):
            day.append((teamlist[i], teamlist[i+1]))
        teamlist.append(teamlist.pop(0))  # rotate teams
        res.append(day)
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
    res = dict()
    for playday in cal:
        for match in playday:
            res[match[0].getClub()] = dict()
            res[match[0].getClub()][match[0].getDay()] = dict()
            tmp = res[match[0].getClub()][match[0].getDay()] 
            if "current" in tmp:
                tmp["current"] += 1
            else:
                tmp["current"] = 1
            if not "total" in tmp:
                tmp["total"] = match[0].getTables()
    
    for _,club in res.items():
        for _,day in club.items():
            if day["current"] * 2 >= day["total"]:
                return True
    
    return False
            


if __name__ == "__main__":
    # Get all teams from csv file
    teamlist = get_teamlist("teams.csv")

    # Get list per ranking
    teamlist_1 = get_teamlist_competition(teamlist, "ERE")
    teamlist_2 = get_teamlist_competition(teamlist, "EERSTE")

    # Remove full teamlist from memory
    del teamlist

    # Randomnize teamlist
    random.shuffle(teamlist_1)
    random.shuffle(teamlist_2)

    constraints = True
    while(constraints):
        # Create Calendar
        calendar_1 = generate_calendar(teamlist_1)
        calendar_2 = generate_calendar(teamlist_2)
        
        # Make the calendars equal in length
        fix_teamlist_lengths(calendar_1,calendar_2)

        # Merge Two Calendars
        calendar = merge_calendars(calendar_1,calendar_2)
        del calendar_1
        del calendar_2

        constraints = check_constraints(calendar)

    for speelweek in calendar:
        for value in speelweek:
            print("({:15},{:15},{:8})".format(value[0].getName(),value[1].getName(), value[0].getRank()))
        print()

    # TODO constraints
    # Tafels thuisploegen mogen maximum niet overlappen
    # 


# 1 2 3 4 5 6 (16 25 34 43 52 61)
# 1 6 2 3 4 5 (15 23 32 46 51 64)
# 1 5 6 2 3 4 (14 26 35 41 53 62)
# 1 4 5 6 2 3 (13 24 31 42 56 65)
# 1 3 4 5 6 2 (12 21 36 45 54 63)
