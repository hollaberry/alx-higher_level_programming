#!/usr/bin/python3
"""script that sends a request to the url, and displays the value
of the X-request-Id variable found in the header response"""


if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
