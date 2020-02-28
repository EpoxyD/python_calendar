import argparse
import csv
import printer
import os

from Team import Team

logger = printer.get_logger()


def get_teamlist(csv_file):
    teams = list()
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for entry in reader:
            teams.append(Team(
                entry['club'],
                entry['name'],
                entry['day'],
            ))
    return teams


def get_teamlist_competition(all_teams, rank):
    ''' return a subset of all teams containing only those with the specified rank '''
    result = list()
    for team in all_teams:
        if team.rank == rank:
            result.append(team)
    if len(result) % 2:
        result.append(Team("FREE", "FREE", "MAANDAG"))
    return result


def remove_old_output(file):
    with open('new_calendar.csv', 'w', newline='') as file:
        fieldnames = ['week', 'day', 'comp', 'team1', 'team2', 'location']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


def generate_output(cal):
    with open('new_calendar.csv', 'a', newline='') as file:
        fieldnames = ['week', 'day', 'comp', 'team1', 'team2', 'location']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for i in range(len(cal)):
            for game in cal[i]:
                writer.writerow({
                    'week': str(i+1),
                    'day': game[0].getDay(),
                    'comp': game[0].getRank(),
                    'team1': game[0].getName(),
                    'team2': game[1].getName(),
                    'location': game[0].getClub()
                })


def get_arguments():
    ''' return a list of csv files '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "files",
        nargs='+',
        help="one csv file per competition"
    )
    parser.add_argument(
        "-r", 
        "--rounds",
        help="Specificy how many rounds for each file (comma separated)"
    )
    args = parser.parse_args()

    for i in range(0, len(args.files)):
        tmp = args.files.pop(i)
        if not '.csv' in tmp:
            tmp += '.csv'
        args.files.insert(i, tmp)
        
    if args.rounds:
        args.rounds = args.rounds.split(',')
        if len(args.rounds) != len(args.files):
            logger.error("Specified nr of rounds mismatch with nr of csv files")
            raise SystemExit
    else:
        args.rounds = list()
        for _ in args.files:
            args.rounds.append(2)

    return args.files, args.rounds


def parse_competitions(csv_files):
    competitions = dict()
    constraints = dict()
    for csv_file in csv_files:
        with open(csv_file) as file:
            logger.info("Parse {csv_file}".format(csv_file=csv_file))
            reader = csv.DictReader(file)
            for entry in reader:
                club = entry['club']
                name = entry['name']
                rank = entry['rank']
                day = entry['day']
                games = entry['games']

                if not rank in competitions:
                    competitions[rank] = list()

                if not club in constraints:
                    constraints[club] = dict()

                competitions[rank].append(Team(club, name, day))
                constraints[club][day] = int(games)
            constraints["FREE"] = dict()
            constraints["FREE"]["MAANDAG"] = 1000
    del csv_files
    return competitions, constraints
