#!/usr/bin/python3

import sys
import signal

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handle the SIGINT signal."""
    print_stats()
    sys.exit(0)


# Register signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)


def process_line(line):
    """Process a single line of input."""
    global total_size, line_count
    parts = line.split()
    if len(parts) != 9:
        return
    try:
        ip, _, _, date, _, request, _, status_code, file_size = parts
        if request != '"GET /projects/260 HTTP/1.1"':
            return
        status_code = int(status_code)
        file_size = int(file_size)
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    except ValueError:
        return


# Read lines from stdin
for line in sys.stdin:
    process_line(line.strip())

# Print final stats if the script ends without interruption
print_stats()
