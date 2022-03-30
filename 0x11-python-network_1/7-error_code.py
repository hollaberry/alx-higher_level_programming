#!/usr/bin/python3
"""Take in URL, send a request to the url
and displays the body of the response"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    m = r.status_code
    if m >= 400:
        print("Error code: {}".format(m))
    else:
        print(r.text)
