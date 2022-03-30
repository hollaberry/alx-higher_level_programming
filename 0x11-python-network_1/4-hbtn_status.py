#!/usr/bin/python3
"""script that sends a request to the url, and displays the value
of the X-request-Id variable found in the header response"""


if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
