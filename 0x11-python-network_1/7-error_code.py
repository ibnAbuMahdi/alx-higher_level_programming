#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import requests
from sys import argv as args

if __name__ == "__main__":
    data = requests.get(args[1])

    if data.status_code >= 400:
        print("Error code: {}".format(data.status_code))
    else:
        print(data.text)
