def print_header():
    print('''
         _____               _    _____        _                   _
        |  __ \             | |  / ____|      | |                 | |
        | |__) |___    ___  | | | |      __ _ | |  ___  _ __    __| |  __ _  _ __
        |  ___// _ \  / _ \ | | | |     / _` || | / _ \| '_ \  / _` | / _` || '__|
        | |   | (_) || (_) || | | |____| (_| || ||  __/| | | || (_| || (_| || |
        |_|    \___/  \___/ |_|  \_____|\__,_||_| \___||_| |_| \__,_| \__,_||_|

                By Evert B.
    ''')

# Print iterations progress


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def print_matchweeks(cal):
    nr_weeks = len(cal)
    rank = cal[0][0][0].getRank()

    for i in range(0, nr_weeks):
        print(
            "|--- WEEK {:2} - {:6} -------------------------------------------------------------|".format(i+1, rank))
        for day in cal[i]:
            print("| {:10} | {:20} VS {:20} @ {:20} |".format(
                day[0].getDay(),
                day[0].getName(),
                day[1].getName(),
                day[0].getClub()
            ))
        print("|----------------------------------------------------------------------------------|".format(i))
        print()
    print()


def print_issues(issues):
    for club, days in issues.items():
        for day, nr_issues in days.items():
            print("Found {} issues on {} for {}".format(nr_issues, day, club))
