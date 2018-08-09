import csv

club_list = []
team_list = []

class Game:
    def __init__(self, day, home=None, away=None):
        self.day = day
        self.home = home
        self.away = away

class Club:
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables

class Team:
    def __init__(self, club, name, rank, day1, day2=None):
        self.club = club
        self.name = name
        self.rank = 1 if rank == 'EERSTE' else 2
        self.day1 = day1
        self.day2 = day2
        self.todo = []
        self.games = []

def populate_club_list(inputfile):
    inputdata = open(inputfile, 'r')
    datareader = csv.reader(inputdata, delimiter=',')
    next(datareader)
    for data in datareader:
        club_list.append(Club(data[0], data[1]))

def populate_team_list(inputfile):
    inputdata = open(inputfile, 'r')
    datareader = csv.reader(inputdata, delimiter=',')
    next(datareader)
    for data in datareader:
        club = next((c for c in club_list if c.name == data[0]), None)
        team_list.append(Team(club, data[1], data[2], data[3], data[4]))

if __name__ == "__main__":
    populate_club_list("clubs.csv")
    populate_team_list("teams.csv")

    for team in team_list:
        if team.day2 == None:
            print('( {0.club.name:15}, {0.club.tables:2}, {0.name:15} , {0.rank:2} , {0.day1:8} )'.format(team))
        else:
            print('( {0.club.name:15}, {0.club.tables:2}, {0.name:15} , {0.rank:2} , {0.day1:8} , {0.day2:8} )'.format(team))

    # # Add all possible teams to the list
    # for team in team_list:
    #     for opponent in team_list:
    #         if team.name == opponent.name:
    #             continue
    #         team.todo.append(opponent)

    # for team in team_list:
    #     for oppo in team.todo:
    #         print('Team {0} vs Team {1}'.format(team.name, oppo.name))
    #     print(' ')

