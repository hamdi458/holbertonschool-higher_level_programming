#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the body of the response.
"""

import requests
import sys
from sys import argv
if __name__ == '__main__':
    response = requests.get(argv[1])

print(response)
