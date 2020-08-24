#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests
from sys import argv

if __name__ == "__main__":
    if len(sys.argv) == 1:
        ltr = ""
    else:
        ltr = argv[1]

    q = {"q": ltr}

    req = requests.post("http://0.0.0.0:5000/search_user", data=q)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
