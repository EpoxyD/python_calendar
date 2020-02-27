import csv
import os
import argparse

from Team import Team


def get_teamlist(csv_file):
    teams = list()
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for entry in reader:
            teams.append(Team(
                entry['club'],
                entry['name'],
                entry['rank'],
                entry['games'],
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
        result.append(Team("FREE", "FREE", rank, 1000))
    return result


def remove_old_output(file):
    if os.path.exists(file):
        os.remove(file)

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
    args = parser.parse_args()
    for i in range(0, len(args.files)):
        tmp = args.files.pop(i)
        if not '.csv' in tmp:
            tmp += '.csv'
        args.files.insert(i, tmp)
    return args.files
