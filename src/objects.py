''' File containing all the object definitions '''


class Game:
    ''' Object containing game data '''

    def __init__(self):
        self.home = home
        self.away = away


class Club:
    ''' Object containing club data '''

    def __init__(self, name, tables):
        self.name = name
        self.tables = tables
        self.matchdays = {}

    def get_name(self):
        ''' Retrieve the club name '''
        return self.name

    def add_matchday(self, matchday):
        ''' Add a matchday '''
        self.matchdays[matchday] = self.tables


class Division:
    '''Object containing division data '''

    def __init__(self, name, rounds):
        self.name = name
        self.rounds = rounds

    def get_name(self):
        ''' Retrieve the division name '''
        return self.name


class Team:
    ''' Object containing team data '''

    def __init__(self, club, name, matchday):
        ''' Team init function '''
        self.club = club
        self.name = name
        self.matchday = matchday

    def get_name(self):
        ''' Retrieve the team name '''
        return self.name

    def get_club(self):
        ''' Retrieve the club name '''
        return self.club.getName()

    def get_matchday(self):
        ''' Retrieve the team matchday '''
        return self.matchday
