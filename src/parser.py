''' csv parser file '''

from csv import DictReader, DictWriter
from os import path, remove

from objects import Club, Team



def csv_parse(inputfile):
    ''' Parse a csv file to a list of teams '''
    teams = []
    clubs = {}
    with open(inputfile) as file:
        reader = DictReader(file)
        for entry in reader:
            club_name = entry["club"]
            team_name = entry["team"]
            division = entry["division"]
            tables = entry["tables"]
            matchday = entry["matchday"]

            club = clubs[club_name] if club_name in clubs else Club(club_name, tables)
            club.add_matchday(matchday)

            team = Team(club, team_name, division, matchday)
            teams.append(team)
    return teams


# def parse_output(calendars):
#     ''' Parse the generated calendars to a csv file '''
#     output_file = "generated_calendar.csv"

#     if path.exists(output_file):
#         remove(output_file)

#     with open(output_file, 'w', newline='') as outputfile:
#         fieldnames = ['week', 'game_day', 'competition',
#                       'team_name_home', 'team_name_away', 'location']
#         writer = DictWriter(outputfile, fieldnames=fieldnames)
#         writer.writeheader()

#         for competition, calendar in calendars.items():
#             for week_nr, game_day in enumerate(calendar):
#                 for _, game in enumerate(game_day):
#                     writer.writerow({
#                         'week': str(week_nr+1),
#                         'game_day': game[0].get_day(),
#                         'competition': competition,
#                         'team_name_home': game[0].get_name(),
#                         'team_name_away': game[1].get_name(),
#                         'location': game[0].get_club()
#                     })
