''' Generate a calendar based on a number of rounds per competition '''

from obj.team import Team


def print_competitions(competitions):
    print("Competitions:")
    for comp in competitions:
        print("[", comp, "]")
        for team in competitions[comp]:
            print("\t-", team)


def print_restrictions(restrictions):
    print("Restrictions")
    for team in restrictions:
        print("[", team, "]")
        for gameday, nr_tables in restrictions[team].items():
            print("\t[ %s ] = ( %s tables )" % (gameday, nr_tables))


def competition_padding(competitions, rounds):
    ''' Maximize nr_teams to accomplish little constraints '''
    free_team = Team("FREE", "FREE", "FREE")
    for comp in competitions:
        if len(competitions[comp]) % 2:
            competitions[comp].append(free_team)

        nr_weeks = rounds["WEEKS"]
        nr_rounds = rounds[comp]
        while(len(competitions[comp]) <= (nr_weeks / nr_rounds) - 1):
            competitions[comp].append(free_team)
            competitions[comp].append(free_team)


def generate_calendar(competitions, restrictions, rounds):
    ''' Generate a complete calendar '''

    free_team = Team("FREE", "FREE", "FREE")
    restrictions["FREE"] = {"FREE": 1000}

    nr_weeks = rounds["WEEKS"]

    for comp in competitions:
        result = dict()
        nr_teams = len(competitions[comp])
        nr_rounds = rounds[comp]
        home = competitions[comp][:nr_teams//2]
        away = competitions[comp][nr_teams//2:]

        for i,_ in enumerate(home):
            game_home = (home[i], away[-i])
            game_away = (away[i], home[i])

            for j in range(0, nr_rounds):
                result["%s" % (i + j*(nr_teams//nr_rounds))] = "hello"
                
        competitions[comp].insert(1, competitions[comp].pop(-1))

    # print_competitions(competitions)
    # print_restrictions(restrictions)

    # result = dict()
    # tll = len(teamlist)
    # for i in range(1, tll):
    #     day_1 = list()
    #     day_2 = list()
    #     home = teamlist[:tll//2]
    #     away = teamlist[tll//2:]
    #     for j in range(len(home)):
    #         if i % 2 == 0:
    #             day_1.append((home[j], away[-j]))
    #             day_2.append((away[-j], home[j]))
    #         else:
    #             day_1.append((away[-j], home[j]))
    #             day_2.append((home[j], away[-j]))

    #     result["%s" % i] = day_1
    #     result["%s" % (i + tll//2)] = day_2
    #     teamlist.insert(1, teamlist.pop(-1))
    # return result

    # 1 2 3 4 5 6 (16 25 34 43 52 61)
    # 1 6 2 3 4 5 (15 23 32 46 51 64)
    # 1 5 6 2 3 4 (14 26 35 41 53 62)
    # 1 4 5 6 2 3 (13 24 31 42 56 65)
    # 1 3 4 5 6 2 (12 21 36 45 54 63)


# def generate_calendar(teamlist):
#     if len(teamlist) % 2:
#         teamlist.append(Team("FREE", "FREE", "MAANDAG"))
#     print("Team length =", len(teamlist))
#     random.shuffle(teamlist)
#     result = dict()
#     tll = len(teamlist)
#     for i in range(1, tll):
#         day_1 = list()
#         day_2 = list()
#         home = teamlist[:tll//2]
#         away = teamlist[tll//2:]
#         for j in range(len(home)):
#             if i % 2 == 0:
#                 day_1.append((home[j], away[-j]))
#                 day_2.append((away[-j], home[j]))
#             else:
#                 day_1.append((away[-j], home[j]))
#                 day_2.append((home[j], away[-j]))

#         result["%s" % i] = day_1
#         result["%s" % (i + tll//2)] = day_2
#         teamlist.insert(1, teamlist.pop(-1))
#     return result

#     # 1 2 3 4 5 6 (16 25 34 43 52 61)
#     # 1 6 2 3 4 5 (15 23 32 46 51 64)
#     # 1 5 6 2 3 4 (14 26 35 41 53 62)
#     # 1 4 5 6 2 3 (13 24 31 42 56 65)
#     # 1 3 4 5 6 2 (12 21 36 45 54 63)
