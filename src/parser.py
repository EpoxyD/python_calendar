''' csv parser file '''

from csv import DictReader, DictWriter
from os import path, remove

from obj.team import Team


def parse_csv(csv_file):
    ''' Parse a csv file containing all teams '''
    competitions = dict()
    restrictions = dict()
    with open(csv_file) as my_file:
        reader = DictReader(my_file)
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

    restrictions["FREE"] = {"FREE": 1000}

    return competitions, restrictions


def parse_output(calendars):
    ''' Parse the generated calendars to a csv file '''
    output_file = "generated_calendar.csv"

    if path.exists(output_file):
        remove(output_file)

    with open(output_file, 'w', newline='') as outputfile:
        fieldnames = ['week', 'game_day', 'competition',
                      'team_name_home', 'team_name_away', 'location']
        writer = DictWriter(outputfile, fieldnames=fieldnames)
        writer.writeheader()

        for competition, calendar in calendars.items():
            for week_nr, game_day in enumerate(calendar):
                for _, game in enumerate(game_day):
                    writer.writerow({
                        'week': str(week_nr+1),
                        'game_day': game[0].get_day(),
                        'competition': competition,
                        'team_name_home': game[0].get_name(),
                        'team_name_away': game[1].get_name(),
                        'location': game[0].get_club()
                    })
