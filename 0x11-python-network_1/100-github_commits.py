#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the repository
"""
import sys
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])
    c = requests.get(url).json()

    j = 0
    for i in c:
        print(
            "{}: {}".format(
                i.get('sha'),
                i.get('commit').get('author').get('name')))
        j = j + 1
        if (j == 10):
            break
