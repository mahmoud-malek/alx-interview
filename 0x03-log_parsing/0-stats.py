#!/usr/bin/python3
"""
Log parsing and metrics for status codes.
"""

import sys

if __name__ == '__main__':
    # Initialize metrics
    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """Print the current statistics."""
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()

            # Update status code count
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass

            # Update file size
            try:
                filesize += int(data[-1])
            except BaseException:
                pass

            # Print stats every 10 lines
            if count % 10 == 0:
                print_stats(stats, filesize)

        # Print final stats
        print_stats(stats, filesize)

    except KeyboardInterrupt:
        # Print stats on keyboard interruption
        print_stats(stats, filesize)
        raise
