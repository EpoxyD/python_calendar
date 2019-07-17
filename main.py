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
        self.tables = t
        self.day1 = d1
        self.day2 = d2

    def print(self):
        print("[{0}, {1}, {2}, {3}, {4}, {5}]".format(
            self.name,
            self.club,
            self.rank,
            self.tables,
            self.day1,
            self.day2
        ))

    def getName(self):
        return self.name


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
                entry['day1'],
                entry['day2'],
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

    for playday in range(0, len(teamlist)):
        day = list()
        day.append((team_1, teamlist[0]))
        for i in range(1, len(teamlist), 2):
            day.append((teamlist[i], teamlist[i+1]))
        teamlist.append(teamlist.pop(0))  # rotate teams
        res.append(day)
    return res


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

    # Create Calendar
    calendar_1 = generate_calendar(teamlist_1)
    calendar_2 = generate_calendar(teamlist_2)

    for day in calendar_1:
        for value in day:
            print("({:15},{:15})".format(value[0].getName(),value[1].getName()))


# 1 2 3 4 5 6 (16 25 34 43 52 61)
# 1 6 2 3 4 5 (15 23 32 46 51 64)
# 1 5 6 2 3 4 (14 26 35 41 53 62)
# 1 4 5 6 2 3 (13 24 31 42 56 65)
# 1 3 4 5 6 2 (12 21 36 45 54 63)
