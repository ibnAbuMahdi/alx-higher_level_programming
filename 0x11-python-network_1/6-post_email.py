#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import requests
from sys import argv as args

if __name__ == "__main__":
    data = requests.post(args[1], {'email': args[2]})
    print(data.text)
