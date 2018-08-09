class Game:
    def __init__(self, day, home=None, away=None):
        self.day = day
        self.home = home
        self.away = away

class Team:
    def __init__(self, club, name, rank, day1, day2=None):
        self.club = club
        self.name = name
        self.rank = rank
        self.day1 = day1
        self.day2 = day2
        self.todo = []
        self.games = []

if __name__ == "__main__":
    team_list = []
    team_list.append(Team("Downtown Jack","DTJ C",2,"Maandag","Woensdag"))
    team_list.append(Team("Downtown Jack","DTJ D",2,"Maandag"))
    team_list.append(Team("Downtown Jack","DTJ F",2,"Woensdag"))
    team_list.append(Team("Shooters","Shooters B",2,"Woensdag"))
    team_list.append(Team("Shooters","Shooters C",2,"Zaterdag","Zondag"))
    team_list.append(Team("Spacemonkeys","Spacemonkeys C",2,"Woensdag"))
    team_list.append(Team("Spacemonkeys","Spacemonkeys D",2,"Woensdag"))
    team_list.append(Team("Poolgate","Poolgate B",2,"Maandag"))
    team_list.append(Team("Bal'Enzo","Bal'Enzo B",2,"Woensdag"))
    team_list.append(Team("Bal'Enzo","Bal'Enzo Girls",2,"Woensdag"))
    team_list.append(Team("Downtown Jack","DTJ A",1,"Maandag"))
    team_list.append(Team("Downtown Jack","DTJ B",1,"Maandag"))
    team_list.append(Team("Downtown Jack","DTJ E",1,"Woensdag"))
    team_list.append(Team("Shooters","Shooters A",1,"Maandag"))
    team_list.append(Team("Spacemonkeys","Spacemonkeys A",1,"Woensdag"))
    team_list.append(Team("Spacemonkeys","Spacemonkeys B",1,"Woensdag"))
    team_list.append(Team("Poolgate","Poolgate A",1,"Maandag"))
    team_list.append(Team("Bal'Enzo","Bal'Enzo A",1,"Maandag"))
    team_list.append(Team("Chaos","Chaos A",1,"Maandag"))

    for team in team_list:
        if team.day2 == None:
            print('( {0.club:15}, {0.name:15} , {0.rank:2} , {0.day1:8} )'.format(team))
        else:
            print('( {0.club:15}, {0.name:15} , {0.rank:2} , {0.day1:8} , {0.day2:8} )'.format(team))

    # Add all possible teams to the list
    for team in team_list:
        for opponent in team_list:
            if team.name == opponent.name:
                continue
            team.todo.append(opponent)

    for team in team_list:
        for oppo in team.todo:
            print('Team {0} vs Team {1}'.format(team.name, oppo.name))
        print(' ')