#!/usr/bin/python3
"""
LOG CHECK
"""

import re
import sys
from collections import defaultdict

# Regular expression to match the input format
log_pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - \[(?P<date>[^\]]+)\] '
    r'"GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)'
)

# Initialize metrics
total_size = 0
status_counts = defaultdict(int)  # Default value of 0 for any missing status code
valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
line_count = 0

def print_stats():
    """Print the collected statistics."""
    global total_size, status_counts

    print(f"File size: {total_size}")
    for status in sorted(valid_status_codes):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def process_line(line):
    """Process a single line if it matches the expected format."""
    global total_size, line_count

    match = log_pattern.match(line)
    if match:
        # Extract status code and file size from the matched line
        status_code = int(match.group('status'))
        file_size = int(match.group('size'))

        # Update metrics
        total_size += file_size
        if status_code in valid_status_codes:
            status_counts[status_code] += 1

        line_count += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

def main():
    """Main function to read from stdin and handle keyboard interruption."""
    try:
        for line in sys.stdin:
            process_line(line)
    except KeyboardInterrupt:
        # Print final stats on keyboard interruption (CTRL + C)
        print_stats()
        sys.exit(0)

if __name__ == "__main__":
    main()

