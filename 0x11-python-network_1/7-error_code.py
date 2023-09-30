#!/usr/bin/python3
"""
This Python script sends a request to the URL and displays the
body of the response (decoded in utf-8).
"""
import sys
import requests


if __name__ == "__main__":
    res = requests.get(sys.argv[1])

    if res.status_code < 400:
        print("{}".format(res.text))
    else:
        print("Error code: {}".format(res.status_code))
