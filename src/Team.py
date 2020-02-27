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
        self.games = int(t)
        self.day = d1

    def dump(self):
        print("[{0}, {1}, {2}, {3}, {4}]".format(
            self.name,
            self.club,
            self.rank,
            self.games,
            self.day
        ))

    def getClub(self):
        return self.club

    def getName(self):
        return self.name

    def getRank(self):
        return self.rank

    def getGames(self):
        return self.games

    def getDay(self):
        return self.day
