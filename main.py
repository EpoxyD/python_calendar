import csv

class Team:
    ''' Object containing all the team data '''

    def __init__(self, n="a", c="test"):
        self.name = n
        self.club = c
    
    def print(self):
        print("{0}, {1}".format(self.name, self.club))

if __name__ == "__main__":
    teamlist = set()
    with open("teams.csv") as file:
        reader = csv.DictReader(file)
        for entry in reader:
            teamlist.add(Team(entry['name'], entry['club']))

    for team in teamlist:
        team.print()