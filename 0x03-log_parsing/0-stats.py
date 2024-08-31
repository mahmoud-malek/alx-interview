#!/usr/bin/python3

""" this is a function to read stdin line by line """

import sys


def valid_line(line: str) -> bool:
    line = line.strip().split(' ')
    if (len(line) != 9):
        return False

    codes = [200, 301, 400, 401, 403, 404, 405, 500]
    if not line[8].isdigit():
        return False
    if not line[7].isdigit() or int(line[7]) not in codes:
        return False

    return True


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
    '500': 0}

while True:
    try:
        for line in sys.stdin:
            if valid_line(line):
                counter += 1
                line = line.strip().split(' ')
                file_size += int(line[8])
                codes[line[7]] += 1

            if counter == 10:
                print(f'File size: {file_size}')
                for key, val in codes.items():
                    if val > 0:
                        print(f'{key}: {val}')
                        codes[key] = 0
                counter, file_size = 0, 0
        break
    except KeyboardInterrupt:
        print(f'File size: {file_size}')
        for key, val in codes.items():
            if val > 0:
                print(f'{key}: {val}')
        sys.exit(1)
