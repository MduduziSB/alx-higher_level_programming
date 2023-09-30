#!/usr/bin/python3
"""
This Python script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    usrname = sys.argv[1]
    pwd = sys.argv[2]
    url = "https://api.github.com/user"
    res = requests.get(url, auth=HTTPBasicAuth(usrname, pwd))
    print(res.json().get("id"))
