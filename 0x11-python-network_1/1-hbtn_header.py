#!/usr/bin/python3
"""script that sends a request to the url, and displays the value
of the X-request-Id variable found in the header response"""


if __name__ == "__main__":
    import urlib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        top = response.headers.get('X-Request-Id')
        print(top)
