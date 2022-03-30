#!/usr/bin/python3
"""script that sends a request to the url, and displays the value
of the X-request-Id variable found in the header response"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
