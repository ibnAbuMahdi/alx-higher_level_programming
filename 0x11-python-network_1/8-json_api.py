#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import requests
from sys import argv as args

if __name__ == "__main__":
    val = args[1] if len(args) > 1 else ""
    data = requests.post("http://0.0.0.0:5000/search_user", {'q': val})

    try:
        j = data.json()
        if data.headers.get('content-type') != 'application/json':
            print("Not a valid JSON")
        elif len(j) == 0:
            print("No result")
        elif 'id' in j and 'name' in j:
            print("[{}] {}".format(j['id'], j['name']))
        else:
            print("Not a valid JSON")
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
