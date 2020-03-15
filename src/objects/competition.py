''' Competition object file '''


class Competition:
    ''' Object containing competition data '''

    def __init__(self, name):
        ''' Team init function '''
        self.name = name
        self.teams = list()

    def get_name(self):
        ''' Retrieve the team name '''
        return self.name

    def get_teams(self):
        ''' Retrieve the team match day '''
        return self.teams

    def add_team(self, team):
        ''' Add a team to the team list '''
        self.teams.append(team)
