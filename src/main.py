''' Main execution file '''

import logging

from controller import start

logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.DEBUG)


if __name__ == "__main__":
    start()
