import csv

club_list = []

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
    def __init__(self, index, club, name, rank, day1, day2=None):
        self.club = club
        self.name = name
        self.rank = 1 if rank == 'EERSTE' else 2
        self.day1 = day1
        self.day2 = day2
        self.todo = []
        self.games = []
        self.index = index
    def __index__(self):
        return self.index

def populate_club_list(inputfile):
    inputdata = open(inputfile, 'r')
    datareader = csv.reader(inputdata, delimiter=',')
    next(datareader)
    for data in datareader:
        club_list.append(Club(data[0], data[1]))

def populate_team_list(inputfile, rank):
    output = []
    inputdata = open(inputfile, 'r')
    datareader = csv.reader(inputdata, delimiter=',')
    next(datareader)
    index = 1
    for data in datareader:
        club = next((c for c in club_list if c.name == data[0]), None)
        if str(data[2]) == str(rank):
            output.append(Team(index, club, data[1], data[2], data[3], data[4]))
            index = index + 1

    return output

def create_matches(team_list):
    return None

if __name__ == "__main__":
    populate_club_list("clubs.csv")
    team_list_1 = populate_team_list("teams.csv", "EERSTE")
    team_list_2 = populate_team_list("teams.csv", "ERE")

    for club in club_list:
        print('( {0.name:15}, {0.tables:2} )'.format(club))

    print(' ')

    for team in team_list_1:
        if team.day2 == None:
            print('( {0.index:2}, {0.club.name:15}, {0.club.tables:2}, {0.name:15} , {0.rank:2} , {0.day1:8} )'.format(team))
        else:
            print('( {0.index:2}, {0.club.name:15}, {0.club.tables:2}, {0.name:15} , {0.rank:2} , {0.day1:8} , {0.day2:8} )'.format(team))

    print(' ')

    for team in team_list_2:
        if team.day2 == None:
            print('( {0.index:2}, {0.club.name:15}, {0.club.tables:2}, {0.name:15} , {0.rank:2} , {0.day1:8} )'.format(team))
        else:
            print('( {0.index:2}, {0.club.name:15}, {0.club.tables:2}, {0.name:15} , {0.rank:2} , {0.day1:8} , {0.day2:8} )'.format(team))
    

    match_list_1 = create_matches(team_list_1)
    match_list_2 = create_matches(team_list_2)
