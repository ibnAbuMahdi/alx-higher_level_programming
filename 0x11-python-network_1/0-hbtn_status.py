#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        data = resp.read()
        info = resp.info()
    print("Body response:")
    print("\t- type:".expandtabs(4), type(data))
    print("\t- content:".expandtabs(4), data)
    if "utf-8" in info['Content-Type']:
        print("\t- utf8 content: OK".expandtabs(4))
