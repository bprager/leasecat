#!/usr/bin/env python3
"""
This script reads a dhcp lease file and converts epoch timesatmp into a human readable datetime
"""

__version__ = '0.20'
__author__ = 'Bernd Prager'

import datetime
import logging
import sys

# setup logging
FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s")
log = logging.getLogger(__name__)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(FORMATTER)
log.setLevel(logging.INFO)
log.addHandler(console_handler)


def main():
    if len(sys.argv) < 2:
        log.error('leasefile argument expected')
        sys.exit(1)
    leaseFileName = sys.argv[1]
    try:
        leaseFile = open(leaseFileName, "r")
    except:
        log.error(f'leasefile {leaseFileName} not found!')
        sys.exit(1)
    lines = leaseFile.readlines()

    for line in lines:
        tkn = line.rstrip().split()
        timeStr = datetime.datetime.fromtimestamp(
            int(tkn[0])).strftime('%Y-%m-%d %H:%M:%S')
        print(f'{timeStr} {" ".join(tkn[1:])}')


if __name__ == '__main__':
    main()
