''' Everything related to stdout '''

import logging
import sys

LOGGER = logging.getLogger('X')
LOGGER.setLevel(logging.DEBUG)
HANDLER = logging.StreamHandler(sys.stdout)
HANDLER.setLevel(logging.DEBUG)
HANDLER.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'))
LOGGER.addHandler(HANDLER)


def get_logger():
    ''' Retrieve the logger '''
    global LOGGER
    return LOGGER


def print_header():
    ''' Print header '''
    print(r'''
         _____               _    _____        _                   _
        |  __ \             | |  / ____|      | |                 | |
        | |__) |___    ___  | | | |      __ _ | |  ___  _ __    __| |  __ _  _ __
        |  ___// _ \  / _ \ | | | |     / _` || | / _ \| '_ \  / _` | / _` || '__|
        | |   | (_) || (_) || | | |____| (_| || ||  __/| | | || (_| || (_| || |
        |_|    \___/  \___/ |_|  \_____|\__,_||_| \___||_| |_| \__,_| \__,_||_|

                By Evert B.
    ''')


def print_progress_bar(iteration, total, prefix='', suffix=''):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
    """
    decimals = 1
    length = 100
    fill = '█'
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar_icon = fill * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s%% %s' % (prefix, bar_icon, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def print_matchweeks(cal):
    ''' Print games in a match week '''
    nr_weeks = len(cal)
    rank = cal[0][0][0].getRank()

    for i in range(0, nr_weeks):
        print(
            "|--- WEEK {:2} - {:6} -------------------------------------|".format(i+1, rank))
        for day in cal[i]:
            print("| {:10} | {:20} VS {:20} @ {:20} |".format(
                day[0].getDay(),
                day[0].getName(),
                day[1].getName(),
                day[0].getClub()
            ))
        print("|--------------------------------------------------------|")
        print()
    print()


def print_issues(issues):
    ''' Print constraint issues '''
    for club, days in issues.items():
        for day, nr_issues in days.items():
            print("Found {} issues on {} for {}".format(nr_issues, day, club))
