#!/usr/bin/python3

""" This script reads stdin line by line and computes metrics """

import sys


def valid_line(line: str) -> bool:
    """ This function validates the line format """
    line = line.strip().split(' ')
    if len(line) != 9:
        return False

    codes = [200, 301, 400, 401, 403, 404, 405, 500]
    if not line[8].isdigit():
        return False
    if not line[7].isdigit() or int(line[7]) not in codes:
        return False

    return True


def print_stats(file_size, codes):
    """ This function prints the statistics """
    print(f'File size: {file_size}')
    for key in sorted(codes.keys()):
        if codes[key] > 0:
            print(f'{key}: {codes[key]}')


counter = 0
file_size = 0
codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

try:
    for line in sys.stdin:
        if valid_line(line):
            counter += 1
            line = line.strip().split(' ')
            file_size += int(line[8])
            codes[line[7]] += 1

        if counter == 10:
            print_stats(file_size, codes)
            counter = 0
except KeyboardInterrupt:
    print_stats(file_size, codes)
    sys.exit(1)
