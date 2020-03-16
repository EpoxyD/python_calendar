''' csv parser file '''

import csv

from obj.team import Team

# LOGGER = printer.get_logger()


# def get_teamlist(csv_file):
#     ''' retrieve all teams from csv '''
#     teams = list()
#     with open(csv_file) as file:
#         reader = csv.DictReader(file)
#         for entry in reader:
#             teams.append(Team(
#                 entry['club'],
#                 entry['name'],
#                 entry['day'],
#             ))
#     return teams


# def get_teamlist_competition(all_teams, rank):
#     ''' return a subset of all teams containing only those with the specified rank '''
#     result = list()
#     for team in all_teams:
#         if team.rank == rank:
#             result.append(team)
#     if len(result) % 2:
#         result.append(Team("FREE", "FREE", "MAANDAG"))
#     return result


# def remove_old_output(file):
#     ''' remove any old new_calendar.csv and replace with a new one '''
#     with open('new_calendar.csv', 'w', newline='') as calendar:
#         fieldnames = ['week', 'day', 'comp', 'team1', 'team2', 'location']
#         writer = csv.DictWriter(calendar, fieldnames=fieldnames)
#         writer.writeheader()


# def generate_output(cal):
#     ''' Write in the clean file '''
#     with open('new_calendar.csv', 'a', newline='') as file:
#         fieldnames = ['week', 'day', 'comp', 'team1', 'team2', 'location']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         for i in enumerate(cal):
#             for game in cal[i]:
#                 writer.writerow({
#                     'week': str(i+1),
#                     'day': game[0].getDay(),
#                     'comp': game[0].getRank(),
#                     'team1': game[0].getName(),
#                     'team2': game[1].getName(),
#                     'location': game[0].getClub()
#                 })


# def parse_competitions(csv_files):
#     ''' Parse all competitions from the input '''
#     competitions = dict()
#     constraints = dict()
#     for csv_file in csv_files:
#         with open(csv_file) as file:
#             LOGGER.info("Parse %s", csv_file)
#             reader = csv.DictReader(file)
#             for entry in reader:
#                 club = entry['club']
#                 name = entry['name']
#                 rank = entry['rank']
#                 day = entry['day']
#                 games = entry['games']

#                 if not rank in competitions:
#                     competitions[rank] = list()

#                 if not club in constraints:
#                     constraints[club] = dict()

#                 competitions[rank].append(Team(club, name, day))
#                 constraints[club][day] = int(games)
#             constraints["FREE"] = dict()
#             constraints["FREE"]["MAANDAG"] = 1000
#     del csv_files
#     return competitions, constraints


def parse_csv(csv_file):
    competitions = dict()
    restrictions = dict()
    with open("csv/teams.csv") as my_file:
        reader = csv.DictReader(my_file)
        for entry in reader:
            club = entry["club_name"]
            team = entry["team_name"]
            game_day = entry["game_day"]
            competition = entry["competition"]
            tables = entry["tables_available"]

            if not competition in competitions:
                competitions[competition] = list()

            if not club in restrictions:
                restrictions[club] = dict()

            if not game_day in restrictions[club]:
                restrictions[club][game_day] = tables

            new_team = Team(club, team, game_day)
            competitions[competition].append(new_team)

    return competitions, restrictions
