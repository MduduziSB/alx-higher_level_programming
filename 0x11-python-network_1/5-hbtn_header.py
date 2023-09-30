#!/usr/bin/python3
"""
This is a Python script that sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print("{}".format(response.headers.get("X-Request-Id")))
