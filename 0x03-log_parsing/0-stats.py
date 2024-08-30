#!/usr/bin/env python3

"""  script that reads stdin line
 by line and computes metrics
 """

import sys
import singal


def is_valid_line(line: str) -> bool:
    """ a function that returns True if the line is valid """
    try:
        parts = line.split(" ")
        status_code = parts[-2]
        size = parts[-1]
        if len(parts) < 2:
            return False
        if not status_code.isnumeric():
            return False
        if len(parts) < 3 or not size.isnumeric():
            return False
        return True
    except Exception:
        return False


def main():
    """ the main function of the script """
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    file_size = 0
    counter = 0

    try:
        for line in sys.stdin:
            counter += 1
            if not is_valid_line(line):
                continue
            parts = line.split(" ")
            status_code = parts[-2]
            size = parts[-1]
            if status_code in status_codes:
                status_codes[status_code] += 1
            file_size += int(size)
            if counter % 10 == 0:
                print(f"File size: {file_size}")
                for k, v in sorted(status_codes.items()):
                    if v != 0:
                        print(f"{k}: {v}")
    except KeyboardInterrupt:
        pass
    finally:
        print(f"File size: {file_size}")
        for k, v in sorted(status_codes.items()):
            if v != 0:
                print(f"{k}: {v}")
