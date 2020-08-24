#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of response"""

import sys
import urllib.request
import urllib.error


if __name__ == "__main__":

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as s:
            print(s.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
