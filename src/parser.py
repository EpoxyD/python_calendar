''' csv parser file '''

from csv import DictReader, DictWriter
from os import path, remove

from objects import Club, Team, Division


def csv_parse(inputfile):
    ''' Parse a csv file to a list of teams '''
    result = {}
    clubs = {}
    divisions = {}
    with open(inputfile) as file:
        reader = DictReader(file)
        for entry in reader:
            club = entry["club"]
            team = entry["team"]
            division = entry["division"]
            tables = entry["tables"]
            matchday = entry["matchday"]
            rounds = entry["rounds"]

            if not club in clubs:
                clubs[club] = Club(club, tables)
            club = clubs[club]

            if not division in divisions:
                divisions[division] = Division(division, rounds)
            division = divisions[division]

            if not division in result:
                result[division] = []

            result[division].append(Team(club, team, matchday))
    return result


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
