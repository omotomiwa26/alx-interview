#!/usr/bin/python3
"""
    This script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size> (if the format is not this one,
    the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>
        (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear or is not an integer,
            don’t print anything
            for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order
"""


import sys

# Initialize metrics
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0


def print_statistics():
    """
        Print the accumulated statistics.
    """
    print(f'File size: {total_size}')
    for key, value in sorted(cache.items()):
        if value != 0:
            print(f'{key}: {value}')


try:
    for line in sys.stdin:
        line_list = line.split()
        if len(line_list) >= 2:
            try:
                code = line_list[-2]
                size = int(line_list[-1])

                # Update metrics only if the status code is valid
                if code in cache:
                    cache[code] += 1

                # Update total file size
                total_size += size
                counter += 1

            except (ValueError, IndexError):
                # Ignore lines with invalid data
                # (non-integer size or malformed format)
                continue

        # Print statistics every 10 lines
        if counter == 10:
            print_statistics()
            counter = 0

# except KeyboardInterrupt:
#     # Handle CTRL + C gracefully
#     print_statistics()
#     sys.exit(0)

finally:
    # Ensure statistics are printed upon script termination
    print_statistics()
