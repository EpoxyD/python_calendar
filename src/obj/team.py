''' Team object file '''


class Team:
    ''' Object containing team data '''

    def __init__(self, club, name, day):
        ''' Team init function '''
        self.club = club
        self.name = name
        self.day = day

    def __str__(self):
        ''' Team tostring function '''
        return "[ %-15s, %-20s, %-8s ]" % (self.name, self.club, self.day)

    def get_club(self):
        ''' Retrieve the club name '''
        return self.club

    def get_name(self):
        ''' Retrieve the team name '''
        return self.name

    def get_day(self):
        ''' Retrieve the team match day '''
        return self.day
