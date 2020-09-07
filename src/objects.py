''' File containing all the object definitions '''


class Club:
    ''' Object containing club data '''

    def __init__(self, name, tables):
        self.name = name
        self.tables = tables
        self.matchdays = {}

    def __str__(self):
        ''' Club tostring function '''
        return f"[ {self.name}, {self.matchdays} ]"

    def get_name(self):
        ''' Retrieve the club name '''
        return self.name

    def add_matchday(self, matchday):
        ''' Add a matchday '''
        self.matchdays[matchday] = self.tables


class Team:
    ''' Object containing team data '''

    def __init__(self, club, name, division, matchday):
        ''' Team init function '''
        self.club = club
        self.name = name
        self.division = division
        self.matchday = matchday

    def __str__(self):
        ''' Team tostring function '''
        return f"[ {self.name}, {self.club}, {self.matchday} ]"

    def get_name(self):
        ''' Retrieve the team name '''
        return self.name

    def get_club(self):
        ''' Retrieve the club name '''
        return self.club.getName()

    def get_matchday(self):
        ''' Retrieve the team matchday '''
        return self.matchday
