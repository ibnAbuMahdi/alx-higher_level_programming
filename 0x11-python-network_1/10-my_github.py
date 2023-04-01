#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import requests
from sys import argv as args

if __name__ == "__main__":
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": "Bearer {}".format(args[2]),
               "X-GitHub-Api-Version": "2022-11-28"}
    data = requests.get("https://api.github.com/{}".format(args[1]),
                        headers=headers)
    print(data.json())
