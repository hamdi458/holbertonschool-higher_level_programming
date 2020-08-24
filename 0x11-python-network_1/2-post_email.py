#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import urllib.request
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')

    with urllib.request.urlopen(sys.argv[1], data) as s:
        html = s.read()
    print(html.decode(encoding="utf-8"))
