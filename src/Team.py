class Team:
    ''' Object containing all the team data '''

    def __init__(self,
                 c=None,
                 n=None,
                 r="EERSTE",
                 t=2,
                 d1="MAANDAG"):
        self.club = c
        self.name = n
        self.rank = r
        self.day = d1

    def dump(self):
        print("[{name}, {club}, {rank}, {day}]".format(
            name = self.name,
            club = self.club,
            rank = self.rank,
            day = self.day
        ))

    def getClub(self):
        return self.club

    def getName(self):
        return self.name

    def getRank(self):
        return self.rank

    def getDay(self):
        return self.day
