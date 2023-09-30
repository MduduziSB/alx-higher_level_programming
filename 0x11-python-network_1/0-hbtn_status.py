#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status by using urllib"""
import urllib.request


if __name__ == "__main__":
    url_to_fetch = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url_to_fetch) as response:
        page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode("utf-8")))
