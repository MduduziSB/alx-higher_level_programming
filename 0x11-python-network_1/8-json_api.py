#!/usr/bin/python3
"""
This Python script sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    data = {"q": q}
    response = requests.post(url, data=data)
    try:
        res_data = response.json()
        if res_data:
            for user in res_data:
                print(f"[{user.get('id')}] {user.get('name')}")
        else:
            print("No result")
    except ValueError as invalid_json:
        print("Not a valid JSON")
