#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    data = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(data.text))
    print("\t- content:", data.text)
