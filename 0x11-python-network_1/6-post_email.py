#!/usr/bin/python3
"""Take in URL and email address, sends a POST request
to the passed URL with the email as a paramter"""


if __name__ == "__main__":
    import requests
    import sys

    value = {'email': sys.argv[2]}   
    r = requests.post(sys.argv[1], value)
    print(r.text)
