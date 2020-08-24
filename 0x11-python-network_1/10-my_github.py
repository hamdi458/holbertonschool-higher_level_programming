#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id"""

import requests
import sys
from requests.auth import HTTPBasicAuth
from sys import argv
if __name__ == "__main__":
    req = requests.get(
        'https://api.github.com/user',
        auth=HTTPBasicAuth(
            argv[1],
            argv[2]))
    print(req.json().get('id'))
