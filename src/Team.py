class Team:
    ''' Object containing team data '''

    def __init__(self, club, name, day):
        self.club = club
        self.name = name
        self.day = day

    def dump(self):
        print("[{name}, {club}, {day}]".format(
            name=self.name,
            club=self.club,
            day=self.day
        ))

    def getClub(self):
        return self.club

    def getName(self):
        return self.name

    def getDay(self):
        return self.day
