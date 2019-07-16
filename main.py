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
    return result


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

    print(len(teamlist_1))
    print(len(teamlist_2))
