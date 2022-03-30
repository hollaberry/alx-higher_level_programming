#!/usr/bin/python3
"""script that sends a request to the url, and displays the value
of the X-request-Id variable found in the header response"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode("utf-8", "replace")
        print(the_page)
